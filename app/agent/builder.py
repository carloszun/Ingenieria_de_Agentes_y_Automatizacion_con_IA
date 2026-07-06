from langgraph.graph import StateGraph, END

from .graph import AgentState
from .router import router
from .nodes import nodo_saludo

workflow = StateGraph(AgentState)

workflow.add_node("router", router)
workflow.add_node("saludo", nodo_saludo)

workflow.set_entry_point("router")

workflow.add_conditional_edges(
    "router",
    lambda state: state["route"],
    {
        "saludo": "saludo",
    },
)

workflow.add_edge("saludo", END)

graph = workflow.compile()