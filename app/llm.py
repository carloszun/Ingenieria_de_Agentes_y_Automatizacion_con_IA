from langchain_google_genai import ChatGoogleGenerativeAI

from utils.config import (
    GEMINI_API_KEY,
    CHAT_MODEL,
)


def crear_llm():
    """
    Crea y devuelve una instancia del modelo Gemini.
    """

    llm = ChatGoogleGenerativeAI(
        model=CHAT_MODEL,
        google_api_key=GEMINI_API_KEY,
        temperature=0,
    )

    return llm