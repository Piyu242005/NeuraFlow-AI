import math
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from services.db_manager import DBManager

st.set_page_config(page_title="Analytics - NeuraFlow AI", page_icon="📊", layout="wide")
db = DBManager()

st.markdown("# 📊 NeuraFlow Analytics")
st.caption("Operational intelligence for routing, RAG quality, streaming, memory, and search.")

# ---------- KPIs ----------
total_queries = db.get_total_queries()
avg_latency = db.get_average_latency()
fallback_rate = db.get_fallback_rate()
provider_avail = db.get_provider_availability()
docs_indexed = db.get_documents_indexed()
total_chunks = db.get_total_chunks()
avg_sim = db.get_average_similarity()
rag_df = db.get_rag_performance_df()
avg_rag_time = rag_df["rag_time"].mean() if not rag_df.empty else 0.0
memory_hits, memory_tokens, memory_turns = db.get_memory_stats()
avg_first_token, avg_tps, stream_success_rate = db.get_streaming_stats()
total_searches = db.get_total_searches()
avg_search_time = db.get_average_search_time()

k1, k2, k3, k4 = st.columns(4)
k1.metric("Queries", total_queries)
k2.metric("Avg Latency", f"{avg_latency:.2f}s")
k3.metric("Fallback Rate", f"{fallback_rate:.1f}%")
k4.metric("Provider Availability", f"{provider_avail:.1f}%")

k5, k6, k7, k8 = st.columns(4)
k5.metric("Documents", docs_indexed)
k6.metric("Chunks", total_chunks)
k7.metric("Avg RAG Score", f"{avg_sim:.2f}")
k8.metric("Retrieval Time", f"{avg_rag_time:.2f}s")

st.divider()

# ---------- Radar / Spider ----------
df_usage = db.get_provider_usage_df()
df_latency = db.get_latency_comparison_df()
providers = sorted(set(df_usage.get("provider", pd.Series(dtype=str)).tolist()) | set(df_latency.get("provider", pd.Series(dtype=str)).tolist()))

st.subheader("🕸️ Provider Intelligence Radar")
if providers:
    latency_map = dict(zip(df_latency["provider"], df_latency["avg_latency"])) if not df_latency.empty else {}
    usage_map = dict(zip(df_usage["provider"], df_usage["count"])) if not df_usage.empty else {}
    max_usage = max(usage_map.values()) if usage_map else 1
    max_latency = max(latency_map.values()) if latency_map else 1

    fig = go.Figure()
    for provider in providers:
        usage_score = (usage_map.get(provider, 0) / max_usage) * 100 if max_usage else 0
        latency_score = 100 - ((latency_map.get(provider, 0) / max_latency) * 100) if max_latency else 0
        availability_score = 100.0
        dimensions = ["Usage", "Speed", "Availability"]
        values = [usage_score, latency_score, availability_score]
        fig.add_trace(go.Scatterpolar(r=values + values[:1], theta=dimensions + dimensions[:1], fill="toself", name=provider))
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        height=480,
        margin=dict(l=30, r=30, t=30, b=30),
        legend=dict(orientation="h", y=-0.1),
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("Run queries to populate provider intelligence.")

# ---------- Query volume / latency ----------
c1, c2 = st.columns(2)
with c1:
    st.subheader("📈 Query Volume")
    df_volume = db.get_query_volume_df()
    if not df_volume.empty:
        fig = px.area(df_volume, x="date", y="count", markers=True)
        fig.update_layout(height=350, margin=dict(l=10, r=10, t=20, b=10), showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No query history yet.")

with c2:
    st.subheader("⏱️ Provider Latency")
    if not df_latency.empty:
        fig = px.bar(df_latency, x="provider", y="avg_latency", text_auto=".2f")
        fig.update_layout(height=350, margin=dict(l=10, r=10, t=20, b=10), showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No latency data yet.")

# ---------- Reliability / RAG ----------
c3, c4 = st.columns(2)
with c3:
    st.subheader("🛡️ Reliability Mix")
    if not df_usage.empty:
        fig = px.pie(df_usage, values="count", names="provider", hole=0.55)
        fig.update_layout(height=350, margin=dict(l=10, r=10, t=20, b=10))
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No provider usage data yet.")

with c4:
    st.subheader("🔎 RAG Retrieval Profile")
    if not rag_df.empty:
        fig = px.box(rag_df, y="rag_time", points="all")
        fig.update_layout(height=350, margin=dict(l=10, r=10, t=20, b=10), yaxis_title="Retrieval Time (s)")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No RAG telemetry yet.")

# ---------- Memory / Streaming ----------
c5, c6 = st.columns(2)
with c5:
    st.subheader("🧠 Memory Utilization")
    mem_labels = ["Hits", "Avg Tokens / 100", "Avg Turns"]
    mem_values = [memory_hits, memory_tokens / 100, memory_turns]
    fig = go.Figure(go.Bar(x=mem_labels, y=mem_values, text=[f"{v:.1f}" for v in mem_values], textposition="auto"))
    fig.update_layout(height=330, margin=dict(l=10, r=10, t=20, b=10), showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

with c6:
    st.subheader("⚡ Streaming Performance")
    stream_labels = ["First Token (s)", "Tokens/sec", "Success %"]
    stream_values = [avg_first_token, avg_tps, stream_success_rate]
    fig = go.Figure(go.Bar(x=stream_labels, y=stream_values, text=[f"{v:.1f}" for v in stream_values], textposition="auto"))
    fig.update_layout(height=330, margin=dict(l=10, r=10, t=20, b=10), showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

# ---------- Search telemetry ----------
st.subheader("🌐 Web Search Telemetry")
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
        fig = px.pie(search_usage, values="count", names="provider", hole=0.55)
        fig.update_layout(height=330, margin=dict(l=10, r=10, t=20, b=10))
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No search provider data available yet.")
with q2:
    if not search_perf.empty:
        fig = px.bar(search_perf, x="provider", y="avg_search_time", text_auto=".2f")
        fig.update_layout(height=330, margin=dict(l=10, r=10, t=20, b=10), showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No search performance data available yet.")

# ---------- Health score ----------
health_score = round(max(0.0, min(100.0, 0.35 * provider_avail + 0.25 * (100 - fallback_rate) + 0.20 * stream_success_rate + 0.20 * min(avg_sim * 100, 100))), 1)
st.divider()
st.subheader("🎯 Overall System Health")
st.progress(health_score / 100, text=f"Health Score: {health_score:.1f}/100")
st.caption("Composite score based on provider availability, fallback rate, streaming success, and RAG similarity.")
