"""
Creación del vector store con FAISS.
"""
from langchain_community.vectorstores import FAISS
from app.loader import cargar_pdf
from app.embeddings import crear_embeddings
from utils.config import RUTA_PDF

def inicializar_vector_store() -> FAISS:
    """
    Inicializa el vector store con el contenido del PDF institucional.
    """
    print("📄 Cargando PDF...")
    documentos = cargar_pdf(RUTA_PDF)
    print(f"📄 {len(documentos)} páginas cargadas.")

    print("🧠 Generando embeddings...")
    embeddings = crear_embeddings()

    print("💾 Creando vector store...")
    vector_store = FAISS.from_documents(
        documents=documentos,
        embedding=embeddings,
    )
    print("✅ Vector store creado correctamente.")
    return vector_store