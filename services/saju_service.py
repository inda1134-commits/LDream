from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI

from config.settings import Settings


class SajuService:

    def __init__(self):
        pass

    def _get_llm(
        self,
        provider: str,
        model: str
    ):

        if provider == "openai":

            return ChatOpenAI(
                api_key=Settings.OPENAI_API_KEY,
                model=model,
                temperature=0.85,
            )

        elif provider == "anthropic":

            return ChatAnthropic(
                api_key=Settings.ANTHROPIC_API_KEY,
                model=model,
                temperature=0.85,
            )

        elif provider == "google":

            return ChatGoogleGenerativeAI(
                google_api_key=Settings.GOOGLE_API_KEY,
                model=model,
                temperature=0.85,
            )

        else:
            raise ValueError("지원하지 않는 provider 입니다.")

    def analyze_saju(
        self,
        provider,
        model,
        birth_date,
        birth_time,
        gender,
        analysis_year,
    ):

        llm = self._get_llm(
            provider=provider,
            model=model
        )

        prompt = f"""
당신은 사주와 운세를
일반인도 쉽게 이해할 수 있도록 설명하는
친절한 상담형 해설 전문가입니다.

절대 어려운 역술 용어를 남용하지 마세요.

==================================================
[사용자 정보]

- 출생일: {birth_date}
- 출생시간: {birth_time if birth_time else "모름"}
- 성별: {gender if gender else "미입력"}
- 분석년도: {analysis_year}

==================================================

다음 형식으로 자세히 설명하세요. (반드시 근거 기재)

# 🌙 타고난 성향

- 성격 특징
- 장점
- 감정 흐름
- 인간관계 특징

--------------------------------------------------

# ✨ 현재 운의 흐름

- 최근 운세 흐름
- 금전운
- 인간관계운
- 일/학업운
- 조심할 점

--------------------------------------------------

# 🍀 행운 포인트

- 추천 행동
- 좋은 습관
- 도움이 되는 방향

--------------------------------------------------

# 🎯 추천 행운 숫자

1~45 사이 숫자 6개 추천

왜 이런 숫자가 나왔는지 설명하세요.

==================================================

규칙:

- 친절하고 따뜻한 말투 사용
- 너무 짧게 작성 금지
- 실제 상담 느낌으로 작성
- 어려운 한자 용어 금지
"""

        response = llm.invoke(prompt)

        return response.content