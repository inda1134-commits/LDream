import streamlit as st


class ProgressManager:

    @staticmethod
    def update(progress_bar, status_text, value, text):
        progress_bar.progress(value)
        status_text.info(text)
