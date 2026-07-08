"""
Configuración del modelo de lenguaje (LLM).

Crea una instancia de ChatGoogleGenerativeAI para interactuar con Gemini.
"""
from langchain_google_genai import ChatGoogleGenerativeAI
from utils.config import CHAT_MODEL, get_google_api_key

def crear_llm() -> ChatGoogleGenerativeAI:
    """
    Crea y devuelve el modelo de chat Gemini.

    Returns:
        ChatGoogleGenerativeAI: Modelo listo para invocar.

    Parámetros:
        - temperature=0.0: Respuestas deterministas (menos creativas, más precisas).

    Nota:
        La API key se obtiene dinámicamente desde el .env en cada llamada.
        Si cambias la clave en el .env, la próxima vez que se ejecute esta
        función usará la nueva clave sin necesidad de reiniciar.
    """
    return ChatGoogleGenerativeAI(
        model=CHAT_MODEL,
        google_api_key=get_google_api_key(),  # 🔁 Clave dinámica
        temperature=0.0,
    )