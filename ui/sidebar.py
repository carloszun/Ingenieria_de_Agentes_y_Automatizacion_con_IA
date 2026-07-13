"""
Barra lateral de la aplicación.

Centraliza toda la información complementaria del asistente.

Actualmente muestra:

- Estadísticas de la conversación.
- Información del proyecto.
- Modelo utilizado.
- Embeddings.
- Vector Store.
- Estado del agente.

En futuras versiones podrá contener:

- Nueva conversación.
- Exportar conversación.
- Configuración.
- Información del repositorio.
- Tiempo de respuesta.
- Tokens consumidos.
"""

import streamlit as st

from utils.config import (
    DEEPSEEK_CHAT_MODEL,
    EMBEDDING_MODEL,
)


def mostrar_sidebar(metricas: dict) -> None:
    """
    Construye la barra lateral de la aplicación.

    Parámetros
    ----------
    metricas : dict

        Diccionario generado por ui.metrics.calcular_metricas().

        Ejemplo:

        {
            "total": 12,
            "preguntas": 6,
            "respuestas": 6,
        }
    """

    with st.sidebar:

        # ==========================================================
        # TÍTULO
        # ==========================================================

        st.title("🦷 DENT")

        st.caption("Asistente Virtual")

        st.divider()

        # ==========================================================
        # ESTADÍSTICAS
        # ==========================================================

        st.subheader("📊 Estadísticas")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Mensajes",
                metricas["total"],
            )

            st.metric(
                "Preguntas",
                metricas["preguntas"],
            )

        with col2:
            st.metric(
                "Respuestas",
                metricas["respuestas"],
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