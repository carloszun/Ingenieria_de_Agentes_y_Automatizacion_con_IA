"""
Creación del Vector Store con FAISS.

En esta versión el índice se construye utilizando todos los
archivos PDF presentes en la carpeta data/.

Esto permite ampliar la base documental sin modificar el código
del asistente.
"""

from langchain_community.vectorstores import FAISS

from app.agent.rag.loader import cargar_todos_los_pdfs
from app.agent.rag.embeddings import crear_embeddings


def inicializar_vector_store() -> FAISS:
    """
    Inicializa el Vector Store con todos los PDF
    encontrados en la carpeta data/.

    Returns
    -------
    FAISS
        Vector Store listo para realizar búsquedas semánticas.
    """

    print("📄 Cargando documentos...")

    documentos = cargar_todos_los_pdfs()

    print(f"📄 {len(documentos)} páginas cargadas.")

    print("🧠 Generando embeddings...")

    embeddings = crear_embeddings()

    print("💾 Creando Vector Store...")

    vector_store = FAISS.from_documents(
        documents=documentos,
        embedding=embeddings,
    )

    print("✅ Vector Store creado correctamente.")

    return vector_store