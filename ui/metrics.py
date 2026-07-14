"""
Métricas de la interfaz.

Este módulo centraliza el cálculo de estadísticas relacionadas con la
conversación del usuario.

Su objetivo es mantener toda la lógica de métricas fuera de la interfaz
(Streamlit), facilitando el mantenimiento y futuras ampliaciones.

Actualmente calcula:

- Cantidad total de mensajes.
- Cantidad de consultas realizadas.
- Cantidad de respuestas generadas.
- Cantidad total de fuentes consultadas.
- Tiempo de la última respuesta.

En futuras versiones podrá incorporar:

- Tiempo promedio de respuesta.
- Tiempo máximo y mínimo.
- Cantidad de tokens consumidos.
- Costo estimado.
- Cantidad de conversaciones.
"""

from typing import List


def calcular_metricas(
    messages: List[dict],
    tiempo: float = 0.0,
) -> dict:
    """
    Calcula las métricas generales de la conversación.

    Parameters
    ----------
    messages : List[dict]
        Historial completo de la conversación almacenado en
        st.session_state.messages.

    tiempo : float, optional
        Tiempo empleado en generar la última respuesta,
        expresado en segundos.

    Returns
    -------
    dict
        Diccionario con todas las métricas de la conversación.
    """

    # ------------------------------------------------------------------
    # Cantidad de consultas realizadas por el usuario
    # ------------------------------------------------------------------

    preguntas = sum(
        1
        for mensaje in messages
        if mensaje["role"] == "user"
    )

    # ------------------------------------------------------------------
    # Cantidad de respuestas generadas por el asistente
    # ------------------------------------------------------------------

    respuestas = sum(
        1
        for mensaje in messages
        if mensaje["role"] == "assistant"
    )

    # ------------------------------------------------------------------
    # Cantidad total de fuentes consultadas
    #
    # Cada respuesta puede contener una lista de fuentes en el campo
    # "sources". Se contabilizan todas las fuentes utilizadas durante
    # la conversación.
    # ------------------------------------------------------------------

    fuentes = 0

    for mensaje in messages:

        if mensaje["role"] != "assistant":
            continue

        if "sources" not in mensaje:
            continue

        if not mensaje["sources"]:
            continue

        if isinstance(mensaje["sources"], list):

            fuentes += len(mensaje["sources"])

        else:
            fuentes += 1

    # ------------------------------------------------------------------
    # Construcción del resultado
    # ------------------------------------------------------------------

    return {

        # Cantidad total de mensajes
        "total": len(messages),

        # Consultas del usuario
        "preguntas": preguntas,

        # Respuestas del asistente
        "respuestas": respuestas,

        # Total de fuentes utilizadas
        "fuentes": fuentes,

        # Tiempo de la última respuesta
        "tiempo": tiempo,

        # Indicador de memoria conversacional
        "memoria": True,

        # Framework utilizado
        "framework": "LangGraph",

    }