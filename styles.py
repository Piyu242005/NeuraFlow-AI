# flake8: noqa: E501
"""NeuraFlow AI — unified design system. Black / red theme."""


def get_css() -> str:
    return """
<style>
/* ============================================================
   DESIGN TOKENS  ·  black-red theme
   ============================================================ */
:root {
  --bg:         #0a0a0a;
  --surface:    #111111;
  --surface2:   #1a1a1a;
  --border:     rgba(255,255,255,0.07);
  --border-hi:  rgba(220,38,38,0.40);
  --primary:    #dc2626;
  --primary-lt: #ef4444;
  --primary-dim: rgba(220,38,38,0.15);
  --accent:     #b91c1c;
  --text:       #f5f5f5;
  --text-muted: #a3a3a3;
  --text-dim:   #525252;
  --success:    #22c55e;
  --warning:    #f59e0b;
  --error:      #ef4444;
  --radius-sm:  6px;
  --radius:     10px;
  --radius-lg:  14px;
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

.block-container {
  padding: 0 2rem 4rem !important;
  max-width: 1400px !important;
}

/* ============================================================
   INTERACTION SAFETY
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
   SIDEBAR  —  solid black, red accents
   ============================================================ */
section[data-testid="stSidebar"] {
  background: #0a0a0a !important;
  border-right: 1px solid rgba(220,38,38,0.25) !important;
  width: 280px !important;
  box-shadow: none !important;
}

section[data-testid="stSidebar"] > div {
  padding: 0 !important;
}

section[data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
  gap: 0 !important;
}

/* kill default streamlit paragraph / caption colour inside sidebar */
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] .stCaption,
section[data-testid="stSidebar"] .stMarkdown p {
  color: var(--text-muted) !important;
  font-size: 12px !important;
  line-height: 1.5 !important;
}

section[data-testid="stSidebar"] label {
  color: var(--text-dim) !important;
  font-size: 9px !important;
  font-weight: 700 !important;
  letter-spacing: 0.9px !important;
  text-transform: uppercase !important;
}

/* radio group inside sidebar */
section[data-testid="stSidebar"] .stRadio > div[role="radiogroup"] {
  display: flex !important;
  flex-direction: column !important;
  gap: 2px !important;
}

section[data-testid="stSidebar"] .stRadio > div[role="radiogroup"] > label {
  background: transparent !important;
  border: none !important;
  border-radius: 0 !important;
  padding: 7px 20px !important;
  margin: 0 !important;
  color: var(--text-muted) !important;
  font-size: 12px !important;
  transition: background 0.12s, color 0.12s;
}

section[data-testid="stSidebar"] .stRadio > div[role="radiogroup"] > label:hover {
  background: rgba(220,38,38,0.08) !important;
  color: var(--text) !important;
}

section[data-testid="stSidebar"] .stRadio > div[role="radiogroup"] > label:has(input:checked) {
  background: rgba(220,38,38,0.12) !important;
  color: #f87171 !important;
  border-left: 2px solid #dc2626 !important;
  padding-left: 18px !important;
}

section[data-testid="stSidebar"] .stCheckbox label {
  color: var(--text-muted) !important;
  font-size: 12px !important;
}

/* ============================================================
   SIDEBAR  —  panel sections (the wireframe boxes)
   ============================================================ */

/* every st.markdown block inside sidebar gets a clean wrapper */
.sb-panel {
  border-bottom: 1px solid rgba(255,255,255,0.07);
  padding: 14px 16px;
}

/* top brand block */
.sb-header-block {
  padding: 16px 16px 14px;
  border-bottom: 1px solid rgba(255,255,255,0.07);
}

.sb-logo-row {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 8px;
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
}

.sb-brand-sub {
  font-size: 9px !important;
  color: var(--text-dim) !important;
  letter-spacing: 1.8px !important;
  text-transform: uppercase !important;
}

.sb-online-row {
  display: flex;
  align-items: center;
  gap: 7px;
  margin-top: 10px;
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
}

/* section titles */
.sb-section-hdr {
  font-size: 9px !important;
  font-weight: 800 !important;
  letter-spacing: 2px !important;
  text-transform: uppercase !important;
  color: var(--text-dim) !important;
  margin: 0 0 8px 0 !important;
}

/* doc row */
.sb-doc-row {
  display: flex;
  align-items: flex-start;
  gap: 9px;
  margin-bottom: 10px;
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
}

.sb-doc-meta {
  font-size: 10px !important;
  color: var(--text-dim) !important;
  margin-top: 2px;
  line-height: 1.5;
}

/* auto-router row */
.sb-router-row {
  display: flex;
  align-items: flex-start;
  gap: 9px;
  margin-bottom: 12px;
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
}

.sb-router-sub {
  font-size: 10px !important;
  color: var(--text-dim) !important;
  margin-top: 2px;
}

/* provider list */
.sb-prov-label {
  font-size: 9px !important;
  font-weight: 700 !important;
  letter-spacing: 1.2px !important;
  text-transform: uppercase !important;
  color: var(--text-dim) !important;
  margin-bottom: 6px !important;
}

.sb-prov-row {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 4px 0;
  font-size: 12px !important;
}

.sb-dot-on  { width:7px;height:7px;border-radius:50%;background:var(--success);box-shadow:0 0 5px rgba(34,197,94,0.6);flex-shrink:0; }
.sb-dot-off { width:7px;height:7px;border-radius:50%;background:#3f3f3f;flex-shrink:0; }

/* capabilities */
.sb-cap-row {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 4px 0;
  font-size: 12px !important;
  color: var(--text-muted) !important;
}

.sb-cap-check {
  font-size: 11px;
  font-weight: 700;
  color: var(--success);
}

/* footer */
.sb-footer {
  padding: 14px 16px;
}

.sb-footer-title {
  font-size: 12px !important;
  font-weight: 700;
  color: var(--text) !important;
}

.sb-footer-meta {
  font-size: 10px !important;
  color: var(--text-dim) !important;
  margin-top: 2px;
}

/* ============================================================
   MAIN  —  header  (large centered icon + bold white title, pic-1 style)
   ============================================================ */
.nf-header {
  padding: 44px 40px 36px;
  margin: 0 -2rem 28px;
  border-bottom: 1px solid rgba(255,255,255,0.07);
  background: #0d0d0d;
  text-align: center;
}

/* the 72px SVG img is already block + centred via inline style */

.nf-header h1 {
  font-size: 40px !important;
  font-weight: 800 !important;
  letter-spacing: -1.2px !important;
  color: #ffffff !important;
  margin: 0 0 10px !important;
  line-height: 1.15 !important;
}

.nf-header p {
  font-size: 15px !important;
  color: var(--text-muted) !important;
  margin: 0 0 24px !important;
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
   SECTION LABELS
   ============================================================ */
.section-label {
  font-size: 9px;
  font-weight: 800;
  color: var(--text-dim);
  letter-spacing: 1.8px;
  text-transform: uppercase;
  margin: 20px 0 9px;
  padding-left: 2px;
}

/* ============================================================
   ENGINE INFO CARD
   ============================================================ */
.engine-provider-info {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 12px;
  background: rgba(220,38,38,0.06);
  border: 1px solid rgba(220,38,38,0.18);
  border-radius: var(--radius-sm);
  margin-bottom: 12px;
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
   FILE UPLOADER
   ============================================================ */
[data-testid="stFileUploadDropzone"] {
  background: rgba(220,38,38,0.03) !important;
  border: 2px dashed rgba(220,38,38,0.30) !important;
  border-radius: var(--radius) !important;
  min-height: 100px !important;
  transition: border-color 0.2s, background 0.2s;
}

[data-testid="stFileUploadDropzone"]:hover {
  border-color: rgba(220,38,38,0.55) !important;
  background: rgba(220,38,38,0.06) !important;
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
  border: 1px solid rgba(220,38,38,0.18) !important;
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
  box-shadow: 0 0 0 2px rgba(220,38,38,0.14) !important;
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
  opacity: 1;
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
  gap: 5px !important;
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
.section-label {
  font-size: 9px;
  font-weight: 800;
  color: var(--text-dim);
  letter-spacing: 1.8px;
  text-transform: uppercase;
  margin: 20px 0 9px;
}

.empty-state {
  text-align: center;
  padding: 52px 24px;
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
::-webkit-scrollbar-thumb { background: rgba(220,38,38,0.30); border-radius: 2px; }

/* ============================================================
   RESPONSIVE
   ============================================================ */
@media (max-width: 1024px) {
  .block-container { padding: 0 1.25rem 3rem !important; }
  .nf-header { padding: 22px 20px 18px; }
}

@media (max-width: 768px) {
  .block-container { padding: 0 0.75rem 2rem !important; }
  .nf-header { margin: 0 -0.75rem 18px; padding: 20px 14px 18px; }
  .nf-header h1 { font-size: 26px !important; }
  section[data-testid="stSidebar"] { width: 100% !important; }
  .stChatMessage[data-testid="stChatMessageUser"] > div,
  .stChatMessage[data-testid="stChatMessageAssistant"] > div { max-width: 92% !important; }
}

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation: none !important; transition: none !important; }
}
</style>
"""
