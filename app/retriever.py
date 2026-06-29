from langchain_core.vectorstores import VectorStoreRetriever

def crear_retriever(vector_store) -> VectorStoreRetriever:
    """
    Crea un retriever a partir del vector store.
    """
    return vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3}  #Con k=3 le decimos que recupere los 3 chunks más relevantes
    )