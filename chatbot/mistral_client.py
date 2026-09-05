import os
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv
from mistralai.client import Mistral

load_dotenv(
    dotenv_path=Path(__file__).resolve().parents[1] / ".env"
)

def ask_mistral(messages):
    api_key = os.getenv("MISTRAL_API_KEY", "")
    if not api_key:
        try:
            api_key = st.secrets.get("MISTRAL_API_KEY", "")
        except Exception:
            api_key = ""

    if not api_key:
        return "Mistral AI is not configured. Add MISTRAL_API_KEY to Streamlit Secrets."

    client = Mistral(api_key=api_key)

    try:
        response = client.chat.complete(
            model="open-mixtral-8x7b",
            messages=messages
        )
    except Exception as error:
        return (
            "The AI assistant request failed: "
            f"{type(error).__name__}: {error}"
        )

    return response.choices[0].message.content
