"""Deployment-safe Streamlit entrypoint with the NeuraFlow UI layer."""

import streamlit as st

from styles import get_css

_original_set_page_config = st.set_page_config


def _portable_page_config(*args, **kwargs):
    kwargs["page_icon"] = "assets/AI.svg"
    result = _original_set_page_config(*args, **kwargs)
    # Inject the design system before app.py renders its widgets.
    st.markdown(get_css(), unsafe_allow_html=True)
    st.markdown(
        """
<style>
/* Product-style workspace polish */
.block-container { max-width: 1180px !important; padding: 1.2rem 1.5rem 7rem !important; }
[data-testid="stAppViewContainer"] { background: radial-gradient(circle at 50% -10%, rgba(124,58,237,.10), transparent 42%), #080D1A !important; }

/* Compact provider controls */
div[role="radiogroup"] { gap: 6px !important; }
div[role="radiogroup"] label { border-radius: 10px !important; padding: 7px 11px !important; background: rgba(255,255,255,.025) !important; border: 1px solid rgba(255,255,255,.06) !important; }
div[role="radiogroup"] label:hover { border-color: rgba(139,92,246,.35) !important; background: rgba(139,92,246,.07) !important; }

/* Document workspace */
[data-testid="stFileUploadDropzone"] { min-height: 110px !important; }
[data-testid="stFileUploadDropzone"] section { padding: 1rem !important; }

/* Conversation */
[data-testid="stChatMessage"] { border-radius: 14px !important; margin: 8px 0 !important; }
[data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] { line-height: 1.7 !important; }

/* Sticky composer: keeps Ask the Agent accessible after long conversations. */
form[data-testid="stForm"]:has(input[placeholder*="Ask anything about the document"]) {
    position: sticky !important;
    bottom: 12px !important;
    z-index: 50 !important;
    background: rgba(8,13,26,.94) !important;
    backdrop-filter: blur(16px) !important;
    -webkit-backdrop-filter: blur(16px) !important;
    border: 1px solid rgba(139,92,246,.18) !important;
    border-radius: 16px !important;
    padding: 10px !important;
    box-shadow: 0 16px 45px rgba(0,0,0,.38) !important;
}
form[data-testid="stForm"]:has(input[placeholder*="Ask anything about the document"]) input {
    min-height: 48px !important;
    font-size: 15px !important;
    padding: 0 16px !important;
    background: rgba(255,255,255,.055) !important;
    border-color: rgba(139,92,246,.28) !important;
}
form[data-testid="stForm"]:has(input[placeholder*="Ask anything about the document"]) button {
    min-height: 44px !important;
}

/* Better metrics/cards */
[data-testid="stMetric"] {
    background: rgba(255,255,255,.025) !important;
    border: 1px solid rgba(255,255,255,.06) !important;
    border-radius: 12px !important;
    padding: 10px 12px !important;
}
[data-testid="stMetricLabel"] { color: #64748B !important; }

/* Accessible focus states */
input:focus-visible, textarea:focus-visible, button:focus-visible, [role="radio"]:focus-visible {
    outline: 2px solid #A78BFA !important;
    outline-offset: 2px !important;
}

/* Mobile */
@media (max-width: 768px) {
    .block-container { padding: .75rem .75rem 6rem !important; }
    section[data-testid="stSidebar"] { width: 86vw !important; }
    h1 { font-size: 1.8rem !important; }
    h2 { font-size: 1.35rem !important; }
    div[role="radiogroup"] { flex-wrap: wrap !important; }
    div[role="radiogroup"] label { flex: 1 1 44% !important; }
    form[data-testid="stForm"]:has(input[placeholder*="Ask anything about the document"]) { bottom: 6px !important; }
}

/* Reduced motion accessibility */
@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after { animation-duration: .01ms !important; transition-duration: .01ms !important; }
}
</style>
        """,
        unsafe_allow_html=True,
    )
    return result


st.set_page_config = _portable_page_config

import app  # noqa: E402,F401
