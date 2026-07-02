import streamlit as st
import google.generativeai as genai

# 1. Configuración inicial
st.set_page_config(page_title="Karen AI", layout="wide")

# Conexión con tu llave guardada en Secrets
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# 2. Estilos CSS (Telaraña grande y fondo negro)
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    [data-testid="stSidebar"] { background-color: #000000; border-right: none !important; }
    @keyframes vibrar {
        0% { transform: scale(1); opacity: 0.8; }
        50% { transform: scale(1.1); opacity: 1; }
        100% { transform: scale(1); opacity: 0.8; }
    }
    .jarvis-vibrar {
        font-size: 250px; 
        animation: vibrar 2s infinite;
        text-align: center;
        margin-top: 80px;
        user-select: none;
        pointer-events: none;
    }
    h1, h2, h3, p, label { color: #ffffff !important; }
    </style>
""", unsafe_allow_html=True)

# 3. Definición de personalidades
system_prompts = {
    "Dashboard": "Eres Karen, un sistema de asistencia general, eficiente y profesional.",
    "Estudios": "Eres Karen, una experta académica. Tu prioridad es explicar conceptos complejos de forma clara, didáctica y estructurada. Sabes de todo.",
    "Basket: Entrenamiento Intensivo": "Eres Karen, Coach táctica de baloncesto. Tu enfoque es técnico, competitivo y analítico. Priorizas la estrategia, el juego de pies, la táctica y el rendimiento físico de élite."
}

# 4. Sidebar y Selección
st.sidebar.markdown("### 🕸️ SISTEMAS")
menu = st.sidebar.selectbox("Selecciona un protocolo", list(system_prompts.keys()))

# Elemento visual
st.markdown('<div class="jarvis-vibrar">🕸️</div>', unsafe_allow_html=True)

# 5. Lógica del Chat
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("¿Qué necesitas, Isaac?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # El modelo cambia su "cerebro" según el menú
    model = genai.GenerativeModel('gemini-pro')
    instruccion = system_prompts[menu]
    full_prompt = f"{instruccion}\n\nPregunta: {prompt}"
    
    response = model.generate_content(full_prompt)
    
    with st.chat_message("assistant"):
        st.markdown(response.text)
    st.session_state.messages.append({"role": "assistant", "content": response.text})
