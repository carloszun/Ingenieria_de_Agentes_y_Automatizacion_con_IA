"""
Módulo de configuración centralizada.

Carga variables de entorno desde .env y define rutas, modelos y parámetros
utilizados en todo el proyecto.
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Cargar variables de entorno UNA SOLA VEZ al inicio
load_dotenv()

# Directorio raíz del proyecto (dos niveles arriba de este archivo)
BASE_DIR = Path(__file__).resolve().parent.parent

# =============================================================================
# RUTAS DE ARCHIVOS
# =============================================================================
RUTA_PDF = BASE_DIR / "data" / "DENT_Manual_Institucional.pdf"

# =============================================================================
# PARÁMETROS DE CHUNKING (no se usa actualmente, se mantiene por escalabilidad)
# =============================================================================
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# =============================================================================
# CONFIGURACIÓN DE MODELOS - EMBEDDINGS (Gemini)
# =============================================================================
EMBEDDING_MODEL = "models/gemini-embedding-2"

# =============================================================================
# CONFIGURACIÓN DE CHAT - DEEPSEEK (ACTIVO)
# =============================================================================
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_CHAT_MODEL = "deepseek-chat"  # o "deepseek-reasoner"
DEEPSEEK_API_BASE = "https://api.deepseek.com/v1"

# =============================================================================
# CONFIGURACIÓN DE CHAT - GEMINI (COMENTADO - PARA REFERENCIA FUTURA)
# =============================================================================
# CHAT_MODEL_GEMINI = "gemini-2.0-flash"
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# =============================================================================
# FUNCIÓN PARA OBTENER LA CLAVE DE GEMINI (SOLO PARA EMBEDDINGS)
# =============================================================================
def get_google_api_key() -> str:
    """
    Devuelve la API key de Google para embeddings.
    """
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError(
            "❌ GOOGLE_API_KEY no definida en el archivo .env.\n"
            "Se necesita para generar embeddings."
        )
    return api_key