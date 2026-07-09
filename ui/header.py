"""
Módulo de interfaz de usuario: Header (logo, título, subtítulos).
"""
# app/ui/header.py
import streamlit as st

def mostrar_header():
    """
    Muestra el logo y el título del asistente con alineación horizontal
    y centrado vertical.
    """
    # CSS para centrar verticalmente el contenido de la columna derecha
    st.markdown(
        """
        <style>
        .header-col {
            display: flex;
            flex-direction: column;
            justify-content: center;
            height: 100%;
            padding-left: 0px;
        }
        .header-col h1 {
            margin: 0;
            padding: 0;
            font-size: 2.2rem;
            line-height: 1.2;
        }
        .header-col h3 {
            margin: 0;
            padding: 0;
            font-size: 1.2rem;
            color: #666;
            font-weight: normal;
        }
        .header-col p {
            margin: 0;
            padding: 0;
            color: #999;
            font-size: 0.9rem;
        }
        /* Asegura que la columna izquierda también centre la imagen */
        .image-col {
            display: flex;
            align-items: center;
            height: 100%;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Columnas: logo más pequeño (1 parte), texto más ancho (4 partes)
    col1, col2 = st.columns([1, 4])

    with col1:
        # Aplicamos clase para centrar la imagen verticalmente
        st.markdown('<div class="image-col">', unsafe_allow_html=True)
        st.image("assets/logo_dent.png", width=80)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        # Contenedor con clase para centrar verticalmente
        st.markdown(
            """
            <div class="header-col">
                <h1>Consultorio Odontológico DENT</h1>
                <h3>Asistente Virtual</h3>
                <p>Asistente Virtual basado en IA</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("---")  # Línea separadora