import streamlit as st
from services.db_manager import DBManager

st.set_page_config(page_title="Evaluation - NeuraFlow AI", page_icon="🧠", layout="wide")

db = DBManager()
st.title("🧠 RAG & AI Evaluation")
st.caption("Track retrieval quality, response efficiency, and reliability signals.")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Avg Similarity", f"{db.get_average_similarity():.2f}")
c2.metric("Avg Latency", f"{db.get_average_latency():.2f}s")
c3.metric("Fallback Rate", f"{db.get_fallback_rate():.1f}%")
c4.metric("Provider Availability", f"{db.get_provider_availability():.1f}%")

st.divider()
st.subheader("Evaluation guidance")
st.markdown("""
Use this page as the operational evaluation workspace. For rigorous offline evaluation, extend the repository dataset with human relevance, faithfulness, correctness, and hallucination labels, then run the evaluation utilities under `evaluation/`.
""")

try:
    rag_df = db.get_rag_performance_df()
except Exception:
    rag_df = None

if rag_df is not None and not rag_df.empty:
    st.subheader("Retrieval performance")
    st.line_chart(rag_df[["rag_time"]])
else:
    st.info("No RAG telemetry is available yet.")
