from langgraph.graph import StateGraph, END

from .graph import AgentState
from .router import router
from .nodes import nodo_saludo
from .nodes import nodo_agradecimiento
from .nodes import nodo_despedida
from .nodes import nodo_rag

workflow = StateGraph(AgentState)

workflow.add_node("router", router)
workflow.add_node("saludo", nodo_saludo)
workflow.add_node("agradecimiento", nodo_agradecimiento)
workflow.add_node("despedida", nodo_despedida)
workflow.add_node("rag", nodo_rag)

workflow.set_entry_point("router")

workflow.add_conditional_edges(
    "router",
    lambda state: state["route"],
    {
        "saludo": "saludo",
        "agradecimiento": "agradecimiento",
        "despedida": "despedida",
        "rag": "rag",
    },
)

workflow.add_edge("saludo", END)
workflow.add_edge("agradecimiento", END)
workflow.add_edge("despedida", END)
workflow.add_edge("rag", END)  

graph = workflow.compile()