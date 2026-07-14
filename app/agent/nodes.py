"""
Nodos del agente LangGraph.

Este módulo implementa la lógica de cada nodo del flujo conversacional.

Responsabilidades
-----------------
- Saludo.
- Despedida.
- Agradecimiento.
- Flujo principal RAG.
- Construcción del contexto.
- Recuperación de documentos.
- Generación de respuestas.

Cada nodo recibe un AgentState y devuelve el mismo estado
actualizado.

El nodo RAG implementa además:

- History-Aware Retrieval.
- Métricas.
- Actualización del estado visual de Streamlit.
"""

from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage,
)

from .state import AgentState

from .history import reescribir_consulta

from .prompts import (
    SYSTEM_PROMPT,
    RAG_PROMPT,
)


# =============================================================================
# NODO SALUDO
# =============================================================================

def nodo_saludo(state: AgentState) -> AgentState:
    """
    Responde un saludo inicial.
    """

    texto = state["question"].lower()

    if "buen día" in texto or "buen dia" in texto:
        saludo = "¡Buen día!"

    elif "buenas tardes" in texto:
        saludo = "¡Buenas tardes!"

    elif "buenas noches" in texto:
        saludo = "¡Buenas noches!"

    else:
        saludo = "¡Hola!"

    state["answer"] = (
        f"{saludo}\n\n"
        "Soy el asistente virtual del Consultorio Odontológico DENT.\n\n"
        "¿En qué puedo ayudarte?"
    )

    return state


# =============================================================================
# NODO AGRADECIMIENTO
# =============================================================================

def nodo_agradecimiento(state: AgentState) -> AgentState:
    """
    Responde un agradecimiento.
    """

    state["answer"] = (
        "¡De nada! 😊\n\n"
        "Estoy para ayudarte."
    )

    return state


# =============================================================================
# NODO DESPEDIDA
# =============================================================================

def nodo_despedida(state: AgentState) -> AgentState:
    """
    Responde una despedida.
    """

    state["answer"] = (
        "¡Hasta luego!\n\n"
        "Gracias por comunicarte con el "
        "Consultorio Odontológico DENT."
    )

    return state


# =============================================================================
# NODO PRINCIPAL RAG
# =============================================================================

def nodo_rag(state: AgentState) -> AgentState:
    """
    Flujo principal Retrieval-Augmented Generation.
    """

    # =====================================================================
    # ETAPA 1
    # =====================================================================

    state["status"].actualizar(
        "🧠 Analizando consulta..."
    )

    # =====================================================================
    # Reescritura utilizando History-Aware Retrieval
    # =====================================================================

    state["status"].actualizar(
        "🔄 Reescribiendo consulta..."
    )

    pregunta_reescrita = reescribir_consulta(
        question=state["question"],
        history=state["history"],
        llm=state["llm"],
    )

    # =====================================================================
    # Métricas
    # =====================================================================

    state["metrics"]["original_question"] = state["question"]

    state["metrics"]["rewritten_question"] = pregunta_reescrita

    print("\nPregunta original:")
    print(state["question"])

    print("\nPregunta reescrita:")
    print(pregunta_reescrita)

    # =====================================================================
    # Recuperación de documentos
    # =====================================================================

    state["status"].actualizar(
        "🔎 Buscando documentación..."
    )

    documentos = state["retriever"].invoke(
        pregunta_reescrita
    )

    state["metrics"]["documents"] = len(documentos)

    # =====================================================================
    # Sin documentos
    # =====================================================================

    if not documentos:

        state["status"].error(
            "No se encontraron documentos relevantes."
        )

        state["answer"] = (
            "No encontré esa información en la documentación "
            "del consultorio DENT."
        )

        state["context"] = ""

        state["sources"] = []

        state["metrics"]["documents"] = 0

        state["metrics"]["sources"] = 0

        return state

    state["metrics"]["route"] = state["route"]

    # =====================================================================
    # Preparación del contexto
    # =====================================================================

    state["status"].actualizar(
        "📄 Preparando contexto..."
    )

    # =====================================================================
    # Construcción del contexto
    # =====================================================================

    contexto = "\n\n".join(
        doc.page_content
        for doc in documentos
    )

    state["context"] = contexto

    # =====================================================================
    # Construcción de las fuentes
    # =====================================================================

    sources = []

    for doc in documentos:

        fuente = {

            "page": doc.metadata.get("page"),

            "source": doc.metadata.get("source"),

        }

        if fuente not in sources:

            sources.append(fuente)

    state["sources"] = sorted(

        sources,

        key=lambda x: x["page"],

    )

    state["metrics"]["sources"] = len(
        state["sources"]
    )

    # =====================================================================
    # Construcción del historial para el LLM
    # =====================================================================

    messages = [

        SystemMessage(
            content=SYSTEM_PROMPT
        )

    ]

    for mensaje in state["history"]:

        if mensaje["role"] == "user":

            messages.append(

                HumanMessage(
                    content=mensaje["content"]
                )

            )

        elif mensaje["role"] == "assistant":

            messages.append(

                AIMessage(
                    content=mensaje["content"]
                )

            )

    # =====================================================================
    # Prompt final RAG
    # =====================================================================

    user_message = RAG_PROMPT.format(

        context=contexto,

        question=state["question"],

    )

    messages.append(

        HumanMessage(
            content=user_message
        )

    )

    # =====================================================================
    # Generación de la respuesta
    # =====================================================================

    state["status"].actualizar(
        "🤖 Generando respuesta..."
    )

    respuesta = state["llm"].invoke(
        messages
    )

    state["answer"] = respuesta.content

    # =====================================================================
    # Respuesta generada correctamente
    # =====================================================================

    state["status"].finalizar()

    # =====================================================================
    # Fin del nodo
    #
    # En este punto el AgentState contiene:
    #
    # - answer
    # - context
    # - sources
    # - history
    # - metrics
    #
    # Las métricas serán utilizadas posteriormente por:
    #
    # - Sidebar
    # - Panel Debug
    # - Estadísticas
    #
    # El componente visual de estado ya fue actualizado
    # mediante state["status"].
    # =====================================================================

    return state

# =============================================================================
# NODO FUERA DE DOMINIO
# =============================================================================

def nodo_fuera_dominio(state: AgentState) -> AgentState:
    """
    Responde consultas que no pertenecen al dominio del
    Consultorio Odontológico DENT.

    Este nodo evita que el asistente responda preguntas
    sobre temas ajenos a la documentación del consultorio.
    """

    state["answer"] = (
        "Lo siento, solamente puedo responder consultas "
        "relacionadas con el Consultorio Odontológico DENT "
        "y la información contenida en su documentación."
    )

    return state