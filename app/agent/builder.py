"""
Construcción del grafo de LangGraph.

Define el flujo de ejecución: router → (saludo/agradecimiento/despedida/rag/fuera_dominio) → END.
"""
from langgraph.graph import StateGraph, END
from .state import AgentState
from .router import router
from .nodes import (
    nodo_saludo,
    nodo_agradecimiento,
    nodo_despedida,
    nodo_rag,
    nodo_fuera_dominio,
)

# 1. Crear el grafo con el estado tipado
workflow = StateGraph(AgentState)

# 2. Registrar todos los nodos
workflow.add_node("router", router)
workflow.add_node("saludo", nodo_saludo)
workflow.add_node("agradecimiento", nodo_agradecimiento)
workflow.add_node("despedida", nodo_despedida)
workflow.add_node("rag", nodo_rag)
workflow.add_node("fuera_dominio", nodo_fuera_dominio)

# 3. Punto de entrada: el router clasifica la consulta
workflow.set_entry_point("router")

# 4. Arista condicional desde router
#    El router devuelve una categoría (ej. "rag") y el grafo salta a ese nodo.
workflow.add_conditional_edges(
    "router",
    lambda state: state["route"],
    {
        "saludo": "saludo",
        "agradecimiento": "agradecimiento",
        "despedida": "despedida",
        "rag": "rag",
        "fuera_dominio": "fuera_dominio",
    },
)

# 5. Todos los nodos terminan en END (fin del flujo)
workflow.add_edge("saludo", END)
workflow.add_edge("agradecimiento", END)
workflow.add_edge("despedida", END)
workflow.add_edge("rag", END)
workflow.add_edge("fuera_dominio", END)

# 6. Compilar el grafo (lo convierte en una función invocable)
graph = workflow.compile()