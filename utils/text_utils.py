import re

def clean_text(text: str) -> str:
    # 불필요한 공백 및 특수문자 제거
    text = re.sub(r"\s+", " ", text)
    text = text.strip()
    return text
