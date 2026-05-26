import tiktoken


class TokenManager:

    @staticmethod
    def count_tokens(text: str, model: str = "gpt-5"):
        try:
            encoding = tiktoken.encoding_for_model(model)
        except Exception:
            encoding = tiktoken.get_encoding("cl100k_base")

        return len(encoding.encode(text))
