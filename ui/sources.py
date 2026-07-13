"""
Funciones auxiliares para el formateo de fuentes.

Este módulo centraliza toda la lógica relacionada con la presentación
de las referencias recuperadas por el Retriever.

Objetivos:

- Evitar código repetido.
- Mantener streamlit_app.py limpio.
- Facilitar futuras mejoras de visualización.

Actualmente genera una única línea compacta, por ejemplo:

📄 Manual Institucional DENT: págs. 2 • 3 • 4 • 7 • 8

En futuras versiones podrá mostrar:

- Links.
- Expanders.
- Tooltips.
- Número de chunks utilizados.
"""

from utils.documentos import nombre_documento


def formatear_fuentes(sources: list) -> str:
    """
    Convierte la lista de fuentes del Retriever en una única línea.

    Parámetros
    ----------
    sources : list

        Lista con elementos del tipo:

        {
            "page": 12,
            "source": ".../Manual.pdf"
        }

    Retorna
    -------
    str

        Cadena lista para mostrar con st.caption().

        Ejemplo:

        📄 Manual Institucional DENT: págs. 2 • 3 • 5 • 8
    """

    if not sources:
        return ""

    # --------------------------------------------------------------
    # Nombre del documento
    # --------------------------------------------------------------

    nombre = nombre_documento(
        sources[0]["source"]
    )

    # --------------------------------------------------------------
    # Eliminar páginas repetidas y ordenarlas
    # --------------------------------------------------------------

    paginas = sorted(
        {
            fuente["page"]
            for fuente in sources
        }
    )

    paginas_str = " • ".join(
        str(pagina)
        for pagina in paginas
    )

    return (
        f"📄 {nombre}: págs. {paginas_str}"
    )