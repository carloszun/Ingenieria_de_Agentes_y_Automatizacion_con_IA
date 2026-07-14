"""
Documentos cargados.

Este módulo muestra los archivos PDF que actualmente forman
la base documental utilizada por el asistente.

En esta primera versión permite:

- Visualizar los documentos disponibles.
- Agregar nuevos PDF.

En futuras versiones permitirá:

- Eliminar documentos.
- Reconstruir el índice FAISS.
"""

from pathlib import Path
import shutil

import streamlit as st


DATA_DIR = Path("data")


def mostrar_documentos():
    """
    Muestra los documentos utilizados por el asistente
    y permite agregar nuevos archivos PDF.
    """

    st.subheader("📄 Base documental")

    # ==========================================================
    # Subir nuevo documento
    # ==========================================================

    uploaded_file = st.file_uploader(
        "Agregar documento",
        type=["pdf"],
    )

    if uploaded_file is not None:

        DATA_DIR.mkdir(exist_ok=True)

        destino = DATA_DIR / uploaded_file.name

        with open(destino, "wb") as f:

            shutil.copyfileobj(
                uploaded_file,
                f,
            )

        st.success(
            f"'{uploaded_file.name}' agregado correctamente."
        )

        st.rerun()

    # ==========================================================
    # Mostrar documentos disponibles
    # ==========================================================

    pdfs = sorted(
        DATA_DIR.glob("*.pdf")
    )

    if not pdfs:

        st.warning(
            "No hay documentos cargados."
        )

        return

    st.caption(
        "Documentos utilizados por el asistente"
    )

    for pdf in pdfs:

        st.write(
            f"📄 {pdf.name}"
        )