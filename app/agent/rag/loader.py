"""
Módulo de carga de PDF.

Convierte un archivo PDF en una lista de documentos de LangChain,
uno por cada página, conservando metadatos (número de página y origen).
"""
from pathlib import Path
from pypdf import PdfReader
from langchain_core.documents import Document

def cargar_pdf(ruta_pdf: Path) -> list[Document]:
    """
    Carga un PDF y devuelve una lista de documentos.

    Args:
        ruta_pdf (Path): Ruta al archivo PDF.

    Returns:
        list[Document]: Lista de objetos Document, uno por página con texto y metadatos.
    """
    reader = PdfReader(ruta_pdf)
    documentos = []

    for num_pagina, pagina in enumerate(reader.pages, start=1):
        texto = pagina.extract_text() or ""
        if not texto.strip():
            continue

        documentos.append(
            Document(
                page_content=texto,
                metadata={
                    "page": num_pagina,
                    "source": Path(ruta_pdf).name,
                },
            )
        )

    return documentos