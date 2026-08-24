import streamlit as st

from services.db_manager import DBManager
from ui_theme import apply_theme

st.set_page_config(page_title="System - NeuraFlow AI", page_icon="⚙️", layout="wide")
apply_theme()

db = DBManager()
st.markdown('<div class="nf-page-header"><div class="nf-page-icon">⚙</div><div><div class="nf-page-title">System</div><div class="nf-page-subtitle">Runtime configuration, capabilities, and operational signals.</div></div></div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
c1.metric("Providers", "Dynamic")
c2.metric("Vector Store", "ChromaDB")
c3.metric("Analytics Store", "SQLite")

st.markdown('<div class="section-label">CAPABILITIES</div>', unsafe_allow_html=True)
left, right = st.columns(2)
capabilities = ["Persistent document RAG", "Policy-based multi-LLM routing", "Automatic provider fallback", "Streaming responses", "Conversation memory", "Agent tools", "Provider telemetry", "Offline evaluation"]
for i, item in enumerate(capabilities):
    (left if i % 2 == 0 else right).markdown(f"**✓** {item}")

st.markdown('<div class="section-label">RUNTIME TELEMETRY</div>', unsafe_allow_html=True)
q = db.get_total_queries()
d = db.get_documents_indexed()
ch = db.get_total_chunks()
fb = db.get_fallback_rate()
pa = db.get_provider_availability()
a, b, c, e, f = st.columns(5)
a.metric("Queries", q)
b.metric("Documents", d)
c.metric("Chunks", ch)
e.metric("Fallback", f"{fb:.1f}%")
f.metric("Availability", f"{pa:.1f}%")
