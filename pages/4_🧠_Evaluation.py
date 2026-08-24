import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from services.db_manager import DBManager
from ui_theme import apply_theme, plotly_layout, RED

st.set_page_config(page_title="Evaluation - NeuraFlow AI", page_icon="🧠", layout="wide")
apply_theme()

db = DBManager()
st.markdown('<div class="nf-page-header"><div class="nf-page-icon">✦</div><div><div class="nf-page-title">RAG & AI Evaluation</div><div class="nf-page-subtitle">Measure retrieval quality, response efficiency, and reliability.</div></div></div>', unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Avg Similarity", f"{db.get_average_similarity():.2f}")
c2.metric("Avg Latency", f"{db.get_average_latency():.2f}s")
c3.metric("Fallback Rate", f"{db.get_fallback_rate():.1f}%")
c4.metric("Provider Availability", f"{db.get_provider_availability():.1f}%")

st.markdown('<div class="section-label">QUALITY SIGNALS</div>', unsafe_allow_html=True)
try:
    rag_df = db.get_rag_performance_df()
except Exception:
    rag_df = pd.DataFrame()

if rag_df.empty:
    st.info("No RAG telemetry is available yet. Run document queries to populate evaluation metrics.")
else:
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**Retrieval Time**")
        fig = go.Figure(go.Scatter(y=rag_df["rag_time"].tolist(), mode="lines+markers", line=dict(color=RED, width=2), marker=dict(color=RED, size=5)))
        plotly_layout(fig, 340)
        fig.update_layout(showlegend=False, yaxis_title="Seconds", xaxis_title="Query")
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
    with c2:
        st.markdown("**Retrieval Distribution**")
        fig = go.Figure(go.Box(y=rag_df["rag_time"].tolist(), boxpoints="all", line=dict(color=RED), marker=dict(color=RED)))
        plotly_layout(fig, 340)
        fig.update_layout(showlegend=False, yaxis_title="Seconds")
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

st.markdown('<div class="section-label">EVALUATION GUIDANCE</div>', unsafe_allow_html=True)
st.info("For rigorous offline evaluation, add human relevance, faithfulness, correctness, and hallucination labels to the evaluation dataset, then run the utilities under evaluation/.")
