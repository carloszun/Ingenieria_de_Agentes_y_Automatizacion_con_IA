"""
Helpers para el manejo de nombres de documentos.
"""

def nombre_documento(source: str) -> str:
    """
    Devuelve un nombre amigable para el documento según el nombre del archivo.

    Args:
        source (str): Nombre original del archivo (ej. "DENT_Manual_Institucional.pdf")

    Returns:
        str: Nombre legible para mostrar al usuario.
    """
    nombres = {
        "DENT_Manual_Institucional.pdf": "Manual Institucional DENT",
    }
    return nombres.get(source, source)  # Si no está en el diccionario, devuelve el original