"""Shared Streamlit black/red theme for every NeuraFlow page."""

import streamlit as st

RED = "#dc2626"
RED_DARK = "#991b1b"
RED_LIGHT = "#ef4444"
RED_SOFT = "#f87171"
BLACK = "#0a0a0a"
SURFACE = "#111111"
SURFACE_2 = "#171717"
TEXT = "#f5f5f5"
MUTED = "#a3a3a3"
GRID = "rgba(255,255,255,0.07)"


def apply_theme() -> None:
    """Apply the shared black/red visual system to a Streamlit page."""
    st.markdown(
        f"""
<style>
:root {{
  --nf-red: {RED}; --nf-red-dark: {RED_DARK}; --nf-red-light: {RED_LIGHT};
  --nf-black: {BLACK}; --nf-surface: {SURFACE}; --nf-surface-2: {SURFACE_2};
  --nf-text: {TEXT}; --nf-muted: {MUTED};
}}
.stApp {{ background:{BLACK} !important; color:{TEXT} !important; }}
header {{ background:transparent !important; }}
#MainMenu {{ visibility:visible !important; display:block !important; }}
footer {{ visibility:hidden !important; }}
.block-container {{ max-width:1400px !important; padding-top:1.2rem !important; }}

/* Native multipage navigation */
section[data-testid="stSidebar"] {{ background:{BLACK} !important; border-right:1px solid rgba(220,38,38,.22) !important; }}
section[data-testid="stSidebarNav"] {{ padding-top:18px !important; }}
section[data-testid="stSidebarNav"] a {{ color:#a3a3a3 !important; border-radius:8px !important; margin:2px 8px !important; transition:background .18s ease,color .18s ease,border-color .18s ease !important; }}
section[data-testid="stSidebarNav"] a:hover {{ background:rgba(220,38,38,.10) !important; color:#f5f5f5 !important; }}
section[data-testid="stSidebarNav"] a[aria-current="page"] {{ background:linear-gradient(90deg,rgba(220,38,38,.20),rgba(220,38,38,.07)) !important; color:#fff !important; border-left:3px solid {RED} !important; font-weight:700 !important; }}
section[data-testid="stSidebarNav"] a[aria-current="page"] span {{ color:#fff !important; }}
section[data-testid="stSidebarNav"] div[data-testid="stSidebarNavSeparator"] {{ border-color:rgba(255,255,255,.07) !important; }}

/* Common page header */
.nf-page-header {{ display:flex;align-items:center;gap:14px;padding:18px 20px;margin-bottom:18px;background:linear-gradient(135deg,rgba(220,38,38,.10),rgba(0,0,0,.20));border:1px solid rgba(220,38,38,.18);border-radius:14px; }}
.nf-page-icon {{ width:44px;height:44px;display:flex;align-items:center;justify-content:center;border-radius:11px;background:linear-gradient(135deg,{RED},{RED_DARK});font-size:21px;box-shadow:0 8px 22px rgba(220,38,38,.22); }}
.nf-page-title {{ font-size:25px;font-weight:800;color:#fff;letter-spacing:-.5px;margin:0; }}
.nf-page-subtitle {{ font-size:12px;color:{MUTED};margin:3px 0 0; }}

/* KPI cards */
[data-testid="stMetric"] {{ background:{SURFACE} !important;border:1px solid rgba(255,255,255,.07) !important;border-radius:11px !important;padding:13px 15px !important; }}
[data-testid="stMetricLabel"] {{ color:{MUTED} !important; }}
[data-testid="stMetricValue"] {{ color:#fff !important; }}
[data-testid="stMetricDelta"] {{ color:{RED_LIGHT} !important; }}

/* Controls */
.stButton > button,.stDownloadButton > button {{ border-radius:8px !important;border-color:rgba(220,38,38,.28) !important; }}
.stButton > button:hover,.stDownloadButton > button:hover {{ border-color:{RED} !important;color:#fff !important;background:rgba(220,38,38,.10) !important; }}
input:focus,textarea:focus {{ border-color:{RED} !important;box-shadow:0 0 0 2px rgba(220,38,38,.12) !important; }}

/* Alerts/status use red-neutral language rather than green/blue accents */
.stAlert {{ background:{SURFACE} !important;border-color:rgba(220,38,38,.20) !important; }}
.stSuccess,.stInfo,.stWarning,.stError {{ border-color:rgba(220,38,38,.25) !important; background:rgba(220,38,38,.05) !important; }}

/* Tables/cards */
[data-testid="stDataFrame"] {{ border:1px solid rgba(255,255,255,.07) !important;border-radius:10px !important;overflow:hidden !important; }}
.js-plotly-plot .plotly {{ border:1px solid rgba(255,255,255,.06);border-radius:10px;overflow:hidden; }}

@media (max-width:768px) {{ .block-container {{ padding:.8rem !important; }} .nf-page-header {{ padding:14px; }} .nf-page-title {{ font-size:21px; }} }}
</style>
""",
        unsafe_allow_html=True,
    )


def plotly_layout(fig, height=320):
    """Apply the shared black/red Plotly theme to a figure."""
    fig.update_layout(
        template="plotly_dark",
        height=height,
        paper_bgcolor=BLACK,
        plot_bgcolor=BLACK,
        font=dict(color=TEXT, family="Inter, sans-serif"),
        margin=dict(l=20, r=20, t=40, b=20),
        coloraxis=dict(colorscale=[[0, RED_DARK], [0.5, RED], [1, RED_SOFT]]),
        colorway=[RED, RED_LIGHT, RED_SOFT, RED_DARK, "#7f1d1d"],
        xaxis=dict(gridcolor=GRID, zerolinecolor=GRID),
        yaxis=dict(gridcolor=GRID, zerolinecolor=GRID),
    )
    return fig
