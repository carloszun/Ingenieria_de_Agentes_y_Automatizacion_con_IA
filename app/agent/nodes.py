"""
Nodos del grafo de LangGraph.

Cada función es un nodo que recibe el estado, lo procesa y devuelve el estado modificado.
"""
from langchain_core.messages import SystemMessage, HumanMessage
from .state import AgentState
from .prompts import SYSTEM_PROMPT, RAG_PROMPT


def nodo_saludo(state: AgentState) -> AgentState:
    """Responde cuando el usuario saluda."""
    state["answer"] = (
        "¡Hola! Soy el asistente virtual del Consultorio Odontológico DENT.\n\n"
        "Estoy preparado para responder consultas sobre turnos, convenios, "
        "políticas e información contenida en la documentación del consultorio.\n\n"
        "¿En qué puedo ayudarte?"
    )
    return state


def nodo_agradecimiento(state: AgentState) -> AgentState:
    """Responde cuando el usuario agradece."""
    state["answer"] = "¡De nada! Quedo a tu disposición para cualquier otra consulta."
    return state


def nodo_despedida(state: AgentState) -> AgentState:
    """Responde cuando el usuario se despide."""
    state["answer"] = "¡Hasta luego! Que tengas un buen día."
    return state


def nodo_fuera_dominio(state: AgentState) -> AgentState:
    """Responde cuando la consulta está fuera del dominio odontológico."""
    state["answer"] = (
        "Soy el asistente virtual del Consultorio Odontológico DENT.\n\n"
        "Puedo responder únicamente consultas relacionadas con turnos, horarios, "
        "convenios, políticas y demás información contenida en la documentación del consultorio.\n\n"
        "Si tenés alguna consulta sobre DENT, estaré encantado de ayudarte."
    )
    return state


def nodo_rag(state: AgentState) -> AgentState:
    """
    Nodo RAG: recupera documentos, genera contexto y respuesta.

    Flujo:
        1. Recupera documentos relevantes usando el retriever.
        2. Si no hay documentos, responde con mensaje predefinido.
        3. Construye el contexto concatenando el texto de los documentos.
        4. Guarda las fuentes (página y documento).
        5. Invoca el LLM con SYSTEM_PROMPT y RAG_PROMPT.
        6. Guarda la respuesta en el estado.
    """
    # 1. Recuperar documentos
    documentos = state["retriever"].invoke(state["question"])

    # 2. Si no hay documentos, respuesta predefinida
    if not documentos:
        state["answer"] = "No encontré esa información en la documentación del consultorio DENT."
        state["context"] = ""
        state["sources"] = []
        return state

    # 3. Construir el contexto
    contexto = "\n\n".join(doc.page_content for doc in documentos)
    state["context"] = contexto

    # 4. Guardar fuentes sin duplicados
    sources = []
    for doc in documentos:
        fuente = {
            "page": doc.metadata.get("page"),
            "source": doc.metadata.get("source"),
        }
        if fuente not in sources:
            sources.append(fuente)
    state["sources"] = sorted(sources, key=lambda f: f["page"])

    # 5. Armar mensajes para el LLM
    user_message = RAG_PROMPT.format(
        context=contexto,
        question=state["question"]
    )
    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=user_message),
    ]

    # 6. Invocar al LLM y guardar respuesta
    respuesta = state["llm"].invoke(messages)
    state["answer"] = respuesta.content

    return state