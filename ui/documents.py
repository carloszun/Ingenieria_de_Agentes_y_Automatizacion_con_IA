"""
Documentos cargados.

Este módulo muestra los archivos PDF que actualmente forman
la base documental utilizada por el asistente.

Permite:

- Visualizar los documentos disponibles.
- Agregar nuevos PDF.

Al agregar un nuevo documento se limpia el caché de recursos
para que el índice FAISS sea reconstruido automáticamente
en la siguiente ejecución de la aplicación.
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

        identificador = (
            uploaded_file.name,
            uploaded_file.size,
        )

        if (
            st.session_state.get("ultimo_pdf_subido")
            != identificador
        ):

            DATA_DIR.mkdir(exist_ok=True)

            destino = DATA_DIR / uploaded_file.name

            with open(destino, "wb") as f:

                shutil.copyfileobj(
                    uploaded_file,
                    f,
                )

            st.session_state.ultimo_pdf_subido = identificador

            st.success(
                f"'{uploaded_file.name}' agregado correctamente."
            )

            # ==================================================
            # Limpiar el caché de recursos para reconstruir
            # automáticamente el índice FAISS.
            # ==================================================

            st.cache_resource.clear()
            st.rerun()

    # ==========================================================
    # Mostrar documentos disponibles
    # ==========================================================

    pdfs = sorted(DATA_DIR.glob("*.pdf"))

    if not pdfs:

        st.warning(
            "No hay documentos cargados."
        )

        return

    st.caption(
        f"📚 {len(pdfs)} documento(s) disponible(s)"
    )

    from pypdf import PdfReader

    for pdf in pdfs:

        col1, col2 = st.columns([8, 1])

        with col1:

            try:
                paginas = len(PdfReader(pdf).pages)
            except Exception:
                paginas = "?"

            st.write(
                f"📄 **{pdf.name}**  \n"
                f"<small>{paginas} página(s)</small>",
                unsafe_allow_html=True,
            )

        with col2:

            if st.button(
                "🗑",
                key=f"delete_{pdf.name}",
                help="Eliminar documento",
            ):

                pdf.unlink()

                st.cache_resource.clear()

                st.rerun()


