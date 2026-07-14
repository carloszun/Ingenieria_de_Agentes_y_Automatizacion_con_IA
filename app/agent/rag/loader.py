"""
Módulo de carga de documentos PDF.

Convierte uno o varios archivos PDF en una lista de documentos
de LangChain, conservando el número de página y el nombre del
archivo de origen.

Este módulo ofrece dos funciones:

- cargar_pdf():
    Carga un único PDF.

- cargar_todos_los_pdfs():
    Carga todos los PDF presentes en la carpeta data/.
"""

from pathlib import Path

from pypdf import PdfReader

from langchain_core.documents import Document


# =============================================================================
# CARGA DE UN ÚNICO PDF
# =============================================================================

def cargar_pdf(ruta_pdf: Path) -> list[Document]:
    """
    Carga un único archivo PDF.

    Parameters
    ----------
    ruta_pdf : Path
        Ruta al archivo PDF.

    Returns
    -------
    list[Document]
        Un Document por cada página del PDF.
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

                    "source": ruta_pdf.name,

                },

            )

        )

    return documentos


# =============================================================================
# CARGA DE TODOS LOS PDF
# =============================================================================

def cargar_todos_los_pdfs(
    carpeta: Path = Path("data"),
) -> list[Document]:
    """
    Carga todos los PDF presentes en una carpeta.

    Parameters
    ----------
    carpeta : Path
        Carpeta donde se encuentran los PDF.

    Returns
    -------
    list[Document]
        Lista unificada con todos los documentos.
    """

    documentos = []

    pdfs = sorted(
        carpeta.glob("*.pdf")
    )

    if not pdfs:

        raise FileNotFoundError(
            f"No se encontraron archivos PDF en {carpeta}"
        )

    for pdf in pdfs:

        print(f"📄 Cargando {pdf.name}")

        documentos.extend(
            cargar_pdf(pdf)
        )

    return documentos