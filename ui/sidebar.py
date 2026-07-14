"""
Barra lateral de la aplicación.

Centraliza toda la información complementaria del asistente.

Actualmente muestra:

- Estadísticas de la conversación.
- Estado del agente.
- Tiempo de respuesta.
- Información del proyecto.

También permite:

- Iniciar una nueva conversación.
- Activar o desactivar el Modo Debug.

El estado del Modo Debug se almacena en
st.session_state.debug para que pueda ser utilizado
por el resto de la aplicación.
"""

import streamlit as st
from ui.documents import mostrar_documentos

from utils.config import (
    DEEPSEEK_CHAT_MODEL,
    EMBEDDING_MODEL,
)


def mostrar_sidebar(metricas: dict) -> bool:
    """
    Construye la barra lateral de la aplicación.

    Parámetros
    ----------
    metricas : dict
        Diccionario generado por calcular_metricas().

    Retorna
    -------
    bool
        True si el usuario presionó el botón
        "Nueva conversación".
    """

    nueva_conversacion = False

    with st.sidebar:

        # ==========================================================
        # TÍTULO
        # ==========================================================

        st.title("🦷 DENT")

        st.caption("Asistente Virtual")

        st.divider()

        # ==========================================================
        # ESTADÍSTICAS DE LA CONVERSACIÓN
        # ==========================================================

        st.subheader("📊 Estadísticas")

        col1, col2 = st.columns([2, 1])  # Ajusta el ancho, la primera columna es más ancha

        with col1:
            st.write("💬 **Mensajes:**")
            st.write("❓ **Preguntas:**")
            st.write("🧠 **Respuestas:**")
            st.write("⚡ **Tiempo:**")

        with col2:
            st.write(metricas['total'])
            st.write(metricas['preguntas'])
            st.write(metricas['respuestas'])
            st.write(f"{metricas['tiempo']:.2f} s")
#        st.write(f"💬 **Mensajes:** {metricas['total']}")
#        st.write(f"❓ **Preguntas:** {metricas['preguntas']}")
#        st.write(f"🤖 **Respuestas:** {metricas['respuestas']}")
#        st.write(f"⚡ **Tiempo:** {metricas['tiempo']:.2f} s")

        st.divider()

        # ==========================================================
        # MODO DEBUG
        #
        # Permite mostrar u ocultar la información técnica
        # debajo de cada respuesta del asistente.
        #
        # El estado queda almacenado en Session State para
        # que pueda ser consultado desde streamlit_app.py.
        # ==========================================================

        st.subheader("🛠 Desarrollo")

        st.session_state.debug = st.toggle(
            "Mostrar información técnica",
            value=st.session_state.get(
                "debug",
                False,
            ),
            help=(
                "Muestra información interna del agente "
                "como la pregunta reescrita, cantidad de "
                "documentos recuperados y métricas de ejecución."
            ),
        )

        st.divider()

        # ==========================================================
        # ESTADO DEL AGENTE
        # ==========================================================

        st.subheader("🤖 Agente")

        st.write(f"**LLM:** {DEEPSEEK_CHAT_MODEL}")

        st.write(f"**Embeddings:** {EMBEDDING_MODEL}")

        st.write("**Vector Store:** FAISS")

        st.write("**Framework:** LangGraph")

        st.write("**Memoria:** ✅ Activa")

        st.write("**History Aware:** ✅ Activo")

        st.divider()

        mostrar_documentos()

        st.divider()

        # ==========================================================
        # NUEVA CONVERSACIÓN
        # ==========================================================

        if st.button(
            "🗑 Nueva conversación",
            use_container_width=True,
        ):
            nueva_conversacion = True

        st.divider()

        # ==========================================================
        # INFORMACIÓN
        # ==========================================================

        st.info(
            "Asistente basado en Retrieval-Augmented Generation (RAG)."
        )

        st.divider()

        st.caption(
            "Ingeniería de Agentes y Automatización con IA"
        )

    return nueva_conversacion