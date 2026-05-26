from dotenv import load_dotenv
import os

load_dotenv()


class Settings:

    # =========================================================
    # 기본 Provider
    # =========================================================
    DEFAULT_LLM_PROVIDER = os.getenv(
        "DEFAULT_LLM_PROVIDER",
        "openai"
    )

    # =========================================================
    # API KEY
    # =========================================================
    OPENAI_API_KEY = os.getenv(
        "OPENAI_API_KEY",
        ""
    )

    ANTHROPIC_API_KEY = os.getenv(
        "ANTHROPIC_API_KEY",
        ""
    )

    GOOGLE_API_KEY = os.getenv(
        "GOOGLE_API_KEY",
        ""
    )

    # =========================================================
    # OpenAI 가성비 모델 추천
    # =========================================================
    OPENAI_MODELS = [

        # 초저비용 + 빠른 응답
        "gpt-4.1-nano",

        # 최고 가성비 범용 모델
        "gpt-4.1-mini",

        # 고성능 추론 + 실무용 밸런스
        "gpt-5-mini",
    ]

    OPENAI_MODEL = os.getenv(
        "OPENAI_MODEL",
        OPENAI_MODELS[1]
    )

    # =========================================================
    # Anthropic 가성비 모델 추천
    # =========================================================
    ANTHROPIC_MODELS = [

        # 초고속 저비용
        "claude-3-5-haiku-latest",

        # 최고 밸런스
        "claude-3-7-sonnet-latest",

        # 최신 고성능 Sonnet
        "claude-sonnet-4-20250514",
    ]

    ANTHROPIC_MODEL = os.getenv(
        "ANTHROPIC_MODEL",
        ANTHROPIC_MODELS[1]
    )

    # =========================================================
    # Google Gemini 가성비 모델 추천
    # =========================================================
    GOOGLE_MODELS = [

        # 초저비용
        "gemini-2.0-flash-lite",

        # 가장 안정적인 가성비
        "gemini-2.0-flash",

        # 최신 고성능 Flash
        "gemini-2.5-flash",
    ]

    GOOGLE_MODEL = os.getenv(
        "GOOGLE_MODEL",
        GOOGLE_MODELS[1]
    )

    # =========================================================
    # 공통 생성 설정
    # =========================================================
    DEFAULT_TEMPERATURE = float(
        os.getenv(
            "DEFAULT_TEMPERATURE",
            "1"
        )
    )

    DEFAULT_MAX_TOKENS = int(
        os.getenv(
            "DEFAULT_MAX_TOKENS",
            "4096"
        )
    )

    # =========================================================
    # Streamlit / App
    # =========================================================
    APP_TITLE = os.getenv(
        "APP_TITLE",
        "AI Multi LLM System"
    )

    DEBUG = os.getenv(
        "DEBUG",
        "False"
    ).lower() == "true"