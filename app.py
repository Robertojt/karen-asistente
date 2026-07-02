import streamlit as st

# Configuración visual
st.set_page_config(page_title="Karen AI", layout="wide")

# Estilo CSS optimizado
st.markdown("""
    <style>
    /* Fondo negro absoluto */
    .stApp {
        background-color: #000000;
    }
    
    /* Panel lateral oscuro y estético */
    [data-testid="stSidebar"] {
        background-color: #0d0d0d;
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
        margin-top: 50px;
        user-select: none;
        pointer-events: none;
    }
    
    /* Estilo para los selectores (azul/blanco fosforescente al tocar) */
    .stSelectbox div[data-baseweb="select"] {
        border: 1px solid #00d4ff !important;
        color: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)

# Barra lateral
st.sidebar.markdown("### 📁 SISTEMAS")
menu = st.sidebar.selectbox("Selecciona un protocolo", 
                            ["Dashboard", "Estudios", "Basket: Entrenamiento Intensivo"])

# --- Interfaz Principal ---
# La telaraña se mantiene siempre visible
st.markdown('<div class="jarvis-vibrar">🕸️</div>', unsafe_allow_html=True)

# Lógica de contenido minimalista
# Aquí no pusimos texto debajo, para que la pantalla quede limpia
if menu == "Dashboard":
    pass
elif menu == "Estudios":
    # Solo mostramos información si es estrictamente necesario en el futuro
    pass
elif menu == "Basket: Entrenamiento Intensivo":
    pass)
