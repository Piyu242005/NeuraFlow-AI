# flake8: noqa: E501
"""NeuraFlow AI design system."""

def get_css() -> str:
    return """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
*,*::before,*::after{font-family:Inter,sans-serif!important;box-sizing:border-box}
.stApp{background:#080D1A!important;color:#E2E8F0!important}
#MainMenu{visibility:visible!important;display:block!important}header{visibility:visible!important;display:block!important;background:transparent!important}footer{visibility:hidden!important}
.block-container{padding:0 2rem 4rem!important;max-width:1400px!important}
.stTextInput,.stTextInput>div,.stTextInput input,.stTextArea,.stTextArea textarea,[data-testid="stChatInput"],[data-testid="stChatInput"] *,button,input,textarea,select,[role="slider"]{pointer-events:auto!important;user-select:text!important}
.stTextInput,.stTextArea,[data-testid="stChatInput"]{position:relative!important;z-index:20!important}.stTextInput input,.stTextArea textarea,[data-testid="stChatInput"] textarea{caret-color:#E2E8F0!important}

/* Modern sidebar */
section[data-testid="stSidebar"]{background:linear-gradient(180deg,#070B16 0%,#0B1020 48%,#070B14 100%)!important;border-right:1px solid rgba(139,92,246,.20)!important;width:304px!important;box-shadow:18px 0 50px rgba(0,0,0,.25)!important}
section[data-testid="stSidebar"]>div{padding:14px 12px 16px!important}
section[data-testid="stSidebar"] [data-testid="stVerticalBlock"]{gap:.45rem!important}
section[data-testid="stSidebar"] hr{margin:12px 4px!important;border-color:rgba(255,255,255,.065)!important}
section[data-testid="stSidebar"] h2{color:#F8FAFC!important;font-size:18px!important;font-weight:800!important;letter-spacing:-.4px!important;margin:0!important}
section[data-testid="stSidebar"] h3{color:#CBD5E1!important;font-size:10px!important;font-weight:800!important;letter-spacing:1.1px!important;text-transform:uppercase!important;margin:14px 5px 5px!important}
section[data-testid="stSidebar"] p,section[data-testid="stSidebar"] .stCaption{color:#7F8CA3!important;font-size:11px!important;line-height:1.55!important}
section[data-testid="stSidebar"] label{color:#64748B!important;font-size:9px!important;font-weight:800!important;letter-spacing:.8px!important;text-transform:uppercase!important}
section[data-testid="stSidebar"] .stTextInput input{background:rgba(255,255,255,.035)!important;border:1px solid rgba(255,255,255,.07)!important;border-radius:10px!important;color:#CBD5E1!important;font-size:12px!important;min-height:38px!important}
section[data-testid="stSidebar"] .stTextInput input:focus{border-color:rgba(139,92,246,.55)!important;box-shadow:0 0 0 3px rgba(139,92,246,.10)!important}
section[data-testid="stSidebar"] .stButton>button{width:100%!important;text-align:left!important;justify-content:flex-start!important;background:rgba(255,255,255,.025)!important;border:1px solid rgba(255,255,255,.055)!important;color:#CBD5E1!important;border-radius:10px!important;min-height:38px!important;padding:7px 10px!important;font-size:12px!important}
section[data-testid="stSidebar"] .stButton>button:hover{background:rgba(139,92,246,.10)!important;border-color:rgba(139,92,246,.28)!important;color:#F8FAFC!important;transform:none!important;box-shadow:none!important}
section[data-testid="stSidebar"] .stRadio>div[role="radiogroup"]{display:grid!important;grid-template-columns:1fr!important;gap:5px!important}
section[data-testid="stSidebar"] .stRadio>div[role="radiogroup"]>label{background:rgba(255,255,255,.025)!important;border:1px solid rgba(255,255,255,.055)!important;border-radius:10px!important;padding:8px 10px!important;margin:0!important;color:#94A3B8!important}
section[data-testid="stSidebar"] .stRadio>div[role="radiogroup"]>label:hover{background:rgba(139,92,246,.08)!important;border-color:rgba(139,92,246,.24)!important}
section[data-testid="stSidebar"] .stRadio>div[role="radiogroup"]>label:has(input:checked){background:linear-gradient(135deg,rgba(124,58,237,.18),rgba(37,99,235,.10))!important;border-color:rgba(139,92,246,.38)!important;color:#E9D5FF!important}

/* Make the existing sidebar markup look like a real AI workspace */
section[data-testid="stSidebar"]>div>div:first-child{position:relative}
section[data-testid="stSidebar"]>div>div:first-child:before{content:'AI DOCUMENT OS';display:block;color:#64748B;font-size:8px;font-weight:800;letter-spacing:1.6px;margin:0 5px 10px}
section[data-testid="stSidebar"] h2:before{content:'✦';display:inline-flex;align-items:center;justify-content:center;width:30px;height:30px;margin-right:8px;border-radius:9px;background:linear-gradient(135deg,#7C3AED,#2563EB);color:#fff;font-size:14px;vertical-align:middle;box-shadow:0 6px 18px rgba(124,58,237,.28)}
section[data-testid="stSidebar"] h2{display:flex!important;align-items:center!important}
section[data-testid="stSidebar"] h2 + p,section[data-testid="stSidebar"] h2 + div{margin-left:40px!important}
section[data-testid="stSidebar"] h2 + p:after{content:'●  SYSTEM ONLINE';display:block;color:#6EE7B7;font-size:9px;font-weight:700;letter-spacing:.6px;margin-top:5px}
section[data-testid="stSidebar"] h2 + p{font-size:10px!important;color:#64748B!important}
section[data-testid="stSidebar"] h2 + p{max-width:205px}
section[data-testid="stSidebar"] h2 + p{border-bottom:1px solid rgba(255,255,255,.06);padding-bottom:13px}
section[data-testid="stSidebar"] h2 + p + hr{margin-top:2px!important}
section[data-testid="stSidebar"] h2 + p + hr + h2{margin-top:4px!important}
section[data-testid="stSidebar"] h2 + p + hr + h2{background:rgba(255,255,255,.025);border:1px solid rgba(139,92,246,.12);border-radius:12px;padding:11px 12px!important}
section[data-testid="stSidebar"] h2 + p + hr + h2:before{content:'◈';background:rgba(139,92,246,.12);box-shadow:none;color:#A78BFA}
section[data-testid="stSidebar"] h2 + p + hr + h2 + p{background:rgba(255,255,255,.018);border:1px solid rgba(255,255,255,.045);border-radius:0 0 11px 11px;padding:10px 11px!important;margin-top:-5px!important;margin-left:0!important}
section[data-testid="stSidebar"] h3{position:relative}
section[data-testid="stSidebar"] h3:before{content:'›';color:#8B5CF6;margin-right:5px}
section[data-testid="stSidebar"] .stMarkdown ul{margin:4px 0 8px!important;padding:9px 12px 9px 27px!important;background:rgba(255,255,255,.018);border:1px solid rgba(255,255,255,.045);border-radius:10px!important}
section[data-testid="stSidebar"] .stMarkdown li{color:#AAB5C5!important;font-size:11px!important;padding:3px 0!important}
section[data-testid="stSidebar"]>div>div:last-child{margin-top:8px!important}

/* Main hero */
.hero{background:linear-gradient(135deg,rgba(139,92,246,.12),rgba(59,130,246,.08));border-bottom:1px solid rgba(139,92,246,.15);padding:48px 40px 40px;margin:0 -2rem 32px;text-align:center}.hero h1{font-size:46px!important;font-weight:800!important;letter-spacing:-1.5px!important;background:linear-gradient(135deg,#A78BFA,#818CF8 50%,#60A5FA);-webkit-background-clip:text!important;-webkit-text-fill-color:transparent!important;margin-bottom:12px!important}.hero p{font-size:17px!important;color:#94A3B8!important;max-width:560px;margin:0 auto 28px!important;line-height:1.6!important}.stats-bar{display:flex;justify-content:center;gap:12px;flex-wrap:wrap}.stat-chip{background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.08);border-radius:20px;padding:7px 16px;font-size:13px;color:#94A3B8}.stat-chip span{color:#A78BFA;font-weight:700}
.stTabs [data-baseweb="tab-list"]{background:rgba(255,255,255,.03)!important;border:1px solid rgba(255,255,255,.07)!important;border-radius:12px!important;padding:4px!important}.stTabs [data-baseweb="tab"]{color:#94A3B8!important;border-radius:8px!important}.stTabs [aria-selected="true"]{background:linear-gradient(135deg,rgba(139,92,246,.25),rgba(59,130,246,.2))!important;color:#A78BFA!important}
.stRadio>div[role="radiogroup"]{gap:6px!important;flex-wrap:wrap!important}.stRadio>div[role="radiogroup"]>label{background:rgba(255,255,255,.035)!important;border:1px solid rgba(255,255,255,.07)!important;border-radius:10px!important;padding:7px 12px!important}.stCheckbox label{color:#CBD5E1!important}
[data-testid="stFileUploadDropzone"]{background:rgba(139,92,246,.03)!important;border:2px dashed rgba(139,92,246,.3)!important;border-radius:14px!important;min-height:130px!important}.file-card{background:rgba(16,185,129,.07);border:1px solid rgba(16,185,129,.22);border-radius:12px;padding:14px 16px;display:flex;align-items:center;gap:12px;margin-top:10px}.file-name{font-size:13px;font-weight:600;color:#E2E8F0;overflow-wrap:anywhere}.file-meta{font-size:11px;color:#94A3B8;margin-top:2px}
.chat-user{display:flex;justify-content:flex-end;margin:12px 0}.bubble-user{background:linear-gradient(135deg,#7C3AED,#2563EB);color:#fff;border-radius:18px 18px 4px 18px;padding:11px 16px;max-width:78%;font-size:14px;line-height:1.6}.chat-ai{display:flex;gap:10px;margin:12px 0;align-items:flex-start}.bubble-ai{background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.08);border-radius:4px 16px 16px 16px;padding:14px 16px;max-width:85%;font-size:14px;line-height:1.75;color:#CBD5E1}
div[data-testid="stForm"]{background:rgba(255,255,255,.025)!important;border:1px solid rgba(139,92,246,.16)!important;border-radius:16px!important;padding:14px!important}div[data-testid="stForm"] .stTextInput input{min-height:48px!important;padding:0 16px!important;border-radius:12px!important;background:rgba(0,0,0,.18)!important}.stTextInput input,.stTextArea textarea{background:rgba(255,255,255,.04)!important;border:1px solid rgba(255,255,255,.09)!important;border-radius:12px!important;color:#E2E8F0!important;font-size:14px!important}.stTextInput input:focus,.stTextArea textarea:focus{border-color:#8B5CF6!important;box-shadow:0 0 0 3px rgba(139,92,246,.12)!important}
.stButton>button,[data-testid="stFormSubmitButton"] button{border-radius:10px!important;font-weight:600!important;font-size:13px!important}.stButton>button[kind="primary"],[data-testid="stFormSubmitButton"] button[kind="primary"]{background:linear-gradient(135deg,#7C3AED,#2563EB)!important;border:none!important;color:#fff!important;padding:10px 20px!important}
[data-testid="stMetric"]{background:rgba(255,255,255,.025)!important;border:1px solid rgba(255,255,255,.06)!important;border-radius:12px!important;padding:12px!important}[data-testid="stMetricLabel"]{color:#64748B!important}[data-testid="stMetricValue"]{color:#E2E8F0!important}.badge{display:inline-flex;gap:6px;padding:4px 12px;border-radius:16px;font-size:11px;font-weight:700;background:rgba(139,92,246,.08);border:1px solid rgba(139,92,246,.18);color:#A78BFA}.section-label{font-size:11px;font-weight:700;color:#64748B;letter-spacing:1.2px;text-transform:uppercase;margin:18px 0 10px}.empty-state{text-align:center;padding:60px 24px}.empty-state .icon{font-size:52px}.empty-state h3{color:#CBD5E1!important}.empty-state p{color:#64748B!important}hr{border-color:rgba(255,255,255,.05)!important}
@media(max-width:768px){.block-container{padding:0 .9rem 2rem!important}.hero{margin:0 -.9rem 20px;padding:32px 18px 28px}.hero h1{font-size:34px!important}section[data-testid="stSidebar"]{width:300px!important}.bubble-user,.bubble-ai{max-width:92%}}
@media(prefers-reduced-motion:reduce){*,*::before,*::after{animation:none!important;transition:none!important}}
::-webkit-scrollbar{width:5px}::-webkit-scrollbar-thumb{background:rgba(139,92,246,.25);border-radius:3px}
</style>
"""
