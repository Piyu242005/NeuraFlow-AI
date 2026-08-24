# flake8: noqa: E501
"""NeuraFlow AI — unified design system. Black / red theme."""


def get_css() -> str:
    return """
<style>
/* ============================================================
   DESIGN TOKENS  ·  black / red
   ============================================================ */
:root {
  --bg: #0a0a0a;
  --surface: #111111;
  --surface2: #1a1a1a;
  --border: rgba(255,255,255,0.07);
  --primary: #dc2626;
  --accent: #b91c1c;
  --text: #f5f5f5;
  --text-muted: #a3a3a3;
  --text-dim: #525252;
  --success: #22c55e;
  --warning: #f59e0b;
  --radius-sm: 6px;
  --radius: 10px;
  --radius-lg: 14px;
}

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

/* Do not override Streamlit's internal icon font. */
body, .stApp, .stMarkdown, .stText, .stCaption,
input, textarea, button, select {
  font-family: Inter, -apple-system, system-ui, sans-serif !important;
}

/* ============================================================
   APP BASE
   ============================================================ */
.stApp { background: var(--bg) !important; color: var(--text) !important; }
#MainMenu { visibility: visible !important; display: block !important; }
header { visibility: visible !important; display: block !important; background: transparent !important; }
footer { visibility: hidden !important; }

.block-container {
  padding-top: 0 !important;
  padding-left: 2rem !important;
  padding-right: 2rem !important;
  padding-bottom: 4rem !important;
  max-width: 1400px !important;
}
.block-container > div:first-child { margin-top: 0 !important; padding-top: 0 !important; }

/* ============================================================
   STREAMLIT NATIVE ICONS — preserve Material Symbols
   ============================================================ */
[data-testid="stIconMaterial"],
[data-testid="stIconMaterial"]::before,
[data-testid="stIconMaterial"]::after,
.material-symbols-rounded,
.material-symbols-outlined,
[class*="material-symbols"] {
  font-family: "Material Symbols Rounded", "Material Symbols Outlined", sans-serif !important;
}

[data-testid="stToolbar"],
[data-testid="stToolbar"] button,
[data-testid="stToolbar"] [role="button"],
[data-testid="stHeader"] button,
[data-testid="stHeader"] [role="button"] {
  font-family: "Material Symbols Rounded", "Material Symbols Outlined", sans-serif !important;
}

/* Never inject generated text into native Streamlit controls. */
[data-testid="stToolbar"]::before,
[data-testid="stToolbar"]::after,
[data-testid="stHeader"]::before,
[data-testid="stHeader"]::after,
[data-testid="stIconMaterial"]::before,
[data-testid="stIconMaterial"]::after { content: none !important; }

/* ============================================================
   INTERACTION SAFETY — never block inputs
   ============================================================ */
.stTextInput,
.stTextInput > div,
.stTextInput input,
.stTextArea,
.stTextArea textarea,
[data-testid="stChatInput"],
[data-testid="stChatInput"] *,
button, input, textarea, select, [role="slider"] {
  pointer-events: auto !important;
  user-select: text !important;
}
.stTextInput, .stTextArea, [data-testid="stChatInput"] { position: relative !important; z-index: 20 !important; }
.stTextInput input, .stTextArea textarea, [data-testid="stChatInput"] textarea { caret-color: var(--text) !important; }

/* ============================================================
   SIDEBAR
   ============================================================ */
section[data-testid="stSidebar"] {
  background: #0a0a0a !important;
  border-right: 1px solid rgba(220,38,38,0.22) !important;
  width: 272px !important;
  box-shadow: none !important;
}
section[data-testid="stSidebar"] > div { padding: 0 !important; }
section[data-testid="stSidebar"] > div > div { padding: 0 !important; gap: 0 !important; }
section[data-testid="stSidebar"] [data-testid="stVerticalBlock"] { gap: 0 !important; padding: 0 !important; }
section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"],
section[data-testid="stSidebar"] .stMarkdown,
section[data-testid="stSidebar"] .element-container { margin: 0 !important; padding: 0 !important; }
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] .stCaption,
section[data-testid="stSidebar"] .stMarkdown p {
  color: var(--text-muted) !important;
  font-size: 12px !important;
  line-height: 1.5 !important;
  margin: 0 !important;
}
section[data-testid="stSidebar"] label { color: var(--text-dim) !important; font-size: 9px !important; font-weight: 700 !important; letter-spacing: .9px !important; text-transform: uppercase !important; }
section[data-testid="stSidebar"] .stRadio { display: none !important; visibility: hidden !important; height: 0 !important; overflow: hidden !important; margin: 0 !important; padding: 0 !important; }
section[data-testid="stSidebar"] .stCheckbox label { color: var(--text-muted) !important; font-size: 12px !important; }

.sb-panel { border-bottom: 1px solid rgba(255,255,255,.07); padding: 14px 16px; }
.sb-header-block { padding: 16px 16px 14px; border-bottom: 1px solid rgba(255,255,255,.07); }
.sb-logo-row { display:flex; align-items:center; gap:10px; margin-bottom:10px; }
.sb-diamond { width:30px; height:30px; border-radius:6px; background:var(--primary); display:flex; align-items:center; justify-content:center; font-size:14px; color:#fff; font-weight:800; flex-shrink:0; }
.sb-brand-name { font-size:14px !important; font-weight:800 !important; color:#fff !important; letter-spacing:.2px; line-height:1.15 !important; margin:0 !important; }
.sb-brand-sub { font-size:9px !important; color:var(--text-dim) !important; letter-spacing:1.8px !important; text-transform:uppercase !important; margin:0 !important; }
.sb-online-row { display:flex; align-items:center; gap:7px; }
.sb-dot-green { width:7px; height:7px; border-radius:50%; background:var(--success); box-shadow:0 0 6px rgba(34,197,94,.7); flex-shrink:0; }
.sb-online-label { font-size:11px !important; font-weight:600; color:#86efac !important; letter-spacing:.4px; margin:0 !important; }
.sb-section-hdr { font-size:9px !important; font-weight:800 !important; letter-spacing:2px !important; text-transform:uppercase !important; color:var(--text-dim) !important; margin:0 0 10px !important; }
.sb-doc-row { display:flex; align-items:flex-start; gap:9px; margin-bottom:8px; }
.sb-doc-icon { font-size:13px; margin-top:1px; flex-shrink:0; color:var(--text-dim); }
.sb-doc-name { font-size:12px !important; font-weight:600; color:var(--text) !important; overflow-wrap:anywhere; line-height:1.35; margin:0 !important; }
.sb-doc-meta { font-size:10px !important; color:var(--text-dim) !important; margin-top:2px !important; line-height:1.5; }
.sb-upload-hint { font-size:10px !important; color:var(--text-dim) !important; margin:0 !important; }
.sb-router-row { display:flex; align-items:flex-start; gap:9px; margin-bottom:10px; }
.sb-router-icon { font-size:14px; flex-shrink:0; margin-top:1px; }
.sb-router-name { font-size:12px !important; font-weight:700; color:#fff !important; letter-spacing:.3px; margin:0 !important; }
.sb-router-sub { font-size:10px !important; color:var(--text-dim) !important; margin:2px 0 0 !important; }
.sb-prov-label { font-size:9px !important; font-weight:700 !important; letter-spacing:1.4px !important; text-transform:uppercase !important; color:var(--text-dim) !important; margin:10px 0 6px !important; }
.sb-prov-row { display:flex; align-items:center; gap:8px; padding:3px 0; font-size:12px !important; }
.sb-dot-on { width:6px; height:6px; border-radius:50%; background:var(--success); box-shadow:0 0 4px rgba(34,197,94,.6); flex-shrink:0; }
.sb-dot-off { width:6px; height:6px; border-radius:50%; background:#333; flex-shrink:0; }
.sb-cap-row { display:flex; align-items:center; gap:8px; padding:3px 0; font-size:12px !important; color:var(--text-muted) !important; margin:0 !important; }
.sb-cap-check { font-size:11px; font-weight:700; color:var(--success); }
.sb-footer { padding:14px 16px; }
.sb-footer-title { font-size:12px !important; font-weight:700; color:var(--text) !important; margin:0 !important; }
.sb-footer-meta { font-size:10px !important; color:var(--text-dim) !important; margin:2px 0 0 !important; }

/* ============================================================
   MAIN
   ============================================================ */
.nf-header { padding:36px 40px 30px; margin:0 -2rem 24px; border-bottom:1px solid rgba(255,255,255,.07); background:#0d0d0d; text-align:center; }
.nf-header h1 { font-size:40px !important; font-weight:800 !important; letter-spacing:-1.2px !important; color:#fff !important; margin:0 0 8px !important; line-height:1.15 !important; }
.nf-header p { font-size:14px !important; color:var(--text-muted) !important; margin:0 0 22px !important; line-height:1.6 !important; }
.nf-badges { display:flex; justify-content:center; gap:8px; flex-wrap:wrap; }
.nf-badge { background:rgba(255,255,255,.05); border:1px solid rgba(255,255,255,.12); border-radius:20px; padding:5px 15px; font-size:12px; color:#a3a3a3; font-weight:500; letter-spacing:.2px; }
.profile-card { display:flex; align-items:center; gap:20px; padding:18px 22px; margin:0 0 4px; background:var(--surface); border:1px solid rgba(255,255,255,.07); border-radius:var(--radius); }
.profile-avatar { width:90px; height:90px; border-radius:10px; object-fit:cover; flex-shrink:0; box-shadow:0 4px 16px rgba(0,0,0,.35); }
.profile-name { font-size:20px !important; font-weight:700; color:#f8fafc !important; letter-spacing:-.3px; margin-bottom:5px; }
.profile-bio { font-size:13px !important; color:var(--text-muted) !important; line-height:1.5; }
.section-label { font-size:9px; font-weight:800; color:var(--text-dim); letter-spacing:1.8px; text-transform:uppercase; margin:20px 0 8px; padding-left:2px; }
.engine-provider-info { display:flex; align-items:center; gap:10px; padding:10px 14px; background:rgba(220,38,38,.05); border:1px solid rgba(220,38,38,.16); border-radius:var(--radius-sm); margin-bottom:14px; }
.engine-provider-name { font-size:13px; font-weight:700; color:var(--text); }
.engine-provider-model { font-size:11px; color:var(--text-muted); margin-top:1px; }
.engine-status-dot { width:8px; height:8px; border-radius:50%; background:var(--success); box-shadow:0 0 6px rgba(34,197,94,.55); flex-shrink:0; margin-left:auto; }
[data-testid="stFileUploadDropzone"] { background:rgba(220,38,38,.03) !important; border:2px dashed rgba(220,38,38,.28) !important; border-radius:var(--radius) !important; transition:border-color .18s,background .18s; }
[data-testid="stFileUploadDropzone"]:hover { border-color:rgba(220,38,38,.55) !important; background:rgba(220,38,38,.06) !important; }
[data-testid="stFileUploadDropzone"] small { color:var(--text-dim) !important; font-size:11px !important; }

/* generic cards/chats/composer */
.file-card { background:rgba(34,197,94,.07); border:1px solid rgba(34,197,94,.22); border-radius:12px; padding:14px 16px; display:flex; align-items:center; gap:12px; margin-top:10px; }
.file-name { font-size:13px; font-weight:600; color:var(--text); overflow-wrap:anywhere; }
.file-meta { font-size:11px; color:var(--text-muted); margin-top:2px; }
[data-testid="stChatMessage"] { border-radius:14px !important; margin:8px 0 !important; }
[data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] { line-height:1.7 !important; }
div[data-testid="stForm"] { background:rgba(255,255,255,.025) !important; border:1px solid rgba(220,38,38,.16) !important; border-radius:16px !important; padding:14px !important; }
div[data-testid="stForm"] .stTextInput input { min-height:48px !important; padding:0 16px !important; border-radius:12px !important; background:rgba(0,0,0,.18) !important; }
.stTextInput input,.stTextArea textarea { background:rgba(255,255,255,.04) !important; border:1px solid rgba(255,255,255,.09) !important; border-radius:12px !important; color:var(--text) !important; font-size:14px !important; }
.stTextInput input:focus,.stTextArea textarea:focus { border-color:var(--primary) !important; box-shadow:0 0 0 3px rgba(220,38,38,.12) !important; }
[data-testid="stMetric"] { background:rgba(255,255,255,.025) !important; border:1px solid rgba(255,255,255,.06) !important; border-radius:12px !important; padding:12px !important; }
[data-testid="stMetricLabel"] { color:var(--text-dim) !important; }
[data-testid="stMetricValue"] { color:var(--text) !important; }
.stButton>button,[data-testid="stFormSubmitButton"] button { border-radius:10px !important; font-weight:600 !important; font-size:13px !important; }
.stButton>button[kind="primary"],[data-testid="stFormSubmitButton"] button[kind="primary"] { background:linear-gradient(135deg,#dc2626,#991b1b) !important; border:none !important; color:#fff !important; }
.badge { display:inline-flex; gap:6px; padding:4px 12px; border-radius:16px; font-size:11px; font-weight:700; background:rgba(220,38,38,.08); border:1px solid rgba(220,38,38,.18); color:#fca5a5; }
.empty-state { text-align:center; padding:60px 24px; }
.empty-state .icon { font-size:52px; }
.empty-state h3 { color:#d4d4d4 !important; }
.empty-state p { color:#737373 !important; }
hr { border-color:rgba(255,255,255,.05) !important; }

@media (max-width:768px) {
  .block-container { padding:0 .9rem 2rem !important; }
  .nf-header { margin:0 -.9rem 20px; padding:32px 18px 28px; }
  .nf-header h1 { font-size:34px !important; }
  section[data-testid="stSidebar"] { width:300px !important; }
}

@media (prefers-reduced-motion:reduce) {
  *,*::before,*::after { animation:none !important; transition:none !important; }
}

::-webkit-scrollbar { width:5px; }
::-webkit-scrollbar-thumb { background:rgba(220,38,38,.28); border-radius:3px; }
</style>
"""
