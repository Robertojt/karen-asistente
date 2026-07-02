import streamlit as st

# Configuración visual
st.set_page_config(page_title="Karen AI", layout="wide")

# Estilo CSS final: Fondo negro, sin líneas, telaraña vibrando y tamaño ajustado
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
    
    /* Sidebar: Fondo negro y SIN borde derecho */
    [data-testid="stSidebar"] {
        background-color: #000000;
        border-right: none !important; 
    }
    
    /* Animación vibración */
    @keyframes vibrar {
        0% { transform: scale(1); opacity: 0.8; }
        50% { transform: scale(1.1); opacity: 1; }
        100% { transform: scale(1); opacity: 0.8; }
    }
    
    .jarvis-vibrar {
        font-size: 250px; /* Tamaño aumentado para mayor impacto */
        animation: vibrar 2s infinite;
        text-align: center;
        margin-top: 80px; /* Ajuste ligero de margen superior */
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
