import streamlit as st
import os
from groq import Groq

# Configuración de diseño
st.set_page_config(page_title="Dashboard", layout="wide")

# CSS para el estilo "Hacker" oscuro
st.markdown("""
    <style>
    .stApp, [data-testid="stSidebar"] { background-color: #000000 !important; }
    header, #MainMenu, footer { visibility: hidden !important; }
    .stChatInput { background-color: #000000 !important; }
    .spider-big { display: flex; justify-content: center; height: 60vh; font-size: 300px; align-items: center; }
    .spider-small { text-align: center; font-size: 100px; margin-bottom: 20px; }
    [data-testid="stSidebar"] * { color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# 1. Dashboard Lateral
with st.sidebar:
    st.markdown("## Dashboard")
    opcion = st.radio("Navegación:", ["Inicio", "Basketball", "Estudios"])

# 2. Inicialización de estados independientes
if "messages_basketball" not in st.session_state: st.session_state.messages_basketball = []
if "messages_estudios" not in st.session_state: st.session_state.messages_estudios = []

# 3. Lógica según la pestaña
if opcion == "Inicio":
    st.markdown('<div class="spider-big">🕸️</div>', unsafe_allow_html=True)

else:
    # Definir qué lista de mensajes usar
    key = "messages_basketball" if opcion == "Basketball" else "messages_estudios"
    st.markdown('<div class="spider-small">🕸️</div>', unsafe_allow_html=True)
    
    # Mostrar historial específico
    for message in st.session_state[key]:
        with st.chat_message(message["role"]): st.markdown(message["content"])
        
    # Input de usuario
    if prompt := st.chat_input(f"Consultando {opcion}..."):
        st.session_state[key].append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        
        with st.chat_message("assistant"):
            try:
                client = Groq(api_key=os.environ["GROQ_API_KEY"])
                chat_completion = client.chat.completions.create(
                    messages=[{"role": "user", "content": prompt}],
                    model="llama-3.1-8b-instant",
                )
                response = chat_completion.choices[0].message.content
                st.markdown(response)
                st.session_state[key].append({"role": "assistant", "content": response})
            except Exception as e:
                st.error("Error técnico")
