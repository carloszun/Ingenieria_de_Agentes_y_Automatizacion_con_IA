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
   Reducir espacio superior
========================================================== */

.block-container{
    padding-top:1.2rem;
}


/* ==========================================================
   Header fijo
========================================================== */

.dent-header{

    position:sticky;

    top:0;

    z-index:999;

    background-color:#0e1117;

    padding-top:15px;

    padding-bottom:10px;

}


/* ==========================================================
   Separador
========================================================== */

hr{

    margin-top:10px;

    margin-bottom:20px;

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

[data-testid="stChatMessage"]{

    border-radius:12px;

}


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