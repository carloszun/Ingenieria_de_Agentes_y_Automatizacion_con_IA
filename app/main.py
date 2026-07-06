from app.agent.builder import graph
from app.agent.graph import AgentState


def main():

    state: AgentState = {
        "question": "Hola",
        "context": "",
        "route": "",
        "answer": "",
        "sources": []
    }

    resultado = graph.invoke(state)

    print(resultado["answer"])


if __name__ == "__main__":
    main()