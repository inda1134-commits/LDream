def get_custom_css():

    return """
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700&family=Noto+Sans+KR:wght@300;400;500;700&display=swap');

    /* =========================================================
       전체 배경
    ========================================================= */

    html, body, [class*="css"] {

        font-family: 'Noto Sans KR', sans-serif;

        background:
            radial-gradient(
                circle at top,
                #261046 0%,
                #14071f 45%,
                #05030d 100%
            );

        color: #ffffff !important;
    }

    .stApp {

        background:
            radial-gradient(
                circle at top,
                #261046 0%,
                #14071f 45%,
                #05030d 100%
            );
    }

    /* =========================================================
       전체 기본 글자
    ========================================================= */

    * {

        color: #ffffff;
    }

    /* =========================================================
       제목
    ========================================================= */

    .main-title {

        text-align: center;

        font-size: 56px;

        font-weight: 700;

        margin-top: 20px;

        margin-bottom: 10px;

        color: #f5d0fe !important;

        font-family: 'Cinzel', serif;

        letter-spacing: 2px;

        text-shadow:
            0 0 12px #d946ef,
            0 0 28px #9333ea,
            0 0 50px #6b21a8;
    }

    .sub-title {

        text-align: center;

        font-size: 18px;

        color: #ede9fe !important;

        margin-bottom: 35px;
    }

    /* =========================================================
       입력 라벨
    ========================================================= */

    .stTextArea label,
    .stTextInput label,
    .stDateInput label,
    .stSelectbox label,
    .stMultiSelect label {

        color: #ffffff !important;

        font-weight: 800 !important;

        font-size: 17px !important;
    }

    /* =========================================================
       TEXT AREA
    ========================================================= */

    .stTextArea textarea {

        background: #ffffff !important;

        color: #111827 !important;

        border-radius: 18px !important;

        border:
            2px solid #8b5cf6 !important;

        font-size: 16px !important;

        font-weight: 700 !important;

        padding: 16px !important;

        box-shadow:
            0 0 15px rgba(139,92,246,0.18);
    }

    .stTextArea textarea::placeholder {

        color: #6b7280 !important;

        opacity: 1 !important;
    }

    /* =========================================================
       INPUT 공통
    ========================================================= */

    input {

        background: #ffffff !important;

        color: #111827 !important;

        font-weight: 700 !important;

        border-radius: 14px !important;
    }

    /* =========================================================
       SELECTBOX 본체
    ========================================================= */

    .stSelectbox div[data-baseweb="select"] {

        background: #ffffff !important;

        border:
            2px solid #8b5cf6 !important;

        border-radius: 14px !important;

        min-height: 50px !important;

        box-shadow:
            0 0 12px rgba(139,92,246,0.15);
    }

    /* 선택된 값 */

    .stSelectbox div[data-baseweb="select"] *,
    .stSelectbox span,
    .stSelectbox div {

        color: #111111 !important;

        font-weight: 900 !important;

        font-size: 15px !important;

        opacity: 1 !important;
    }

    /* =========================================================
       SELECTBOX 드롭다운 팝업
    ========================================================= */

    div[role="listbox"],
    ul[role="listbox"] {

        background: #ffffff !important;

        border:
            2px solid #7c3aed !important;

        border-radius: 14px !important;

        overflow-y: auto !important;
        overflow-x: hidden !important;

        max-height: 320px !important;

        box-shadow:
            0 0 25px rgba(0,0,0,0.35) !important;
    }

    /* =========================================================
       드롭다운 옵션 글자색 강제
    ========================================================= */

    div[role="option"],
    div[role="option"] *,
    ul[role="listbox"] li,
    ul[role="listbox"] li *,
    li[role="option"],
    li[role="option"] * {

        background: #ffffff !important;

        color: #111111 !important;

        font-weight: 900 !important;

        font-size: 16px !important;

        line-height: 1.6 !important;

        opacity: 1 !important;
    }

    /* =========================================================
       드롭다운 hover
    ========================================================= */

    div[role="option"]:hover,
    div[role="option"]:hover *,
    li[role="option"]:hover,
    li[role="option"]:hover * {

        background:
            linear-gradient(
                135deg,
                #7c3aed,
                #06b6d4
            ) !important;

        color: #ffffff !important;
    }

    /* =========================================================
       DATE INPUT
    ========================================================= */

    .stDateInput input {

        background: #ffffff !important;

        color: #111827 !important;

        font-weight: 900 !important;

        border:
            2px solid #8b5cf6 !important;

        border-radius: 14px !important;
    }

    /* =========================================================
       달력 팝업
    ========================================================= */

    div[data-baseweb="calendar"] {

        background: #ffffff !important;

        border:
            2px solid #7c3aed !important;

        border-radius: 18px !important;

        box-shadow:
            0 0 30px rgba(0,0,0,0.35) !important;
    }

    /* =========================================================
       달력 전체 글자
    ========================================================= */

    div[data-baseweb="calendar"] * {

        color: #000000 !important;

        font-weight: 900 !important;

        opacity: 1 !important;
    }

    /* =========================================================
       요일 헤더
    ========================================================= */

    div[role="columnheader"] {

        background: #ede9fe !important;

        color: #4c1d95 !important;

        font-weight: 900 !important;

        font-size: 15px !important;
    }

    /* =========================================================
       날짜 버튼
    ========================================================= */

    button[role="gridcell"] {

        background: #ffffff !important;

        color: #000000 !important;

        font-weight: 900 !important;

        font-size: 15px !important;

        border-radius: 10px !important;
    }

    /* =========================================================
       날짜 hover
    ========================================================= */

    button[role="gridcell"]:hover {

        background:
            linear-gradient(
                135deg,
                #7c3aed,
                #06b6d4
            ) !important;

        color: #ffffff !important;
    }

    /* =========================================================
       선택된 날짜
    ========================================================= */

    button[aria-selected="true"] {

        background:
            linear-gradient(
                135deg,
                #7c3aed,
                #9333ea
            ) !important;

        color: #ffffff !important;

        font-weight: 900 !important;
    }

    /* =========================================================
       버튼
    ========================================================= */

    .stButton button {

        background:
            linear-gradient(
                135deg,
                #7c3aed,
                #9333ea,
                #06b6d4
            );

        color: #ffffff !important;

        border: none !important;

        border-radius: 18px !important;

        height: 60px !important;

        font-size: 20px !important;

        font-weight: 800 !important;

        letter-spacing: 1px !important;

        box-shadow:
            0 0 20px rgba(139,92,246,0.35);
    }

    .stButton button:hover {

        filter: brightness(1.08);

        transform: scale(1.01);
    }

    /* =========================================================
       다운로드 버튼
    ========================================================= */

    .stDownloadButton button {

        background:
            linear-gradient(
                135deg,
                #0f766e,
                #14b8a6,
                #22d3ee
            ) !important;

        color: #ffffff !important;

        border: none !important;

        border-radius: 16px !important;

        font-weight: 800 !important;

        height: 54px !important;
    }

    /* =========================================================
       EXPANDER
    ========================================================= */

    .stExpander {

        background:
            rgba(20, 10, 35, 0.92) !important;

        border:
            1px solid rgba(168,85,247,0.35) !important;

        border-radius: 16px !important;
    }

    .streamlit-expanderHeader {

        color: #f5d0fe !important;

        font-weight: 800 !important;
    }

    /* =========================================================
       SIDEBAR
    ========================================================= */

    section[data-testid="stSidebar"] {

        background:
            linear-gradient(
                180deg,
                #14071f 0%,
                #1c1038 50%,
                #0b0618 100%
            );

        border-right:
            1px solid rgba(168,85,247,0.2);
    }

    /* =========================================================
       SUCCESS
    ========================================================= */

    .stSuccess {

        background:
            rgba(34,197,94,0.15) !important;

        border:
            1px solid rgba(74,222,128,0.4) !important;

        border-radius: 14px !important;

        color: #dcfce7 !important;
    }

    /* =========================================================
       스크롤바
    ========================================================= */

    ::-webkit-scrollbar {

        width: 10px;
    }

    ::-webkit-scrollbar-track {

        background: #14071f;
    }

    ::-webkit-scrollbar-thumb {

        background:
            linear-gradient(
                #7c3aed,
                #06b6d4
            );

        border-radius: 20px;
    }
    
    /* =========================================================
    Streamlit 상단 메뉴 배경 통일
    ========================================================= */

    header[data-testid="stHeader"] {

        background:
            linear-gradient(
                180deg,
                #0f172a,
                #111827
            ) !important;
    }

    [data-testid="stToolbar"] {

        background:
            linear-gradient(
                180deg,
                #0f172a,
                #111827
            ) !important;
    }

    [data-testid="stDecoration"] {

        background: transparent !important;
    }

    [data-testid="stStatusWidget"] {

        background: transparent !important;
    }

    /* =========================================================
    Sidebar Collapse 버튼 (<<) 색상
    ========================================================= */

    button[kind="header"] {

        color: #ffffff !important;
    }

    button[kind="header"]:hover {

        color: #c084fc !important;
    }
    </style>
    """