import pandas as pd
import streamlit as st

from services.db_manager import DBManager
from ui_theme import apply_theme

st.set_page_config(page_title="Documents - NeuraFlow AI", page_icon="📄", layout="wide")
apply_theme()

db = DBManager()
st.markdown('<div class="nf-page-header"><div class="nf-page-icon">📄</div><div><div class="nf-page-title">Documents</div><div class="nf-page-subtitle">Manage indexed knowledge and ingestion history.</div></div></div>', unsafe_allow_html=True)

try:
    with db._get_connection() as conn:
        df = pd.read_sql_query("SELECT filename, pages, chunks, file_size, upload_time FROM documents ORDER BY upload_time DESC", conn)
except Exception as exc:
    st.error("Unable to load document history.")
    with st.expander("Technical details"):
        st.exception(exc)
    df = pd.DataFrame()

c1, c2, c3 = st.columns(3)
c1.metric("Documents", len(df))
c2.metric("Pages", int(df["pages"].sum()) if not df.empty else 0)
c3.metric("Chunks", int(df["chunks"].sum()) if not df.empty else 0)

st.markdown('<div class="section-label">KNOWLEDGE BASE</div>', unsafe_allow_html=True)
if df.empty:
    st.info("No indexed documents yet. Upload a PDF from the main workspace to populate this page.")
else:
    search = st.text_input("Search documents", placeholder="Filter by filename…", label_visibility="collapsed")
    view = df.copy()
    if search.strip():
        view = view[view["filename"].str.contains(search.strip(), case=False, na=False)]
    view["file_size_mb"] = (view["file_size"] / (1024 * 1024)).round(2)
    view = view.drop(columns=["file_size"])
    view.columns = ["Filename", "Pages", "Chunks", "Upload Time", "Size (MB)"]
    st.dataframe(view, use_container_width=True, hide_index=True)
