"""
Clasificador híbrido: usa reglas para casos triviales y LLM para casos complejos.
Reduce el consumo de tokens significativamente.
"""
import re
from langchain_core.language_models import BaseChatModel
from .prompts import ROUTER_PROMPT

# Palabras clave para detección rápida (sin LLM)
SALUDOS = {"hola", "buen", "buenos", "buenas", "qué tal", "cómo estás", "saludos", "hey", "buen día"}
AGRADECIMIENTOS = {"gracias", "muchas gracias", "mil gracias", "gracias por", "agradecido"}
DESPEDIDAS = {"chau", "adiós", "hasta luego", "hasta pronto", "nos vemos", "bye", "chao"}

def _detectar_por_palabras(texto: str) -> str | None:
    """
    Detecta saludo, agradecimiento o despedida por palabras clave.
    Devuelve la categoría o None si no se detecta.
    """
    texto_lower = texto.lower().strip()
    
    if any(p in texto_lower for p in SALUDOS):
        return "saludo"
    if any(p in texto_lower for p in AGRADECIMIENTOS):
        return "agradecimiento"
    if any(p in texto_lower for p in DESPEDIDAS):
        return "despedida"
    return None

def clasificar_consulta(question: str, llm: BaseChatModel) -> str:
    """
    Clasifica la consulta usando primero reglas simples, y si no,
    recurre al LLM para diferenciar entre rag y fuera_dominio.
    """
    # 1. Detección rápida por palabras clave
    categoria = _detectar_por_palabras(question)
    if categoria:
        return categoria

    # 2. Si no es trivial, usar el LLM para decidir entre rag / fuera_dominio
    prompt = ROUTER_PROMPT.format(question=question)
    respuesta = llm.invoke(prompt)

    # Limpiar respuesta
    categoria = respuesta.content.strip().lower()
    categoria = re.sub(r'[^\w\s]', '', categoria).strip()

    # Validar
    validas = {"rag", "fuera_dominio"}
    if categoria not in validas:
        categoria = "rag"  # fallback seguro

    return categoria