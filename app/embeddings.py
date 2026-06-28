from langchain_google_genai import GoogleGenerativeAIEmbeddings

from utils.config import (
    GOOGLE_API_KEY,
    EMBEDDING_MODEL
)


def crear_embeddings():

    embeddings = GoogleGenerativeAIEmbeddings(
        model=EMBEDDING_MODEL,
        google_api_key=GOOGLE_API_KEY
    )

    return embeddings