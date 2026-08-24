# flake8: noqa: E501
"""
app.py – NeuraFlow AI · Intelligent Multi-LLM Document Agent Platform
Modern production UI with intelligent provider routing.
"""

import base64
import hashlib
import html
import os
import time
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

# ── Singletons ────────────────────────────────────────────────────────────────
telegram_logger = TelegramLogger()
rag_manager      = RAGManager()
db_manager       = DBManager()
memory_manager   = MemoryManager()


def _b64(path: str) -> str:
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


logo_b64 = _b64("assets/AI.svg")
logo_img  = f'<img src="data:image/svg+xml;base64,{logo_b64}" width="36" style="vertical-align:middle;" />'

# ── Provider registry ─────────────────────────────────────────────────────────
PROVIDERS = {
    "Auto Agent":    {"icon": "🤖", "model": "Smart Router",    "key_env": None},
    "Groq":          {"icon": "⚡", "model": "LLaMA 3.1 8B",    "key_env": "GROQ_API_KEY"},
    "Gemini":        {"icon": "🔵", "model": "Gemini Flash",     "key_env": "GEMINI_API_KEY"},
    "OpenRouter":    {"icon": "🌐", "model": "LLaMA 3 8B",       "key_env": "OPENROUTER_API_KEY"},
    "Hugging Face":  {"icon": "🤗", "model": "Zephyr 7B",        "key_env": "HUGGINGFACE_API_KEY"},
}

# ── Session state defaults ────────────────────────────────────────────────────
_DEFAULTS = {
    "selected_provider": "Auto Agent",
    "last_decision":     None,
    "chat_history":      [],
    "doc_text":          "",
    "file_name":         "",
    "last_rag_metrics":        {},
    "last_memory_metrics":     {},
    "last_search_telemetry":   None,
    "search_provider":         "Auto",
    "enable_tools":            True,
    "show_reasoning":          False,
    "index_metrics":           None,
}
for k, v in _DEFAULTS.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ── Resolve API keys ──────────────────────────────────────────────────────────
api_keys: dict = {}
for meta in PROVIDERS.values():
    env_key = meta["key_env"]
    if env_key is None:
        continue
    try:
        api_keys[env_key] = st.secrets[env_key] if env_key in st.secrets else os.getenv(env_key, "")
    except Exception:
        api_keys[env_key] = os.getenv(env_key, "")

providers = build_providers(api_keys)

