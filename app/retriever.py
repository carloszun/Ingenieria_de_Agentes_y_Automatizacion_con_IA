"""
Configuración del retriever con MMR.
"""
from langchain_core.vectorstores import VectorStoreRetriever
from langchain_community.vectorstores import FAISS

def crear_retriever(vector_store: FAISS) -> VectorStoreRetriever:
    """
    Crea un retriever con estrategia MMR (Maximum Marginal Relevance).
    """
    return vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 20,
            "fetch_k": 40,
            "lambda_mult": 0.7,
        }
    )