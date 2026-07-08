"""
Configuración del modelo de embeddings.

Utiliza GoogleGenerativeAIEmbeddings para convertir texto en vectores
que serán indexados en FAISS.
"""
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from utils.config import EMBEDDING_MODEL, get_google_api_key

def crear_embeddings() -> GoogleGenerativeAIEmbeddings:
    """
    Crea y devuelve una instancia del modelo de embeddings.

    Returns:
        GoogleGenerativeAIEmbeddings: Modelo listo para generar embeddings.

    Nota:
        La API key se obtiene dinámicamente desde el .env en cada llamada.
        Si cambias la clave en el .env, la próxima vez que se ejecute esta
        función usará la nueva clave sin necesidad de reiniciar.
    """
    return GoogleGenerativeAIEmbeddings(
        model=EMBEDDING_MODEL,
        google_api_key=get_google_api_key(),  # 🔁 Clave dinámica
    )