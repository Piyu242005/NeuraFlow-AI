import streamlit as st
from services.db_manager import DBManager

st.set_page_config(page_title="System - NeuraFlow AI", page_icon="⚙️", layout="wide")

db = DBManager()
st.title("⚙️ System")
st.caption("Operational configuration, capabilities, and runtime signals.")

c1, c2, c3 = st.columns(3)
c1.metric("Providers Available", "Dynamic")
c2.metric("Vector Store", "ChromaDB")
c3.metric("Analytics Store", "SQLite")

st.divider()
st.subheader("Capabilities")
for item in ["Persistent document RAG", "Policy-based multi-LLM routing", "Automatic provider fallback", "Streaming responses", "Conversation memory", "Agent tools", "Provider telemetry", "Offline evaluation"]:
    st.markdown(f"✅ {item}")

st.divider()
st.subheader("Runtime telemetry")
st.json({
    "queries": db.get_total_queries(),
    "documents": db.get_documents_indexed(),
    "chunks": db.get_total_chunks(),
    "fallback_rate": round(db.get_fallback_rate(), 2),
    "provider_availability": round(db.get_provider_availability(), 2),
})
