# flake8: noqa: E501
"""NeuraFlow AI — unified design system."""


def get_css() -> str:
    return """
<style>
/* ============================================================
   DESIGN TOKENS
   ============================================================ */
:root {
  --bg:        #080D1A;
  --surface:   #0C1222;
  --surface2:  #111827;
  --border:    rgba(255,255,255,0.07);
  --border-hi: rgba(139,92,246,0.30);
  --primary:   #8B5CF6;
  --primary-dk:#7C3AED;
  --secondary: #3B82F6;
  --text:      #E2E8F0;
  --text-muted:#94A3B8;
  --text-dim:  #64748B;
  --success:   #10B981;
  --warning:   #F59E0B;
  --error:     #EF4444;
  --radius-sm: 8px;
  --radius:    12px;
  --radius-lg: 16px;
}

/* ============================================================
   RESET & BASE
   ============================================================ */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

*, *::before, *::after {
  font-family: Inter, -apple-system, system-ui, sans-serif !important;
  box-sizing: border-box;
}

.stApp {
  background: var(--bg) !important;
  color: var(--text) !important;
}

/* Streamlit native elements */
#MainMenu  { visibility: visible !important; display: block !important; }
header     { visibility: visible !important; display: block !important; background: transparent !important; }
footer     { visibility: hidden !important; }

.block-container {
  padding: 0 2rem 4rem !important;
  max-width: 1400px !important;
}

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
   SIDEBAR
   ============================================================ */
section[data-testid="stSidebar"] {
  background: linear-gradient(180deg, #070B16 0%, #0B1020 60%, #070B14 100%) !important;
  border-right: 1px solid rgba(139,92,246,0.18) !important;
  width: 292px !important;
  box-shadow: 8px 0 32px rgba(0,0,0,0.30) !important;
}

section[data-testid="stSidebar"] > div {
  padding: 16px 14px 20px !important;
}

section[data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
  gap: 0.4rem !important;
}

section[data-testid="stSidebar"] hr {
  margin: 10px 0 !important;
  border-color: rgba(255,255,255,0.06) !important;
}

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
  letter-spacing: 0.8px !important;
  text-transform: uppercase !important;
}

section[data-testid="stSidebar"] .stRadio > div[role="radiogroup"] {
  display: grid !important;
  grid-template-columns: 1fr !important;
  gap: 4px !important;
}

section[data-testid="stSidebar"] .stRadio > div[role="radiogroup"] > label {
  background: rgba(255,255,255,0.025) !important;
  border: 1px solid rgba(255,255,255,0.06) !important;
  border-radius: var(--radius-sm) !important;
  padding: 7px 10px !important;
  margin: 0 !important;
  color: var(--text-muted) !important;
  font-size: 12px !important;
  transition: background 0.15s, border-color 0.15s;
}

section[data-testid="stSidebar"] .stRadio > div[role="radiogroup"] > label:hover {
  background: rgba(139,92,246,0.08) !important;
  border-color: rgba(139,92,246,0.22) !important;
}

section[data-testid="stSidebar"] .stRadio > div[role="radiogroup"] > label:has(input:checked) {
  background: linear-gradient(135deg, rgba(124,58,237,0.18), rgba(37,99,235,0.10)) !important;
  border-color: rgba(139,92,246,0.36) !important;
  color: #E9D5FF !important;
}

section[data-testid="stSidebar"] .stCheckbox label {
  color: var(--text-muted) !important;
  font-size: 12px !important;
}

/* ============================================================
   SIDEBAR CUSTOM COMPONENTS
   ============================================================ */
.sb-brand {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 4px;
}

.sb-brand-icon {
  width: 32px;
  height: 32px;
  border-radius: 9px;
  background: linear-gradient(135deg, #7C3AED, #2563EB);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 15px;
  flex-shrink: 0;
  box-shadow: 0 4px 14px rgba(124,58,237,0.28);
}

.sb-brand-title {
  font-size: 16px !important;
  font-weight: 800 !important;
  color: #F8FAFC !important;
  letter-spacing: -0.3px;
  margin: 0 !important;
  line-height: 1.2 !important;
}

.sb-brand-sub {
  font-size: 9px !important;
  color: var(--text-dim) !important;
  letter-spacing: 1.4px !important;
  text-transform: uppercase !important;
  margin: 0 !important;
}

.sb-status {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 6px 10px;
  background: rgba(16,185,129,0.07);
  border: 1px solid rgba(16,185,129,0.18);
  border-radius: 20px;
  font-size: 11px !important;
  font-weight: 600;
  color: #6EE7B7 !important;
  width: fit-content;
}

.sb-status-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: #10B981;
  box-shadow: 0 0 6px rgba(16,185,129,0.60);
  flex-shrink: 0;
}

.sb-section-title {
  font-size: 9px !important;
  font-weight: 800 !important;
  letter-spacing: 1.4px !important;
  text-transform: uppercase !important;
  color: var(--text-dim) !important;
  margin: 14px 0 6px !important;
}

.sb-doc-card {
  background: rgba(255,255,255,0.025);
  border: 1px solid rgba(255,255,255,0.06);
  border-radius: var(--radius-sm);
  padding: 10px 12px;
}

.sb-doc-name {
  font-size: 12px !important;
  font-weight: 600;
  color: var(--text) !important;
  overflow-wrap: anywhere;
  margin-bottom: 4px;
}

.sb-doc-meta {
  font-size: 10px !important;
  color: var(--text-dim) !important;
  line-height: 1.6;
}

.sb-provider-row {
  display: flex;
  align-items: center;
  gap: 7px;
  padding: 5px 0;
  font-size: 12px !important;
  color: var(--text-muted) !important;
}

.sb-dot-online  { width:7px;height:7px;border-radius:50%;background:#10B981;box-shadow:0 0 5px rgba(16,185,129,0.5);flex-shrink:0; }
.sb-dot-offline { width:7px;height:7px;border-radius:50%;background:#475569;flex-shrink:0; }

.sb-caps {
  background: rgba(255,255,255,0.02);
  border: 1px solid rgba(255,255,255,0.05);
  border-radius: var(--radius-sm);
  padding: 8px 12px;
}

.sb-cap-row {
  display: flex;
  align-items: center;
  gap: 7px;
  font-size: 11px !important;
  color: var(--text-muted) !important;
  padding: 3px 0;
}

.sb-cap-check {
  color: #10B981;
  font-size: 12px;
}

.sb-footer-card {
  background: rgba(255,255,255,0.02);
  border: 1px solid rgba(255,255,255,0.05);
  border-radius: var(--radius-sm);
  padding: 10px 12px;
  margin-top: 12px;
  text-align: center;
}

.sb-footer-title {
  font-size: 11px !important;
  font-weight: 700;
  color: var(--text) !important;
  margin-bottom: 2px;
}

.sb-footer-meta {
  font-size: 10px !important;
  color: var(--text-dim) !important;
}

/* ============================================================
   HEADER / HERO
   ============================================================ */
.nf-header {
  padding: 32px 40px 28px;
  margin: 0 -2rem 28px;
  border-bottom: 1px solid rgba(139,92,246,0.12);
  background: linear-gradient(135deg, rgba(139,92,246,0.08), rgba(59,130,246,0.05));
  text-align: center;
}

.nf-header h1 {
  font-size: 38px !important;
  font-weight: 800 !important;
  letter-spacing: -1.2px !important;
  background: linear-gradient(135deg, #A78BFA, #818CF8 50%, #60A5FA);
  -webkit-background-clip: text !important;
  -webkit-text-fill-color: transparent !important;
  margin-bottom: 8px !important;
}

.nf-header p {
  font-size: 15px !important;
  color: var(--text-muted) !important;
  margin: 0 0 20px !important;
}

.nf-badges {
  display: flex;
  justify-content: center;
  gap: 8px;
  flex-wrap: wrap;
}

.nf-badge {
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 20px;
  padding: 5px 14px;
  font-size: 12px;
  color: var(--text-muted);
  font-weight: 500;
}

/* ============================================================
   SECTION LABELS
   ============================================================ */
.section-label {
  font-size: 10px;
  font-weight: 700;
  color: var(--text-dim);
  letter-spacing: 1.3px;
  text-transform: uppercase;
  margin: 22px 0 10px;
  padding-left: 2px;
}

/* ============================================================
   AI ENGINE CARD
   ============================================================ */
.engine-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 16px;
  margin-bottom: 4px;
}

.engine-provider-info {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-top: 8px;
  padding: 10px 12px;
  background: rgba(139,92,246,0.05);
  border: 1px solid rgba(139,92,246,0.14);
  border-radius: var(--radius-sm);
}

.engine-provider-name {
  font-size: 13px;
  font-weight: 600;
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
  background: #10B981;
  box-shadow: 0 0 6px rgba(16,185,129,0.5);
  flex-shrink: 0;
  margin-left: auto;
}

/* ============================================================
   FILE UPLOADER & DOCUMENT CARD
   ============================================================ */
[data-testid="stFileUploadDropzone"] {
  background: rgba(139,92,246,0.03) !important;
  border: 2px dashed rgba(139,92,246,0.28) !important;
  border-radius: var(--radius) !important;
  min-height: 110px !important;
  transition: border-color 0.2s, background 0.2s;
}

[data-testid="stFileUploadDropzone"]:hover {
  border-color: rgba(139,92,246,0.50) !important;
  background: rgba(139,92,246,0.06) !important;
}

.file-card {
  background: rgba(16,185,129,0.06);
  border: 1px solid rgba(16,185,129,0.20);
  border-radius: var(--radius);
  padding: 14px 16px;
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
  border: 1px solid var(--border) !important;
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
  background: linear-gradient(135deg, #7C3AED, #2563EB) !important;
  border-radius: 18px 18px 4px 18px !important;
  max-width: 78% !important;
}

.stChatMessage[data-testid="stChatMessageAssistant"] > div {
  background: rgba(255,255,255,0.04) !important;
  border: 1px solid rgba(255,255,255,0.07) !important;
  border-radius: 4px 16px 16px 16px !important;
  max-width: 85% !important;
}

/* ============================================================
   FORM & INPUT
   ============================================================ */
div[data-testid="stForm"] {
  background: rgba(255,255,255,0.025) !important;
  border: 1px solid rgba(139,92,246,0.14) !important;
  border-radius: var(--radius-lg) !important;
  padding: 14px !important;
}

div[data-testid="stForm"] .stTextInput input {
  min-height: 48px !important;
  padding: 0 16px !important;
}

.stTextInput input,
.stTextArea textarea {
  background: rgba(255,255,255,0.04) !important;
  border: 1px solid rgba(255,255,255,0.08) !important;
  border-radius: var(--radius) !important;
  color: var(--text) !important;
  font-size: 14px !important;
}

.stTextInput input:focus,
.stTextArea textarea:focus {
  border-color: var(--primary) !important;
  box-shadow: 0 0 0 3px rgba(139,92,246,0.12) !important;
  outline: none !important;
}

/* ============================================================
   BUTTONS
   ============================================================ */
.stButton > button,
[data-testid="stFormSubmitButton"] button {
  border-radius: var(--radius-sm) !important;
  font-weight: 600 !important;
  font-size: 13px !important;
  transition: opacity 0.15s, transform 0.12s;
}

.stButton > button[kind="primary"],
[data-testid="stFormSubmitButton"] button[kind="primary"] {
  background: linear-gradient(135deg, #7C3AED, #2563EB) !important;
  border: none !important;
  color: #fff !important;
  padding: 10px 20px !important;
}

.stButton > button[kind="primary"]:hover,
[data-testid="stFormSubmitButton"] button[kind="primary"]:hover {
  opacity: 0.88;
  transform: translateY(-1px);
}

/* ============================================================
   RADIO + CHECKBOXES (main area)
   ============================================================ */
.stRadio > div[role="radiogroup"] {
  gap: 6px !important;
  flex-wrap: wrap !important;
}

.stRadio > div[role="radiogroup"] > label {
  background: rgba(255,255,255,0.035) !important;
  border: 1px solid rgba(255,255,255,0.07) !important;
  border-radius: var(--radius-sm) !important;
  padding: 7px 12px !important;
}

.stCheckbox label { color: var(--text-muted) !important; }

/* ============================================================
   TABS
   ============================================================ */
.stTabs [data-baseweb="tab-list"] {
  background: rgba(255,255,255,0.03) !important;
  border: 1px solid rgba(255,255,255,0.07) !important;
  border-radius: var(--radius) !important;
  padding: 4px !important;
}

.stTabs [data-baseweb="tab"] { color: var(--text-muted) !important; border-radius: var(--radius-sm) !important; }
.stTabs [aria-selected="true"] {
  background: linear-gradient(135deg, rgba(139,92,246,0.22), rgba(59,130,246,0.18)) !important;
  color: #A78BFA !important;
}

/* ============================================================
   BADGE & MISC
   ============================================================ */
.badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 4px 12px;
  border-radius: 16px;
  font-size: 11px;
  font-weight: 700;
  background: rgba(139,92,246,0.08);
  border: 1px solid rgba(139,92,246,0.18);
  color: #A78BFA;
}

.provider-badge {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  padding: 2px 8px;
  border-radius: 10px;
  font-size: 11px;
  font-weight: 600;
  background: rgba(139,92,246,0.10);
  border: 1px solid rgba(139,92,246,0.20);
  color: #A78BFA;
  margin-top: 6px;
}

.empty-state {
  text-align: center;
  padding: 56px 24px;
}

.empty-state .icon { font-size: 48px; }
.empty-state h3 { color: var(--text-muted) !important; font-size: 17px !important; margin: 14px 0 6px !important; }
.empty-state p  { color: var(--text-dim) !important; font-size: 14px !important; }

hr { border-color: rgba(255,255,255,0.05) !important; }

/* ============================================================
   EXPANDERS
   ============================================================ */
[data-testid="stExpander"] {
  background: var(--surface) !important;
  border: 1px solid var(--border) !important;
  border-radius: var(--radius) !important;
}

/* ============================================================
   SOURCES
   ============================================================ */
.source-item {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  padding: 10px 12px;
  background: rgba(255,255,255,0.025);
  border: 1px solid rgba(255,255,255,0.06);
  border-radius: var(--radius-sm);
  margin-bottom: 6px;
}

.source-icon { font-size: 15px; flex-shrink: 0; margin-top: 1px; }
.source-name { font-size: 12px; font-weight: 600; color: var(--text); }
.source-meta { font-size: 11px; color: var(--text-muted); margin-top: 2px; }

/* ============================================================
   SCROLLBAR
   ============================================================ */
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-thumb { background: rgba(139,92,246,0.22); border-radius: 3px; }

/* ============================================================
   RESPONSIVE
   ============================================================ */
@media (max-width: 1024px) {
  .block-container { padding: 0 1.5rem 3rem !important; }
  .nf-header { padding: 24px 20px 20px; }
}

@media (max-width: 768px) {
  .block-container { padding: 0 0.8rem 2rem !important; }
  .nf-header { margin: 0 -0.8rem 20px; padding: 24px 16px 20px; }
  .nf-header h1 { font-size: 28px !important; }
  section[data-testid="stSidebar"] { width: 100% !important; }
  .stChatMessage[data-testid="stChatMessageUser"] > div,
  .stChatMessage[data-testid="stChatMessageAssistant"] > div { max-width: 92% !important; }
}

/* ============================================================
   REDUCED MOTION
   ============================================================ */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation: none !important; transition: none !important; }
}
</style>
"""
