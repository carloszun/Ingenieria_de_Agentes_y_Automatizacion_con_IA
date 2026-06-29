from app.loader import leer_pdf
from app.splitter import dividir_texto
from app.embeddings import crear_embeddings
from langchain_community.vectorstores import FAISS
from utils.config import RUTA_PDF

def inicializar_vector_store():
    paginas = leer_pdf(RUTA_PDF)
    texto = "\n".join(paginas)
    chunks = dividir_texto(texto)
    embeddings = crear_embeddings()
    vector_store = FAISS.from_texts(
        texts=chunks,
        embedding=embeddings
    )

    return vector_store