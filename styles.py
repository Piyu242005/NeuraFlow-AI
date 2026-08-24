# flake8: noqa: E501
"""
styles.py – Complete Design System · NeuraFlow AI
"""


def get_css() -> str:
    return """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

*, *::before, *::after { font-family: 'Inter', sans-serif !important; box-sizing: border-box; }
.stApp { background: #080D1A !important; color: #E2E8F0 !important; }
#MainMenu {
    visibility: visible !important;
    display: block !important;
}

header {
    visibility: visible !important;
    display: block !important;
    background: transparent !important;
}

footer {
    visibility: hidden !important;
}

.block-container { padding: 0 2rem 4rem !important; max-width: 1400px !important; }

/* Interaction safety */
.stTextInput, .stTextInput > div, .stTextInput [data-baseweb="input"],
.stTextInput input, .stTextArea, .stTextArea > div, .stTextArea textarea,
[data-testid="stChatInput"], [data-testid="stChatInput"] *,
button, input, textarea, select { pointer-events: auto !important; user-select: text !important; }
.stTextInput, .stTextArea, [data-testid="stChatInput"] { position: relative !important; z-index: 20 !important; }
.stTextInput input, .stTextArea textarea, [data-testid="stChatInput"] textarea {
    caret-color: #E2E8F0 !important;
    -webkit-user-select: text !important;
    user-select: text !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #0C1222 !important;
    border-right: 1px solid rgba(139,92,246,0.15) !important;
    width: 272px !important;
}
section[data-testid="stSidebar"] > div { padding: 1.5rem 1.1rem !important; }
section[data-testid="stSidebar"] .stTextInput input {
    background: rgba(255,255,255,0.04) !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    border-radius: 8px !important; color: #CBD5E1 !important;
    font-size: 13px !important;
}
section[data-testid="stSidebar"] .stTextInput input:focus {
    border-color: rgba(139,92,246,0.5) !important;
    box-shadow: 0 0 0 2px rgba(139,92,246,0.12) !important;
}
section[data-testid="stSidebar"] label { color: #94A3B8 !important; font-size: 11px !important; font-weight: 600 !important; letter-spacing: 0.8px !important; text-transform: uppercase !important; }

/* Hero */
.hero {
    background: linear-gradient(135deg, rgba(139,92,246,0.12) 0%, rgba(59,130,246,0.08) 100%);
    border-bottom: 1px solid rgba(139,92,246,0.15);
    padding: 48px 40px 40px; margin: 0 -2rem 32px; text-align: center;
}
.hero h1 {
    font-size: 46px !important; font-weight: 800 !important; letter-spacing: -1.5px !important;
    background: linear-gradient(135deg,#A78BFA 0%,#818CF8 50%,#60A5FA 100%);
    -webkit-background-clip: text !important; -webkit-text-fill-color: transparent !important;
    margin-bottom: 12px !important;
}
.hero p { font-size: 17px !important; color: #94A3B8 !important; max-width: 560px; margin: 0 auto 28px !important; line-height: 1.6 !important; }
.stats-bar { display: flex; justify-content: center; gap: 12px; flex-wrap: wrap; }
.stat-chip { background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); border-radius: 20px; padding: 7px 16px; font-size: 13px; color: #94A3B8; font-weight: 500; }
.stat-chip span { color: #A78BFA; font-weight: 700; }
.left-panel { background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.06); border-radius: 16px; padding: 20px; height: fit-content; }
.right-panel { background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.06); border-radius: 16px; padding: 20px; min-height: 500px; }

/* Tabs / provider controls */
.stTabs [data-baseweb="tab-list"] { background: rgba(255,255,255,0.03) !important; border: 1px solid rgba(255,255,255,0.07) !important; border-radius: 12px !important; padding: 4px !important; gap: 2px !important; }
.stTabs [data-baseweb="tab"] { color: #94A3B8 !important; border-radius: 8px !important; font-weight: 500 !important; font-size: 13px !important; padding: 8px 14px !important; }
.stTabs [aria-selected="true"] { background: linear-gradient(135deg,rgba(139,92,246,0.25),rgba(59,130,246,0.2)) !important; color: #A78BFA !important; font-weight: 600 !important; }
.stRadio > div[role="radiogroup"] { gap: 6px !important; flex-wrap: wrap !important; }
.stRadio > div[role="radiogroup"] > label {
    background: rgba(255,255,255,0.035) !important;
    border: 1px solid rgba(255,255,255,0.07) !important;
    border-radius: 10px !important;
    padding: 7px 12px !important;
    transition: border-color .18s ease, background .18s ease !important;
}
.stRadio > div[role="radiogroup"] > label:hover { background: rgba(139,92,246,0.08) !important; border-color: rgba(139,92,246,0.3) !important; }
.stCheckbox label { color: #CBD5E1 !important; }

/* Upload */
[data-testid="stFileUploadDropzone"] { background: rgba(139,92,246,0.03) !important; border: 2px dashed rgba(139,92,246,0.3) !important; border-radius: 14px !important; transition: all 0.25s ease !important; min-height: 130px !important; }
[data-testid="stFileUploadDropzone"]:hover { background: rgba(139,92,246,0.07) !important; border-color: rgba(139,92,246,0.55) !important; transform: translateY(-1px); }
[data-testid="stFileUploadDropzoneInstructions"] { color: #94A3B8 !important; }
.file-card { background: rgba(16,185,129,0.07); border: 1px solid rgba(16,185,129,0.22); border-radius: 12px; padding: 14px 16px; display: flex; align-items: center; gap: 12px; margin-top: 10px; }
.file-name { font-size: 13px; font-weight: 600; color: #E2E8F0; overflow-wrap: anywhere; }
.file-meta { font-size: 11px; color: #94A3B8; margin-top: 2px; }

/* Chat */
.chat-user { display: flex; justify-content: flex-end; margin: 12px 0; }
.bubble-user { background: linear-gradient(135deg,#7C3AED,#2563EB); color: white; border-radius: 18px 18px 4px 18px; padding: 11px 16px; max-width: 78%; font-size: 14px; line-height: 1.6; }
.chat-ai { display: flex; gap: 10px; margin: 12px 0; align-items: flex-start; }
.ai-avatar { width: 34px; height: 34px; border-radius: 9px; flex-shrink: 0; background: linear-gradient(135deg,#8B5CF6,#3B82F6); display: flex; align-items: center; justify-content: center; font-size: 15px; }
.bubble-ai { background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); border-radius: 4px 16px 16px 16px; padding: 14px 16px; max-width: 85%; font-size: 14px; line-height: 1.75; color: #CBD5E1; }
.bubble-ai pre { background: rgba(0,0,0,0.3) !important; border-radius: 8px !important; padding: 12px !important; font-size: 12px !important; overflow-x: auto !important; }

/* Composer / form */
div[data-testid="stForm"] { background: rgba(255,255,255,0.025) !important; border: 1px solid rgba(139,92,246,0.16) !important; border-radius: 16px !important; padding: 14px !important; }
div[data-testid="stForm"] .stTextInput { margin-bottom: 6px !important; }
div[data-testid="stForm"] .stTextInput input { min-height: 48px !important; padding: 0 16px !important; border-radius: 12px !important; background: rgba(0,0,0,0.18) !important; }
div[data-testid="stForm"] [data-testid="stFormSubmitButton"] button { min-height: 42px !important; }
div[data-testid="stForm"] [data-testid="stFormSubmitButton"]:first-child button { font-weight: 700 !important; }
.stTextInput input, .stTextArea textarea { background: rgba(255,255,255,0.04) !important; border: 1px solid rgba(255,255,255,0.09) !important; border-radius: 12px !important; color: #E2E8F0 !important; font-size: 14px !important; }
.stTextInput input:focus, .stTextArea textarea:focus { border-color: #8B5CF6 !important; box-shadow: 0 0 0 3px rgba(139,92,246,0.12) !important; }
[data-testid="stChatInput"] textarea { background: rgba(255,255,255,0.04) !important; color: #E2E8F0 !important; border: 1px solid rgba(139,92,246,0.35) !important; border-radius: 14px !important; }
[data-testid="stChatInput"] textarea:focus { border-color: #8B5CF6 !important; box-shadow: 0 0 0 3px rgba(139,92,246,0.12) !important; }

/* Buttons */
.stButton > button, [data-testid="stFormSubmitButton"] button { border-radius: 10px !important; font-weight: 600 !important; font-size: 13px !important; transition: all 0.2s ease !important; }
.stButton > button[kind="primary"], [data-testid="stFormSubmitButton"] button[kind="primary"] { background: linear-gradient(135deg,#7C3AED,#2563EB) !important; border: none !important; color: white !important; padding: 10px 20px !important; }
.stButton > button[kind="primary"]:hover, [data-testid="stFormSubmitButton"] button[kind="primary"]:hover { opacity: 0.9 !important; transform: translateY(-1px) !important; box-shadow: 0 6px 20px rgba(124,58,237,0.35) !important; }
.stButton > button[kind="secondary"], [data-testid="stFormSubmitButton"] button[kind="secondary"] { background: rgba(255,255,255,0.05) !important; border: 1px solid rgba(255,255,255,0.1) !important; color: #94A3B8 !important; }
.stButton > button[kind="secondary"]:hover, [data-testid="stFormSubmitButton"] button[kind="secondary"]:hover { background: rgba(255,255,255,0.09) !important; color: #E2E8F0 !important; }

/* Metrics / status */
[data-testid="stMetric"] { background: rgba(255,255,255,0.025) !important; border: 1px solid rgba(255,255,255,0.06) !important; border-radius: 12px !important; padding: 12px !important; }
[data-testid="stMetricLabel"] { color: #64748B !important; }
[data-testid="stMetricValue"] { color: #E2E8F0 !important; }
.dp-grid { display: grid; grid-template-columns: repeat(auto-fit,minmax(120px,1fr)); gap: 10px; margin: 14px 0; }
.dp-chip { background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.07); border-radius: 10px; padding: 10px 12px; }
.dp-chip .lbl { font-size: 10px; color: #64748B; font-weight: 600; text-transform: uppercase; letter-spacing: 0.6px; margin-bottom: 4px; }
.dp-chip .val { font-size: 13px; color: #CBD5E1; font-weight: 600; }
.status-row { display: flex; justify-content: space-between; align-items: center; padding: 7px 0; border-bottom: 1px solid rgba(255,255,255,0.04); }
.status-row:last-child { border-bottom: none; }
.dot { width: 7px; height: 7px; border-radius: 50%; display: inline-block; margin-right: 5px; }
.dot-on { background: #10B981; box-shadow: 0 0 5px #10B981; }
.dot-off { background: #374151; }

/* General */
.badge { display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; border-radius: 16px; font-size: 11px; font-weight: 700; letter-spacing: 0.4px; margin-bottom: 10px; text-transform: uppercase; background: rgba(139,92,246,.08); border: 1px solid rgba(139,92,246,.18); color: #A78BFA; }
.section-label { font-size: 11px; font-weight: 700; color: #64748B; letter-spacing: 1.2px; text-transform: uppercase; margin: 18px 0 10px; }
.suggestion-pill { display: inline-block; background: rgba(139,92,246,0.08); border: 1px solid rgba(139,92,246,0.25); border-radius: 20px; padding: 6px 14px; font-size: 12px; color: #A78BFA; cursor: pointer; margin: 4px 2px; transition: all 0.2s ease; }
.suggestion-pill:hover { background: rgba(139,92,246,0.18); }
hr { border-color: rgba(255,255,255,0.05) !important; margin: 16px 0 !important; }
.stAlert { border-radius: 10px !important; }
.stSuccess { background: rgba(16,185,129,0.08) !important; border: 1px solid rgba(16,185,129,0.25) !important; }
.stWarning { background: rgba(245,158,11,0.08) !important; border: 1px solid rgba(245,158,11,0.25) !important; }
.stError { background: rgba(239,68,68,0.08) !important; border: 1px solid rgba(239,68,68,0.25) !important; }
details { background: rgba(255,255,255,0.02) !important; border: 1px solid rgba(255,255,255,0.06) !important; border-radius: 10px !important; }
summary { color: #94A3B8 !important; font-size: 13px !important; font-weight: 500 !important; padding: 10px 14px !important; cursor: pointer !important; }
.empty-state { text-align: center; padding: 60px 24px; }
.empty-state .icon { font-size: 52px; margin-bottom: 16px; }
.empty-state h3 { color: #CBD5E1 !important; font-size: 18px !important; margin-bottom: 8px !important; }
.empty-state p { color: #64748B !important; font-size: 14px !important; }
.stDownloadButton > button { background: rgba(16,185,129,0.1) !important; border: 1px solid rgba(16,185,129,0.3) !important; color: #34D399 !important; border-radius: 8px !important; font-size: 12px !important; }

/* Mobile */
@media (max-width: 768px) {
    .block-container { padding: 0 0.9rem 2rem !important; }
    .hero { margin: 0 -0.9rem 20px; padding: 32px 18px 28px; }
    .hero h1 { font-size: 34px !important; }
    .hero p { font-size: 14px !important; }
    .stats-bar { gap: 6px; }
    .stat-chip { font-size: 11px; padding: 6px 10px; }
    section[data-testid="stSidebar"] { width: 300px !important; }
    .bubble-user, .bubble-ai { max-width: 92%; }
    div[data-testid="stForm"] { padding: 10px !important; }
    div[data-testid="stForm"] [data-testid="stHorizontalBlock"] { gap: 6px !important; }
    [data-testid="stMetric"] { padding: 9px !important; }
}

@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; }
}

::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-thumb { background: rgba(139,92,246,0.25); border-radius: 3px; }
@keyframes fadeUp { from{opacity:0;transform:translateY(10px)} to{opacity:1;transform:translateY(0)} }
.animate { animation: fadeUp 0.3s ease forwards; }
</style>
"""
