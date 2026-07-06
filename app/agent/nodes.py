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