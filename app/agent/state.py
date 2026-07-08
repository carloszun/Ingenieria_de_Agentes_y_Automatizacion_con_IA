"""
Definición del estado del agente.
"""
from typing import Any, TypedDict, List

class AgentState(TypedDict):
    question: str
    context: str
    route: str
    answer: str
    sources: List[dict]
    retriever: Any
    llm: Any