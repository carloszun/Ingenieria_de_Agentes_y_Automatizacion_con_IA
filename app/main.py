from app.loader import leer_pdf
from app.splitter import dividir_texto
from app.embeddings import crear_embeddings

from utils.config import RUTA_PDF


def main():

    paginas = leer_pdf(RUTA_PDF)

    texto = "\n".join(paginas)

    chunks = dividir_texto(texto)

    print(f"Cantidad de chunks: {len(chunks)}")

    print()

    print("Primer chunk")

    print("-" * 50)

    print(chunks[0])

    print()

    embeddings = crear_embeddings()

    vector = embeddings.embed_query(
        "¿Cuál es la política de cancelación de turnos?"
    )

    print(f"Dimensión del vector: {len(vector)}")
    print(vector[:10])


if __name__ == "__main__":
    main()