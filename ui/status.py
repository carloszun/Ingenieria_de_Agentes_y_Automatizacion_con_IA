"""
Componente visual de estado del agente.

Este módulo encapsula el uso de st.status() para mostrar al usuario
las distintas etapas de procesamiento del asistente.

Objetivos
---------
- Mejorar la experiencia del usuario.
- Mostrar que el agente está trabajando.
- Mantener streamlit_app.py limpio.
- Centralizar toda la lógica relacionada con el estado visual.

Ejemplo
-------

estado = crear_status()

estado.actualizar("🧠 Analizando consulta...")
estado.actualizar("🔍 Buscando documentación...")
estado.actualizar("🤖 Generando respuesta...")

estado.finalizar()
"""

import streamlit as st


class EstadoAgente:
    """
    Controlador del componente visual de estado.

    Encapsula un st.status() de Streamlit y ofrece métodos simples
    para actualizar el mensaje mostrado al usuario.
    """

    def __init__(self):
        """
        Crea el componente visual.

        El estado comienza expandido para que el usuario vea
        inmediatamente el progreso del asistente.
        """

        self.status = st.status(
            "🧠 Iniciando procesamiento...",
            expanded=True,
        )

    # ------------------------------------------------------------------
    # Actualizar mensaje
    # ------------------------------------------------------------------

    def actualizar(self, mensaje: str):
        """
        Actualiza el texto mostrado en el panel de estado.

        Parameters
        ----------
        mensaje : str
            Texto descriptivo de la etapa actual.
        """

        self.status.update(
            label=mensaje,
            state="running",
            expanded=True,
        )

    # ------------------------------------------------------------------
    # Finalizar correctamente
    # ------------------------------------------------------------------

    def finalizar(self):
        """
        Marca el procesamiento como finalizado correctamente.
        """

        self.status.update(
            label="✅ Respuesta generada correctamente",
            state="complete",
            expanded=False,
        )

    # ------------------------------------------------------------------
    # Mostrar error
    # ------------------------------------------------------------------

    def error(self, mensaje: str):
        """
        Marca el procesamiento como fallido.

        Parameters
        ----------
        mensaje : str
            Descripción del error.
        """

        self.status.update(
            label=f"❌ {mensaje}",
            state="error",
            expanded=True,
        )


# =============================================================================
# Factory
# =============================================================================

def crear_status() -> EstadoAgente:
    """
    Crea un nuevo controlador visual del estado del agente.

    Returns
    -------
    EstadoAgente
        Instancia lista para utilizar.
    """

    return EstadoAgente()