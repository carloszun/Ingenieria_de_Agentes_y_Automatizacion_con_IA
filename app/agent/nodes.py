from langchain_core.messages import SystemMessage, HumanMessage
from .graph import AgentState
from .prompts import SYSTEM_PROMPT, RAG_PROMPT


def nodo_saludo(state: AgentState) -> AgentState:
    """
    Responde cuando el usuario solamente saluda.
    """
    state["answer"] = (
        "¡Hola! Soy el asistente virtual del Consultorio Odontológico DENT.\n\n"
        "Estoy preparado para responder consultas sobre "
        "turnos, convenios, políticas e información "
        "contenida en la documentación del consultorio.\n\n"
        "¿En qué puedo ayudarte?"
    )
    return state


def nodo_agradecimiento(state: AgentState) -> AgentState:
    state["answer"] = "¡De nada! Quedo a tu disposición para cualquier otra consulta."
    return state


def nodo_despedida(state: AgentState) -> AgentState:
    state["answer"] = "¡Hasta luego! Que tengas un buen día."
    return state


def nodo_rag(state: AgentState) -> AgentState:
    """
    Nodo de Retrieval-Augmented Generation (RAG).
    Recupera documentos relevantes, construye el contexto y genera
    una respuesta usando el LLM con el SYSTEM_PROMPT y RAG_PROMPT.
    """
    # 1. Recuperar documentos
    documentos = state["retriever"].invoke(state["question"])

    # 2. Construir el contexto
    contexto = "\n\n".join(doc.page_content for doc in documentos)
    state["context"] = contexto

    # 3. Guardar fuentes (metadatos)
    state["sources"] = [doc.metadata for doc in documentos]

    # 4. Formatear el mensaje del usuario con el contexto y la pregunta
    user_message = RAG_PROMPT.format(
        context=contexto,
        question=state["question"]
    )

    # 5. Construir la lista de mensajes para LangChain
    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=user_message)
    ]

    # 6. Invocar al LLM (debe ser un modelo de chat de LangChain)
    respuesta = state["llm"].invoke(messages)

    # 7. Guardar la respuesta
    state["answer"] = respuesta.content

    return state