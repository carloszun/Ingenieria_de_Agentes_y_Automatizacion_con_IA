"""
Nodo router del grafo.

Clasifica la pregunta del usuario y escribe la ruta en el estado.
"""
from .state import AgentState
from .classifier import clasificar_consulta

def router(state: AgentState) -> AgentState:
    """
    Nodo que clasifica la consulta y actualiza state["route"].

    Args:
        state (AgentState): Estado actual del agente.

    Returns:
        AgentState: Estado con el campo "route" actualizado.
    """
    ruta = clasificar_consulta(state["question"], state["llm"])
    state["route"] = ruta
    return state