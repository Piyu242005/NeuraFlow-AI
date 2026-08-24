import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from services.db_manager import DBManager
from ui_theme import apply_theme, plotly_layout, RED, RED_DARK, RED_LIGHT, RED_SOFT

st.set_page_config(page_title="Analytics - NeuraFlow AI", page_icon="📊", layout="wide")
apply_theme()
db = DBManager()

st.markdown('<div class="nf-page-header"><div class="nf-page-icon">▥</div><div><div class="nf-page-title">Analytics</div><div class="nf-page-subtitle">Insights into your AI interactions and system performance.</div></div></div>', unsafe_allow_html=True)

# KPIs
total_queries = db.get_total_queries()
avg_latency = db.get_average_latency()
docs_indexed = db.get_documents_indexed()
total_chunks = db.get_total_chunks()
provider_avail = db.get_provider_availability()
fallback_rate = db.get_fallback_rate()
avg_sim = db.get_average_similarity()
rag_df = db.get_rag_performance_df()
avg_rag = rag_df["rag_time"].mean() if not rag_df.empty else 0.0

# Define memory/streaming telemetry before any section can reference it.
memory_hits, memory_tokens, memory_turns = db.get_memory_stats()
avg_first_token, avg_tps, stream_success_rate = db.get_streaming_stats()

total_searches = db.get_total_searches()
avg_search_time = db.get_average_search_time()
qdf = db.get_query_volume_df()
usage = db.get_provider_usage_df()
latency = db.get_latency_comparison_df()

k1, k2, k3, k4, k5 = st.columns(5)
k1.metric("Total Queries", f"{total_queries:,}")
k2.metric("Documents Processed", f"{docs_indexed:,}")
k3.metric("Avg. Response Time", f"{avg_latency:.2f}s")
k4.metric("Chunks Indexed", f"{total_chunks:,}")
k5.metric("Success Rate", f"{provider_avail:.1f}%")

# Query trends and provider distribution
c1, c2 = st.columns([1.35, 1])
with c1:
    st.markdown("**Query Trends**")
    if not qdf.empty:
        fig = px.area(qdf, x="date", y="count")
        fig.update_traces(line_color=RED, fillcolor="rgba(220,38,38,.18)")
        plotly_layout(fig, 320)
        fig.update_layout(showlegend=False, yaxis_title="Queries", xaxis_title="")
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
    else:
        st.info("No query history yet.")
with c2:
    st.markdown("**Queries by Provider**")
    if not usage.empty:
        fig = px.pie(usage, values="count", names="provider", hole=.62)
        fig.update_traces(marker=dict(colors=[RED, RED_DARK, RED_LIGHT, RED_SOFT, "#7f1d1d"]))
        plotly_layout(fig, 320)
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
    else:
        st.info("No provider data yet.")

# Spider + latency + RAG
r1, r2, r3 = st.columns([1.0, 1.0, 1.15])
with r1:
    st.markdown("**AI Provider Usage — Spider**")
    if not usage.empty:
        providers = usage["provider"].astype(str).tolist()
        vals = usage["count"].astype(float).tolist()
        vmax = max(vals) if vals else 1
        normalized = [v / vmax * 100 for v in vals]
        fig = go.Figure(go.Scatterpolar(r=normalized + normalized[:1], theta=providers + providers[:1], fill="toself", line=dict(color=RED, width=2), fillcolor="rgba(220,38,38,.22)"))
        fig.update_layout(height=280, paper_bgcolor="#0a0a0a", polar=dict(bgcolor="#0a0a0a", radialaxis=dict(visible=True, range=[0,100], gridcolor="rgba(255,255,255,.10)"), angularaxis=dict(gridcolor="rgba(255,255,255,.10)")), margin=dict(l=10,r=10,t=10,b=10), showlegend=False)
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
    else:
        st.info("No provider data yet.")
with r2:
    st.markdown("**Response Time Distribution**")
    if not rag_df.empty:
        fig = px.box(rag_df, y="rag_time", points="all")
        fig.update_traces(marker_color=RED, line_color=RED)
        plotly_layout(fig, 280)
        fig.update_layout(showlegend=False, yaxis_title="Seconds")
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
    else:
        st.info("No response-time data yet.")
with r3:
    st.markdown("**Provider Latency**")
    if not latency.empty:
        fig = px.bar(latency, x="provider", y="avg_latency")
        fig.update_traces(marker_color=RED)
        plotly_layout(fig, 280)
        fig.update_layout(showlegend=False, yaxis_title="Seconds", xaxis_title="")
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
    else:
        st.info("No latency data yet.")

# Memory and streaming
m1, m2 = st.columns(2)
with m1:
    st.markdown("**Memory Utilization**")
    fig = go.Figure(go.Bar(x=["Hits", "Avg Tokens / 100", "Avg Turns"], y=[memory_hits, memory_tokens / 100, memory_turns], marker_color=RED, text=[memory_hits, memory_tokens / 100, memory_turns], textposition="auto"))
    plotly_layout(fig, 280)
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
with m2:
    st.markdown("**Streaming Performance**")
    fig = go.Figure(go.Bar(x=["First Token", "Tokens/sec", "Success %"], y=[avg_first_token, avg_tps, stream_success_rate], marker_color=RED_DARK, text=[avg_first_token, avg_tps, stream_success_rate], textposition="auto"))
    plotly_layout(fig, 280)
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

# Search telemetry
st.markdown('<div class="section-label">WEB SEARCH TELEMETRY</div>', unsafe_allow_html=True)
s1, s2, s3, s4 = st.columns(4)
s1.metric("Searches", total_searches)
s2.metric("Avg Search Time", f"{avg_search_time:.2f}s")
s3.metric("Tavily", db.get_tavily_searches())
s4.metric("DuckDuckGo", db.get_ddg_searches())
search_usage = db.get_search_provider_usage_df()
search_perf = db.get_search_performance_df()
q1, q2 = st.columns(2)
with q1:
    if not search_usage.empty:
        fig = px.pie(search_usage, values="count", names="provider", hole=.62)
        fig.update_traces(marker=dict(colors=[RED, RED_DARK, RED_LIGHT, RED_SOFT]))
        plotly_layout(fig, 300)
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
    else:
        st.info("No search provider data available yet.")
with q2:
    if not search_perf.empty:
        fig = px.bar(search_perf, x="provider", y="avg_search_time")
        fig.update_traces(marker_color=RED)
        plotly_layout(fig, 300)
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
    else:
        st.info("No search performance data available yet.")

# Health
health_score = round(max(0.0, min(100.0, 0.35 * provider_avail + 0.25 * (100 - fallback_rate) + 0.20 * stream_success_rate + 0.20 * min(avg_sim * 100, 100))), 1)
st.markdown('<div class="section-label">SYSTEM HEALTH</div>', unsafe_allow_html=True)
st.progress(health_score / 100, text=f"Health Score · {health_score:.1f}/100")
st.caption("Composite score based on provider availability, fallback rate, streaming success, and RAG similarity.")
