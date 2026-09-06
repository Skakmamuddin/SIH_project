import os
from pathlib import Path
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

load_dotenv(
    dotenv_path=Path(__file__).resolve().parents[1] / ".env"
)

def ask_mistral(messages):
    
    api_key = os.getenv("GROQ_API_KEY", "")
    if not api_key:
        try:
            api_key = st.secrets.get("GROQ_API_KEY", "")
        except Exception:
            api_key = ""

    if not api_key:
        return "Groq AI is not configured. Add GROQ_API_KEY to Streamlit Secrets."

    client = Groq(api_key=api_key)

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages
        )
    except Exception as error:
        return (
            "The AI assistant request failed: "
            f"{type(error).__name__}: {error}"
        )

    return response.choices[0].message.content
