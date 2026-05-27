import streamlit as st

from datetime import date, datetime

from ui.sidebar import sidebar_ui

from services.dream_service import DreamService
from services.saju_service import SajuService
from services.lotto_service import LottoService
from services.report_service import ReportService

from core.progress import ProgressManager
from core.logger import logger

from ui.lotto_ui import lotto_balls
from ui.styles import get_custom_css

from config.settings import Settings
from config.constants import ZODIAC_ANIMALS


st.set_page_config(
    page_title="Mystic Dream Lotto",
    layout="wide"
)

st.markdown(
    get_custom_css(),
    unsafe_allow_html=True
)

# =========================================================
# Session State
# =========================================================

if "progress" not in st.session_state:
    st.session_state.progress = 0

if "runtime_api_key" not in st.session_state:
    st.session_state.runtime_api_key = ""

# =========================================================
# Sidebar
# =========================================================

inputs = sidebar_ui()

# =========================================================
# 런타임 API KEY 관리
# Streamlit Cloud 배포 시 노출 방지
# =========================================================

st.session_state.runtime_api_key = inputs["api_key"]

if inputs["provider"] == "openai":
    Settings.OPENAI_API_KEY = st.session_state.runtime_api_key

elif inputs["provider"] == "anthropic":
    Settings.ANTHROPIC_API_KEY = st.session_state.runtime_api_key

elif inputs["provider"] == "google":
    Settings.GOOGLE_API_KEY = st.session_state.runtime_api_key

# =========================================================
# Main UI
# =========================================================

st.markdown(
    """
    <div class="main-title">
        🔮 Mystic Dream Lotto
    </div>
    <div class="sub-title">
        꿈 · 사주 · 무의식의 상징을 분석하여 숨겨진 숫자를 찾아냅니다
    </div>
    """,
    unsafe_allow_html=True
)

dream_text = st.text_area(
    "🌙 해몽할 꿈 내용을 입력하세요",
    height=220,
    placeholder="예: 조상님이 꿈속에 나타났어요...(없으면 '꿈이 없음')"
)

st.markdown("---")

st.subheader("🪐 사주 정보 입력")

col1, col2 = st.columns(2)

with col1:
    birth_date = st.date_input(
        "📅 출생년월일(양력)",
        min_value=date(1920, 1, 1),
        max_value=date.today(),
        value=date(1990, 1, 1)
    )

with col2:

    birth_time_options = [
        "선택하지 않음"
    ] + list(ZODIAC_ANIMALS.keys())

    birth_time = st.selectbox(
        "🐉 생시 선택",
        options=birth_time_options,
        index=0,
        format_func=lambda x:
        "생시 모름"
        if x == "선택하지 않음"
        else f"{x} {ZODIAC_ANIMALS[x]}"
    )

birth_time_value = (
    ""
    if birth_time == "선택하지 않음"
    else birth_time
)

gender = st.selectbox(
    "⚖ 성별",
    ["선택 안함", "남성", "여성"]
)

gender_val = (
    ""
    if gender == "선택 안함"
    else gender
)

st.markdown("---")

# =========================================================
# 분석 시작
# =========================================================

if st.button(
    "✨ 운명의 숫자 해석 시작",
    use_container_width=True
):

    if not dream_text.strip():
        st.error("꿈 내용을 입력하세요.")
        st.stop()

    if not st.session_state.runtime_api_key:
        st.error("API 키를 입력하세요.")
        st.stop()

    try:

        progress_bar = st.progress(0)
        status_text = st.empty()

        analysis_year = date.today().year

        # =====================================================
        # 꿈 분석
        # =====================================================

        ProgressManager.update(
            progress_bar,
            status_text,
            0.1,
            "🌙 꿈의 상징을 분석하는 중..."
        )

        dream_result = DreamService.analyze(
            provider=inputs["provider"],
            model=inputs["model"],
            dream_text=dream_text
        )

        # =====================================================
        # 사주 분석
        # =====================================================

        ProgressManager.update(
            progress_bar,
            status_text,
            0.4,
            "🪐 사주 흐름을 계산하는 중..."
        )

        saju_service = SajuService()

        saju_result = saju_service.analyze_saju(
            provider=inputs["provider"],
            model=inputs["model"],
            birth_date=birth_date.strftime("%Y-%m-%d"),
            birth_time=birth_time_value,
            gender=gender_val,
            analysis_year=analysis_year
        )

        # =====================================================
        # 번호 추출
        # =====================================================

        ProgressManager.update(
            progress_bar,
            status_text,
            0.7,
            "🎲 숨겨진 숫자를 추출하는 중..."
        )

        combined_text = (
            str(dream_result)
            + "\n"
            + str(saju_result)
        )

        symbol_numbers = (
            LottoService.extract_numbers_from_text(
                combined_text
            )
        )

        lotto_result = (
            LottoService.recommend_numbers(
                symbol_numbers
            )
        )

        lotto_numbers = lotto_result["numbers"]
        lotto_reasons = lotto_result["reasons"]

        ProgressManager.update(
            progress_bar,
            status_text,
            1.0,
            "🔮 분석 완료"
        )

        st.success(
            "운명의 숫자 분석이 완료되었습니다."
        )

        # =====================================================
        # 결과 출력
        # =====================================================

        st.markdown("## 🎯 추천 로또 번호")

        lotto_balls(lotto_numbers)

        st.markdown("---")

        with st.expander("🌙 꿈 해몽 결과 보기"):
            st.write(dream_result)

        with st.expander("🪐 사주 분석 결과 보기"):
            st.write(saju_result)

        with st.expander("🎲 숫자 추천 이유 보기"):

            for number, reason in lotto_reasons.items():

                st.markdown(
                    f"**{number}** → {reason}"
                )

        # =====================================================
        # PDF 리포트 생성
        # =====================================================

        report_data = {
            "provider": inputs["provider"],
            "model": inputs["model"],
            "dream_text": dream_text,
            "birth_date": birth_date.strftime("%Y-%m-%d"),
            "birth_time": birth_time_value,
            "gender": gender_val,
            "analysis_year": analysis_year,
            "dream_result": dream_result,
            "saju_result": saju_result,
            "lotto_numbers": lotto_numbers,
            "lotto_reasons": lotto_reasons,
        }

        # API KEY 저장 금지
        pdf_buffer = (
            ReportService.generate_pdf(
                report_data
            )
        )

        ReportService.save_report(report_data)

        st.download_button(
            label="📥 PDF 분석 리포트 다운로드",
            data=pdf_buffer,
            file_name=(
                f"dream_report_"
                f"{date.today().strftime('%Y%m%d')}.pdf"
            ),
            mime="application/pdf",
            use_container_width=True
        )
    except Exception as e:

        logger.exception(e)

        st.error(
            "분석 중 오류가 발생했습니다."
        )

        if Settings.DEBUG:
            st.exception(e)