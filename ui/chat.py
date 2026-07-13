"""
Componente de interfaz encargado de mostrar el historial de la conversación.

Este módulo encapsula toda la lógica relacionada con la visualización
del chat en Streamlit.

Objetivos
---------

- Mantener streamlit_app.py limpio.
- Centralizar el renderizado del historial.
- Facilitar futuras mejoras visuales del chat.
- Evitar código duplicado.

Actualmente cada mensaje puede contener:

- role
- content
- sources (opcional)

Si existen fuentes, se muestran debajo de la respuesta utilizando
st.caption() para que ocupen poco espacio visual.
"""

import streamlit as st


def mostrar_chat(messages: list) -> None:
    """
    Renderiza el historial completo de la conversación.

    Parámetros
    ----------
    messages : list
        Historial almacenado en st.session_state.messages.

    Formato esperado:

    [
        {
            "role": "assistant",
            "content": "...",
            "sources": "..."
        },
        {
            "role": "user",
            "content": "..."
        }
    ]
    """

    for mensaje in messages:

        with st.chat_message(mensaje["role"]):

            # ----------------------------------------------------------
            # Mostrar el contenido principal del mensaje
            # ----------------------------------------------------------

            st.write(
                mensaje["content"]
            )

            # ----------------------------------------------------------
            # Mostrar las fuentes únicamente cuando existan.
            # Normalmente sólo aparecen en los mensajes del asistente.
            # ----------------------------------------------------------

            if mensaje.get("sources"):

                st.caption(
                    mensaje["sources"]
                )