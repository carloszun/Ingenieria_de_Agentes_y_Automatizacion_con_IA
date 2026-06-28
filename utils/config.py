from pathlib import Path
import os

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

RUTA_PDF = BASE_DIR / "data" / "DENT_Manual_Institucional.pdf"

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

EMBEDDING_MODEL = "gemini-embedding-001"

LLM_MODEL = "gemini-2.5-flash-lite"