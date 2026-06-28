from .loader import leer_pdf, cantidad_paginas
from .splitter import dividir_texto
from utils.config import RUTA_PDF, CHUNK_SIZE, CHUNK_OVERLAP

def main():

    paginas = leer_pdf(RUTA_PDF)

    texto = "\n".join(paginas)

    chunks = dividir_texto(texto)

    print(f"Cantidad de chunks: {len(chunks)}")

    print()

    print("Primer chunk:")

    print("-" * 50)

    print(chunks[0])

if __name__ == "__main__":
    main()