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