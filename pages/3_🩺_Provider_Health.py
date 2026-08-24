import streamlit as st
from services.db_manager import DBManager

st.set_page_config(page_title="Provider Health - NeuraFlow AI", page_icon="🩺", layout="wide")

db = DBManager()
st.title("🩺 Provider Health")
st.caption("Reliability, latency, and failure signals across configured LLM providers.")

try:
    with db._get_connection() as conn:
        df = __import__("pandas").read_sql_query(
            "SELECT provider_name, COUNT(*) attempts, AVG(response_time) avg_latency, SUM(CASE WHEN success=1 THEN 1 ELSE 0 END) successes FROM provider_logs GROUP BY provider_name ORDER BY attempts DESC",
            conn,
        )
except Exception as exc:
    st.error("Unable to load provider health data.")
    with st.expander("Technical details"):
        st.exception(exc)
    df = __import__("pandas").DataFrame()

if df.empty:
    st.info("No provider telemetry yet. Run a few queries from the main app.")
else:
    df["success_rate"] = (df["successes"] / df["attempts"] * 100).round(1)
    for _, row in df.iterrows():
        c1, c2, c3, c4 = st.columns([2.2, 1.2, 1.2, 1.4])
        c1.markdown(f"**{row['provider_name']}**")
        c2.metric("Attempts", int(row["attempts"]))
        c3.metric("Avg Latency", f"{row['avg_latency']:.2f}s")
        c4.metric("Success", f"{row['success_rate']:.1f}%")
        st.progress(min(max(float(row["success_rate"]) / 100, 0), 1))
        st.divider()
