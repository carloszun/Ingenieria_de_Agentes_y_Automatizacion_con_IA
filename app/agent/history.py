"""
Funciones relacionadas con el historial de conversación.

Este módulo implementa la lógica necesaria para convertir una
pregunta dependiente del contexto en una pregunta completa e
independiente (History-Aware Retrieval).

El objetivo es mejorar la búsqueda de documentos en el Retriever.

Ejemplo:

Historial:
    Usuario: ¿Atienden por OSDE?
    Asistente: Sí.

Nueva pregunta:
    ¿Qué planes?

Pregunta reescrita:
    ¿Qué planes de OSDE atiende el Consultorio Odontológico DENT?
"""

from langchain_core.messages import HumanMessage

from .prompts import HISTORY_PROMPT


def reescribir_consulta(
    question: str,
    history: list,
    llm,
) -> str:
    """
    Reescribe la pregunta del usuario utilizando el historial
    de conversación.

    Parámetros
    ----------
    question : str
        Última pregunta realizada por el usuario.

    history : list
        Historial de la conversación.

    llm :
        Modelo de lenguaje utilizado para la reescritura.

    Retorna
    -------
    str
        Pregunta reescrita, lista para ser utilizada por
        el Retriever.
    """

    # ------------------------------------------------------------------
    # Convertir el historial en texto
    # ------------------------------------------------------------------

    historial = []

    for mensaje in history:

        rol = "Usuario" if mensaje["role"] == "user" else "Asistente"

        historial.append(
            f"{rol}: {mensaje['content']}"
        )

    historial = "\n".join(historial)

    # ------------------------------------------------------------------
    # Construir el prompt
    # ------------------------------------------------------------------

    prompt = HISTORY_PROMPT.format(
        history=historial,
        question=question,
    )

    # ------------------------------------------------------------------
    # Invocar el LLM
    # ------------------------------------------------------------------

    respuesta = llm.invoke([
        HumanMessage(content=prompt)
    ])
    # ------------------------------------------------------------------
    # Devolver únicamente la pregunta reescrita
    # ------------------------------------------------------------------

    return respuesta.content.strip()