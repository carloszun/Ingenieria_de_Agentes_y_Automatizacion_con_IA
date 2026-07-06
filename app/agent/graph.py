from typing import Any, TypedDict

class AgentState(TypedDict):
    question: str
    context: str
    route: str
    answer: str
    sources: list[str]
    retriever: Any