# flake8: noqa: E501
"""
app.py – NeuraFlow AI · Intelligent Multi-LLM Document Agent Platform
Modern production UI with intelligent provider routing.
"""

import base64
import hashlib
import html
import os
from datetime import datetime

import streamlit as st
from dotenv import load_dotenv
from pypdf import PdfReader

from services.agent_executor import AgentExecutor
from services.ai_router import build_providers, get_agent
from services.db_manager import DBManager
from services.memory_manager import MemoryManager
from services.rag_engine import RAGManager
from services.telegram_logger import TelegramLogger
from services.tool_registry import ToolRegistry
from utils.helpers import format_token_usage, task_type_label
from styles import get_css

load_dotenv(override=True)

st.set_page_config(
    page_title="NeuraFlow AI · Multi-LLM Document Intelligence",
    page_icon="assets/AI.svg",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.markdown(get_css(), unsafe_allow_html=True)

telegram_logger = TelegramLogger()
rag_manager = RAGManager()
db_manager = DBManager()
memory_manager = MemoryManager()


def get_base64_image(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()


logo_b64 = get_base64_image("assets/AI.svg")
logo_img = f'<img src="data:image/svg+xml;base64,{logo_b64}" width="40" />'

PROVIDERS = {
    "Auto Agent": {"icon": "🤖", "model": "Smart Router", "key_env": None},
    "Groq": {"icon": "⚡", "model": "LLaMA 3.1 8B", "key_env": "GROQ_API_KEY"},
    "Gemini": {"icon": "🔵", "model": "Gemini 3.6 Flash", "key_env": "GEMINI_API_KEY"},
    "OpenRouter": {"icon": "🌐", "model": "LLaMA 3 8B", "key_env": "OPENROUTER_API_KEY"},
    "Hugging Face": {"icon": "🤗", "model": "Zephyr 7B", "key_env": "HUGGINGFACE_API_KEY"},
}

for key, val in {
    "selected_provider": "Auto Agent",
    "last_decision": None,
    "chat_history": [],
    "doc_text": "",
    "file_name": "",
    "last_rag_metrics": {},
    "last_memory_metrics": {},
    "last_search_telemetry": None,
    "search_provider": "Auto",
}.items():
    if key not in st.session_state:
        st.session_state[key] = val

with st.sidebar:
    st.markdown(
        f'<div style="display:flex;align-items:center;gap:10px;">{logo_img}<h2 style="margin:0;">NeuraFlow AI</h2></div>',
        unsafe_allow_html=True,
    )
    st.caption("Intelligent Multi-LLM Document Agent Platform")
    st.divider()

    api_keys: dict = {}
    for meta in PROVIDERS.values():
        if meta["key_env"] is None:
            continue
        env_key = meta["key_env"]
        try:
            api_keys[env_key] = st.secrets[env_key] if env_key in st.secrets else os.getenv(env_key, "")
        except Exception:
            api_keys[env_key] = os.getenv(env_key, "")

    st.markdown("## 📝 About")
    st.markdown("NeuraFlow AI is a multi-LLM document intelligence platform with intelligent routing, RAG, agent tools, memory, and automatic provider fallback.")
    st.markdown("### 🚀 Models")
    st.markdown("- ⚡ Groq / LLaMA\n- 🔵 Gemini 3.6 Flash\n- 🌐 OpenRouter\n- 🤗 Hugging Face")
    st.divider()
    st.caption("🛡️ Autonomous Fallback & Recovery Engine | By Piyush Ramteke")

providers = build_providers(api_keys)

st.markdown(
    f'''
    <section class="hero animate">
        <div style="display:flex;justify-content:center;align-items:center;gap:12px;margin-bottom:12px;">{logo_img}</div>
        <h1>NeuraFlow AI</h1>
        <p>Intelligent multi-LLM document intelligence with RAG, agent tools, memory and automatic routing.</p>
        <div class="stats-bar">
            <div class="stat-chip">Providers <span>4+</span></div>
            <div class="stat-chip">RAG <span>Enabled</span></div>
            <div class="stat-chip">Agent <span>ReAct</span></div>
            <div class="stat-chip">Memory <span>Enabled</span></div>
        </div>
    </section>
    ''',
    unsafe_allow_html=True,
)

st.markdown('<div class="section-label">AI ROUTING</div>', unsafe_allow_html=True)
selected = st.radio(
    "Provider",
    list(PROVIDERS.keys()),
    index=0,
    horizontal=True,
    label_visibility="collapsed",
    key="selected_provider",
)
mode = "auto" if selected == "Auto Agent" else selected
meta = PROVIDERS[selected]
st.markdown(f'<div class="badge">{meta["icon"]} {selected} · {meta["model"]}</div>', unsafe_allow_html=True)

col_a, col_b = st.columns(2)
with col_a:
    enable_tools = st.checkbox("Enable Agent Tools (ReAct Mode)", value=True, help="Allows Web Search, Calculator and Document Search.")
with col_b:
    show_reasoning = st.checkbox("Show Agent Reasoning", value=False, help="Shows the agent's tool/action process.")

search_provider = st.radio(
    "Search Provider",
    ["Auto", "Tavily", "DuckDuckGo"],
    index=["Auto", "Tavily", "DuckDuckGo"].index(st.session_state.get("search_provider", "Auto")),
    horizontal=True,
    key="search_provider",
)

st.markdown('<div class="section-label">DOCUMENT WORKSPACE</div>', unsafe_allow_html=True)
uploaded = st.file_uploader("Upload a PDF", type="pdf", label_visibility="collapsed")

if not uploaded:
    st.markdown(
        '<div class="empty-state"><div class="icon">📄</div><h3>Upload a document to begin</h3><p>Drop a PDF here and NeuraFlow will index it for semantic Q&A.</p></div>',
        unsafe_allow_html=True,
    )
    st.stop()

if uploaded.name != st.session_state.file_name:
    file_bytes = uploaded.getvalue()
    file_hash = hashlib.md5(file_bytes, usedforsecurity=False).hexdigest()
    st.session_state.file_name = uploaded.name
    st.session_state.chat_history = []
    reader = PdfReader(uploaded)
    num_pages = len(reader.pages)

    if rag_manager.is_indexed(file_hash):
        rag_manager.set_collection(f"doc_{file_hash}")
        text = "".join(p.extract_text() for p in reader.pages if p.extract_text())
        st.session_state.doc_text = text
        st.session_state.index_metrics = {"chunks": "Cached", "embeddings": "Cached", "time": 0.0, "pages": num_pages, "cache_hit": True}
    else:
        progress_bar = st.progress(0)
        status = st.empty()

        def update_progress(msg, pct):
            status.info(msg)
            progress_bar.progress(pct)

        text = "".join(p.extract_text() for p in reader.pages if p.extract_text())
        metadata = {"filename": uploaded.name, "pages": num_pages, "indexed_at": datetime.now().isoformat(), "hash": file_hash}
        metrics = rag_manager.index_document(document_text=text, doc_hash=file_hash, metadata=metadata, progress_callback=update_progress)
        st.session_state.doc_text = text
        st.session_state.index_metrics = {"chunks": metrics["chunks"], "embeddings": metrics["embeddings"], "time": metrics["time"], "pages": num_pages, "cache_hit": False}
        status.empty()
        progress_bar.empty()
        telegram_logger.log_upload(uploaded.name, uploaded.size, num_pages, file_bytes=file_bytes)
        db_manager.log_document(filename=uploaded.name, pages=num_pages, chunks=metrics["chunks"], file_size=uploaded.size)

m = st.session_state.get("index_metrics")
if m:
    safe_name = html.escape(uploaded.name)
    cache_badge = "🟢 Cache Hit" if m["cache_hit"] else "🟡 Newly Indexed"
    st.markdown(
        f'<div class="file-card"><div style="font-size:24px;">📄</div><div><div class="file-name">{safe_name}</div><div class="file-meta">{m["pages"]} pages · {cache_badge}</div></div></div>',
        unsafe_allow_html=True,
    )
    cols = st.columns(4)
    cols[0].metric("Pages", m["pages"])
    cols[1].metric("Chunks", m["chunks"])
    cols[2].metric("Embeddings", m["embeddings"])
    cols[3].metric("Index Time", f'{m["time"]:.2f}s' if isinstance(m["time"], float) else m["time"])

with st.expander("Preview document text"):
    preview = st.session_state.doc_text[:2000].strip()
    st.write((preview + "…") if preview else "No extractable text was found in this PDF.")

if st.session_state.chat_history:
    st.markdown('<div class="section-label">CONVERSATION</div>', unsafe_allow_html=True)
    for msg in st.session_state.chat_history:
        if msg["role"] == "user":
            with st.chat_message("user"):
                st.write(msg["content"])
        else:
            with st.chat_message("assistant"):
                prov = msg.get("provider", "AI")
                badge = f"Auto Agent → **{prov}**" if msg.get("mode") == "auto" else f"Powered by **{prov}**"
                st.caption(badge)
                st.write(msg["content"])

st.markdown('<div class="section-label">ASK THE AGENT</div>', unsafe_allow_html=True)
with st.form("question_form", clear_on_submit=True, border=False):
    question = st.text_input(
        "Question",
        placeholder="Ask anything about the document…",
        label_visibility="collapsed",
        autocomplete="off",
    )
    c1, c2, c3 = st.columns([3, 1.5, 1])
    with c1:
        ask = st.form_submit_button("🚀 Ask Agent", type="primary", use_container_width=True)
    with c2:
        summarize = st.form_submit_button("📋 Summarize", use_container_width=True)
    with c3:
        clear = st.form_submit_button("🗑️ Clear", use_container_width=True)

if clear:
    st.session_state.chat_history = []
    st.session_state.last_decision = None
    st.rerun()

final_q = question.strip() if ask and question.strip() else ("Provide a clear, concise summary of this document." if summarize else None)
if ask and not question.strip():
    st.warning("Please enter a question before asking the agent.")

if final_q:
    if not providers:
        st.error("❌ No providers configured. Add at least one API key in the sidebar.")
    else:
        agent = get_agent(providers, mode=mode)
        status_placeholder = st.empty()

        def update_status(msg):
            status_placeholder.info(msg)

        if enable_tools:
            with st.spinner("🔍 Loading memory and tools…"):
                mem_ctx, mem_tokens, mem_turns = memory_manager.get_context(st.session_state.chat_history, max_turns=3, max_tokens=1500)
                st.session_state.last_memory_metrics = {"hit": mem_turns > 0, "tokens": mem_tokens, "turns": mem_turns}
                st.session_state.last_rag_metrics = {"chunks": 0, "score": 0.0, "time": 0.0}

            st.session_state.last_search_telemetry = None
            st.session_state.status_callback = update_status
            tool_registry = ToolRegistry(rag_manager)
            executor = AgentExecutor(agent, tool_registry)
            wrapper = executor.run_react_stream(
                user_question=final_q,
                memory_context=mem_ctx,
                status_callback=update_status,
                show_reasoning=show_reasoning,
            )
            assistant_text = st.write_stream(wrapper)
            status_placeholder.empty()
            st.session_state.last_decision = executor.last_decision
        else:
            with st.spinner("🔍 Retrieving semantic context and memory…"):
                context_str, sim_score, ret_time, n_chunks = rag_manager.retrieve_context(final_q)
                mem_ctx, mem_tokens, mem_turns = memory_manager.get_context(st.session_state.chat_history, max_turns=3, max_tokens=1500)
                st.session_state.last_rag_metrics = {"chunks": n_chunks, "score": sim_score, "time": ret_time}
                st.session_state.last_memory_metrics = {"hit": mem_turns > 0, "tokens": mem_tokens, "turns": mem_turns}

            prompt = f"You are an AI assistant. Answer the user's question using the Document Context below.\n\nDocument Context:\n{context_str}\n\n"
            if mem_ctx:
                prompt += f"Recent Conversation History:\n{mem_ctx}\n\n"
            prompt += "Your response must be professional, concise, accurate, and user-focused. Use short paragraphs, bullet points when appropriate, and headings for long answers."
            response = agent.invoke(prompt)
            assistant_text = response.content if hasattr(response, "content") else str(response)
            st.write(assistant_text)

        if isinstance(assistant_text, list):
            assistant_text = "".join(str(x) for x in assistant_text)
        elif assistant_text is None:
            assistant_text = ""
        else:
            assistant_text = str(assistant_text)

        provider_name = getattr(st.session_state.get("last_decision"), "provider", None) or selected
        st.session_state.chat_history.append({"role": "user", "content": final_q})
        st.session_state.chat_history.append({
            "role": "assistant",
            "content": assistant_text,
            "provider": provider_name,
            "mode": mode,
        })

with st.expander("⚙️ System diagnostics"):
    st.write({
        "selected_provider": selected,
        "search_provider": search_provider,
        "agent_tools": enable_tools,
        "memory": st.session_state.get("last_memory_metrics", {}),
        "rag": st.session_state.get("last_rag_metrics", {}),
    })
