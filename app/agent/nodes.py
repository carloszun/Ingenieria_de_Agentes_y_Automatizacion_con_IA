"""
Nodos del grafo de LangGraph.

Cada función representa un nodo del grafo y recibe un AgentState.
El nodo procesa la información y devuelve el mismo estado con nuevos
campos completados (respuesta, contexto, fuentes, etc.).

En este módulo se implementa el nodo RAG principal del asistente.
"""

from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage,
)

from .state import AgentState
from .prompts import SYSTEM_PROMPT, RAG_PROMPT
from .history import reescribir_consulta


def nodo_saludo(state: AgentState) -> AgentState:
    """
    Responde cuando el usuario únicamente saluda.
    """
    state["answer"] = (
        "¡Hola! Soy el asistente virtual del Consultorio Odontológico DENT.\n\n"
        "Estoy preparado para responder consultas sobre turnos, convenios, "
        "políticas e información contenida en la documentación del consultorio.\n\n"
        "¿En qué puedo ayudarte?"
    )

    return state


def nodo_agradecimiento(state: AgentState) -> AgentState:
    """
    Responde cuando el usuario agradece.
    """
    state["answer"] = (
        "¡De nada! Quedo a tu disposición para cualquier otra consulta."
    )

    return state


def nodo_despedida(state: AgentState) -> AgentState:
    """
    Responde cuando el usuario se despide.
    """
    state["answer"] = (
        "¡Hasta luego! Que tengas un buen día."
    )

    return state


def nodo_fuera_dominio(state: AgentState) -> AgentState:
    """
    Responde cuando la consulta no pertenece al dominio del consultorio.
    """
    state["answer"] = (
        "Soy el asistente virtual del Consultorio Odontológico DENT.\n\n"
        "Puedo responder únicamente consultas relacionadas con turnos, horarios, "
        "convenios, políticas y demás información contenida en la documentación "
        "del consultorio.\n\n"
        "Si tenés alguna consulta sobre DENT, estaré encantado de ayudarte."
    )

    return state


def nodo_rag(state: AgentState) -> AgentState:
    """
    Nodo principal de Retrieval-Augmented Generation (RAG).

    Flujo general:

        1. Recupera documentos relevantes utilizando el Retriever.
        2. Si no encuentra documentos, devuelve una respuesta estándar.
        3. Construye el contexto concatenando los documentos recuperados.
        4. Guarda las fuentes sin duplicados.
        5. Construye el historial de conversación.
        6. Invoca al LLM.
        7. Guarda la respuesta en el estado.

    --------------------------------------------------------------------------

    Novedad:

    Ahora el nodo incorpora el historial de conversación almacenado
    en state["history"].

    Esto permite que el modelo conozca el contexto conversacional
    (preguntas anteriores y respuestas anteriores).

    IMPORTANTE:

    Todavía el Retriever sigue buscando únicamente utilizando
    la pregunta actual.

    La memoria conversacional ayuda al LLM a interpretar referencias
    como:

        Usuario:
            ¿Atienden por OSDE?

        Asistente:
            Sí...

        Usuario:
            ¿Y qué planes?

    pero todavía NO mejora la búsqueda vectorial.
    Eso lo implementaremos en el siguiente paso.
    """

    # ==========================================================
    # 1. Reescribir la consulta utilizando el historial
    # ==========================================================

    pregunta_reescrita = reescribir_consulta(
        question=state["question"],
        history=state["history"],
        llm=state["llm"],
    )

    # ==========================================================
    # DEBUG (temporal)
    # ==========================================================

    print("\nPregunta original:")
    print(state["question"])

    print("\nPregunta reescrita:")
    print(pregunta_reescrita)

    # ==========================================================
    # 2. Recuperar documentos utilizando la consulta reescrita
    # ==========================================================

    documentos = state["retriever"].invoke(
        pregunta_reescrita
    )

    if not documentos:

        state["answer"] = (
            "No encontré esa información en la documentación del consultorio DENT."
        )

        state["context"] = ""
        state["sources"] = []

        return state

    # ==========================================================
    # 3. Construcción del contexto
    # ==========================================================

    contexto = "\n\n".join(
        doc.page_content
        for doc in documentos
    )

    state["context"] = contexto

    # ==========================================================
    # 4. Construcción de fuentes
    # ==========================================================

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
        key=lambda x: x["page"]
    )

    # ==========================================================
    # 5. Construcción del historial de conversación
    # ==========================================================

    messages = [
        SystemMessage(content=SYSTEM_PROMPT)
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

    # ==========================================================
    # 6. Agregar el prompt RAG con contexto
    # ==========================================================

    user_message = RAG_PROMPT.format(
        context=contexto,
        question=state["question"]
    )

    messages.append(
        HumanMessage(content=user_message)
    )

    # ==========================================================
    # 7. Invocar el modelo
    # ==========================================================

    respuesta = state["llm"].invoke(messages)

    # ==========================================================
    # 8. Guardar respuesta
    # ==========================================================

    state["answer"] = respuesta.content

    return state