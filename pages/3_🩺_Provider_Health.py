import pandas as pd
import streamlit as st

from services.db_manager import DBManager
from ui_theme import apply_theme, RED

st.set_page_config(page_title="Provider Health - NeuraFlow AI", page_icon="🩺", layout="wide")
apply_theme()

db = DBManager()
st.markdown('<div class="nf-page-header"><div class="nf-page-icon">◉</div><div><div class="nf-page-title">Provider Health</div><div class="nf-page-subtitle">Reliability, latency, and failure signals across configured LLM providers.</div></div></div>', unsafe_allow_html=True)

try:
    with db._get_connection() as conn:
        df = pd.read_sql_query("SELECT provider_name, COUNT(*) attempts, AVG(response_time) avg_latency, SUM(CASE WHEN success=1 THEN 1 ELSE 0 END) successes FROM provider_logs GROUP BY provider_name ORDER BY attempts DESC", conn)
except Exception as exc:
    st.error("Unable to load provider health data.")
    with st.expander("Technical details"):
        st.exception(exc)
    df = pd.DataFrame()

if df.empty:
    st.info("No provider telemetry yet. Run a few queries from the main app.")
else:
    df["success_rate"] = (df["successes"] / df["attempts"] * 100).round(1)
    avg_success = df["success_rate"].mean()
    avg_latency = df["avg_latency"].mean()
    c1, c2, c3 = st.columns(3)
    c1.metric("Providers", len(df))
    c2.metric("Avg Success", f"{avg_success:.1f}%")
    c3.metric("Avg Latency", f"{avg_latency:.2f}s")
    st.markdown('<div class="section-label">PROVIDER STATUS</div>', unsafe_allow_html=True)
    for _, row in df.iterrows():
        c1, c2, c3, c4 = st.columns([2.2, 1.2, 1.2, 1.4])
        c1.markdown(f"**{row['provider_name']}**")
        c2.metric("Attempts", int(row["attempts"]))
        c3.metric("Latency", f"{row['avg_latency']:.2f}s")
        c4.metric("Success", f"{row['success_rate']:.1f}%")
        st.progress(min(max(float(row["success_rate"]) / 100, 0), 1))
