from pathlib import Path


class PromptService:

    BASE_PATH = Path("prompts")

    @classmethod
    def load_prompt(cls, filename: str):
        path = cls.BASE_PATH / filename
        return path.read_text(encoding="utf-8")
