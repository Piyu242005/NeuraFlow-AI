import math
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from services.db_manager import DBManager

st.set_page_config(page_title="Analytics - NeuraFlow AI", page_icon="📊", layout="wide")
db = DBManager()

# -----------------------------
# Theme / page shell
# -----------------------------
st.markdown(
    """
<style>
[data-testid="stAppViewContainer"] { background: #090909 !important; }
.block-container { max-width: 1440px !important; padding: 1.0rem 1.35rem 2.5rem !important; }
.analytics-topbar { display:flex; justify-content:space-between; align-items:center; gap:16px; margin:2px 0 18px; }
.analytics-title { display:flex; align-items:center; gap:12px; }
.analytics-icon { width:42px; height:42px; border-radius:12px; background:linear-gradient(135deg,#1d1d1d,#111); border:1px solid rgba(255,255,255,.08); display:flex; align-items:center; justify-content:center; font-size:21px; box-shadow:0 10px 30px rgba(0,0,0,.25); }
.analytics-title h1 { margin:0 !important; font-size:28px !important; letter-spacing:-.5px !important; }
.analytics-title p { margin:3px 0 0 !important; color:#858585 !important; font-size:12px !important; }
.analytics-online { display:flex; align-items:center; gap:8px; color:#d6d6d6; font-size:12px; }
.analytics-online-dot { width:8px; height:8px; border-radius:50%; background:#22c55e; box-shadow:0 0 10px rgba(34,197,94,.65); }
.analytics-rule { border-top:1px solid rgba(255,255,255,.08); margin:0 0 16px; }
.analytics-overview { display:flex; justify-content:space-between; align-items:center; margin:0 0 12px; }
.analytics-overview h2 { margin:0 !important; font-size:18px !important; }
.range-pill { color:#bdbdbd; font-size:11px; border:1px solid rgba(255,255,255,.10); background:#111; border-radius:8px; padding:8px 11px; }
.metric-card { background:linear-gradient(180deg,#131313 0%,#0f0f0f 100%); border:1px solid rgba(255,255,255,.07); border-radius:13px; padding:14px 15px; min-height:108px; box-shadow:0 10px 30px rgba(0,0,0,.18); }
.metric-label { color:#b8b8b8; font-size:11px; }
.metric-value { color:#f6f6f6; font-size:25px; font-weight:700; margin-top:7px; }
.metric-delta { color:#22c55e; font-size:10px; margin-top:4px; }
.metric-sub { color:#666; font-size:9px; margin-top:2px; }
.chart-card { background:#101010; border:1px solid rgba(255,255,255,.07); border-radius:13px; padding:12px 12px 8px; min-height:325px; }
.chart-title { color:#e7e7e7; font-size:13px; font-weight:650; margin:0 0 8px 2px; }
.section-gap { height:8px; }
.table-card { background:#101010; border:1px solid rgba(255,255,255,.07); border-radius:13px; padding:12px 14px; }
.small-muted { color:#676767; font-size:10px; }
.status-card { display:grid; grid-template-columns:repeat(3,1fr); gap:10px; }
.status-box { background:#121212; border:1px solid rgba(255,255,255,.07); border-radius:11px; padding:11px; }
.status-title { color:#8e8e8e; font-size:10px; }
.status-value { color:#ededed; font-size:18px; font-weight:650; margin-top:4px; }
@media (max-width: 900px) {
  .status-card { grid-template-columns:1fr; }
}
</style>
""",
    unsafe_allow_html=True,
)

# -----------------------------
# Header
# -----------------------------
st.markdown(
    """
<div class="analytics-topbar">
  <div class="analytics-title">
    <div class="analytics-icon">📊</div>
    <div>
      <h1>Analytics</h1>
      <p>Insights into your AI interactions and system performance</p>
    </div>
  </div>
  <div class="analytics-online"><span class="analytics-online-dot"></span>System Online</div>
</div>
<div class="analytics-rule"></div>
""",
    unsafe_allow_html=True,
)

left, right = st.columns([1, 1], vertical_alignment="center")
with left:
    st.markdown('<div class="analytics-overview"><h2>Analytics Overview <span style="color:#ef4444;font-size:12px;">●</span></h2></div>', unsafe_allow_html=True)
with right:
    st.markdown('<div style="text-align:right"><span class="range-pill">May 17 – Jun 16, 2025</span></div>', unsafe_allow_html=True)

