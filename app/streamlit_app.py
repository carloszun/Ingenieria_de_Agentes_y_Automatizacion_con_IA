# ==============================================================================
# app/streamlit_app.py
#
# Interfaz principal del Asistente Virtual del Consultorio Odontológico DENT.
#
# Este archivo actúa como ORQUESTADOR de la aplicación Streamlit.
#
# Su responsabilidad es únicamente coordinar los distintos componentes
# de la interfaz y del agente.
#
# La lógica específica de cada componente se encuentra separada en módulos:
#
# ui/
# ├── header.py
# ├── sidebar.py
# ├── chat.py
# ├── styles.py
# ├── metrics.py
# └── sources.py
#
# De esta forma el archivo principal permanece limpio, fácil de leer
# y sencillo de mantener.
# ==============================================================================

import sys
from pathlib import Path

# ------------------------------------------------------------------------------
# Agregar la raíz del proyecto al PYTHONPATH
#
# Esto permite utilizar importaciones absolutas como:
#
#     from app.agent...
#
# independientemente del directorio desde el cual se ejecute Streamlit.
# ------------------------------------------------------------------------------

ROOT_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT_DIR))

import streamlit as st
import time

# ------------------------------------------------------------------------------
# Componentes principales del agente
# ------------------------------------------------------------------------------

from app.agent.builder import graph
from app.agent.state import AgentState

from app.agent.rag.vector_store import inicializar_vector_store
from app.agent.rag.retriever import crear_retriever
from app.agent.rag.llm import crear_llm
from app.agent.factory import crear_estado
from ui.debug import mostrar_debug
from ui.status import crear_status
from app.agent.classifier import clasificar_consulta

# ------------------------------------------------------------------------------
# Componentes de la interfaz
# ------------------------------------------------------------------------------

from ui.header import mostrar_header
from ui.sidebar import mostrar_sidebar
from ui.chat import mostrar_chat
from ui.styles import aplicar_estilos

# ------------------------------------------------------------------------------
# Componentes auxiliares
# ------------------------------------------------------------------------------

from ui.metrics import calcular_metricas
from ui.sources import formatear_fuentes

# ==============================================================================
# CONFIGURACIÓN GENERAL DE STREAMLIT
# ==============================================================================

st.set_page_config(
    page_title="Consultorio DENT",
    page_icon="🦷",
    layout="centered",
    initial_sidebar_state="auto",
)

# ==============================================================================
# ESTILOS PERSONALIZADOS
# ==============================================================================

aplicar_estilos()

# ==============================================================================
# HEADER
# ==============================================================================

mostrar_header()

# ==============================================================================
# CARGA DE RECURSOS PESADOS
#
# Gracias a cache_resource estos objetos se crean una única vez
# durante toda la sesión del usuario.
# ==============================================================================

@st.cache_resource
def cargar_recursos():
    """
    Inicializa todos los recursos del asistente.

    Recursos cargados:

    - Vector Store (FAISS)
    - Retriever
    - Modelo de lenguaje (DeepSeek)

    Returns
    -------
    tuple
        (retriever, llm)
    """

    vector_store = inicializar_vector_store()

    retriever = crear_retriever(
        vector_store
    )

    llm = crear_llm()

    return retriever, llm


retriever, llm = cargar_recursos()

# ==============================================================================
# INICIALIZACIÓN DEL HISTORIAL
#
# El historial completo de la conversación se almacena en
# st.session_state.messages.
#
# Este historial es utilizado tanto para mostrar el chat como para
# implementar memoria conversacional (History-Aware Retrieval).
# ==============================================================================

if "messages" not in st.session_state:

    st.session_state.messages = [

        {
            "role": "assistant",

            "content":
                "¡Hola! Soy el asistente virtual del "
                "Consultorio Odontológico DENT.\n\n"
                "¿En qué puedo ayudarte?"
        }

    ]

# ==============================================================================
# SIDEBAR
#
# Calcula estadísticas dinámicas de la conversación y las envía
# al panel lateral.
# ==============================================================================

