# ==============================================================================
# app/streamlit_app.py
# Interfaz de usuario con Streamlit para el Asistente Virtual DENT
# ==============================================================================

import sys
from pathlib import Path

# Agrega la raíz del proyecto al sys.path para que las importaciones
# absolutas (como 'from app.agent...') funcionen correctamente.
ROOT_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT_DIR))

import streamlit as st

# ------------------------------------------------------------------------------
# Importaciones del núcleo del asistente
# ------------------------------------------------------------------------------
from app.agent.rag.vector_store import inicializar_vector_store
from app.agent.rag.retriever import crear_retriever
from app.agent.rag.llm import crear_llm

from app.agent.builder import graph
from app.agent.state import AgentState

from utils.documentos import nombre_documento

# ------------------------------------------------------------------------------
# Importación del header (UI separada)
# ------------------------------------------------------------------------------
from ui.header import mostrar_header


# ==============================================================================
# 1. CONFIGURACIÓN DE LA PÁGINA
# ==============================================================================

st.set_page_config(
    page_title="Consultorio DENT",
    page_icon="🦷",
    layout="centered",
    initial_sidebar_state="auto",
)


# ==============================================================================
# 2. HEADER: LOGO + TÍTULO (desde ui/header.py)
# ==============================================================================

mostrar_header()


# ==============================================================================
# 3. CARGA DE RECURSOS PESADOS (con caché)
# ==============================================================================

@st.cache_resource
def cargar_recursos():
    """
    Carga el vector store, el retriever y el LLM una sola vez.

    Streamlit almacenará estos objetos en caché para evitar volver a
    generar los embeddings y el índice FAISS en cada interacción.
    """
    vector_store = inicializar_vector_store()
    retriever = crear_retriever(vector_store)
    llm = crear_llm()

    return retriever, llm


retriever, llm = cargar_recursos()


# ==============================================================================
# 4. HISTORIAL DE CONVERSACIÓN
# ==============================================================================

if "messages" not in st.session_state:

    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "¡Hola! Soy el asistente virtual del Consultorio "
                "Odontológico DENT.\n\n"
                "¿En qué puedo ayudarte?"
            ),
        }
    ]


# ==============================================================================
# 5. MOSTRAR HISTORIAL
# ==============================================================================

for mensaje in st.session_state.messages:

    with st.chat_message(mensaje["role"]):

        st.write(mensaje["content"])

        if mensaje.get("sources"):
            st.caption(mensaje["sources"])


# ==============================================================================
# 6. ENTRADA DEL USUARIO
# ==============================================================================

pregunta = st.chat_input("Escriba su consulta")


# ==============================================================================
# 7. PROCESAR NUEVA CONSULTA
# ==============================================================================

if pregunta:

    # --------------------------------------------------------------------------
    # 7.1 Mostrar pregunta del usuario
    # --------------------------------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": pregunta,
        }
    )

    with st.chat_message("user"):
        st.write(pregunta)

    # --------------------------------------------------------------------------
    # 7.2 Crear el estado inicial del agente
    # --------------------------------------------------------------------------
    
    history = []

    for mensaje in st.session_state.messages:

        history.append(
            {
                "role": mensaje["role"],
                "content": mensaje["content"],
            }
        )

    state: AgentState = {
        "question": pregunta,
        "context": "",
        "route": "",
        "answer": "",
        "sources": [],
        "history": history,
        "retriever": retriever,
        "llm": llm,

        # NUEVO
        # En el próximo paso LangGraph utilizará este historial.
        "history": st.session_state.messages,
    }

    # --------------------------------------------------------------------------
    # 7.3 Ejecutar LangGraph
    # --------------------------------------------------------------------------

    with st.spinner("Consultando documentación..."):

        resultado = graph.invoke(state)

    # --------------------------------------------------------------------------
    # 7.4 Construir texto compacto de fuentes
    # --------------------------------------------------------------------------

    fuentes_texto = ""

    if resultado["sources"]:

        nombre = nombre_documento(
            resultado["sources"][0]["source"]
        )

        paginas = sorted(
            {
                fuente["page"]
                for fuente in resultado["sources"]
            }
        )

        paginas_str = " • ".join(
            str(pagina)
            for pagina in paginas
        )

        fuentes_texto = (
            f"📄 {nombre}: págs. {paginas_str}"
        )

    # --------------------------------------------------------------------------
    # 7.5 Mostrar respuesta
    # --------------------------------------------------------------------------

    with st.chat_message("assistant"):

        st.write(resultado["answer"])

        if fuentes_texto:
            st.caption(fuentes_texto)

    # --------------------------------------------------------------------------
    # 7.6 Guardar respuesta en el historial
    # --------------------------------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": resultado["answer"],
            "sources": fuentes_texto,
        }
    )