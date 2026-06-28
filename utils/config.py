# utils/config.py
from pathlib import Path

# Obtiene la raíz del proyecto (subimos 2 niveles desde utils/ hasta la raíz)
BASE_DIR = Path(__file__).resolve().parent.parent

# Ruta al PDF (relativa a la raíz)
RUTA_PDF = BASE_DIR / "data" / "DENT_Manual_Institucional.pdf"

# Parámetros de chunking
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200