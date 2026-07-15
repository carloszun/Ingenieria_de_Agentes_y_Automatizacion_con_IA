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