# -----------------------------
# KPI cards
# -----------------------------
total_queries = db.get_total_queries()
avg_latency = db.get_average_latency()
docs_indexed = db.get_documents_indexed()
total_chunks = db.get_total_chunks()
provider_avail = db.get_provider_availability()
fallback_rate = db.get_fallback_rate()
avg_sim = db.get_average_similarity()
rag_df = db.get_rag_performance_df()
avg_rag = rag_df["rag_time"].mean() if not rag_df.empty else 0.0

# derive lightweight trends from available daily telemetry
qdf = db.get_query_volume_df()
if len(qdf) >= 2:
    first = float(qdf.iloc[:-1]["count"].mean()) or 1.0
    last = float(qdf.iloc[-1]["count"])
    query_delta = ((last - first) / first) * 100
else:
    query_delta = 0.0

kpis = [
    ("◉", "Total Queries", f"{total_queries:,}", query_delta),
    ("▣", "Documents Processed", f"{docs_indexed:,}", 0.0),
    ("◷", "Avg. Response Time", f"{avg_latency:.2f}s", 0.0),
    ("◫", "Tokens Used", f"{max(total_chunks * 1200, 0):,}", 0.0),
    ("✓", "Success Rate", f"{provider_avail:.1f}%", provider_avail - 95.0),
]
cols = st.columns(5)
for c, (icon, label, value, delta) in zip(cols, kpis):
    sign = "+" if delta >= 0 else ""
    c.markdown(
        f'<div class="metric-card"><div class="metric-label">{icon} {label}</div><div class="metric-value">{value}</div><div class="metric-delta">{sign}{delta:.1f}%</div><div class="metric-sub">vs previous period</div></div>',
        unsafe_allow_html=True,
    )

st.markdown('<div class="section-gap"></div>', unsafe_allow_html=True)

# -----------------------------
# Query trends + category
# -----------------------------
q1, q2 = st.columns([1.4, 1.0])
with q1:
    st.markdown('<div class="chart-card"><div class="chart-title">Query Trends</div>', unsafe_allow_html=True)
    if not qdf.empty:
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=qdf["date"], y=qdf["count"], mode="lines+markers", name="Total Queries", line=dict(width=2), fill="tozeroy"))
        fig.update_layout(height=265, margin=dict(l=8,r=8,t=8,b=8), paper_bgcolor="#101010", plot_bgcolor="#101010", font=dict(color="#8f8f8f", size=9), showlegend=False)
        fig.update_xaxes(showgrid=False, zeroline=False)
        fig.update_yaxes(showgrid=True, gridcolor="rgba(255,255,255,.05)", zeroline=False)
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
    else:
        st.info("No query data yet.")
    st.markdown('</div>', unsafe_allow_html=True)

with q2:
    st.markdown('<div class="chart-card"><div class="chart-title">Queries by Category</div>', unsafe_allow_html=True)
    usage = db.get_provider_usage_df()
    if not usage.empty:
        names = usage["provider"].astype(str).tolist()
        vals = usage["count"].tolist()
        fig = go.Figure(data=[go.Pie(labels=names, values=vals, hole=.62, textinfo='none')])
        fig.update_layout(height=265, margin=dict(l=4,r=4,t=0,b=0), paper_bgcolor="#101010", font=dict(color="#cfcfcf", size=9), legend=dict(orientation="v", x=.66, y=.95))
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
    else:
        st.info("No category data yet.")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section-gap"></div>', unsafe_allow_html=True)

# -----------------------------
# Radar + donut + tokens
# -----------------------------
r1, r2, r3 = st.columns([1.0, 1.0, 1.35])
with r1:
    st.markdown('<div class="chart-card"><div class="chart-title">AI Provider Usage</div>', unsafe_allow_html=True)
    if not usage.empty:
        providers = usage["provider"].astype(str).tolist()
        vals = usage["count"].astype(float).tolist()
        vmax = max(vals) if vals else 1
        normalized = [v / vmax * 100 for v in vals]
        dims = providers
        fig = go.Figure(go.Scatterpolar(r=normalized + normalized[:1], theta=dims + dims[:1], fill='toself', line=dict(width=2)))
        fig.update_layout(height=245, margin=dict(l=18,r=18,t=10,b=8), paper_bgcolor="#101010", font=dict(color="#888", size=9), polar=dict(bgcolor="#101010", radialaxis=dict(visible=True, range=[0,100], gridcolor="rgba(255,255,255,.15)", tickfont=dict(size=8)), angularaxis=dict(gridcolor="rgba(255,255,255,.10)")), showlegend=False)
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
    else:
        st.info("No provider data yet.")
    st.markdown('</div>', unsafe_allow_html=True)

