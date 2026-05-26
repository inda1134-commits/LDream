import streamlit as st
from config.constants import ZODIAC_ANIMALS


def zodiac_display(selected_key):
    cols = st.columns(12)
    for idx, (key, emoji) in enumerate(ZODIAC_ANIMALS.items()):
        with cols[idx]:
            if st.button(f"{emoji}\n{key}", key=f"zodiac_{key}"):
                return key
    return selected_key
