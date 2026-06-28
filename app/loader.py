from pypdf import PdfReader

def leer_pdf(ruta_pdf):
    """
    Lee un archivo PDF y devuelve una lista con el texto de cada página.
    """

    reader = PdfReader(ruta_pdf)

    paginas = []

    for pagina in reader.pages:
        texto = pagina.extract_text()

        # Si una página no tiene texto, guardar una cadena vacía
        if texto is None:
            texto = ""

        paginas.append(texto)

    return paginas


def cantidad_paginas(ruta_pdf):
    """
    Devuelve la cantidad de páginas del PDF.
    """

    reader = PdfReader(ruta_pdf)

    return len(reader.pages)