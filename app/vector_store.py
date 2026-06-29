from langchain_community.vectorstores import FAISS

from app.embeddings import crear_embeddings


def crear_vector_store(chunks):
    """
    Crea una base vectorial FAISS a partir de los chunks.
    """

    embeddings = crear_embeddings()

    vector_store = FAISS.from_texts(
        texts=chunks,
        embedding=embeddings
    )

    return vector_store