metricas = calcular_metricas(

    st.session_state.messages,

    st.session_state.get(
        "last_response_time",
        0.0,
    ),

)

if mostrar_sidebar(metricas):

    st.session_state.messages = [

        {
            "role": "assistant",

            "content":
                "¡Hola! Soy el asistente virtual del "
                "Consultorio Odontológico DENT.\n\n"
                "¿En qué puedo ayudarte?"
        }

    ]

    st.session_state.last_response_time = 0.0

    st.rerun()

# ==============================================================================
# CHAT
#
# Muestra todo el historial almacenado en la sesión.
# ==============================================================================

mostrar_chat(
    st.session_state.messages
)

# ==============================================================================
# ENTRADA DEL USUARIO
# ==============================================================================

pregunta = st.chat_input(
    "Escriba su consulta"
)

# ==============================================================================
# SI EL USUARIO TODAVÍA NO ESCRIBIÓ NADA,
# FINALIZA AQUÍ EL SCRIPT.
# ==============================================================================

if not pregunta:
    st.stop()

# ==============================================================================
# AGREGAR MENSAJE DEL USUARIO
#
# Se almacena inmediatamente en el historial para que también
# forme parte de la memoria conversacional.
# ==============================================================================

st.session_state.messages.append(

    {
        "role": "user",
        "content": pregunta,
    }

)

with st.chat_message("user"):

    st.write(pregunta)

# ==============================================================================
# CONSTRUCCIÓN DEL ESTADO DEL AGENTE
#
# La creación del AgentState se encuentra centralizada en
# app/agent/factory.py.
#
# Esto permite mantener este archivo limpio y evita duplicación de código.
# ==============================================================================
ruta = clasificar_consulta(
    pregunta,
    llm,
)

status = None

if ruta == "rag":
    status = crear_status()

state = crear_estado(
    question=pregunta,
    history=st.session_state.messages,
    retriever=retriever,
    llm=llm,
    status=status,
)

# ==============================================================================
# EJECUCIÓN DEL AGENTE
#
# El spinner informa al usuario que el asistente se encuentra
# procesando la consulta.
# ==============================================================================

inicio = time.perf_counter()

resultado = graph.invoke(state)

fin = time.perf_counter()

if status:
    status.finalizar()

# -------------------------------------------------------------
# Guardar tiempo de respuesta
# -------------------------------------------------------------

resultado["metrics"]["response_time"] = fin - inicio

st.session_state.last_response_time = resultado["metrics"]["response_time"]

# ==============================================================================
# FORMATEO DE LAS FUENTES
#
# La lógica se encuentra encapsulada dentro de ui/sources.py.
# ==============================================================================

fuentes_texto = formatear_fuentes(
    resultado["sources"]
)

# ==============================================================================
# MOSTRAR RESPUESTA DEL ASISTENTE
#
# Si el usuario activó el Modo Debug desde la sidebar,
# también se mostrará el panel técnico debajo de la respuesta.
# ==============================================================================

with st.chat_message("assistant"):

    st.write(
        resultado["answer"]
    )

    if fuentes_texto:

        st.caption(
            fuentes_texto
        )

    # ----------------------------------------------------------
    # Panel Debug
    # ----------------------------------------------------------

    if st.session_state.get("debug", False):
        
        mostrar_debug(
            resultado["metrics"]
        )


# ==============================================================================
# ACTUALIZAR HISTORIAL
#
# Se almacena la respuesta junto con las fuentes y las métricas
# utilizadas durante esa consulta.
# ==============================================================================

st.session_state.messages.append(

    {

        "role": "assistant",

        "content": resultado["answer"],

        "sources": fuentes_texto,

        "metrics": resultado["metrics"],

    }

)

# ==============================================================================
# FIN DE LA EJECUCIÓN
#
# Streamlit volverá a ejecutar automáticamente este archivo
# cuando el usuario envíe una nueva consulta.
#
# Gracias al uso de st.session_state la conversación permanece
# disponible durante toda la sesión del usuario.
# ==============================================================================