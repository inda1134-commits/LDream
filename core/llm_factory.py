from openai import OpenAI

import anthropic

from google import genai

from config.settings import Settings


class LLMFactory:

    @staticmethod
    def get_client(provider: str):

        if provider == "openai":

            return OpenAI(
                api_key=Settings.OPENAI_API_KEY
            )

        elif provider == "anthropic":

            return anthropic.Anthropic(
                api_key=Settings.ANTHROPIC_API_KEY
            )

        elif provider == "google":

            return genai.Client(
                api_key=Settings.GOOGLE_API_KEY
            )

        else:

            raise ValueError(
                f"지원하지 않는 provider: {provider}"
            )