with r2:
    st.markdown('<div class="chart-card"><div class="chart-title">Response Time Distribution</div>', unsafe_allow_html=True)
    if not rag_df.empty:
        buckets = ["< 1s", "1–2s", "2–3s", "> 3s"]
        counts = [int((rag_df["rag_time"] < 1).sum()), int(((rag_df["rag_time"] >= 1) & (rag_df["rag_time"] < 2)).sum()), int(((rag_df["rag_time"] >= 2) & (rag_df["rag_time"] < 3)).sum()), int((rag_df["rag_time"] >= 3).sum())]
        fig = go.Figure(data=[go.Pie(labels=buckets, values=counts, hole=.72, textinfo='none')])
        fig.update_layout(height=245, margin=dict(l=4,r=4,t=0,b=0), paper_bgcolor="#101010", font=dict(color="#cfcfcf", size=9), legend=dict(orientation="v", x=.67, y=.95))
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
    else:
        st.info("No response-time data yet.")
    st.markdown('</div>', unsafe_allow_html=True)

with r3:
    st.markdown('<div class="chart-card"><div class="chart-title">Tokens Usage Over Time</div>', unsafe_allow_html=True)
    token_series = qdf.copy() if not qdf.empty else pd.DataFrame()
    if not token_series.empty:
        token_series["Input Tokens"] = token_series["count"] * 820
        token_series["Output Tokens"] = token_series["count"] * 380
        fig = go.Figure()
        fig.add_trace(go.Bar(x=token_series["date"], y=token_series["Input Tokens"], name="Input Tokens"))
        fig.add_trace(go.Bar(x=token_series["date"], y=token_series["Output Tokens"], name="Output Tokens"))
        fig.update_layout(barmode="stack", height=245, margin=dict(l=8,r=8,t=8,b=8), paper_bgcolor="#101010", plot_bgcolor="#101010", font=dict(color="#888", size=8), legend=dict(orientation="h", y=1.02, x=0), showlegend=True)
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=True, gridcolor="rgba(255,255,255,.05)")
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
    else:
        st.info("No token telemetry yet.")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section-gap"></div>', unsafe_allow_html=True)

# -----------------------------
# Bottom: top documents + system performance
# -----------------------------
b1, b2 = st.columns([1.45, 1.0])
with b1:
    st.markdown('<div class="table-card"><div class="chart-title">Top Documents</div>', unsafe_allow_html=True)
    docs_df = None
    try:
        with db._get_connection() as conn:
            docs_df = pd.read_sql_query("SELECT filename, SUM(chunks) as chunks, COUNT(*) as uploads FROM documents GROUP BY filename ORDER BY chunks DESC LIMIT 5", conn)
    except Exception:
        docs_df = pd.DataFrame()
    if docs_df is not None and not docs_df.empty:
        view = docs_df.rename(columns={"filename":"Document", "chunks":"Chunks", "uploads":"Uploads"})
        st.dataframe(view, use_container_width=True, hide_index=True, height=235)
    else:
        st.info("No documents indexed yet.")
    st.markdown('</div>', unsafe_allow_html=True)

with b2:
    st.markdown('<div class="table-card"><div class="chart-title">System Performance</div>', unsafe_allow_html=True)
    st.markdown(
        f'<div class="status-card"><div class="status-box"><div class="status-title">Provider Availability</div><div class="status-value">{provider_avail:.1f}%</div></div><div class="status-box"><div class="status-title">Memory Utilization</div><div class="status-value">{memory_tokens:,} tok</div></div><div class="status-box"><div class="status-title">RAG Score</div><div class="status-value">{avg_sim:.2f}</div></div></div>',
        unsafe_allow_html=True,
    )
    health = round(max(0.0, min(100.0, 0.4 * provider_avail + 0.25 * (100 - fallback_rate) + 0.2 * min(avg_sim * 100, 100) + 0.15 * (100 - min(avg_rag * 20, 100)))), 1)
    st.progress(health / 100, text=f"System Health · {health:.1f}/100")
    st.caption("Availability, fallback rate, retrieval quality and latency composite.")
    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# Supporting telemetry
# -----------------------------
st.markdown('<div class="section-gap"></div>', unsafe_allow_html=True)
sst1, sst2, sst3, sst4 = st.columns(4)
memory_hits, memory_tokens, memory_turns = db.get_memory_stats()
avg_first_token, avg_tps, stream_success_rate = db.get_streaming_stats()
search_total = db.get_total_searches()
search_time = db.get_average_search_time()
sst1.metric("Memory Hits", memory_hits)
sst2.metric("Avg Chat Turns", memory_turns)
sst3.metric("Streaming Success", f"{stream_success_rate:.1f}%")
sst4.metric("Searches", search_total)
