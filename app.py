import streamlit as st

# Configuración visual
st.set_page_config(page_title="Karen AI", layout="wide")

# Estilo CSS restaurado y limpio
st.markdown("""
    <style>
    /* Fondo total negro absoluto */
    .stApp {
        background-color: #000000;
    }
    
    /* Ocultar franja superior */
    header[data-testid="stHeader"] {
        background-color: transparent;
    }
    
    /* Sidebar fondo negro */
    [data-testid="stSidebar"] {
        background-color: #000000;
        border-right: 1px solid #222;
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
    
    /* Color de textos globales en blanco */
    h1, h2, h3, p, label {
        color: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)

# Barra lateral
st.sidebar.markdown("### 🕸️ SISTEMAS")
menu = st.sidebar.selectbox("Selecciona un protocolo", 
                            ["Dashboard", "Estudios", "Basket: Entrenamiento Intensivo"])

# --- Elemento visual central ---
st.markdown('<div class="jarvis-vibrar">🕸️</div>', unsafe_allow_html=True)
