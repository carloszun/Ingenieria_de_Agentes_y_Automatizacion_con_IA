from .graph import AgentState

def router(state: AgentState) -> AgentState:

    pregunta = state["question"].lower()

    SALUDOS = [
        "hola",
        "buen día",
        "buenos días",
        "buenas tardes",
        "buenas noches",
    ]

    AGRADECIMIENTOS = [
    ]

    DESPEDIDAS = [
    ]

    if any(saludo in pregunta for saludo in SALUDOS):
        state["route"] = "saludo"

    elif any(gracias in pregunta for gracias in AGRADECIMIENTOS):
        state["route"] = "agradecimiento"

    elif any(despedida in pregunta for despedida in DESPEDIDAS):
        state["route"] = "despedida"

    else:
        state["route"] = "rag"

    return state