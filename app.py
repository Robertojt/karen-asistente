import streamlit as st

# Configuración inicial
st.set_page_config(page_title="Karen AI", layout="wide")

# Título y presentación
st.title("🕸️ Karen: Asistente Personal")
st.subheader("Estado: Sistemas activos")

# Menú lateral para organizar funciones
menu = st.sidebar.selectbox("Selecciona un módulo", ["Inicio", "Basket", "Entrenamiento"])

if menu == "Inicio":
    st.write("Hola, Isaac. Estoy lista para asistirte. ¿Qué protocolo ejecutamos hoy?")
    if st.button("Autodiagnóstico"):
        st.write("Sistemas al 100%. Memoria y procesadores optimizados.")

elif menu == "Basket":
    st.write("### Análisis de Dribles")
    st.write("Función en desarrollo. Aquí pondremos tus estadísticas.")

elif menu == "Entrenamiento":
    st.write("### Plan de Entrenamiento")
    st.write("Aquí registraremos tus rutinas de Taekwondo y físico.")
