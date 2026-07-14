"""
Definición del estado compartido del agente.

El AgentState representa toda la información que circula entre los
nodos del grafo de LangGraph.

Cada nodo puede leer y modificar este estado.

Campos
------
question
    Pregunta realizada por el usuario.

context
    Contexto recuperado por el Retriever.

route
    Ruta elegida por el Router.

answer
    Respuesta generada por el modelo.

sources
    Lista de documentos utilizados para responder.

history
    Historial completo de la conversación.

metrics
    Diccionario con métricas generadas durante la ejecución del agente.

retriever
    Retriever utilizado por el nodo RAG.

llm
    Modelo de lenguaje.
"""

from typing import Any
from typing import TypedDict
from typing import List


class AgentState(TypedDict):
    """
    Estado compartido del agente.
    """

    # ==========================================================
    # Entrada del usuario
    # ==========================================================

    question: str

    # ==========================================================
    # Contexto recuperado
    # ==========================================================

    context: str

    # ==========================================================
    # Ruta elegida por el Router
    # ==========================================================

    route: str

    # ==========================================================
    # Respuesta final
    # ==========================================================

    answer: str

    # ==========================================================
    # Fuentes utilizadas
    # ==========================================================

    sources: List[dict]

    # ==========================================================
    # Historial de conversación
    # ==========================================================

    history: List[dict]

    # ==========================================================
    # Métricas del agente
    # ==========================================================

    metrics: dict

    # ==========================================================
    # Componentes compartidos
    # ==========================================================

    retriever: Any

    llm: Any

    # ==========================================================
    # Estado visual de Streamlit
    # ==========================================================

    status: Any    