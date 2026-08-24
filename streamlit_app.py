"""Deployment-safe Streamlit entrypoint.

The legacy app.py contains a Windows-local page-icon path. This launcher
normalizes that argument so the application works on Linux/Streamlit Cloud
without changing the existing UI implementation.
"""

import streamlit as st

_original_set_page_config = st.set_page_config


def _portable_page_config(*args, **kwargs):
    kwargs["page_icon"] = "assets/AI.svg"
    return _original_set_page_config(*args, **kwargs)


st.set_page_config = _portable_page_config

import app  # noqa: E402,F401
