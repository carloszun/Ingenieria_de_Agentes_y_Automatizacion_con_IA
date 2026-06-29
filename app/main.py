from app.vector_store import inicializar_vector_store
from app.retriever import crear_retriever

def main():
    vector_store = inicializar_vector_store()
    retriever = crear_retriever(vector_store)
    
    pregunta = "¿Cómo puedo cancelar un turno?"

    documentos = retriever.invoke(pregunta)

    print(f"\nSe encontraron {len(documentos)} documentos.\n")

    for i, doc in enumerate(documentos, start=1):
        print("=" * 70)
        print(f"DOCUMENTO {i}")
        print("=" * 70)
        print(doc.page_content)

if __name__ == "__main__":
    main()