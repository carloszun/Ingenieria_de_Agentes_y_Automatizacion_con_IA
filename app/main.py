from app.vector_store import inicializar_vector_store
from app.retriever import crear_retriever
from app.agent.builder import graph
from app.agent.graph import AgentState
from app.llm import crear_llm

def main():

    vector_store = inicializar_vector_store()
    retriever = crear_retriever(vector_store)
    llm = crear_llm()

    while True:

        pregunta = input("\nConsulta: ")

        if pregunta.lower() == "salir":
            break

        state: AgentState = {
            "question": pregunta,
            "context": "",
            "route": "",
            "answer": "",
            "sources": [],
            "retriever": retriever,
            "llm": llm,
        }

        resultado = graph.invoke(state)

        print("\nDENT:")
        print(resultado["answer"])


if __name__ == "__main__":
    main()