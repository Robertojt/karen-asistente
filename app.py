import streamlit as st

# Configuración visual
st.set_page_config(page_title="Karen AI", layout="wide")

# Estilo CSS optimizado
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
    
    /* Sidebar: Fondo gris oscuro/negro para buena visibilidad */
    [data-testid="stSidebar"] {
        background-color: #121212;
        border-right: 1px solid #333;
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
    
    /* Aseguramos que los textos sean legibles */
    h1, h2, h3, p, label, div {
        color: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)

# Barra lateral
st.sidebar.markdown("### 🕸️ SISTEMAS")
menu = st.sidebar.selectbox("Selecciona un protocolo", 
                            ["Dashboard", "Estudios", "Basket: Entrenamiento Intensivo"])

# --- Elemento central ---
st.markdown('<div class="jarvis-vibrar">🕸️</div>', unsafe_allow_html=True)
