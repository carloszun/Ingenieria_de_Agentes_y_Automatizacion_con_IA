"""
Factory del AgentState.

Este módulo concentra la creación del estado inicial utilizado por
LangGraph.

Objetivos
---------

- Evitar código duplicado.
- Centralizar la construcción del estado.
- Facilitar futuras ampliaciones del AgentState.
- Mantener streamlit_app.py limpio.

Si en el futuro el estado incorpora nuevos campos
(user_id, session_id, debug, métricas, etc.)
solamente será necesario modificar este archivo.
"""

from .state import AgentState


def crear_estado(
    question: str,
    history: list,
    retriever,
    llm,
    status,
) -> AgentState:
    """
    Crea el estado inicial del agente.

    Parámetros
    ----------
    question : str
        Pregunta realizada por el usuario.

    history : list
        Historial completo de conversación.

    retriever
        Retriever utilizado por el nodo RAG.

    llm
        Modelo de lenguaje.

    Returns
    -------
    AgentState
        Estado listo para ser enviado al grafo.
    """

    return {

        "question": question,

        "context": "",

        "route": "",

        "answer": "",

        "sources": [],

                

        # ----------------------------------------------------------
        # Se pasa una copia del historial para evitar modificaciones
        # accidentales durante la ejecución del grafo.
        # ----------------------------------------------------------

        "history": history.copy(),

        "retriever": retriever,

        "llm": llm,

        "status": status,

        "metrics": {},

    }