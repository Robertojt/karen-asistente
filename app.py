import streamlit as st
import time

# Configuración visual
st.set_page_config(page_title="Karen AI - Central de Mando", layout="wide")

# Estilo CSS para el efecto "Vibración Jarvis"
st.markdown("""
    <style>
    @keyframes vibrar {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    .jarvis-vibrar {
        font-size: 50px;
        animation: vibrar 1.5s infinite;
        display: inline-block;
    }
    </style>
""", unsafe_allow_html=True)

# Cabecera tipo Jarvis con el efecto visual
st.markdown('<div class="jarvis-vibrar">🕸️</div>', unsafe_allow_html=True)
st.title("KAREN: SISTEMA TÁCTICO DE ALTO RENDIMIENTO")
st.markdown("---")

# Barra lateral de navegación
st.sidebar.header("📁 Módulos Activos")
menu = st.sidebar.selectbox("Selecciona una sección", 
                            ["Dashboard", "Estudios", "Basket: Entrenamiento Intensivo"])

# --- Lógica ---
if menu == "Dashboard":
    st.subheader("Estado de Sistemas: Enfoque Total")
    if st.button("Iniciar Protocolo de Concentración"):
        with st.spinner("Sincronizando red neuronal..."):
            time.sleep(2)
        st.success("Sistemas conectados. Isaac, la telaraña está activa.")

elif menu == "Estudios":
    st.subheader("📚 Módulo de Estudios")
    st.write("Gestionando carga académica...")

elif menu == "Basket: Entrenamiento Intensivo":
    st.subheader("🏀 Módulo de Basket: Enfoque Profesional")
    st.write("Analizando rendimiento de tiro y movilidad.")
