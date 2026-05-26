from services.prompt_service import PromptService
from core.llm_factory import LLMFactory
from core.token_manager import TokenManager
from core.logger import logger


class DreamService:

    @staticmethod
    def analyze(
        provider: str,
        model: str,
        dream_text: str
    ):

        client = LLMFactory.get_client(provider)

        prompt = PromptService.load_prompt(
            "dream_prompt.txt"
        )

        full_prompt = f"""
{prompt}

[사용자 꿈]
{dream_text}
"""

        logger.info("꿈 해몽 분석 시작")

        # =====================================================
        # OpenAI
        # =====================================================

        if provider == "openai":

            response = (
                client.chat.completions.create(
                    model=model,
                    messages=[
                        {
                            "role": "user",
                            "content": full_prompt
                        }
                    ]
                )
            )

            text = (
                response
                .choices[0]
                .message
                .content
            )

        # =====================================================
        # Anthropic
        # =====================================================

        elif provider == "anthropic":

            response = client.messages.create(
                model=model,
                max_tokens=1500,
                messages=[
                    {
                        "role": "user",
                        "content": full_prompt
                    }
                ]
            )

            text = response.content[0].text

        # =====================================================
        # Google
        # =====================================================

        elif provider == "google":

            response = client.models.generate_content(
                model=model,
                contents=full_prompt
            )

            text = response.text

        else:

            raise ValueError(
                "지원하지 않는 LLM 제공자"
            )

        token_count = (
            TokenManager.count_tokens(
                full_prompt + text
            )
        )

        logger.info(
            f"꿈 해몽 토큰 사용량: {token_count}"
        )

        return text