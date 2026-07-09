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
    """
    return GoogleGenerativeAIEmbeddings(
        model=EMBEDDING_MODEL,
        google_api_key=get_google_api_key(),
    )