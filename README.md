# 🦷 Asistente Virtual Inteligente para Consultorio Odontológico DENT

<!-- markdownlint-disable MD033 -->

> Agente conversacional basado en Inteligencia Artificial desarrollado con **LangGraph**, **LangChain** y **Retrieval-Augmented Generation (RAG)** para responder consultas utilizando exclusivamente documentación institucional.

<p align="center">

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![LangChain](https://img.shields.io/badge/LangChain-1.x-green)
![LangGraph](https://img.shields.io/badge/LangGraph-1.x-orange)
![FAISS](https://img.shields.io/badge/Vector%20Store-FAISS-red)
![DeepSeek](https://img.shields.io/badge/LLM-DeepSeek-purple)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-ff4b4b)
![License](https://img.shields.io/badge/License-MIT-blue)

</p>

---

## 📖 Descripción

Este proyecto implementa un **Agente Inteligente** capaz de responder preguntas sobre la documentación del **Consultorio Odontológico DENT** utilizando una arquitectura **Retrieval-Augmented Generation (RAG)**.

El sistema combina búsqueda semántica mediante **FAISS**, memoria conversacional (**History-Aware Retrieval**) y un modelo de lenguaje (**DeepSeek**) para generar respuestas fundamentadas únicamente en la documentación disponible.

Toda la aplicación fue desarrollada utilizando una arquitectura modular basada en **LangGraph**, separando claramente la interfaz, el flujo conversacional, el procesamiento documental y los componentes del agente.

---

## ✨ Características principales

- ✅ Arquitectura basada en LangGraph
- ✅ Router inteligente de consultas
- ✅ Retrieval-Augmented Generation (RAG)
- ✅ History-Aware Retrieval
- ✅ Búsqueda semántica mediante FAISS
- ✅ Modelo de lenguaje DeepSeek
- ✅ Carga dinámica de documentos PDF
- ✅ Reconstrucción automática del índice vectorial
- ✅ Memoria conversacional
- ✅ Panel de depuración (Debug)
- ✅ Estados visuales del agente
- ✅ Interfaz desarrollada con Streamlit
- ✅ Arquitectura modular y escalable

## 🏗 Arquitectura

El proyecto está organizado en módulos independientes siguiendo una arquitectura basada en **LangGraph**, donde cada componente tiene una responsabilidad específica.

```text
                 Usuario
                     │
                     ▼
            Interfaz Streamlit
                     │
                     ▼
               LangGraph
                     │
              ┌──────┴──────┐
              │             │
           Router       Saludos
              │
              ▼
           Nodo RAG
              │
              ▼
  History-Aware Retrieval
              │
              ▼
             FAISS
              │
              ▼
          DeepSeek LLM
              │
              ▼
           Respuesta
```

### Componentes

- **Streamlit**: interfaz de usuario.
- **LangGraph**: orquesta el flujo del agente.
- **Router**: clasifica la intención de la consulta.
- **Nodo RAG**: recupera contexto y genera la respuesta.
- **FAISS**: realiza la búsqueda semántica sobre los documentos.
- **DeepSeek**: genera la respuesta utilizando el contexto recuperado.

## 📂 Estructura del proyecto

```text
Ingenieria_de_Agentes_y_Automatizacion_con_IA/
│
├── app/
│   ├── agent/
│   │   ├── rag/
│   │   │   ├── embeddings.py
│   │   │   ├── llm.py
│   │   │   ├── loader.py
│   │   │   ├── retriever.py
│   │   │   ├── splitter.py
│   │   │   └── vector_store.py
│   │   ├── builder.py
│   │   ├── classifier.py
│   │   ├── factory.py
│   │   ├── history.py
│   │   ├── nodes.py
│   │   ├── prompts.py
│   │   ├── router.py
│   │   └── state.py
│   │
│   ├── streamlit_app.py
│   └── main.py
│
├── assets/
│   └── logo_dent.png
│
├── data/
│   └── DENT_Manual_Institucional.pdf
│
├── ui/
│   ├── chat.py
│   ├── debug.py
│   ├── documents.py
│   ├── header.py
│   ├── metrics.py
│   ├── sidebar.py
│   ├── sources.py
│   ├── status.py
│   └── styles.py
│
├── utils/
│   ├── config.py
│   └── documentos.py
│
├── .env.example
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

### Organización

| Carpeta        | Descripción                                                            |
| -------------- | ---------------------------------------------------------------------- |
| `app/agent`    | Lógica del agente, LangGraph, Router y RAG.                            |
| `app/agent/rag`| Componentes del procesamiento documental y búsqueda semántica.         |
| `ui`           | Componentes reutilizables de la interfaz Streamlit.                    |
| `utils`        | Configuración y utilidades del proyecto.                               |
| `data`         | Base documental consumida por el agente.                               |
| `assets`       | Recursos gráficos utilizados por la aplicación.                        |

## ⚙️ Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/Ingenieria_de_Agentes_y_Automatizacion_con_IA.git

cd Ingenieria_de_Agentes_y_Automatizacion_con_IA
```

> Reemplazá `TU_USUARIO` por tu usuario de GitHub.

### 2. Crear un entorno virtual

#### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar las variables de entorno

Copiar el archivo de ejemplo:

```bash
cp .env.example .env
```

Luego completar las credenciales correspondientes.

> En Windows también puede copiarse manualmente el archivo `.env.example` como `.env`.

### 5. Ejecutar la aplicación

```bash
streamlit run app/streamlit_app.py
```

La aplicación quedará disponible en:

```text

http://localhost:8501
```

## 🔑 Configuración

La aplicación utiliza variables de entorno para almacenar las credenciales necesarias para acceder a los servicios de Inteligencia Artificial.

Estas variables deben definirse en el archivo `.env`.

### Variables utilizadas

| Variable | Descripción |
| -------- | ----------- |
| `DEEPSEEK_API_KEY` | Clave de acceso a la API de DeepSeek. |
| `DEEPSEEK_API_BASE` | URL base de la API compatible con OpenAI. |
| `DEEPSEEK_CHAT_MODEL` | Modelo de lenguaje utilizado por el agente. |
| `GOOGLE_API_KEY` | Clave de acceso a la API de Google AI (opcional). |
| `CHAT_MODEL_GEMINI` | Modelo de Gemini (opcional). |
| `EMBEDDING_MODEL` | Modelo utilizado para generar los embeddings. |

### Archivo `.env`

Ejemplo:

```env
DEEPSEEK_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxx

DEEPSEEK_API_BASE=https://api.deepseek.com

DEEPSEEK_CHAT_MODEL=deepseek-chat

GOOGLE_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxx

CHAT_MODEL_GEMINI=gemini-2.5-flash-lite

EMBEDDING_MODEL=models/gemini-embedding-2
```

> **Importante:** Nunca compartas tu archivo `.env` ni publiques claves de API en el repositorio. El proyecto incluye un archivo `.env.example` como referencia para facilitar la configuración.

## ▶️ Uso de la aplicación

Una vez iniciada la aplicación, el asistente estará disponible desde el navegador en:

```text
http://localhost:8501
```

La interfaz permite interactuar con el agente de forma conversacional y administrar la base documental utilizada para responder las consultas.

### Realizar consultas

Escriba una pregunta en el cuadro de texto y presione **Enter**.

Ejemplos:

- ¿Cómo puedo solicitar un turno?
- ¿Qué obras sociales aceptan?
- ¿Atienden los sábados?
- ¿Debo concurrir con estudios previos?
- ¿Cuál es la política de cancelación?

Durante el procesamiento se mostrarán las distintas etapas de ejecución del agente:

- 🧠 Analizando consulta...
- ✍️ Reescribiendo consulta...
- 🔍 Buscando documentación...
- 🤖 Generando respuesta...

Al finalizar, el asistente mostrará la respuesta junto con las fuentes utilizadas.

---

### Administrar la base documental

Desde la barra lateral es posible administrar los documentos que forman parte de la base de conocimiento.

Actualmente se puede:

- Agregar nuevos documentos PDF.
- Visualizar los documentos cargados.
- Eliminar documentos existentes.

Cada vez que se agrega o elimina un documento, el índice vectorial **FAISS** se reconstruye automáticamente para que los cambios estén disponibles de forma inmediata.

---

### Modo Debug

La aplicación incorpora un **Modo Debug** que puede activarse desde la barra lateral.

Cuando está habilitado se muestra información técnica sobre la ejecución del agente, incluyendo:

- Consulta original.
- Consulta reescrita.
- Ruta seleccionada por el Router.
- Cantidad de documentos recuperados.
- Cantidad de fuentes utilizadas.
- Tiempo de respuesta.

Esta información resulta útil para comprender el funcionamiento interno del sistema y facilitar las tareas de desarrollo y depuración.

## 🧠 Funcionamiento interno

El asistente implementa una arquitectura basada en **LangGraph**, donde cada consulta recorre una serie de etapas antes de generar una respuesta.

El siguiente diagrama resume el flujo completo del procesamiento.

```text
                Usuario
                    │
                    ▼
          Interfaz Streamlit
                    │
                    ▼
             LangGraph (Graph)
                    │
                    ▼
                Router
                    │
        ┌───────────┴───────────┐
        │                       │
  Saludos / Despedidas      Nodo RAG
                                │
                                ▼
                 History-Aware Retrieval
                                │
                                ▼
                         Retriever (FAISS)
                                │
                                ▼
                    Recuperación de contexto
                                │
                                ▼
                     Construcción del prompt
                                │
                                ▼
                        DeepSeek (LLM)
                                │
                                ▼
                    Generación de respuesta
                                │
                                ▼
                     Respuesta al usuario
```

### 1. Recepción de la consulta

El usuario realiza una pregunta desde la interfaz desarrollada con Streamlit.

La aplicación crea el estado inicial del agente (`AgentState`), incorporando la consulta, el historial de conversación, el retriever y el modelo de lenguaje.

---

### 2. Clasificación mediante el Router

La primera etapa del grafo corresponde al **Router**.

Su función es clasificar la intención de la consulta y decidir qué nodo deberá ejecutarse.

Actualmente el Router puede derivar la conversación hacia:

- Saludo.
- Agradecimiento.
- Despedida.
- Consulta documental (RAG).

Esta estrategia evita ejecutar búsquedas innecesarias cuando la respuesta puede generarse directamente.

---

### 3. Reescritura de la consulta

Cuando una consulta requiere acceder a la documentación, el flujo ingresa al nodo RAG.

Antes de realizar la búsqueda, el agente aplica la técnica **History-Aware Retrieval**, que reescribe la pregunta incorporando el contexto de la conversación previa.

**Ejemplo de interacción:**

> **Usuario:** ¿Atienden OSDE?  
> **Usuario:** ¿Y qué planes?

En este caso, la consulta que se envía al buscador se transforma en:

> **Consulta reescrita:** ¿Qué planes de OSDE atiende el Consultorio Odontológico DENT?

De este modo, el sistema mantiene conversaciones naturales y fluidas, sin perder el hilo contextual.

---

### 4. Recuperación de documentos

La consulta reescrita es enviada al **Retriever**, implementado sobre un índice vectorial **FAISS**.

Cada página del documento institucional es convertida previamente en embeddings mediante el modelo:

```text
models/gemini-embedding-2
```

El Retriever recupera únicamente los fragmentos más relevantes para responder la consulta.

---

### 5. Construcción del contexto

Los documentos recuperados se concatenan para construir el contexto que será enviado al modelo de lenguaje.

Además, el sistema identifica automáticamente las páginas utilizadas y las almacena como fuentes para ser mostradas al usuario.

---

### 6. Generación de la respuesta

El contexto recuperado, junto con el historial de conversación y los prompts del sistema, son enviados al modelo **DeepSeek**.

El modelo genera una respuesta fundamentada exclusivamente en la documentación disponible.

Si la información no se encuentra en la base documental, el asistente informa explícitamente que no dispone de esa información.

---

### 7. Presentación de resultados

Finalmente la aplicación muestra:

- La respuesta generada.
- Las páginas utilizadas como fuente.
- El tiempo de respuesta.
- Las métricas de ejecución (cuando el modo Debug está habilitado).

Todo este proceso ocurre de forma transparente para el usuario y normalmente se completa en pocos segundos.

## 🧩 Componentes principales

La aplicación se encuentra organizada en módulos independientes, cada uno con una responsabilidad específica.

### `streamlit_app.py`

Es el punto de entrada de la aplicación.

Se encarga de:

- Inicializar los recursos principales.
- Construir la interfaz de usuario.
- Administrar el estado de la conversación.
- Ejecutar el agente.
- Mostrar la respuesta y las fuentes recuperadas.

---

### `builder.py`

Define el flujo de ejecución del agente utilizando **LangGraph**.

En este módulo se:

- Registran los nodos.
- Se establece el nodo inicial.
- Se configuran las transiciones del grafo.
- Se compila el grafo para obtener el agente ejecutable.

---

### `router.py`

Clasifica la intención de la consulta recibida.

Su objetivo es decidir qué camino debe seguir la conversación.

Actualmente puede derivar la ejecución hacia:

- Saludos.
- Agradecimientos.
- Despedidas.
- Consultas documentales (RAG).

---

### `nodes.py`

Implementa los distintos nodos del grafo.

Cada nodo representa una etapa específica del procesamiento, por ejemplo:

- Saludo.
- Agradecimiento.
- Despedida.
- Recuperación de información mediante RAG.

---

### `classifier.py`

Utiliza el modelo de lenguaje para determinar la intención de la consulta del usuario.

Su resultado es utilizado por el Router para seleccionar el flujo más adecuado.

---

### `state.py`

Define el estado compartido (`AgentState`) que circula entre todos los nodos del grafo.

Contiene información como:

- Consulta del usuario.
- Historial de conversación.
- Ruta seleccionada.
- Contexto recuperado.
- Respuesta generada.
- Fuentes utilizadas.

---

### `factory.py`

Centraliza la creación del estado inicial del agente.

Permite construir un `AgentState` consistente antes de ejecutar el grafo.

---

### `history.py`

Implementa el mecanismo de **History-Aware Retrieval**, encargado de reescribir las consultas teniendo en cuenta el historial conversacional.

Gracias a este componente el asistente puede comprender preguntas dependientes del contexto.

---

### `prompts.py`

Contiene todos los prompts utilizados por el sistema.

Centralizar los prompts facilita su mantenimiento y evita tener texto distribuido por distintos módulos.

---

### `rag/loader.py`

Carga los documentos PDF y los transforma en objetos `Document` de LangChain, preservando su contenido y metadatos.

---

### `rag/splitter.py`

Divide el contenido de los documentos en fragmentos adecuados para el proceso de indexación y recuperación semántica.

---

### `rag/embeddings.py`

Genera los embeddings utilizando el modelo configurado en Google AI.

Estos embeddings representan cada fragmento del documento en el espacio vectorial.

---

### `rag/vector_store.py`

Construye el índice vectorial utilizando **FAISS**.

Cada vez que cambia la base documental, este módulo reconstruye automáticamente el índice para mantener la información actualizada.

---

### `rag/retriever.py`

Configura el Retriever encargado de recuperar los documentos más relevantes mediante búsqueda semántica.

Actualmente utiliza la estrategia **Maximum Marginal Relevance (MMR)** para mejorar la diversidad de los resultados.

---

### `rag/llm.py`

Inicializa el modelo de lenguaje utilizado por el agente.

Actualmente el proyecto emplea **DeepSeek**, aunque la arquitectura permite incorporar otros proveedores compatibles.

---

### `ui/`

Agrupa todos los componentes reutilizables de la interfaz desarrollada con Streamlit.

Entre ellos se encuentran:

- Encabezado.
- Barra lateral.
- Chat.
- Estado del agente.
- Panel de depuración.
- Gestión de documentos.
- Visualización de fuentes.
- Métricas de conversación.

---

### `utils/`

Contiene utilidades compartidas por toda la aplicación.

Principalmente incluye:

- Configuración general.
- Variables de entorno.
- Funciones auxiliares relacionadas con la documentación.
