from loader import leer_pdf, cantidad_paginas


RUTA_PDF = "D:/proyectos/Ingenieria_de_Agentes_y_Automatizacion_con_IA/data/DENT_Manual_Institucional.pdf"


print("=" * 50)
print("LECTURA DEL PDF")
print("=" * 50)

print(f"\nCantidad de páginas: {cantidad_paginas(RUTA_PDF)}")

paginas = leer_pdf(RUTA_PDF)

print("\nPrimeras dos páginas:\n")

for i, pagina in enumerate(paginas[:2], start=1):
    print("-" * 50)
    print(f"Página {i}\n")
    print(pagina[:1000])   # solo muestra los primeros 1000 caracteres