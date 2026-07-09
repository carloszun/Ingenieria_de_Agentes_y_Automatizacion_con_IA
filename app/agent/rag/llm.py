"""
Configuración del modelo de lenguaje (LLM).

Soporta múltiples proveedores: Gemini (Google) o DeepSeek.
Por defecto usa DeepSeek por su bajo costo y estabilidad.
"""
from langchain_openai import ChatOpenAI
from utils.config import DEEPSEEK_API_KEY, DEEPSEEK_CHAT_MODEL, DEEPSEEK_API_BASE

# =============================================================================
# DEEPSEEK (ACTIVO)
# =============================================================================
def crear_llm() -> ChatOpenAI:
    """
    Crea y devuelve el modelo de chat DeepSeek (compatible con OpenAI).

    Returns:
        ChatOpenAI: Modelo listo para invocar.

    Parámetros:
        - temperature=0.0: Respuestas deterministas (menos creativas, más precisas).
        - base_url: URL de la API de DeepSeek (compatible con OpenAI).
    """
    return ChatOpenAI(
        model=DEEPSEEK_CHAT_MODEL,
        api_key=DEEPSEEK_API_KEY,
        base_url=DEEPSEEK_API_BASE,
        temperature=0.0,
    )


# =============================================================================
# GEMINI (COMENTADO - PARA REFERENCIA FUTURA)
# =============================================================================
# from langchain_google_genai import ChatGoogleGenerativeAI
# from utils.config import CHAT_MODEL_GEMINI, GOOGLE_API_KEY
#
# def crear_llm() -> ChatGoogleGenerativeAI:
#     return ChatGoogleGenerativeAI(
#         model=CHAT_MODEL_GEMINI,
#         google_api_key=GOOGLE_API_KEY,
#         temperature=0.0,
#     )