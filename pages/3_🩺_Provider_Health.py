import pandas as pd
import streamlit as st

from services.db_manager import DBManager
from ui_theme import apply_theme, RED

st.set_page_config(page_title="Provider Health - NeuraFlow AI", page_icon="🩺", layout="wide")
apply_theme()

db = DBManager()
st.markdown('<div class="nf-page-header"><div class="nf-page-icon">◉</div><div><div class="nf-page-title">Provider Health</div><div class="nf-page-subtitle">Reliability, latency, failures, and rate-limit visibility across configured LLM providers.</div></div></div>', unsafe_allow_html=True)

try:
    with db._get_connection() as conn:
        df = pd.read_sql_query("SELECT provider_name, COUNT(*) attempts, AVG(response_time) avg_latency, SUM(CASE WHEN success=1 THEN 1 ELSE 0 END) successes FROM provider_logs GROUP BY provider_name ORDER BY attempts DESC", conn)
except Exception as exc:
    st.error("Unable to load provider health data.")
    with st.expander("Technical details"):
        st.exception(exc)
    df = pd.DataFrame()

if not df.empty:
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
else:
    st.info("No provider telemetry yet. Run a few queries from the main app.")

# ------------------------------------------------------------
# LLM rate limits / quotas
# ------------------------------------------------------------
st.markdown('<div class="section-label">LLM RATE LIMITS & QUOTAS</div>', unsafe_allow_html=True)
st.caption("Limits vary by model, account, billing tier, and provider. Values marked account-specific must be checked in the provider console; they are not fabricated as fixed limits.")

limit_data = [
    {
        "Provider": "Google Gemini",
        "Typical dimensions": "RPM · Input TPM · RPD",
        "RPM": "Account / tier specific",
        "TPM": "Account / tier specific",
        "Daily": "RPD · account specific",
        "Status": "Dynamic",
    },
    {
        "Provider": "Groq",
        "Typical dimensions": "RPM · RPD · TPM · TPD",
        "RPM": "Model / plan specific",
        "TPM": "Model / plan specific",
        "Daily": "RPD / TPD",
        "Status": "Dynamic",
    },
    {
        "Provider": "OpenRouter",
        "Typical dimensions": "Requests · Tokens · Credits",
        "RPM": "Model / account specific",
        "TPM": "Model / account specific",
        "Daily": "Credits / plan specific",
        "Status": "Dynamic",
    },
    {
        "Provider": "Hugging Face",
        "Typical dimensions": "Inference requests · Credits",
        "RPM": "Account / provider specific",
        "TPM": "Provider / model specific",
        "Daily": "Plan / credit specific",
        "Status": "Dynamic",
    },
]

limits_df = pd.DataFrame(limit_data)
st.dataframe(
    limits_df,
    use_container_width=True,
    hide_index=True,
    column_config={
        "Provider": st.column_config.TextColumn("Provider", width="medium"),
        "Typical dimensions": st.column_config.TextColumn("Rate-limit dimensions", width="large"),
        "RPM": st.column_config.TextColumn("RPM", width="medium"),
        "TPM": st.column_config.TextColumn("TPM", width="medium"),
        "Daily": st.column_config.TextColumn("Daily / quota", width="medium"),
        "Status": st.column_config.TextColumn("Limits", width="small"),
    },
)

# Model-specific / provider notes
with st.expander("Provider limit details"):
    st.markdown(f"""
<div style="background:#111;border:1px solid rgba(220,38,38,.18);border-left:3px solid {RED};border-radius:10px;padding:12px 14px;line-height:1.7;color:#a3a3a3;font-size:12px;">
<b style="color:#f5f5f5">Gemini</b><br>
RPM, input TPM and RPD are controlled by the project usage tier and model. Active limits are visible in Google AI Studio.<br><br>
<b style="color:#f5f5f5">Groq</b><br>
Limits are model and plan dependent and can include RPM, RPD, TPM and TPD. Groq also exposes remaining-limit information through rate-limit response headers.<br><br>
<b style="color:#f5f5f5">OpenRouter</b><br>
Limits depend on the account, model and plan/credits. Do not treat a single global RPM/TPM number as universal across OpenRouter models.<br><br>
<b style="color:#f5f5f5">Hugging Face</b><br>
Inference availability and quotas depend on the account, selected inference provider/model, and plan. Display account-specific values when telemetry/API headers are available.
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-label">LIMIT MONITORING</div>', unsafe_allow_html=True)
l1, l2, l3 = st.columns(3)
l1.metric("429 / Rate-limit errors", "Telemetry dependent")
l2.metric("Fallback protection", "Enabled")
l3.metric("Retry strategy", "Provider dependent")
st.caption("The dashboard currently shows provider limit policy and health telemetry. Live remaining-quota values require provider-specific API headers or management APIs and are intentionally not guessed.")