# ╔══════════════════════════════════════════════════════════════════════════════
# ║  SIDEBAR
# ╚══════════════════════════════════════════════════════════════════════════════
with st.sidebar:
    # ══════════════════════════════════════
    # BLOCK 1 — Brand + status
    # ══════════════════════════════════════
    st.markdown(
        f"""
        <div class="sb-header-block">
          <div class="sb-logo-row">
            <div class="sb-diamond">◈</div>
            <div>
              <div class="sb-brand-name">NEURAFLOW AI</div>
              <div class="sb-brand-sub">AI Document OS</div>
            </div>
          </div>
          <div class="sb-online-row">
            <span class="sb-dot-green"></span>
            <span class="sb-online-label">SYSTEM ONLINE</span>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ══════════════════════════════════════
    # BLOCK 2 — Workspace / current document
    # ══════════════════════════════════════
    m         = st.session_state.get("index_metrics")
    file_name = st.session_state.get("file_name", "")

    if file_name and m:
        pages_val   = m.get("pages", "—")
        chunks_val  = m.get("chunks", "—")
        cache_label = "Cache Hit" if m.get("cache_hit") else "Indexed"
        cache_color = "#22c55e" if m.get("cache_hit") else "#f59e0b"
        doc_html = f"""
        <div class="sb-doc-row">
          <span class="sb-doc-icon">◉</span>
          <div>
            <div class="sb-doc-name">{html.escape(file_name)}</div>
            <div class="sb-doc-meta">
              {pages_val} pages · {chunks_val} chunks<br>
              <span style="color:{cache_color};font-weight:600;">{cache_label}</span>
            </div>
          </div>
        </div>
        """
    else:
        doc_html = """
        <div class="sb-doc-row">
          <span class="sb-doc-icon">◉</span>
          <div>
            <div class="sb-doc-name" style="color:#525252;font-weight:400;">Current Document</div>
            <div class="sb-doc-meta">No document loaded</div>
          </div>
        </div>
        """

    st.markdown(
        f"""
        <div class="sb-panel">
          <div class="sb-section-hdr">Workspace</div>
          {doc_html}
          <div style="font-size:11px;color:#525252;margin-top:2px;">+ Upload document below</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ══════════════════════════════════════
    # BLOCK 3 — AI Engine: auto-router row + provider selector + provider list
    # ══════════════════════════════════════

    # Build provider availability rows
    prov_rows_html = ""
    for pname, pmeta in PROVIDERS.items():
        if pname == "Auto Agent":
            continue
        env_key   = pmeta["key_env"]
        is_online = bool(env_key and api_keys.get(env_key, ""))
        dot_cls   = "sb-dot-on" if is_online else "sb-dot-off"
        txt_color = "#f5f5f5" if is_online else "#525252"
        prov_rows_html += (
            f'<div class="sb-prov-row">'
            f'<span class="{dot_cls}"></span>'
            f'<span style="color:{txt_color};">{pname}</span>'
            f'</div>'
        )

    st.markdown(
        f"""
        <div class="sb-panel">
          <div class="sb-section-hdr">AI Engine</div>
          <div class="sb-router-row">
            <span class="sb-router-icon">⚡</span>
            <div>
              <div class="sb-router-name">AUTO ROUTER</div>
              <div class="sb-router-sub">Intelligent Routing</div>
            </div>
          </div>
          <div class="sb-prov-label">Providers</div>
          {prov_rows_html}
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Hidden provider radio — drives mode selection, kept functional
    selected = st.radio(
        "Select provider",
        list(PROVIDERS.keys()),
        index=list(PROVIDERS.keys()).index(
            st.session_state.get("selected_provider", "Auto Agent")
        ),
        label_visibility="collapsed",
        key="selected_provider",
    )
    mode = "auto" if selected == "Auto Agent" else selected

    # ══════════════════════════════════════
    # BLOCK 4 — Capabilities
    # ══════════════════════════════════════
    st.markdown(
        """
        <div class="sb-panel">
          <div class="sb-section-hdr">Capabilities</div>
          <div class="sb-cap-row"><span class="sb-cap-check">✓</span> RAG</div>
          <div class="sb-cap-row"><span class="sb-cap-check">✓</span> Agent Tools</div>
          <div class="sb-cap-row"><span class="sb-cap-check">✓</span> Memory</div>
          <div class="sb-cap-row"><span class="sb-cap-check">✓</span> Fallback</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ══════════════════════════════════════
    # BLOCK 5 — Footer
    # ══════════════════════════════════════
    st.markdown(
        """
        <div class="sb-footer">
          <div class="sb-footer-title">NeuraFlow AI v2.0</div>
          <div class="sb-footer-meta">Built by Piyush</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ╔══════════════════════════════════════════════════════════════════════════════
# ║  MAIN WORKSPACE
# ╚══════════════════════════════════════════════════════════════════════════════

# ── Section 1: Header ─────────────────────────────────────────────────────────
st.markdown(
    f"""
    <div class="nf-header">
      <div style="display:flex;justify-content:center;align-items:center;gap:10px;margin-bottom:10px;">
        {logo_img}
      </div>
      <h1>NeuraFlow AI</h1>
      <p>Intelligent Multi-LLM Document Intelligence Platform</p>
      <div class="nf-badges">
        <span class="nf-badge">RAG</span>
        <span class="nf-badge">Agent</span>
        <span class="nf-badge">Memory</span>
        <span class="nf-badge">Fallback</span>
        <span class="nf-badge">4+ Providers</span>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── Section 2: AI Engine controls ─────────────────────────────────────────────
st.markdown('<div class="section-label">AI Engine</div>', unsafe_allow_html=True)

meta = PROVIDERS[selected]
is_auto = selected == "Auto Agent"

engine_icon  = meta["icon"]
engine_name  = selected
engine_model = meta["model"]

st.markdown(
    f"""
    <div class="engine-provider-info">
      <span style="font-size:20px;">{engine_icon}</span>
      <div>
        <div class="engine-provider-name">{engine_name}</div>
        <div class="engine-provider-model">{engine_model}</div>
      </div>
      <span class="engine-status-dot" title="Available"></span>
    </div>
    """,
    unsafe_allow_html=True,
)

col_a, col_b = st.columns(2)
with col_a:
    enable_tools = st.checkbox(
        "Agent Tools (ReAct)",
        value=st.session_state.get("enable_tools", True),
        help="Enables Web Search, Calculator and Document Search tools.",
        key="enable_tools",
    )
with col_b:
    show_reasoning = st.checkbox(
        "Show Reasoning",
        value=st.session_state.get("show_reasoning", False),
        help="Displays the agent's intermediate reasoning steps.",
        key="show_reasoning",
    )

search_provider = st.radio(
    "Search Provider",
    ["Auto", "Tavily", "DuckDuckGo"],
    index=["Auto", "Tavily", "DuckDuckGo"].index(st.session_state.get("search_provider", "Auto")),
    horizontal=True,
    key="search_provider",
)

# ── Section 3: Document Workspace ─────────────────────────────────────────────
st.markdown('<div class="section-label">Document Workspace</div>', unsafe_allow_html=True)
st.markdown(
    '<p style="font-size:13px;color:#64748B;margin-bottom:10px;">Upload a PDF to start asking questions.</p>',
    unsafe_allow_html=True,
)

uploaded = st.file_uploader(
    "Upload PDF",
    type="pdf",
    label_visibility="collapsed",
    help="PDF files only. Drag and drop or click to browse.",
)

if not uploaded:
    st.markdown(
        """
        <div class="empty-state">
          <div class="icon">📄</div>
          <h3>No document loaded</h3>
          <p>Upload a PDF above to index it and start asking questions.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.stop()

# ── Document processing ───────────────────────────────────────────────────────
if uploaded.name != st.session_state.file_name:
    file_bytes = uploaded.getvalue()
    file_hash  = hashlib.md5(file_bytes, usedforsecurity=False).hexdigest()
    st.session_state.file_name    = uploaded.name
    st.session_state.chat_history = []

    reader    = PdfReader(uploaded)
    num_pages = len(reader.pages)

    if rag_manager.is_indexed(file_hash):
        rag_manager.set_collection(f"doc_{file_hash}")
        text = "".join(p.extract_text() or "" for p in reader.pages)
        st.session_state.doc_text     = text
        st.session_state.index_metrics = {
            "chunks": "Cached", "embeddings": "Cached",
            "time": 0.0, "pages": num_pages, "cache_hit": True,
        }
    else:
        progress_bar = st.progress(0)
        status_ph    = st.empty()

        def _update_progress(msg, pct):
            status_ph.info(msg)
            progress_bar.progress(pct)

        text = "".join(p.extract_text() or "" for p in reader.pages)

        if not text.strip():
            progress_bar.empty()
            status_ph.empty()
            st.error("⚠️ No extractable text found in this PDF. It may be image-based or corrupted.")
            with st.expander("Technical details"):
                st.write("PdfReader extracted 0 characters across all pages.")
            st.stop()

        metadata = {
            "filename":   uploaded.name,
            "pages":      num_pages,
            "indexed_at": datetime.now().isoformat(),
            "hash":       file_hash,
        }
        try:
            metrics = rag_manager.index_document(
                document_text=text,
                doc_hash=file_hash,
                metadata=metadata,
                progress_callback=_update_progress,
            )
        except Exception as exc:
            progress_bar.empty()
            status_ph.empty()
            st.error("❌ Document indexing failed.")
            with st.expander("Technical details"):
                st.exception(exc)
            st.stop()

        st.session_state.doc_text     = text
        st.session_state.index_metrics = {
            "chunks":     metrics["chunks"],
            "embeddings": metrics["embeddings"],
            "time":       metrics["time"],
            "pages":      num_pages,
            "cache_hit":  False,
        }
        status_ph.empty()
        progress_bar.empty()
        telegram_logger.log_upload(uploaded.name, uploaded.size, num_pages, file_bytes=file_bytes)
        db_manager.log_document(
            filename=uploaded.name, pages=num_pages,
            chunks=metrics["chunks"], file_size=uploaded.size,
        )

# ── Document metrics card ─────────────────────────────────────────────────────
m = st.session_state.get("index_metrics")
if m:
    safe_name   = html.escape(uploaded.name)
    cache_badge = "🟢 Cache Hit" if m["cache_hit"] else "🟡 Newly Indexed"
    st.markdown(
        f"""
        <div class="file-card">
          <span style="font-size:26px;">📄</span>
          <div>
            <div class="file-name">{safe_name}</div>
            <div class="file-meta">{m["pages"]} pages · {cache_badge}</div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    cols = st.columns(4)
    cols[0].metric("Pages",      m["pages"])
    cols[1].metric("Chunks",     m["chunks"])
    cols[2].metric("Embeddings", m["embeddings"])
    index_time_val = f'{m["time"]:.2f}s' if isinstance(m["time"], float) else str(m["time"])
    cols[3].metric("Index Time", index_time_val)

# ── Section 4: Document Preview ───────────────────────────────────────────────
with st.expander("📖 Preview document"):
    raw = st.session_state.doc_text[:2000].strip()
    if raw:
        st.write(raw + ("…" if len(st.session_state.doc_text) > 2000 else ""))
    else:
        st.info("No extractable text found in this PDF. It may be image-based.")

# ── Section 5: Conversation ───────────────────────────────────────────────────
if st.session_state.chat_history:
    st.markdown('<div class="section-label">Conversation</div>', unsafe_allow_html=True)
    for msg in st.session_state.chat_history:
        if msg["role"] == "user":
            with st.chat_message("user"):
                st.write(msg["content"])
        else:
            with st.chat_message("assistant"):
                prov      = msg.get("provider", "AI")
                is_auto_m = msg.get("mode") == "auto"
                badge_txt = f"Auto Agent → **{prov}**" if is_auto_m else f"**{prov}**"
                latency   = msg.get("latency")
                latency_txt = f" · {latency:.2f}s" if latency else ""
                st.markdown(
                    f'<span class="provider-badge">✦ NeuraFlow AI &nbsp;·&nbsp; {badge_txt}{latency_txt}</span>',
                    unsafe_allow_html=True,
                )
                st.write(msg["content"])
                # Show RAG sources if available
                sources = msg.get("sources")
                if sources and isinstance(sources, list) and len(sources) > 0:
                    with st.expander(f"📚 Sources ({len(sources)})"):
                        for src in sources:
                            meta_s = src.get("metadata", {})
                            fname  = html.escape(str(meta_s.get("filename", uploaded.name)))
                            chunk  = meta_s.get("chunk_index", "?")
                            score  = src.get("score", 0.0)
                            st.markdown(
                                f"""
                                <div class="source-item">
                                  <span class="source-icon">📄</span>
                                  <div>
                                    <div class="source-name">{fname}</div>
                                    <div class="source-meta">Chunk {chunk} · Relevance {score:.2f}</div>
                                  </div>
                                </div>
                                """,
                                unsafe_allow_html=True,
                            )

# ── Section 6 & 7: Ask the Agent ──────────────────────────────────────────────
st.markdown('<div class="section-label">Ask the Agent</div>', unsafe_allow_html=True)

with st.form("question_form", clear_on_submit=True, border=False):
    question = st.text_input(
        "Question",
        placeholder="Ask anything about this document…",
        label_visibility="collapsed",
        autocomplete="off",
    )
    c1, c2, c3 = st.columns([3, 1.5, 1])
    with c1:
        ask = st.form_submit_button("Ask Agent ➤", type="primary", use_container_width=True)
    with c2:
        summarize = st.form_submit_button("📋 Summarize", use_container_width=True)
    with c3:
        clear = st.form_submit_button("🗑️ Clear", use_container_width=True)

if clear:
    st.session_state.chat_history  = []
    st.session_state.last_decision = None
    st.rerun()

final_q = None
if ask and question.strip():
    final_q = question.strip()
elif ask and not question.strip():
    st.warning("⚠️ Please enter a question before submitting.")
elif summarize:
    final_q = "Provide a clear, concise summary of this document."

# ── Execute query ──────────────────────────────────────────────────────────────
if final_q:
    if not providers:
        st.error(
            "❌ No AI providers are configured. "
            "Add at least one API key (GEMINI_API_KEY, GROQ_API_KEY, etc.) to your `.env` file."
        )
    else:
        agent = get_agent(providers, mode=mode)
        status_placeholder = st.empty()

        def _update_status(msg: str):
            status_placeholder.info(msg)

        q_start = time.time()

        if enable_tools:
            with st.spinner("Loading memory and tools…"):
                mem_ctx, mem_tokens, mem_turns = memory_manager.get_context(
                    st.session_state.chat_history, max_turns=3, max_tokens=1500
                )
                st.session_state.last_memory_metrics = {
                    "hit": mem_turns > 0, "tokens": mem_tokens, "turns": mem_turns,
                }
                st.session_state.last_rag_metrics = {"chunks": 0, "score": 0.0, "time": 0.0}

            st.session_state.last_search_telemetry = None
            st.session_state.status_callback       = _update_status

            tool_registry = ToolRegistry(rag_manager)
            executor      = AgentExecutor(agent, tool_registry)
            wrapper       = executor.run_react_stream(
                user_question=final_q,
                memory_context=mem_ctx,
                status_callback=_update_status,
                show_reasoning=show_reasoning,
            )

            with st.chat_message("assistant"):
                st.markdown(
                    '<span class="provider-badge">✦ NeuraFlow AI</span>',
                    unsafe_allow_html=True,
                )
                assistant_text = st.write_stream(wrapper)

            status_placeholder.empty()
            st.session_state.last_decision = executor.last_decision
            sources_data = None

        else:
            with st.spinner("Retrieving semantic context…"):
                context_str, sim_score, ret_time, n_chunks = rag_manager.retrieve_context(final_q)
                sources_result = rag_manager.retrieve_with_sources(final_q)
                mem_ctx, mem_tokens, mem_turns = memory_manager.get_context(
                    st.session_state.chat_history, max_turns=3, max_tokens=1500
                )
                st.session_state.last_rag_metrics    = {"chunks": n_chunks, "score": sim_score, "time": ret_time}
                st.session_state.last_memory_metrics = {"hit": mem_turns > 0, "tokens": mem_tokens, "turns": mem_turns}

            prompt = (
                "You are an AI assistant. Answer the user's question using the Document Context below.\n\n"
                f"Document Context:\n{context_str}\n\n"
            )
            if mem_ctx:
                prompt += f"Recent Conversation History:\n{mem_ctx}\n\n"
            prompt += (
                "Your response must be professional, concise, accurate, and user-focused. "
                "Use short paragraphs, bullet points when appropriate, and headings for long answers."
            )

            try:
                response = agent.invoke(prompt)
                assistant_text = response.content if hasattr(response, "content") else str(response)
            except Exception as exc:
                st.error("❌ The AI provider failed to respond.")
                with st.expander("Technical details"):
                    st.exception(exc)
                assistant_text = ""

            if assistant_text:
                with st.chat_message("assistant"):
                    st.markdown(
                        '<span class="provider-badge">✦ NeuraFlow AI</span>',
                        unsafe_allow_html=True,
                    )
                    st.write(assistant_text)

            sources_data = sources_result.get("items", []) if sources_result else None

            if sources_data:
                with st.expander(f"📚 Sources ({len(sources_data)})"):
                    for src in sources_data:
                        meta_s = src.get("metadata", {})
                        fname  = html.escape(str(meta_s.get("filename", uploaded.name)))
                        chunk  = meta_s.get("chunk_index", "?")
                        score  = src.get("score", 0.0)
                        st.markdown(
                            f"""
                            <div class="source-item">
                              <span class="source-icon">📄</span>
                              <div>
                                <div class="source-name">{fname}</div>
                                <div class="source-meta">Chunk {chunk} · Relevance {score:.2f}</div>
                              </div>
                            </div>
                            """,
                            unsafe_allow_html=True,
                        )

        # Normalise assistant_text
        if isinstance(assistant_text, list):
            assistant_text = "".join(str(x) for x in assistant_text)
        elif assistant_text is None:
            assistant_text = ""
        else:
            assistant_text = str(assistant_text)

        q_latency     = round(time.time() - q_start, 2)
        provider_name = (
            getattr(st.session_state.get("last_decision"), "actual_provider", None)
            or selected
        )

        st.session_state.chat_history.append({"role": "user", "content": final_q})
        assistant_record = {
            "role":     "assistant",
            "content":  assistant_text,
            "provider": provider_name,
            "mode":     mode,
            "latency":  q_latency,
        }
        if not enable_tools and sources_data:
            assistant_record["sources"] = sources_data
        st.session_state.chat_history.append(assistant_record)

        # Log telemetry
        rag_m = st.session_state.get("last_rag_metrics", {})
        mem_m = st.session_state.get("last_memory_metrics", {})
        decision = st.session_state.get("last_decision")
        fallback_used = getattr(decision, "fallback_used", False) if decision else False
        db_manager.log_query(
            provider=provider_name,
            latency=q_latency,
            rag_time=float(rag_m.get("time", 0.0)),
            similarity_score=float(rag_m.get("score", 0.0)),
            fallback_used=fallback_used,
            memory_hit=bool(mem_m.get("hit", False)),
            memory_tokens=int(mem_m.get("tokens", 0)),
            chat_turns=int(mem_m.get("turns", 0)),
        )

# ── System diagnostics (collapsed by default) ──────────────────────────────────
with st.expander("⚙️ System diagnostics"):
    decision = st.session_state.get("last_decision")
    diag = {
        "selected_provider":  selected,
        "search_provider":    search_provider,
        "agent_tools":        enable_tools,
        "memory":             st.session_state.get("last_memory_metrics", {}),
        "rag":                st.session_state.get("last_rag_metrics", {}),
    }
    if decision:
        diag["routing"] = {
            "task_type":        getattr(decision, "task_type", "—"),
            "selected":         getattr(decision, "selected_provider", "—"),
            "actual":           getattr(decision, "actual_provider", "—"),
            "reason":           getattr(decision, "reason", "—"),
            "fallback_used":    getattr(decision, "fallback_used", False),
        }
    st.write(diag)
