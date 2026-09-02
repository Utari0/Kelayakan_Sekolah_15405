import streamlit as st
import pandas as pd
import joblib
import textwrap
import datetime
import base64
import plotly.graph_objects as go


# =========================================================
# KONFIGURASI HALAMAN
# =========================================================

st.set_page_config(
    page_title="Prediksi Sekolah Unggul | AI Classifier",
    page_icon="🏫",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# LOAD MODEL & ASSETS
# =========================================================

try:
    model = joblib.load("decision_tree_sekolah.joblib")
except Exception as e:
    st.error("❌ Model Decision Tree tidak dapat dibuka.")
    st.code(str(e))
    st.stop()


@st.cache_data
def get_base64_logo():
    try:
        with open("logo.png", "rb") as f:
            return base64.b64encode(f.read()).decode()
    except Exception:
        return ""


logo_b64 = get_base64_logo()


# =========================================================
# CSS STYLING (AESTHETIC PASTEL PINK & GOLD + ANIMATIONS)
# =========================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

:root {
    --pink: #5dade2;
    --pink-soft: #85c1e9;
    --pink-light: #d6ecfa;
    --pink-subtle: #eef8ff;

    --yellow: #42a5f5;
    --yellow-soft: #bbdefb;
    --yellow-gold: #1976d2;

    --surface: #ffffff;
    --surface-soft: #f7fbff;

    --ink: #243b53;
    --ink-light: #486581;
    --muted: #627d98;

    --line: #c9e6f5;

    --shadow-sm: 0 4px 12px rgba(33, 150, 243, 0.08);
    --shadow-md: 0 8px 24px rgba(33, 150, 243, 0.12);
    --shadow-lg: 0 14px 32px rgba(33, 150, 243, 0.16);
}


/* =========================================================
   GLOBAL
   ========================================================= */

html, body, .stApp {
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: var(--ink);
}

h1, h2, h3, h4, h5, h6, p, label,
.main-title, .main-subtitle, .section-title, .card {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
}

.stApp {
    animation: pageFade 0.6s ease both;

    background: linear-gradient(
        140deg,
        #f0f8ff 0%,
        #ffffff 45%,
        #e8f5ff 100%
    );
}

@keyframes pageFade {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}

@keyframes softRise {
    from {
        opacity: 0;
        transform: translateY(14px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.main .block-container {
    max-width: 1200px;
    padding: 2.2rem 2.2rem 2rem;
}

div[data-testid="stHorizontalBlock"] {
    gap: 1rem;
}


/* =========================================================
   LOGO HERO
   ========================================================= */

.logo-hero-box {
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
    padding: 10px 0;
    min-height: 230px;
}

.logo-aura {
    position: absolute;
    width: 230px;
    height: 230px;
    border-radius: 50%;

    background: radial-gradient(
        circle,
        rgba(93, 173, 226, 0.45) 0%,
        rgba(66, 165, 245, 0.30) 50%,
        rgba(255, 255, 255, 0) 72%
    );

    animation: pulseAura 3.5s ease-in-out infinite alternate;
    z-index: 0;
    pointer-events: none;
}

@keyframes pulseAura {
    0% {
        transform: scale(0.88);
        opacity: 0.5;
    }

    100% {
        transform: scale(1.2);
        opacity: 0.95;
    }
}

.floating-logo {
    position: relative;
    z-index: 1;
    width: 220px;
    height: 220px;
    object-fit: contain;

    animation: floatMotion 3.8s ease-in-out infinite;

    filter: drop-shadow(
        0 10px 24px rgba(33, 150, 243, 0.28)
    );

    transition:
        transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1),
        filter 0.3s ease;

    cursor: pointer;
}

.floating-logo:hover {
    transform: scale(1.10) rotate(5deg) translateY(-6px) !important;

    filter: drop-shadow(
        0 18px 34px rgba(33, 150, 243, 0.45)
    ) !important;
}

@keyframes floatMotion {
    0%, 100% {
        transform: translateY(0px) rotate(0deg);
    }

    50% {
        transform: translateY(-11px) rotate(2deg);
    }
}


/* =========================================================
   SIDEBAR
   ========================================================= */

.sidebar-logo-box {
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
    padding: 14px 0 8px;
}

.sidebar-logo {
    width: 230px;
    height: 230px;
    max-width: 95%;
    object-fit: contain;

    animation: floatMotion 4.2s ease-in-out infinite 0.6s;

    filter: drop-shadow(
        0 10px 24px rgba(0, 0, 0, 0.22)
    );

    transition:
        transform 0.35s cubic-bezier(0.34, 1.56, 0.64, 1),
        filter 0.3s ease;
}

.sidebar-logo:hover {
    transform: scale(1.08) rotate(-3deg);

    filter: drop-shadow(
        0 16px 30px rgba(0, 0, 0, 0.32)
    );
}

section[data-testid="stSidebar"] {
    border-radius: 0 24px 24px 0;

    background: linear-gradient(
        180deg,
        #5dade2 0%,
        #3498db 45%,
        #1976d2 100%
    ) !important;

    box-shadow:
        6px 0 25px rgba(33, 150, 243, 0.20);
}

section[data-testid="stSidebar"] * {
    color: #ffffff !important;
}

.sidebar-badge {
    display: inline-block;

    background: rgba(255, 255, 255, 0.22);

    backdrop-filter: blur(8px);

    padding: 5px 14px;
    border-radius: 999px;

    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.5px;

    margin-bottom: 8px;

    border: 1px solid rgba(255, 255, 255, 0.35);
}

.sidebar-card {
    background: rgba(255, 255, 255, 0.16);

    backdrop-filter: blur(10px);

    border: 1px solid rgba(255, 255, 255, 0.30);

    border-radius: 16px;

    padding: 16px;

    margin-top: 14px;

    font-size: 13.5px;
    line-height: 1.6;
}


/* =========================================================
   HEADER
   ========================================================= */

.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;

    background: linear-gradient(
        90deg,
        #d6ecfa,
        #e3f2fd
    );

    color: #1976d2;

    border: 1px solid #b3ddf5;

    padding: 6px 14px;

    border-radius: 999px;

    font-size: 13px;
    font-weight: 700;

    margin-bottom: 12px;

    box-shadow: var(--shadow-sm);

    animation: softPulse 3s infinite alternate;
}

@keyframes softPulse {
    0% {
        transform: scale(1);
        box-shadow:
            0 4px 12px rgba(33, 150, 243, 0.06);
    }

    100% {
        transform: scale(1.02);
        box-shadow:
            0 6px 18px rgba(33, 150, 243, 0.15);
    }
}

.main-title {
    font-size: 36px;
    font-weight: 800;

    color: #1976d2;

    line-height: 1.2;

    margin-bottom: 6px;

    letter-spacing: -0.5px;
}

.main-subtitle {
    color: var(--muted);

    font-size: 15.5px;

    line-height: 1.6;
}


/* =========================================================
   CARDS
   ========================================================= */

.card {
    position: relative;
    overflow: hidden;

    background: var(--surface);

    color: var(--ink);

    padding: 22px 26px;

    border-radius: 18px;

    border: 1px solid var(--line);

    box-shadow: var(--shadow-sm);

    margin: 1rem 0 1.5rem;

    animation: softRise 0.45s ease both;

    transition:
        transform 0.25s ease,
        box-shadow 0.25s ease;
}

.card:hover {
    transform: translateY(-2px);

    box-shadow: var(--shadow-md);
}

.card::before {
    content: "";

    position: absolute;

    inset: 0 0 auto;

    height: 4px;

    background: linear-gradient(
        90deg,
        #5dade2,
        #85c1e9,
        #42a5f5
    );
}

.card h3 {
    margin: 0 0 8px;

    font-size: 1.15rem;

    font-weight: 700;

    color: #1976d2;
}

.card p {
    color: var(--muted);

    line-height: 1.65;

    margin: 0;

    font-size: 14.5px;
}


/* =========================================================
   SECTION TITLE
   ========================================================= */

.section-title {
    position: relative;

    color: #1976d2;

    font-size: 21px;

    font-weight: 800;

    margin: 1.6rem 0 1rem;

    display: flex;

    align-items: center;

    gap: 8px;
}

.section-title::after {
    content: "";

    display: block;

    height: 3px;

    flex-grow: 1;

    max-width: 90px;

    border-radius: 999px;

    background: linear-gradient(
        90deg,
        #5dade2,
        #42a5f5
    );

    margin-left: 10px;
}


/* =========================================================
   INPUT
   ========================================================= */

.stNumberInput,
.stSelectbox,
.stTextInput,
div[data-testid="stTextInput"],
div[data-testid="stSelectbox"],
div[data-testid="stNumberInput"] {

    position: relative;

    overflow: hidden;

    background: rgba(255, 255, 255, 0.95) !important;

    border: 1.5px solid var(--line) !important;

    border-radius: 16px !important;

    box-shadow: var(--shadow-sm) !important;

    padding: 13px 16px 14px !important;

    margin-bottom: 14px !important;

    transition:
        transform 0.25s ease,
        box-shadow 0.25s ease,
        border-color 0.25s ease !important;

    animation: softRise 0.4s ease both;
}

.stNumberInput::before,
.stSelectbox::before,
.stTextInput::before,
div[data-testid="stTextInput"]::before,
div[data-testid="stSelectbox"]::before,
div[data-testid="stNumberInput"]::before {

    content: "";

    position: absolute;

    left: 0;
    top: 0;
    bottom: 0;

    width: 4px;

    background: linear-gradient(
        180deg,
        #5dade2,
        #42a5f5
    );
}

.stNumberInput:hover,
.stSelectbox:hover,
.stTextInput:hover,
div[data-testid="stTextInput"]:hover,
div[data-testid="stSelectbox"]:hover,
div[data-testid="stNumberInput"]:hover {

    border-color: #85c1e9 !important;

    box-shadow: var(--shadow-md) !important;

    transform: translateY(-2px);
}

.stNumberInput label,
.stSelectbox label,
.stTextInput label,
div[data-testid="stTextInput"] label,
div[data-testid="stSelectbox"] label,
div[data-testid="stNumberInput"] label,
div[data-testid="stTextInput"] label p,
div[data-testid="stSelectbox"] label p,
div[data-testid="stNumberInput"] label p {

    color: var(--muted) !important;

    font-size: 13.5px !important;

    font-weight: 700 !important;

    margin-bottom: 6px !important;
}


/* =========================================================
   INPUT INTERIOR
   ========================================================= */

div[data-testid="stNumberInput"] [data-baseweb="input"],
div[data-testid="stTextInput"] [data-baseweb="input"] {

    background-color: #f5fbff !important;

    border: 1.5px solid #c9e6f5 !important;

    border-radius: 12px !important;

    min-height: 44px !important;

    height: 44px !important;

    overflow: hidden !important;

    box-shadow: none !important;

    transition: all 0.2s ease !important;
}

div[data-testid="stNumberInput"] [data-baseweb="input"]:focus-within,
div[data-testid="stTextInput"] [data-baseweb="input"]:focus-within {

    border-color: #5dade2 !important;

    background-color: #ffffff !important;

    box-shadow:
        0 0 0 3px rgba(93, 173, 226, 0.15) !important;
}

div[data-testid="stNumberInput"] input,
div[data-testid="stTextInput"] input {

    background-color: transparent !important;

    border: none !important;

    color: var(--ink) !important;

    font-size: 14.5px !important;

    font-weight: 600 !important;

    padding: 0 14px !important;

    height: 44px !important;
}


/* =========================================================
   NUMBER BUTTON
   ========================================================= */

div[data-testid="stNumberInput"] button {

    background-color: #e3f2fd !important;

    border: none !important;

    color: #1976d2 !important;

    border-radius: 8px !important;

    margin: 3px !important;

    height: 36px !important;

    width: 36px !important;

    transition: all 0.15s ease !important;
}

div[data-testid="stNumberInput"] button:hover {

    background-color: #bbdefb !important;

    color: #1565c0 !important;
}

div[data-testid="stNumberInput"] button svg {

    fill: #1976d2 !important;
}


/* =========================================================
   SELECTBOX
   ========================================================= */

div[data-testid="stSelectbox"] [data-baseweb="select"],
.stSelectbox [data-baseweb="select"] {

    background-color: transparent !important;
}

div[data-testid="stSelectbox"] [data-baseweb="select"] > div,
.stSelectbox [data-baseweb="select"] > div {

    background-color: #f5fbff !important;

    border: 1.5px solid #c9e6f5 !important;

    border-radius: 12px !important;

    min-height: 44px !important;

    height: 44px !important;

    box-shadow: none !important;

    cursor: pointer !important;

    transition: all 0.2s ease !important;
}

div[data-testid="stSelectbox"] [data-baseweb="select"] > div:hover {

    border-color: #5dade2 !important;
}

div[data-testid="stSelectbox"] [data-baseweb="select"] > div:focus-within {

    border-color: #5dade2 !important;

    background-color: #ffffff !important;

    box-shadow:
        0 0 0 3px rgba(93, 173, 226, 0.15) !important;
}

div[data-testid="stSelectbox"] [data-baseweb="select"] *,
.stSelectbox [data-baseweb="select"] * {

    color: var(--ink) !important;

    background-color: transparent !important;

    font-size: 14.5px !important;

    font-weight: 600 !important;
}

div[data-testid="stSelectbox"] [data-baseweb="select"] svg,
.stSelectbox [data-baseweb="select"] svg {

    fill: var(--ink-light) !important;

    color: var(--ink-light) !important;
}


/* =========================================================
   DROPDOWN
   ========================================================= */

div[data-baseweb="popover"],
div[data-baseweb="popover"] > div,
div[data-baseweb="menu"],
ul[data-baseweb="menu"],
div[role="listbox"] {

    background-color: #ffffff !important;

    border: 1.5px solid #c9e6f5 !important;

    border-radius: 14px !important;

    box-shadow: var(--shadow-lg) !important;
}

li[data-baseweb="menu-item"],
li[role="option"],
div[role="option"],
div[data-baseweb="popover"] [role="option"] {

    background-color: #ffffff !important;

    color: var(--ink) !important;

    border-radius: 10px !important;

    font-size: 14.5px !important;

    padding: 10px 14px !important;

    transition: all 0.15s ease !important;
}

li[data-baseweb="menu-item"]:hover,
li[role="option"]:hover,
div[role="option"]:hover,
div[data-baseweb="popover"] [role="option"]:hover {

    background-color: #e3f2fd !important;

    color: #1976d2 !important;
}

li[aria-selected="true"],
div[role="option"][aria-selected="true"],
div[data-baseweb="popover"] [role="option"][aria-selected="true"] {

    background-color: #d6ecfa !important;

    color: #1976d2 !important;

    font-weight: 700 !important;
}


/* =========================================================
   RATIO CARD
   ========================================================= */

.ratio-card-wrapper {

    position: relative;

    overflow: hidden;

    background: linear-gradient(
        135deg,
        #ffffff 0%,
        #f3faff 100%
    );

    border: 2px solid #85c1e9;

    border-radius: 20px;

    padding: 22px 24px;

    margin: 10px 0 18px;

    box-shadow:
        0 8px 24px rgba(33, 150, 243, 0.12);

    display: flex;

    align-items: center;

    justify-content: space-between;

    flex-wrap: wrap;

    gap: 16px;

    animation: softRise 0.45s ease both;

    transition:
        transform 0.25s ease,
        box-shadow 0.25s ease;
}

.ratio-card-wrapper:hover {

    transform: translateY(-2px);

    box-shadow:
        0 12px 28px rgba(33, 150, 243, 0.18);
}

.ratio-card-wrapper::before {

    content: "";

    position: absolute;

    inset: 0 0 auto;

    height: 4px;

    background: linear-gradient(
        90deg,
        #5dade2,
        #1976d2
    );
}

.ratio-info h4 {

    margin: 0 0 4px;

    font-size: 15px;

    color: #486581;

    font-weight: 700;
}

.ratio-info .ratio-big-value {

    font-size: 34px;

    font-weight: 800;

    color: #1976d2;

    line-height: 1.1;
}

.ratio-info p {

    margin: 4px 0 0;

    font-size: 13px;

    color: #627d98;
}

.ratio-badge {

    padding: 8px 16px;

    border-radius: 999px;

    font-size: 13.5px;

    font-weight: 700;

    display: inline-flex;

    align-items: center;

    gap: 6px;
}


/* =========================================================
   BUTTON PRIMARY
   ========================================================= */

div.stButton > button[kind="primary"],
button[data-testid="baseButton-primary"] {

    background: linear-gradient(
        90deg,
        #1976d2 0%,
        #42a5f5 35%,
        #90caf9 70%,
        #1976d2 100%
    ) !important;

    background-size: 200% auto !important;

    animation: gradientShine 5s linear infinite !important;

    color: #ffffff !important;

    border: none !important;

    border-radius: 16px !important;

    height: 56px !important;

    font-size: 16.5px !important;

    font-weight: 800 !important;

    letter-spacing: 0.5px !important;

    box-shadow:
        0 8px 24px rgba(33, 150, 243, 0.30) !important;

    transition: all 0.25s ease !important;
}

@keyframes gradientShine {

    0% {
        background-position: 0% 50%;
    }

    50% {
        background-position: 100% 50%;
    }

    100% {
        background-position: 0% 50%;
    }
}

div.stButton > button[kind="primary"]:hover,
button[data-testid="baseButton-primary"]:hover {

    transform: translateY(-3px) !important;

    filter: brightness(1.05) !important;

    box-shadow:
        0 14px 32px rgba(33, 150, 243, 0.42) !important;
}


/* =========================================================
   SECONDARY BUTTON
   ========================================================= */

div.stButton > button[kind="secondary"],
button[data-testid="baseButton-secondary"] {

    background: #ffffff !important;

    color: #1976d2 !important;

    border: 1.5px solid #b3ddf5 !important;

    border-radius: 999px !important;

    height: 42px !important;

    font-size: 13px !important;

    font-weight: 700 !important;

    box-shadow:
        0 3px 10px rgba(33, 150, 243, 0.06) !important;

    transition: all 0.2s ease !important;

    padding: 0 14px !important;
}

div.stButton > button[kind="secondary"]:hover,
button[data-testid="baseButton-secondary"]:hover {

    background: #e3f2fd !important;

    border-color: #5dade2 !important;

    color: #1565c0 !important;

    transform: translateY(-2px) !important;

    box-shadow:
        0 6px 16px rgba(33, 150, 243, 0.14) !important;
}


/* =========================================================
   DOWNLOAD BUTTON
   ========================================================= */

div.stDownloadButton > button {

    background: linear-gradient(
        135deg,
        #ffffff,
        #e3f2fd
    ) !important;

    color: #1976d2 !important;

    border: 1.5px solid #c9e6f5 !important;

    border-radius: 14px !important;

    height: 48px !important;

    font-size: 14.5px !important;

    font-weight: 700 !important;

    box-shadow: var(--shadow-sm) !important;

    transition: all 0.2s ease !important;
}

div.stDownloadButton > button:hover {

    border-color: #5dade2 !important;

    background: #d6ecfa !important;

    transform: translateY(-1px);
}


/* =========================================================
   HASIL UNGGUL
   ========================================================= */

.result-unggul {

    background: linear-gradient(
        135deg,
        #e3f2fd 0%,
        #f7fbff 100%
    );

    border: 2.5px solid #5dade2;

    border-radius: 22px;

    padding: 28px;

    text-align: center;

    box-shadow:
        0 12px 28px rgba(33, 150, 243, 0.16);

    animation: softRise 0.5s ease both;
}

.result-unggul h2 {

    color: #1976d2;

    font-size: 28px;

    font-weight: 800;

    margin: 10px 0 6px;
}

.result-unggul p {

    color: #486581;

    font-size: 15px;

    margin: 0;
}


/* =========================================================
   HASIL TIDAK UNGGUL
   ========================================================= */

.result-tidak {

    background: linear-gradient(
        135deg,
        #eaf4ff 0%,
        #f7fbff 100%
    );

    border: 2.5px solid #85c1e9;

    border-radius: 22px;

    padding: 28px;

    text-align: center;

    box-shadow:
        0 12px 28px rgba(33, 150, 243, 0.12);

    animation: softRise 0.5s ease both;
}

.result-tidak h2 {

    color: #1565c0;

    font-size: 28px;

    font-weight: 800;

    margin: 10px 0 6px;
}

.result-tidak p {

    color: #486581;

    font-size: 15px;

    margin: 0;
}


/* =========================================================
   INSIGHT
   ========================================================= */

.insight-card {

    background: #ffffff;

    border: 1.5px solid var(--line);

    border-radius: 18px;

    padding: 20px 22px;

    height: 100%;

    box-shadow: var(--shadow-sm);

    transition:
        transform 0.25s ease,
        box-shadow 0.25s ease;
}

.insight-card:hover {

    transform: translateY(-2px);

    box-shadow: var(--shadow-md);
}

.insight-card h4 {

    margin: 0 0 12px;

    font-size: 16px;

    font-weight: 700;

    display: flex;

    align-items: center;

    gap: 8px;
}

.insight-list {

    list-style: none;

    padding: 0;

    margin: 0;
}

.insight-list li {

    position: relative;

    padding-left: 22px;

    margin-bottom: 10px;

    font-size: 14px;

    line-height: 1.55;

    color: var(--ink);
}

.insight-list li::before {

    content: "•";

    position: absolute;

    left: 6px;

    font-size: 18px;

    color: #42a5f5;
}


/* =========================================================
   EXPANDER
   ========================================================= */

[data-testid="stExpander"] {

    background: #ffffff !important;

    border: 1.5px solid var(--line) !important;

    border-radius: 16px !important;

    box-shadow: var(--shadow-sm) !important;

    overflow: hidden !important;

    margin-top: 1rem !important;
}

[data-testid="stExpander"] summary {

    padding: 14px 18px !important;

    color: var(--ink) !important;

    font-weight: 700 !important;

    font-size: 14.5px !important;
}

[data-testid="stExpander"] summary:hover {

    color: #1976d2 !important;

    background-color: #f0f8ff !important;
}

[data-testid="stExpanderToggleIcon"] {

    color: #1976d2 !important;

    fill: #1976d2 !important;
}


/* =========================================================
   FOOTER
   ========================================================= */

.footer {

    position: relative;

    text-align: center;

    color: #627d98;

    margin-top: 3rem;

    padding: 30px 20px 20px;

    font-size: 13.5px;
}

.footer::before {

    content: "";

    position: absolute;

    top: 0;

    left: 20%;

    right: 20%;

    height: 3px;

    border-radius: 999px;

    background: linear-gradient(
        90deg,
        #5dade2,
        #42a5f5,
        #1976d2
    );
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HELPER FUNCTIONS & PRESETS
# =========================================================

def render_html(markup):
    st.html(textwrap.dedent(markup))


PRESETS = {
    "unggul": {
        "nama": "Sekolah Unggul (Favorit)",
        "jumlah_siswa": 450,
        "jumlah_guru": 30,
        "persentase_guru_bersertifikasi": 92.5,
        "rata_rata_nilai": 91.0,
        "prestasi_akademik": 24,
        "akreditasi": "A",
        "persentase_fasilitas_layak": 95.0,
        "kehadiran_siswa": 96.0,
        "persentase_lulusan_melanjutkan": 92.0
    },
    "standar": {
        "nama": "Sekolah Menengah (Standar)",
        "jumlah_siswa": 400,
        "jumlah_guru": 20,
        "persentase_guru_bersertifikasi": 65.0,
        "rata_rata_nilai": 76.0,
        "prestasi_akademik": 8,
        "akreditasi": "B",
        "persentase_fasilitas_layak": 72.0,
        "kehadiran_siswa": 85.0,
        "persentase_lulusan_melanjutkan": 70.0
    },
    "peningkatan": {
        "nama": "Sekolah Butuh Peningkatan",
        "jumlah_siswa": 350,
        "jumlah_guru": 12,
        "persentase_guru_bersertifikasi": 40.0,
        "rata_rata_nilai": 62.0,
        "prestasi_akademik": 2,
        "akreditasi": "C",
        "persentase_fasilitas_layak": 48.0,
        "kehadiran_siswa": 75.0,
        "persentase_lulusan_melanjutkan": 45.0
    },
    "default": {
        "nama": "Default",
        "jumlah_siswa": 500,
        "jumlah_guru": 30,
        "persentase_guru_bersertifikasi": 80.0,
        "rata_rata_nilai": 80.0,
        "prestasi_akademik": 10,
        "akreditasi": "A",
        "persentase_fasilitas_layak": 85.0,
        "kehadiran_siswa": 90.0,
        "persentase_lulusan_melanjutkan": 80.0
    }
}

# Inisialisasi default state
if "input_jumlah_siswa" not in st.session_state:
    st.session_state["input_jumlah_siswa"] = PRESETS["default"]["jumlah_siswa"]
if "input_jumlah_guru" not in st.session_state:
    st.session_state["input_jumlah_guru"] = PRESETS["default"]["jumlah_guru"]
if "input_guru_bersertifikasi" not in st.session_state:
    st.session_state["input_guru_bersertifikasi"] = PRESETS["default"]["persentase_guru_bersertifikasi"]
if "input_rata_rata_nilai" not in st.session_state:
    st.session_state["input_rata_rata_nilai"] = PRESETS["default"]["rata_rata_nilai"]
if "input_prestasi_akademik" not in st.session_state:
    st.session_state["input_prestasi_akademik"] = PRESETS["default"]["prestasi_akademik"]
if "input_akreditasi" not in st.session_state:
    st.session_state["input_akreditasi"] = PRESETS["default"]["akreditasi"]
if "input_fasilitas_layak" not in st.session_state:
    st.session_state["input_fasilitas_layak"] = PRESETS["default"]["persentase_fasilitas_layak"]
if "input_kehadiran_siswa" not in st.session_state:
    st.session_state["input_kehadiran_siswa"] = PRESETS["default"]["kehadiran_siswa"]
if "input_lulusan_melanjutkan" not in st.session_state:
    st.session_state["input_lulusan_melanjutkan"] = PRESETS["default"]["persentase_lulusan_melanjutkan"]


def apply_preset(preset_key):
    preset = PRESETS[preset_key]
    st.session_state["input_jumlah_siswa"] = int(preset["jumlah_siswa"])
    st.session_state["input_jumlah_guru"] = int(preset["jumlah_guru"])
    st.session_state["input_guru_bersertifikasi"] = float(preset["persentase_guru_bersertifikasi"])
    st.session_state["input_rata_rata_nilai"] = float(preset["rata_rata_nilai"])
    st.session_state["input_prestasi_akademik"] = int(preset["prestasi_akademik"])
    st.session_state["input_akreditasi"] = preset["akreditasi"]
    st.session_state["input_fasilitas_layak"] = float(preset["persentase_fasilitas_layak"])
    st.session_state["input_kehadiran_siswa"] = float(preset["kehadiran_siswa"])
    st.session_state["input_lulusan_melanjutkan"] = float(preset["persentase_lulusan_melanjutkan"])


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:
    if logo_b64:
        render_html(f"""
        <div class="sidebar-logo-box">
            <img src="data:image/png;base64,{logo_b64}" class="sidebar-logo" alt="Logo Sekolah Unggul" />
        </div>
        """)
    else:
        st.image("logo.png", use_container_width=True)

    render_html("""
    <div style="text-align:center; padding: 2px 0 12px;">
        <span class="sidebar-badge">✨ AI EDUCATION SYSTEM</span>
        <h2 style="margin: 4px 0 2px; font-weight: 800;">Sekolah Unggul</h2>
        <p style="margin: 0; opacity: 0.9; font-size: 13.5px;">
            Sistem Prediksi Berbasis Machine Learning
        </p>
    </div>
    """)

    st.markdown("---")

    render_html("""
    <div class="sidebar-card">
        <h4 style="margin: 0 0 8px; color: #ffffff; font-weight: 800;">📌 Tentang Sistem</h4>
        Sistem ini menggunakan algoritma klasifikasi <b>Decision Tree</b> untuk memprediksi mutu kelayakan sekolah berdasarkan 9 indikator utama kualitas pendidikan.
        <br><br>
        <b>Model:</b> 🌳 Decision Tree Classifier<br>
        <b>Fitur:</b> 🎯 Visualisasi Mutu & Analisis Cerdas
    </div>
    """)


# =========================================================
# HEADER / HERO SECTION (DENGAN ANIMASI LOGO MELAYANG & AURA)
# =========================================================

col_logo, col_hero = st.columns([1.25, 4.75])

with col_logo:
    if logo_b64:
        render_html(f"""
        <div class="logo-hero-box">
            <div class="logo-aura"></div>
            <img src="data:image/png;base64,{logo_b64}" class="floating-logo" alt="Logo Sekolah Unggul" />
        </div>
        """)
    else:
        st.image("logo.png", width=200)

with col_hero:
    render_html("""
    <div class="hero-badge">
        <span>✨</span> Machine Learning Decision Tree Classifier • Standar Mutu Pendidikan
    </div>
    <div class="main-title">Sistem Prediksi Sekolah Unggul</div>
    <div class="main-subtitle">
        Evaluasi dan klasifikasikan kualitas sekolah secara otomatis berdasarkan data akademik, tenaga pendidik, fasilitas, serta capaian kelulusan siswa.
    </div>
    """)

st.markdown("---")


# =========================================================
# KARTU PETUNJUK
# =========================================================

render_html("""
<div class="card">
    <h3>💡 Petunjuk Penggunaan</h3>
    <p>
        Pilih salah satu <b>Preset Simulasi Cepat</b> di bawah untuk mengisi data otomatis dalam 1 klik, atau sesuaikan nilai indikator sekolah pada formulir. Setelah data terisi, klik tombol <b>🔍 Prediksi Kelayakan Sekolah Unggul</b> untuk melihat hasil analisis mutu dan visualisasi grafiknya.
    </p>
</div>

<div class="card">
    <h3>💡 Petunjuk Penggunaan</h3>
    <p>
        Pilih salah satu <b>Preset Simulasi Cepat</b> di bawah untuk mengisi data otomatis dalam 1 klik, atau sesuaikan nilai indikator sekolah pada formulir. Setelah data terisi, klik tombol <b>🔍 Prediksi Kelayakan Sekolah Unggul</b> untuk melihat hasil analisis mutu dan visualisasi grafiknya.
    </p>
</div>
""")


# =========================================================
# TOMBOL PRESET / QUICK DEMO (PILL CHIPS)
# =========================================================

st.markdown('<div class="section-title">⚡ Simulasi Cepat (Quick Preset)</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">⚡ KIMPUL (Quick Preset)</div>', unsafe_allow_html=True)

col_p1, col_p2, col_p3, col_p4 = st.columns(4)

with col_p1:
    if st.button("🌟 Sekolah UHUYY", type="secondary", use_container_width=True):
        apply_preset("unggul")
        st.rerun()

with col_p1:
    if st.button("🌟 Sekolah UHUYY", type="secondary", use_container_width=True):
        apply_preset("unggul")
        st.rerun()

with col_p2:
    if st.button("🏫 Sekolah Standar", type="secondary", use_container_width=True):
        apply_preset("standar")
        st.rerun()

with col_p3:
    if st.button("⚠️ Perlu Peningkatan", type="secondary", use_container_width=True):
        apply_preset("peningkatan")
        st.rerun()

with col_p4:
    if st.button("🔄 Reset ke Awal", type="secondary", use_container_width=True):
        apply_preset("default")
        st.rerun()


# =========================================================
# FORMULIR DATA SEKOLAH
# =========================================================

st.markdown('<div class="section-title">📋 Formulir Indikator Sekolah</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">📋 Formulir Pendaftaran Sekolah</div>', unsafe_allow_html=True)

col_left, col_right = st.columns(2)

with col_left:
    jumlah_siswa = st.number_input(
        "👨‍🎓 Jumlah Siswa",
        min_value=1,
        max_value=5000,
        step=1,
        key="input_jumlah_siswa"
    )

    jumlah_guru = st.number_input(
        "👩‍🏫 Jumlah Guru",
        min_value=1,
        max_value=500,
        step=1,
        key="input_jumlah_guru"
    )

    persentase_guru_bersertifikasi = st.number_input(
        "🎓 Guru Bersertifikasi (%)",
        min_value=0.0,
        max_value=100.0,
        step=0.5,
        format="%.1f",
        key="input_guru_bersertifikasi"
    )

    rata_rata_nilai = st.number_input(
        "📚 Rata-rata Nilai Akademik",
        min_value=0.0,
        max_value=100.0,
        step=0.5,
        format="%.1f",
        key="input_rata_rata_nilai"
    )

    prestasi_akademik = st.number_input(
        "🏆 Jumlah Prestasi Akademik",
        min_value=0,
        max_value=100,
        step=1,
        key="input_prestasi_akademik"
    )

with col_right:
    akreditasi_options = ["A", "B", "C"]
    akreditasi = st.selectbox(
        "🏅 Akreditasi Sekolah",
        akreditasi_options,
        key="input_akreditasi"
    )

    persentase_fasilitas_layak = st.number_input(
        "🏢 Fasilitas Layak (%)",
        min_value=0.0,
        max_value=100.0,
        step=0.5,
        format="%.1f",
        key="input_fasilitas_layak"
    )

    kehadiran_siswa = st.number_input(
        "📅 Kehadiran Siswa (%)",
        min_value=0.0,
        max_value=100.0,
        step=0.5,
        format="%.1f",
        key="input_kehadiran_siswa"
    )

    persentase_lulusan_melanjutkan = st.number_input(
        "🎓 Lulusan Melanjutkan Pendidikan (%)",
        min_value=0.0,
        max_value=100.0,
        step=0.5,
        format="%.1f",
        key="input_lulusan_melanjutkan"
    )


# =========================================================
# RASIO GURU & SISWA DENGAN STATUS CERDAS
# =========================================================

rasio_guru_siswa = jumlah_siswa / max(jumlah_guru, 1)

if 12 <= rasio_guru_siswa <= 20:
    badge_status = "🟢 Rasio Sangat Ideal"
    badge_color = "#2b8a3e"
    badge_bg = "#ebfbee"
    badge_text = "Sangat sesuai dengan standar Permendikbud (1 : 15 s/d 1 : 20)"
elif 20 < rasio_guru_siswa <= 28:
    badge_status = "🟡 Rasio Cukup Wajar"
    badge_color = "#d97706"
    badge_bg = "#fffbeb"
    badge_text = "Masih dalam batas wajar kapasitas pengajaran guru"
elif rasio_guru_siswa > 28:
    badge_status = "🔴 Rasio Padat (Kurang Guru)"
    badge_color = "#e11d48"
    badge_bg = "#ffe4e6"
    badge_text = "Jumlah siswa per guru cukup tinggi, disarankan penambahan guru"
else:
    badge_status = "🔵 Rasio Sangat Renggang"
    badge_color = "#2563eb"
    badge_bg = "#eff6ff"
    badge_text = "Proporsi guru sangat mencukupi dibanding jumlah siswa"

render_html(f"""
<div class="ratio-card-wrapper">
    <div class="ratio-info">
        <h4>👥 Rasio Guru dan Siswa</h4>
        <div class="ratio-big-value">1 : {rasio_guru_siswa:.2f}</div>
        <p>Setiap 1 orang guru membimbing rata-rata {rasio_guru_siswa:.1f} siswa</p>
    </div>
    <div>
        <div class="ratio-badge" style="color: {badge_color}; background: {badge_bg}; border: 1px solid {badge_color}33;">
            {badge_status}
        </div>
        <div style="font-size: 12.5px; color: #8a5362; margin-top: 6px; text-align: right;">
            {badge_text}
        </div>
    </div>
</div>
""")


# =========================================================
# TOMBOL PREDIKSI
# =========================================================

st.markdown("<br>", unsafe_allow_html=True)

prediksi = st.button("🔍  PREDIKSI KELAYAKAN SEKOLAH UNGGUL", type="primary", use_container_width=True)


# =========================================================
# PROSES PREDIKSI & VISUALISASI
# =========================================================

if prediksi:

    # One-Hot Encoding Akreditasi
    akreditasi_A = 1 if akreditasi == "A" else 0
    akreditasi_B = 1 if akreditasi == "B" else 0
    akreditasi_C = 1 if akreditasi == "C" else 0

    data_encoded = pd.DataFrame({
        "akreditasi_A": [akreditasi_A],
        "akreditasi_B": [akreditasi_B],
        "akreditasi_C": [akreditasi_C],
        "jumlah_siswa": [jumlah_siswa],
        "jumlah_guru": [jumlah_guru],
        "rasio_guru_siswa": [rasio_guru_siswa],
        "persentase_guru_bersertifikasi": [persentase_guru_bersertifikasi],
        "rata_rata_nilai": [rata_rata_nilai],
        "prestasi_akademik": [prestasi_akademik],
        "persentase_fasilitas_layak": [persentase_fasilitas_layak],
        "kehadiran_siswa": [kehadiran_siswa],
        "persentase_lulusan_melanjutkan": [persentase_lulusan_melanjutkan]
    })

    try:
        hasil = model.predict(data_encoded)[0]
        probabilitas = model.predict_proba(data_encoded)[0]
        prob_dict = dict(zip(model.classes_, probabilitas))
        confidence_unggul = prob_dict.get("Unggul", 0.0) * 100
        confidence_tidak = prob_dict.get("Tidak Unggul", 0.0) * 100

        # Efek Balon Animasi jika Unggul
        if hasil == "Unggul":
            st.balloons()

        st.markdown("---")
        st.markdown('<div class="section-title">🎯 Hasil Klasifikasi & Analisis Mutu</div>', unsafe_allow_html=True)

        # 1. BANNER HASIL
        if hasil == "Unggul":
            render_html(f"""
            <div class="result-unggul">
                <div style="font-size: 64px; line-height: 1;">🏆</div>
                <h2>SEKOLAH TERKLASIFIKASI UNGGUL</h2>
                <p>
                    Berdasarkan evaluasi algoritma Decision Tree, sekolah ini memiliki mutu di atas rata-rata dengan tingkat keyakinan model sebesar <b>{confidence_unggul:.1f}%</b>.
                </p>
            </div>
            """)
        else:
            render_html(f"""
            <div class="result-tidak">
                <div style="font-size: 64px; line-height: 1;">📌</div>
                <h2>SEKOLAH BELUM UNGGUL</h2>
                <p>
                    Berdasarkan evaluasi indikator saat ini, sekolah memerlukan peningkatan pada beberapa aspek mutu untuk mencapai predikat Unggul (Keyakinan: <b>{confidence_tidak:.1f}%</b>).
                </p>
            </div>
            """)

        st.markdown("<br>", unsafe_allow_html=True)

        # 2. GRAFIK INTERAKTIF (DONUT CHART & RADAR CHART)
        col_g1, col_g2 = st.columns([1.1, 1.4])

        with col_g1:
            st.markdown('<h4 style="color:#d6336c; font-weight:700; margin-bottom:0;">🍩 Tingkat Keyakinan Model</h4>', unsafe_allow_html=True)
            
            # Donut Chart Plotly
            donut_colors = ['#ff6f91', '#ffd166'] if model.classes_[0] == 'Unggul' else ['#ffd166', '#ff6f91']
            fig_donut = go.Figure(data=[go.Pie(
                labels=list(model.classes_),
                values=[float(p) for p in probabilitas],
                hole=0.64,
                marker=dict(
                    colors=donut_colors,
                    line=dict(color='#ffffff', width=3)
                ),
                textinfo='label+percent',
                textfont=dict(size=13, family='Plus Jakarta Sans', color='#4a2835'),
                hoverinfo='label+percent',
            )])

            highest_prob = max(probabilitas) * 100
            fig_donut.update_layout(
                showlegend=False,
                margin=dict(l=15, r=15, t=20, b=20),
                height=280,
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                annotations=[dict(
                    text=f"<b>{highest_prob:.1f}%</b><br><span style='font-size:12px;color:#8a5362;'>Keyakinan</span>",
                    x=0.5, y=0.5, font_size=20, font_color='#d6336c', showarrow=False
                )]
            )
            st.plotly_chart(fig_donut, use_container_width=True)

        with col_g2:
            st.markdown('<h4 style="color:#d6336c; font-weight:700; margin-bottom:0;">🕸️ Profil Mutu vs Benchmark Unggul</h4>', unsafe_allow_html=True)
            
            # Radar Chart Plotly
            categories = ['Akademik', 'Fasilitas', 'Guru Sertifikasi', 'Kehadiran', 'Kelulusan']
            school_values = [
                rata_rata_nilai,
                persentase_fasilitas_layak,
                persentase_guru_bersertifikasi,
                kehadiran_siswa,
                persentase_lulusan_melanjutkan
            ]
            benchmark_values = [85.0, 85.0, 80.0, 90.0, 85.0]

            fig_radar = go.Figure()
            fig_radar.add_trace(go.Scatterpolar(
                r=school_values,
                theta=categories,
                fill='toself',
                name='Sekolah Ini',
                line_color='#ff6f91',
                fillcolor='rgba(255, 111, 145, 0.35)'
            ))
            fig_radar.add_trace(go.Scatterpolar(
                r=benchmark_values,
                theta=categories,
                fill='toself',
                name='Standar Unggul',
                line_color='#f59f00',
                fillcolor='rgba(255, 209, 102, 0.20)'
            ))

            fig_radar.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        range=[0, 100],
                        tickfont=dict(size=10, color='#8a5362')
                    ),
                    bgcolor='rgba(255, 255, 255, 0.6)'
                ),
                showlegend=True,
                legend=dict(orientation="h", yanchor="bottom", y=-0.15, xanchor="center", x=0.5),
                margin=dict(l=25, r=25, t=25, b=25),
                height=280,
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)'
            )
            st.plotly_chart(fig_radar, use_container_width=True)

        # 3. SMART INSIGHTS & REKOMENDASI PINTAR
        st.markdown('<div class="section-title">💡 Analisis Pintar & Rekomendasi</div>', unsafe_allow_html=True)

        strengths = []
        improvements = []

        if akreditasi == "A":
            strengths.append("<b>Akreditasi A:</b> Sekolah memiliki legalitas dan penilaian institusi peringkat tertinggi.")
        else:
            improvements.append(f"<b>Peningkatan Akreditasi:</b> Akreditasi saat ini ({akreditasi}) dapat ditingkatkan ke A melalui pemenuhan 8 Standar Nasional Pendidikan.")

        if rata_rata_nilai >= 85:
            strengths.append(f"<b>Akademik Sangat Baik:</b> Rata-rata nilai ({rata_rata_nilai}) berada di atas standar unggul.")
        elif rata_rata_nilai >= 75:
            strengths.append(f"<b>Akademik Baik:</b> Rata-rata nilai ({rata_rata_nilai}) sudah cukup baik.")
        else:
            improvements.append(f"<b>Penguatan Nilai Akademik:</b> Nilai rata-rata ({rata_rata_nilai}) masih di bawah standar 80. Disarankan program bimbingan belajar intensif.")

        if persentase_fasilitas_layak >= 85:
            strengths.append(f"<b>Fasilitas Prima:</b> Kelayakan sarana dan prasarana ({persentase_fasilitas_layak}%) sangat menunjang pembelajaran.")
        else:
            improvements.append(f"<b>Modernisasi Fasilitas:</b> Fasilitas layak ({persentase_fasilitas_layak}%) perlu ditingkatkan terutama lab komputer, perpustakaan, dan ruang kelas.")

        if persentase_guru_bersertifikasi >= 80:
            strengths.append(f"<b>SDM Pendidik Profesional:</b> Sebanyak {persentase_guru_bersertifikasi}% guru telah memiliki sertifikasi pendidik.")
        else:
            improvements.append(f"<b>Program Sertifikasi Guru:</b> Tingkat guru bersertifikasi ({persentase_guru_bersertifikasi}%) perlu didorong melalui program PPG.")

        if prestasi_akademik >= 10:
            strengths.append(f"<b>Kaya Prestasi:</b> Memiliki {prestasi_akademik} torehan prestasi akademik di tingkat daerah/nasional.")
        else:
            improvements.append(f"<b>Dukungan Kompetisi Siswa:</b> Prestasi akademik ({prestasi_akademik}) dapat ditingkatkan dengan memfasilitasi olimpiade dan lomba sains.")

        if persentase_lulusan_melanjutkan >= 80:
            strengths.append(f"<b>Daya Saing Kelulusan:</b> {persentase_lulusan_melanjutkan}% lulusan berhasil melanjutkan pendidikan ke jenjang lebih tinggi.")
        else:
            improvements.append(f"<b>Bimbingan Karir & Studi:</b> Sebanyak {100 - persentase_lulusan_melanjutkan:.1f}% lulusan belum melanjutkan studi. Perlu konseling karir dan informasi beasiswa.")

        col_ins1, col_ins2 = st.columns(2)

        with col_ins1:
            render_html(f"""
            <div class="insight-card" style="border-top: 4px solid #2b8a3e;">
                <h4 style="color: #2b8a3e;">🌟 Keunggulan Utama Sekolah</h4>
                <ul class="insight-list">
                    {''.join([f'<li>{s}</li>' for s in strengths]) if strengths else '<li>Data indikator masih dalam tahap berkembang.</li>'}
                </ul>
            </div>
            """)

        with col_ins2:
            render_html(f"""
            <div class="insight-card" style="border-top: 4px solid #f59f00;">
                <h4 style="color: #d97706;">🚀 Rekomendasi Peningkatan Mutu</h4>
                <ul class="insight-list">
                    {''.join([f'<li>{imp}</li>' for imp in improvements]) if improvements else '<li>Pertahankan seluruh standar mutu prima yang sudah dicapai!</li>'}
                </ul>
            </div>
            """)

        # 4. TABEL DETAIL DATA MODEL
        with st.expander("Lihat Data Matriks yang Diproses Model"):
            st.dataframe(
                data_encoded.style
                .set_properties(**{
                    "background-color": "#fff9fb",
                    "color": "#4a2835",
                    "border-color": "#ffd6df"
                })
                .set_table_styles([
                    {
                        "selector": "th",
                        "props": [
                            ("background-color", "#ff8fab"),
                            ("color", "#ffffff"),
                            ("font-weight", "700"),
                            ("border-color", "#ffd6df")
                        ]
                    },
                    {
                        "selector": "td",
                        "props": [
                            ("background-color", "#fff9fb"),
                            ("color", "#4a2835"),
                            ("border-color", "#ffd6df")
                        ]
                    }
                ]),
                use_container_width=True
            )

        # 5. TOMBOL DOWNLOAD LAPORAN EVALUASI
        st.markdown("<br>", unsafe_allow_html=True)
        now_str = datetime.datetime.now().strftime("%d %B %Y, %H:%M:%S")

        report_content = f"""==================================================
LAPORAN EVALUASI & KLASIFIKASI MUTU SEKOLAH
Sistem Berbasis Decision Tree Machine Learning
==================================================
Waktu Evaluasi : {now_str}
Hasil Prediksi : SEKOLAH {hasil.upper()}
Tingkat Keyakinan : {highest_prob:.2f}%

RINGKASAN INDIKATOR SEKOLAH:
- Akreditasi Sekolah              : {akreditasi}
- Jumlah Siswa                    : {jumlah_siswa} orang
- Jumlah Guru                     : {jumlah_guru} orang
- Rasio Guru : Siswa              : 1 : {rasio_guru_siswa:.2f} ({badge_status})
- Persentase Guru Bersertifikasi : {persentase_guru_bersertifikasi}%
- Rata-rata Nilai Akademik        : {rata_rata_nilai}
- Jumlah Prestasi Akademik        : {prestasi_akademik} prestasi
- Fasilitas Layak                 : {persentase_fasilitas_layak}%
- Tingkat Kehadiran Siswa         : {kehadiran_siswa}%
- Lulusan Melanjutkan Pendidikan  : {persentase_lulusan_melanjutkan}%

PROBABILITAS MODEL:
"""
        for cls_name, p in prob_dict.items():
            report_content += f"- {cls_name}: {p*100:.2f}%\n"

        report_content += "\nPOIN KEUNGGULAN UTAMA:\n"
        for s in strengths:
            clean_s = s.replace("<b>", "").replace("</b>", "")
            report_content += f"* {clean_s}\n"

        report_content += "\nREKOMENDASI PERBAIKAN MUTU:\n"
        for imp in improvements:
            clean_imp = imp.replace("<b>", "").replace("</b>", "")
            report_content += f"* {clean_imp}\n"

        report_content += "\n==================================================\n"
        report_content += "Dicetak otomatis oleh Sistem Prediksi Sekolah Unggul\n"

        col_d1, col_d2, col_d3 = st.columns([1, 2, 1])
        with col_d2:
            st.download_button(
                label="📥 Unduh Ringkasan Laporan Mutu (.txt)",
                data=report_content,
                file_name=f"Laporan_Prediksi_Sekolah_{hasil}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                mime="text/plain",
                use_container_width=True
            )

    except Exception as e:
        st.error("❌ Terjadi kesalahan saat melakukan prediksi.")
        st.code(str(e))


# =========================================================
# FOOTER
# =========================================================

render_html("""
<div class="footer">
    🏫 <b>Prediksi Sekolah Unggul</b> • Sistem Klasifikasi Mutu Pendidikan
    <br><br>
    Decision Tree Classifier • Streamlit • Plotly Analytics
</div>
""")