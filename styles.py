# flake8: noqa: E501
"""NeuraFlow AI — unified design system. Black / red theme."""


def get_css() -> str:
    return """
<style>
/* ============================================================
   DESIGN TOKENS  ·  black / red
   ============================================================ */
:root {
  --bg:          #0a0a0a;
  --surface:     #111111;
  --surface2:    #1a1a1a;
  --border:      rgba(255,255,255,0.07);
  --primary:     #dc2626;
  --accent:      #b91c1c;
  --text:        #f5f5f5;
  --text-muted:  #a3a3a3;
  --text-dim:    #525252;
  --success:     #22c55e;
  --warning:     #f59e0b;
  --radius-sm:   6px;
  --radius:      10px;
  --radius-lg:   14px;
}

/* ============================================================
   FONT
   ============================================================ */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

*, *::before, *::after {
  font-family: Inter, -apple-system, system-ui, sans-serif !important;
  box-sizing: border-box;
}

/* ============================================================
   APP BASE
   ============================================================ */
.stApp {
  background: var(--bg) !important;
  color: var(--text) !important;
}

#MainMenu  { visibility: visible !important; display: block !important; }
header     { visibility: visible !important; display: block !important; background: transparent !important; }
footer     { visibility: hidden !important; }

/* Remove ALL top padding from main block so header sits flush */
.block-container {
  padding-top: 0 !important;
  padding-left: 2rem !important;
  padding-right: 2rem !important;
  padding-bottom: 4rem !important;
  max-width: 1400px !important;
}

/* Also kill the default Streamlit inner-block top margin */
.block-container > div:first-child {
  margin-top: 0 !important;
  padding-top: 0 !important;
}

/* ============================================================
   INTERACTION SAFETY  —  never block inputs
   ============================================================ */
.stTextInput,
.stTextInput > div,
.stTextInput input,
.stTextArea,
.stTextArea textarea,
[data-testid="stChatInput"],
[data-testid="stChatInput"] *,
button, input, textarea, select {
  pointer-events: auto !important;
  user-select: text !important;
}

.stTextInput, .stTextArea, [data-testid="stChatInput"] {
  position: relative !important;
  z-index: 20 !important;
}

.stTextInput input,
.stTextArea textarea,
[data-testid="stChatInput"] textarea {
  caret-color: var(--text) !important;
}

/* ============================================================
   SIDEBAR  —  solid black shell
   ============================================================ */
section[data-testid="stSidebar"] {
  background: #0a0a0a !important;
  border-right: 1px solid rgba(220,38,38,0.22) !important;
  width: 272px !important;
  box-shadow: none !important;
}

/* Zero out ALL default Streamlit padding inside sidebar */
section[data-testid="stSidebar"] > div {
  padding: 0 !important;
}

section[data-testid="stSidebar"] > div > div {
  padding: 0 !important;
  gap: 0 !important;
}

section[data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
  gap: 0 !important;
  padding: 0 !important;
}

/* Kill the default margin on every stMarkdownContainer inside sidebar */
section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"],
section[data-testid="stSidebar"] .stMarkdown,
section[data-testid="stSidebar"] .element-container {
  margin: 0 !important;
  padding: 0 !important;
}

/* Kill default paragraph margins inside sidebar */
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] .stCaption,
section[data-testid="stSidebar"] .stMarkdown p {
  color: var(--text-muted) !important;
  font-size: 12px !important;
  line-height: 1.5 !important;
  margin: 0 !important;
}

section[data-testid="stSidebar"] label {
  color: var(--text-dim) !important;
  font-size: 9px !important;
  font-weight: 700 !important;
  letter-spacing: 0.9px !important;
  text-transform: uppercase !important;
}

/* ── HIDE the provider radio widget visually (kept for state) ── */
section[data-testid="stSidebar"] .stRadio {
  display: none !important;
  visibility: hidden !important;
  height: 0 !important;
  overflow: hidden !important;
  margin: 0 !important;
  padding: 0 !important;
}

section[data-testid="stSidebar"] .stCheckbox label {
  color: var(--text-muted) !important;
  font-size: 12px !important;
}

/* ============================================================
   SIDEBAR  —  panel blocks
   ============================================================ */

/* shared panel style: thin bottom border, consistent padding */
.sb-panel {
  border-bottom: 1px solid rgba(255,255,255,0.07);
  padding: 14px 16px;
}

/* ── Header block ── */
.sb-header-block {
  padding: 16px 16px 14px;
  border-bottom: 1px solid rgba(255,255,255,0.07);
}

.sb-logo-row {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 10px;
}

.sb-diamond {
  width: 30px;
  height: 30px;
  border-radius: 6px;
  background: var(--primary);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
  color: #fff;
  font-weight: 800;
  flex-shrink: 0;
}

.sb-brand-name {
  font-size: 14px !important;
  font-weight: 800 !important;
  color: #ffffff !important;
  letter-spacing: 0.2px;
  line-height: 1.15 !important;
  margin: 0 !important;
}

.sb-brand-sub {
  font-size: 9px !important;
  color: var(--text-dim) !important;
  letter-spacing: 1.8px !important;
  text-transform: uppercase !important;
  margin: 0 !important;
}

.sb-online-row {
  display: flex;
  align-items: center;
  gap: 7px;
}

.sb-dot-green {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: var(--success);
  box-shadow: 0 0 6px rgba(34,197,94,0.7);
  flex-shrink: 0;
}

.sb-online-label {
  font-size: 11px !important;
  font-weight: 600;
  color: #86efac !important;
  letter-spacing: 0.4px;
  margin: 0 !important;
}

/* ── Section headers inside panels ── */
.sb-section-hdr {
  font-size: 9px !important;
  font-weight: 800 !important;
  letter-spacing: 2px !important;
  text-transform: uppercase !important;
  color: var(--text-dim) !important;
  margin: 0 0 10px 0 !important;
}

/* ── Document row ── */
.sb-doc-row {
  display: flex;
  align-items: flex-start;
  gap: 9px;
  margin-bottom: 8px;
}

.sb-doc-icon {
  font-size: 13px;
  margin-top: 1px;
  flex-shrink: 0;
  color: var(--text-dim);
}

.sb-doc-name {
  font-size: 12px !important;
  font-weight: 600;
  color: var(--text) !important;
  overflow-wrap: anywhere;
  line-height: 1.35;
  margin: 0 !important;
}

.sb-doc-meta {
  font-size: 10px !important;
  color: var(--text-dim) !important;
  margin-top: 2px !important;
  line-height: 1.5;
}

.sb-upload-hint {
  font-size: 10px !important;
  color: var(--text-dim) !important;
  margin: 0 !important;
}

/* ── Router row ── */
.sb-router-row {
  display: flex;
  align-items: flex-start;
  gap: 9px;
  margin-bottom: 10px;
}

.sb-router-icon {
  font-size: 14px;
  flex-shrink: 0;
  margin-top: 1px;
}

.sb-router-name {
  font-size: 12px !important;
  font-weight: 700;
  color: #ffffff !important;
  letter-spacing: 0.3px;
  margin: 0 !important;
}

.sb-router-sub {
  font-size: 10px !important;
  color: var(--text-dim) !important;
  margin: 2px 0 0 0 !important;
}

/* ── Provider list ── */
.sb-prov-label {
  font-size: 9px !important;
  font-weight: 700 !important;
  letter-spacing: 1.4px !important;
  text-transform: uppercase !important;
  color: var(--text-dim) !important;
  margin: 10px 0 6px 0 !important;
}

.sb-prov-row {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 3px 0;
  font-size: 12px !important;
}

.sb-dot-on  { width:6px;height:6px;border-radius:50%;background:var(--success);box-shadow:0 0 4px rgba(34,197,94,0.6);flex-shrink:0; }
.sb-dot-off { width:6px;height:6px;border-radius:50%;background:#333333;flex-shrink:0; }

/* ── Capabilities ── */
.sb-cap-row {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 3px 0;
  font-size: 12px !important;
  color: var(--text-muted) !important;
  margin: 0 !important;
}

.sb-cap-check {
  font-size: 11px;
  font-weight: 700;
  color: var(--success);
}

/* ── Footer ── */
.sb-footer {
  padding: 14px 16px;
}

.sb-footer-title {
  font-size: 12px !important;
  font-weight: 700;
  color: var(--text) !important;
  margin: 0 !important;
}

.sb-footer-meta {
  font-size: 10px !important;
  color: var(--text-dim) !important;
  margin: 2px 0 0 0 !important;
}

/* ============================================================
   MAIN  —  header block
   Sits flush at the top; SVG icon is 72px centered above title.
   ============================================================ */
.nf-header {
  padding: 36px 40px 30px;
  /* negative margins cancel block-container side padding so header is full-width */
  margin: 0 -2rem 24px;
  border-bottom: 1px solid rgba(255,255,255,0.07);
  background: #0d0d0d;
  text-align: center;
}

.nf-header h1 {
  font-size: 40px !important;
  font-weight: 800 !important;
  letter-spacing: -1.2px !important;
  color: #ffffff !important;
  margin: 0 0 8px 0 !important;
  line-height: 1.15 !important;
}

.nf-header p {
  font-size: 14px !important;
  color: var(--text-muted) !important;
  margin: 0 0 22px 0 !important;
  line-height: 1.6 !important;
}

.nf-badges {
  display: flex;
  justify-content: center;
  gap: 8px;
  flex-wrap: wrap;
}

.nf-badge {
  background: rgba(255,255,255,0.05);
  border: 1px solid rgba(255,255,255,0.12);
  border-radius: 20px;
  padding: 5px 15px;
  font-size: 12px;
  color: #a3a3a3;
  font-weight: 500;
  letter-spacing: 0.2px;
}

/* ============================================================
   PROFILE CARD
   ============================================================ */
.profile-card {
  display: flex;
  align-items: center;
  gap: 20px;
  padding: 18px 22px;
  margin: 0 0 4px;
  background: var(--surface);
  border: 1px solid rgba(255,255,255,0.07);
  border-radius: var(--radius);
}

.profile-avatar {
  width: 90px;
  height: 90px;
  border-radius: 10px;
  object-fit: cover;
  flex-shrink: 0;
  box-shadow: 0 4px 16px rgba(0,0,0,0.35);
}

.profile-name {
  font-size: 20px !important;
  font-weight: 700;
  color: #f8fafc !important;
  letter-spacing: -0.3px;
  margin-bottom: 5px;
}

.profile-bio {
  font-size: 13px !important;
  color: var(--text-muted) !important;
  line-height: 1.5;
}

/* ============================================================
   SECTION LABELS  (main area)
   ============================================================ */
.section-label {
  font-size: 9px;
  font-weight: 800;
  color: var(--text-dim);
  letter-spacing: 1.8px;
  text-transform: uppercase;
  margin: 20px 0 8px;
  padding-left: 2px;
}

/* ============================================================
   ENGINE INFO CARD
   ============================================================ */
.engine-provider-info {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 14px;
  background: rgba(220,38,38,0.05);
  border: 1px solid rgba(220,38,38,0.16);
  border-radius: var(--radius-sm);
  margin-bottom: 14px;
}

.engine-provider-name {
  font-size: 13px;
  font-weight: 700;
  color: var(--text);
}

.engine-provider-model {
  font-size: 11px;
  color: var(--text-muted);
  margin-top: 1px;
}

.engine-status-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--success);
  box-shadow: 0 0 6px rgba(34,197,94,0.55);
  flex-shrink: 0;
  margin-left: auto;
}

/* ============================================================
   FILE UPLOADER  —  hide duplicate "Browse files" text label
   ============================================================ */
[data-testid="stFileUploadDropzone"] {
  background: rgba(220,38,38,0.03) !important;
  border: 2px dashed rgba(220,38,38,0.28) !important;
  border-radius: var(--radius) !important;
  transition: border-color 0.18s, background 0.18s;
}

[data-testid="stFileUploadDropzone"]:hover {
  border-color: rgba(220,38,38,0.55) !important;
  background: rgba(220,38,38,0.06) !important;
}

/* The inner upload button — suppress the plain-text label that doubles */
[data-testid="stFileUploadDropzone"] small {
  color: var(--text-dim) !important;
  font-size: 11px !important;
}

/* ============================================================
   DOCUMENT CARD
   ============================================================ */
.file-card {
  background: rgba(34,197,94,0.05);
  border: 1px solid rgba(34,197,94,0.18);
  border-radius: var(--radius);
  padding: 12px 14px;
  display: flex;
  align-items: center;
  gap: 12px;
  margin-top: 10px;
}

.file-name {
  font-size: 13px;
  font-weight: 600;
  color: var(--text);
  overflow-wrap: anywhere;
}

.file-meta {
  font-size: 11px;
  color: var(--text-muted);
  margin-top: 3px;
}

/* ============================================================
   METRICS
   ============================================================ */
[data-testid="stMetric"] {
  background: var(--surface) !important;
  border: 1px solid rgba(255,255,255,0.06) !important;
  border-radius: var(--radius) !important;
  padding: 12px !important;
}

[data-testid="stMetricLabel"] { color: var(--text-dim) !important; }
[data-testid="stMetricValue"] { color: var(--text) !important; }

/* ============================================================
   CHAT MESSAGES
   ============================================================ */
.stChatMessage[data-testid="stChatMessageUser"] {
  flex-direction: row-reverse !important;
}

.stChatMessage[data-testid="stChatMessageUser"] > div {
  background: var(--primary) !important;
  border-radius: 14px 14px 3px 14px !important;
  max-width: 78% !important;
}

.stChatMessage[data-testid="stChatMessageAssistant"] > div {
  background: var(--surface) !important;
  border: 1px solid rgba(255,255,255,0.07) !important;
  border-radius: 3px 14px 14px 14px !important;
  max-width: 85% !important;
}

/* ============================================================
   FORM & INPUT
   ============================================================ */
div[data-testid="stForm"] {
  background: var(--surface) !important;
  border: 1px solid rgba(220,38,38,0.16) !important;
  border-radius: var(--radius-lg) !important;
  padding: 14px !important;
}

.stTextInput input,
.stTextArea textarea {
  background: var(--surface2) !important;
  border: 1px solid rgba(255,255,255,0.08) !important;
  border-radius: var(--radius) !important;
  color: var(--text) !important;
  font-size: 14px !important;
}

.stTextInput input:focus,
.stTextArea textarea:focus {
  border-color: var(--primary) !important;
  box-shadow: 0 0 0 2px rgba(220,38,38,0.12) !important;
  outline: none !important;
}

div[data-testid="stForm"] .stTextInput input {
  min-height: 46px !important;
  padding: 0 16px !important;
}

/* ============================================================
   BUTTONS
   ============================================================ */
.stButton > button,
[data-testid="stFormSubmitButton"] button {
  border-radius: var(--radius-sm) !important;
  font-weight: 600 !important;
  font-size: 13px !important;
}

.stButton > button[kind="primary"],
[data-testid="stFormSubmitButton"] button[kind="primary"] {
  background: var(--primary) !important;
  border: none !important;
  color: #fff !important;
  padding: 10px 20px !important;
}

.stButton > button[kind="primary"]:hover,
[data-testid="stFormSubmitButton"] button[kind="primary"]:hover {
  background: var(--accent) !important;
}

.stButton > button[kind="secondary"],
[data-testid="stFormSubmitButton"] button:not([kind="primary"]) {
  background: var(--surface2) !important;
  border: 1px solid rgba(255,255,255,0.09) !important;
  color: var(--text-muted) !important;
}

/* ============================================================
   RADIO + CHECKBOXES  (main area)
   ============================================================ */
.stRadio > div[role="radiogroup"] {
  gap: 6px !important;
  flex-wrap: wrap !important;
}

.stRadio > div[role="radiogroup"] > label {
  background: var(--surface) !important;
  border: 1px solid rgba(255,255,255,0.07) !important;
  border-radius: var(--radius-sm) !important;
  padding: 6px 12px !important;
  color: var(--text-muted) !important;
  font-size: 12px !important;
}

.stRadio > div[role="radiogroup"] > label:has(input:checked) {
  background: rgba(220,38,38,0.10) !important;
  border-color: rgba(220,38,38,0.35) !important;
  color: #fca5a5 !important;
}

/* radio label text (the "Search Provider" heading Streamlit auto-renders) */
.stRadio > label {
  font-size: 9px !important;
  font-weight: 800 !important;
  color: var(--text-dim) !important;
  letter-spacing: 1.6px !important;
  text-transform: uppercase !important;
}

.stCheckbox label { color: var(--text-muted) !important; }

/* ============================================================
   TABS
   ============================================================ */
.stTabs [data-baseweb="tab-list"] {
  background: var(--surface) !important;
  border: 1px solid rgba(255,255,255,0.07) !important;
  border-radius: var(--radius) !important;
  padding: 3px !important;
}

.stTabs [data-baseweb="tab"] { color: var(--text-muted) !important; border-radius: var(--radius-sm) !important; }
.stTabs [aria-selected="true"] {
  background: rgba(220,38,38,0.15) !important;
  color: #fca5a5 !important;
}

/* ============================================================
   PROVIDER BADGE (chat)
   ============================================================ */
.provider-badge {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  padding: 2px 8px;
  border-radius: 8px;
  font-size: 11px;
  font-weight: 600;
  background: rgba(220,38,38,0.10);
  border: 1px solid rgba(220,38,38,0.22);
  color: #fca5a5;
  margin-bottom: 6px;
}

/* ============================================================
   MISC
   ============================================================ */
.empty-state {
  text-align: center;
  padding: 48px 24px;
}

.empty-state .icon { font-size: 44px; }
.empty-state h3 { color: var(--text-muted) !important; font-size: 16px !important; margin: 12px 0 5px !important; }
.empty-state p  { color: var(--text-dim) !important; font-size: 13px !important; }

hr { border-color: rgba(255,255,255,0.06) !important; }

[data-testid="stExpander"] {
  background: var(--surface) !important;
  border: 1px solid rgba(255,255,255,0.06) !important;
  border-radius: var(--radius) !important;
}

/* sources */
.source-item {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  padding: 9px 11px;
  background: var(--surface2);
  border: 1px solid rgba(255,255,255,0.05);
  border-radius: var(--radius-sm);
  margin-bottom: 5px;
}

.source-icon { font-size: 13px; flex-shrink: 0; margin-top: 1px; }
.source-name { font-size: 12px; font-weight: 600; color: var(--text); }
.source-meta { font-size: 11px; color: var(--text-muted); margin-top: 2px; }

/* ============================================================
   SCROLLBAR
   ============================================================ */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-thumb { background: rgba(220,38,38,0.28); border-radius: 2px; }

/* ============================================================
   RESPONSIVE
   ============================================================ */
@media (max-width: 1024px) {
  .block-container { padding-left: 1.25rem !important; padding-right: 1.25rem !important; }
  .nf-header { padding: 28px 24px 22px; }
}

@media (max-width: 768px) {
  .block-container { padding-left: 0.75rem !important; padding-right: 0.75rem !important; }
  .nf-header { margin: 0 -0.75rem 18px; padding: 24px 16px 20px; }
  .nf-header h1 { font-size: 28px !important; }
  section[data-testid="stSidebar"] { width: 100% !important; }
  .stChatMessage[data-testid="stChatMessageUser"] > div,
  .stChatMessage[data-testid="stChatMessageAssistant"] > div { max-width: 92% !important; }
}

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation: none !important; transition: none !important; }
}
</style>
"""
