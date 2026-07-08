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
# CONFIGURACIÓN DE MODELOS
# =============================================================================
EMBEDDING_MODEL = "models/gemini-embedding-2"
CHAT_MODEL = "gemini-2.0-flash"


# =============================================================================
# CLAVE API CON RECARGA DINÁMICA
# =============================================================================
def get_google_api_key() -> str:
    """
    Devuelve la API key de Google leyéndola del archivo .env CADA VEZ.

    Esto permite cambiar la clave en el .env sin reiniciar el programa.
    Si la clave no está definida, lanza un error claro.
    """
    # Recargar el .env para obtener el valor actualizado
    load_dotenv(override=True)  # override=True fuerza la recarga
    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        raise ValueError(
            "❌ GOOGLE_API_KEY no definida en el archivo .env.\n"
            "Asegúrate de tener una línea como:\n"
            "GOOGLE_API_KEY=AIzaSyA..."
        )

    return api_key