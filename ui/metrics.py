"""
Métricas de la interfaz de usuario.

Este módulo concentra todas las funciones relacionadas con estadísticas
de la conversación y del estado de la aplicación.

La idea es mantener esta lógica fuera de streamlit_app.py para que
el archivo principal actúe únicamente como orquestador de la interfaz.

Actualmente calcula:

- Cantidad total de mensajes.
- Cantidad de preguntas del usuario.
- Cantidad de respuestas del asistente.

En el futuro podrá incorporar:

- Tiempo promedio de respuesta.
- Tokens consumidos.
- Cantidad de consultas RAG.
- Cantidad de consultas fuera de dominio.
- Tiempo total de la sesión.
"""

from typing import Dict, List


def calcular_metricas(messages: List[dict]) -> Dict[str, int]:
    """
    Calcula estadísticas básicas de la conversación.

    Parámetros
    ----------
    messages : list
        Historial almacenado en st.session_state.messages.

    Retorna
    -------
    dict

    Ejemplo:

    {
        "total": 8,
        "preguntas": 4,
        "respuestas": 4,
    }
    """

    preguntas = sum(
        1
        for mensaje in messages
        if mensaje["role"] == "user"
    )

    respuestas = sum(
        1
        for mensaje in messages
        if mensaje["role"] == "assistant"
    )

    return {
        "total": len(messages),
        "preguntas": preguntas,
        "respuestas": respuestas,
    }