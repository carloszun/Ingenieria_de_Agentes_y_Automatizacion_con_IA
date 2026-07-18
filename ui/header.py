"""
Módulo de interfaz de usuario: Header (logo, título, subtítulos).
"""
import streamlit as st
import base64
from pathlib import Path

def mostrar_header():
    """
    Muestra el logo y el título del asistente con alineación horizontal
    y centrado vertical, todo dentro de un único contenedor HTML.
    La imagen se incrusta en base64 para que funcione sin archivos estáticos.
    """

    # -------- Cargar la imagen y codificarla en base64 --------
    logo_path = Path("assets/logo_dent.png")
    if logo_path.exists():
        with open(logo_path, "rb") as f:
            image_data = f.read()
        image_base64 = base64.b64encode(image_data).decode("utf-8")
        img_tag = f'<img src="data:image/png;base64,{image_base64}" width="80" style="display: block;">'
    else:
        # Si no se encuentra la imagen, mostramos un placeholder
        img_tag = '<div style="width:80px; height:80px; background-color:#2d333b; border-radius:8px;"></div>'
#                    <p style="margin: 0; color: #999; font-size: 0.9rem;">Asistente Virtual basado en IA</p>
#                    <h1 style="margin: 0; font-size: 2.2rem; line-height: 1.2;">Consultorio Odontológico DENT</h1>
#                   <h3 style="margin: 0; font-size: 1.2rem; font-weight: normal; color: #666;">Asistente Virtual</h3>


    # -------- Generar el header en un solo bloque HTML --------
    st.markdown(
        f"""
        <div class="dent-header">
            <div style="display: flex; align-items: center; gap: 20px;">
                <div>
                    {img_tag}
                </div>
                <div>
                    <h1 style="margin: 0; font-size: 2.2rem; line-height: 1;">Consultorio Odontológico DENT</h1>
                    <h3 style="margin: -5px 0 0 0; font-size: 1.2rem; font-weight: normal; color: #666;">Asistente Virtual</h3>
                </div>
            </div>
        </div>
        <div class="header-spacer"></div>
        """,
        unsafe_allow_html=True,
    )