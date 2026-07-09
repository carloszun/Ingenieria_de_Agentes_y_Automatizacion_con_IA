# app/splitter.py
from langchain_text_splitters import RecursiveCharacterTextSplitter
from utils.config import CHUNK_SIZE, CHUNK_OVERLAP

def dividir_texto(documentos):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=["\n\n", "\n", ". ", " ", ""]
    )
    chunks = splitter.split_documents(documentos)
    
    # Modificar cada chunk para incluir la página de origen
    for chunk in chunks:
        # Extraer el número de página de los metadatos
        page = chunk.metadata.get("page", "desconocida")
        # Agregar el número de página al inicio del texto
        chunk.page_content = f"[Página {page}]\n{chunk.page_content}"
    
    return chunks