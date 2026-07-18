"""
Estilos CSS personalizados para la aplicación Streamlit.

Toda la personalización visual de la interfaz se concentra en este
archivo para mantener streamlit_app.py limpio y facilitar el
mantenimiento del proyecto.

Actualmente se personaliza:

- Ocultar elementos propios de Streamlit.
- Fijar el encabezado superior.
- Ajustar márgenes.
- Mejorar el aspecto general del chat.

En el futuro este módulo contendrá también:

- Colores corporativos.
- Botones.
- Sidebar.
- Animaciones.
- Responsive Design.
"""

import streamlit as st


def aplicar_estilos():
    """
    Aplica todos los estilos personalizados de la aplicación.
    """

    st.markdown(
        """
<style>

/* ==========================================================
   Ocultar elementos propios de Streamlit
========================================================== */

header[data-testid="stHeader"]{
    display:none;
}

footer{
    display:none;
}


/* ==========================================================
   Reducir espacio superior (lo manejamos con el spacer)
========================================================== */

.block-container{
    padding-top: 0 !important;  /* Eliminamos el padding para que el header fijo no se desplace */
}


/* ==========================================================
   Header fijo (ahora con position:fixed)
========================================================== */
.dent-header{
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    width: 100%;
    box-sizing: border-box;
    z-index: 999;
    background-color: #0e1117;
    padding: 15px 30rem 10px 30rem;  /* padding horizontal */
    border-bottom: 1px solid #2d333b;
}


/* ==========================================================
   Separador (lo usamos para dar espacio debajo del header)
========================================================== */

.header-spacer {
    height: 170px;  /* Ajusta este valor según la altura real de tu header */
}


/* ==========================================================
   Fuentes
========================================================== */

.small-font{
    font-size:0.85rem;
    color:#9aa0a6;
}


/* ==========================================================
   Chat
========================================================== */

[data-testid="stChatMessage"]{border-radius:12px;}


/* ==========================================================
   Caption
========================================================== */

.caption{
    font-size:0.80rem;
}

</style>
        """,
        unsafe_allow_html=True,
    )