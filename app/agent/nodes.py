from .graph import AgentState

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
    # Aquí iría la lógica de RAG (ya la tienes definida en nodes.py)
    documentos = state["retriever"].invoke(state["question"])
    state["context"] = "\n\n".join(doc.page_content for doc in documentos)
    state["sources"] = [f"Documento {i+1}" for i in range(len(documentos))]
    # Puedes agregar aquí la generación de respuesta con un LLM
    state["answer"] = "Respuesta generada a partir de los documentos..."
    return state