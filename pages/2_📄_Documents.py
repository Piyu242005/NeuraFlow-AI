import html
import streamlit as st
from services.db_manager import DBManager

st.set_page_config(page_title="Documents - NeuraFlow AI", page_icon="📄", layout="wide")

db = DBManager()
st.title("📄 Document Workspace")
st.caption("Review indexed documents, chunk counts, and ingestion history.")

try:
    with db._get_connection() as conn:
        df = __import__("pandas").read_sql_query(
            "SELECT filename, pages, chunks, file_size, upload_time FROM documents ORDER BY upload_time DESC",
            conn,
        )
except Exception as exc:
    st.error("Unable to load document history.")
    with st.expander("Technical details"):
        st.exception(exc)
    df = __import__("pandas").DataFrame()

c1, c2, c3 = st.columns(3)
c1.metric("Documents", len(df))
c2.metric("Pages", int(df["pages"].sum()) if not df.empty else 0)
c3.metric("Chunks", int(df["chunks"].sum()) if not df.empty else 0)

st.divider()
if df.empty:
    st.info("No indexed documents yet. Upload a PDF from the main workspace to populate this page.")
else:
    search = st.text_input("Search documents", placeholder="Filter by filename…")
    view = df.copy()
    if search.strip():
        view = view[view["filename"].str.contains(search.strip(), case=False, na=False)]
    view["file_size_mb"] = (view["file_size"] / (1024 * 1024)).round(2)
    view = view.drop(columns=["file_size"])
    view.columns = ["Filename", "Pages", "Chunks", "Upload Time", "Size (MB)"]
    st.dataframe(view, use_container_width=True, hide_index=True)
