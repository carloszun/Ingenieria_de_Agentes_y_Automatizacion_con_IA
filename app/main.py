from app.loader import leer_pdf
from app.splitter import dividir_texto
from app.vector_store import crear_vector_store
from utils.config import RUTA_PDF


def main():

    paginas = leer_pdf(RUTA_PDF)

    texto = "\n".join(paginas)

    chunks = dividir_texto(texto)

    print(f"Cantidad de chunks: {len(chunks)}")

    vector_store = crear_vector_store(chunks)

    print("✅ Vector Store creado correctamente.")


if __name__ == "__main__":
    main()