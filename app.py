import streamlit as st
import time

# Configuración visual
st.set_page_config(page_title="Karen AI", layout="wide")

# Estilo CSS para fondo negro y vibración
st.markdown("""
    <style>
    /* Fondo negro */
    .stApp {
        background-color: #000000;
        color: white;
    }
    
    /* Animación vibración */
    @keyframes vibrar {
        0% { transform: scale(1); opacity: 0.8; }
        50% { transform: scale(1.1); opacity: 1; }
        100% { transform: scale(1); opacity: 0.8; }
    }
    .jarvis-vibrar {
        font-size: 150px; /* Telaraña más grande */
        animation: vibrar 2s infinite;
        text-align: center;
        margin-top: 100px;
    }
    </style>
""", unsafe_allow_html=True)

# Barra lateral de navegación
st.sidebar.header("📁 Módulos Activos")
menu = st.sidebar.selectbox("Selecciona una sección", 
                            ["Dashboard", "Estudios", "Basket: Entrenamiento Intensivo"])

# --- Lógica de la pantalla ---

if menu == "Dashboard":
    # Muestra solo la telaraña vibrando en modo Dashboard
    st.markdown('<div class="jarvis-vibrar">🕸️</div>', unsafe_allow_html=True)
    
    # Opcional: un pequeño botón que aparece solo al pasar el mouse o al hacer clic
    if st.button("Iniciar Sistema"):
        st.experimental_rerun()

elif menu == "Estudios":
    st.title("📚 Módulo de Estudios")
    st.write("Gestionando carga académica...")

elif menu == "Basket: Entrenamiento Intensivo":
    st.title("🏀 Módulo de Basket")
    st.write("Analizando rendimiento de tiro.")
