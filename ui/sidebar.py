import streamlit as st

from config.settings import Settings


def sidebar_ui():

    with st.sidebar:

        st.markdown("## 🔮 AI 설정")

        provider = st.selectbox(
            "LLM 공급사",
            ["openai", "anthropic", "google"],
            index=0
        )

        # =====================================================
        # OpenAI
        # =====================================================

        if provider == "openai":

            api_key = st.text_input(
                "OpenAI API Key",
                value="",
                type="password",
                placeholder="sk-..."
            )

            model = st.selectbox(
                "OpenAI 모델",
                Settings.OPENAI_MODELS,
                index=1
            )

        # =====================================================
        # Anthropic
        # =====================================================

        elif provider == "anthropic":

            api_key = st.text_input(
                "Anthropic API Key",
                value="",
                type="password",
                placeholder="sk-ant-..."
            )

            model = st.selectbox(
                "Anthropic 모델",
                Settings.ANTHROPIC_MODELS,
                index=1
            )

        # =====================================================
        # Google
        # =====================================================

        else:

            api_key = st.text_input(
                "Google API Key",
                value="",
                type="password",
                placeholder="AIza..."
            )

            model = st.selectbox(
                "Gemini 모델",
                Settings.GOOGLE_MODELS,
                index=1
            )

        st.markdown("---")

        st.caption(
            "🌙 꿈 · 사주 · 로또 AI 분석 시스템"
        )

        st.info(
            "🔐 API KEY는 세션에만 유지되며 저장되지 않습니다."
        )

    return {
        "provider": provider,
        "api_key": api_key,
        "model": model
    }