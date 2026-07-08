"""
Punto de entrada principal del asistente DENT.

Inicializa el vector store, el retriever, el LLM y el grafo,
luego ejecuta un loop interactivo para consultar al asistente.
"""
import sys
from app.vector_store import inicializar_vector_store
from app.retriever import crear_retriever
from app.llm import crear_llm
from app.agent.builder import graph
from app.agent.state import AgentState
from utils.documentos import nombre_documento

def main():
    """
    Función principal que inicia el asistente y maneja la interacción con el usuario.
    """
    print("\n🦷 Inicializando asistente DENT...")

    # 1. Inicializar componentes
    try:
        vector_store = inicializar_vector_store()
    except Exception as e:
        print(f"❌ Error al inicializar el vector store: {e}")
        sys.exit(1)

    retriever = crear_retriever(vector_store)
    llm = crear_llm()

    print("✅ Asistente listo. Escribe tu consulta o 'salir' para terminar.\n")

    # 2. Loop interactivo
    while True:
        pregunta = input("\n👤 Consulta: ").strip()
        if not pregunta:
            continue
        if pregunta.lower() in ("salir", "exit", "quit"):
            break

        # 3. Construir el estado inicial
        state: AgentState = {
            "question": pregunta,
            "context": "",
            "route": "",
            "answer": "",
            "sources": [],
            "retriever": retriever,
            "llm": llm,
        }

        # 4. Ejecutar el grafo
        try:
            resultado = graph.invoke(state)
        except Exception as e:
            print(f"\n❌ Error al ejecutar el grafo: {e}")
            continue

        # 5. Mostrar respuesta
        print("\n🦷 DENT:")
        print(resultado["answer"])

        # 6. Mostrar fuentes (solo si hay y no es el mensaje de "no encontré")
        if resultado["sources"] and "No encontré esa información" not in resultado["answer"]:
            print("\n📄 Fuentes:")
            for fuente in resultado["sources"]:
                nombre = nombre_documento(fuente.get("source", "Desconocido"))
                pagina = fuente.get("page", "N/A")
                print(f"• {nombre} (pág. {pagina})")

        # 7. Preguntar si desea continuar
        continuar = input("\n¿Desea realizar otra consulta? (S/N): ").strip().lower()
        if continuar not in ("s", "si", "sí"):
            break

    print("\n🦷 DENT:\nGracias por utilizar el asistente virtual del Consultorio Odontológico DENT.\n¡Que tenga un excelente día!")

if __name__ == "__main__":
    main()