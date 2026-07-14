"""
Panel de información técnica (Debug).

Este módulo concentra toda la visualización de información
interna del agente.

Objetivos
---------
- Facilitar el desarrollo y depuración.
- Mostrar el funcionamiento interno del agente.
- Mantener streamlit_app.py limpio.
- Permitir activar o desactivar la información técnica
  desde la barra lateral.

La información mostrada puede incluir:

- Pregunta original.
- Pregunta reescrita.
- Cantidad de documentos recuperados.
- Cantidad de fuentes utilizadas.
- Tiempo total de respuesta.

En futuras versiones podrán incorporarse:

- Tiempo del Retriever.
- Tiempo del LLM.
- Tokens de entrada y salida.
- Costo estimado.
- Ruta seguida dentro del grafo.
"""

import streamlit as st


def mostrar_debug(metrics: dict):
    """
    Muestra el panel de depuración del agente.

    Parameters
    ----------
    metrics : dict
        Diccionario de métricas generado durante la
        ejecución del agente.

    Returns
    -------
    None
    """

    if not metrics:
        return

    with st.expander("🔎 Información técnica", expanded=False):

        # ----------------------------------------------------------
        # Pregunta original
        # ----------------------------------------------------------

        st.markdown("### 📝 Pregunta original")

        st.code(
            metrics.get(
                "original_question",
                "-"
            ),
            language="text",
        )

        # ----------------------------------------------------------
        # Pregunta reescrita
        # ----------------------------------------------------------

        st.markdown("### 🔄 Pregunta reescrita")

        st.code(
            metrics.get(
                "rewritten_question",
                "-"
            ),
            language="text",
        )

        # ----------------------------------------------------------
        # Métricas
        # ----------------------------------------------------------

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Documentos",
                metrics.get(
                    "documents",
                    0,
                ),
            )

            st.metric(
                "Fuentes",
                metrics.get(
                    "sources",
                    0,
                ),
            )

        with col2:

            st.metric(
                "Tiempo",
                f'{metrics.get("response_time", 0):.2f} s'
            )

            st.metric(
                "Memoria",
                "✅"
            )

        # ----------------------------------------------------------
        # Información adicional
        # ----------------------------------------------------------

        if "route" in metrics:

            st.markdown("---")

            st.write(
                f"**Ruta seleccionada:** `{metrics['route']}`"
            )