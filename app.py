import streamlit as st

# Configuración visual
st.set_page_config(page_title="Karen AI", layout="wide")

# Estilo CSS para un look "Full Black" y estético
st.markdown("""
    <style>
    /* Fondo total negro */
    .stApp {
        background-color: #000000;
    }
    
    /* Ocultar franja blanca superior */
    header[data-testid="stHeader"] {
        background-color: transparent;
    }
    
    /* Sidebar: Fondo negro */
    [data-testid="stSidebar"] {
        background-color: #000000;
        border-right: 1px solid #222;
    }
    
    /* Estética del menú desplegable (Selectbox) */
    .stSelectbox div[data-baseweb="select"] {
        background-color: #000000 !important;
        color: #ffffff !important;
        border: 1px solid #ffffff !important;
    }
    
    /* Fuerza el color del texto dentro del menú */
    div[role="listbox"] {
        background-color: #000000 !important;
        color: #ffffff !important;
    }
    
    /* Animación vibración */
    @keyframes vibrar {
        0% { transform: scale(1); opacity: 0.8; }
        50% { transform: scale(1.1); opacity: 1; }
        100% { transform: scale(1); opacity: 0.8; }
    }
    
    .jarvis-vibrar {
        font-size: 150px;
        animation: vibrar 2s infinite;
        text-align: center;
        margin-top: 100px;
        user-select: none;
        pointer-events: none;
    }
    
    /* Texto estético general */
    h1, h2, h3, p, label, div {
        color: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)

# Barra lateral estilizada
st.sidebar.markdown("### 🕸️ SISTEMAS")
st.sidebar.markdown("---") # Línea divisoria estética
menu = st.sidebar.selectbox("Selecciona un protocolo", 
                            ["Dashboard", "Estudios", "Basket: Entrenamiento Intensivo"])

# --- Elemento visual central ---
st.markdown('<div class="jarvis-vibrar">🕸️</div>', unsafe_allow_html=True)
