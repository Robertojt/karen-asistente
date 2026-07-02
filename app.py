import streamlit as st

# Configuración visual
st.set_page_config(page_title="Karen AI", layout="wide")

# Estilo CSS unificado
st.markdown("""
    <style>
    /* Fondo negro */
    .stApp {
        background-color: #000000;
    }
    
    /* Animación vibración */
    @keyframes vibrar {
        0% { transform: scale(1); opacity: 0.8; }
        50% { transform: scale(1.1); opacity: 1; }
        100% { transform: scale(1); opacity: 0.8; }
    }
    
    /* Clase de la telaraña: Bloqueamos selección y clicks */
    .jarvis-vibrar {
        font-size: 150px;
        animation: vibrar 2s infinite;
        text-align: center;
        margin-top: 50px;
        user-select: none;         /* Impide que se seleccione */
        -webkit-user-select: none; /* Para navegadores basados en WebKit */
        pointer-events: none;      /* Ignora el mouse sobre ella */
    }
    
    /* Color de textos */
    h2, p {
        color: #ffffff !important;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Barra lateral
st.sidebar.header("📁 Módulos Activos")
menu = st.sidebar.selectbox("Selecciona una sección", 
                            ["Dashboard", "Estudios", "Basket: Entrenamiento Intensivo"])

# --- Elemento visual permanente ---
st.markdown('<div class="jarvis-vibrar">🕸️</div>', unsafe_allow_html=True)

# Lógica de contenido
if menu == "Dashboard":
    st.markdown("<h2>SISTEMA EN REPOSO</h2>", unsafe_allow_html=True)
elif menu == "Estudios":
    st.markdown("<h2>MÓDULO DE ESTUDIOS</h2>", unsafe_allow_html=True)
elif menu == "Basket: Entrenamiento Intensivo":
    st.markdown("<h2>MÓDULO DE BASKET</h2>", unsafe_allow_html=True)
