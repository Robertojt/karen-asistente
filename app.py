import streamlit as st
import os
from groq import Groq

# Configuración de página
st.set_page_config(page_title="Dashboard", layout="wide")

# CSS para el estilo "Hackeado" y oscuro absoluto
st.markdown("""
    <style>
    /* Fondo negro absoluto en toda la app */
    .stApp { background-color: #000000 !important; }
    [data-testid="stSidebar"] { background-color: #000000 !important; border-right: 1px solid #333; }
    
    /* Ocultar elementos sobrantes */
    header { visibility: hidden !important; }
    
    /* Centrar telaraña */
    .spider-center { text-align: center; font-size: 150px; margin-top: 20px; }
    
    /* Estilo de la radio button (Dashboard) */
    div[role="radiogroup"] label { color: #ffffff !important; }
    </style>
    """, unsafe_allow_html=True)

# 1. Dashboard Lateral
with st.sidebar:
    st.markdown("<h2 style='color:white;'>Dashboard</h2>", unsafe_allow_html=True)
    opcion = st.radio("Selecciona:", ["Inicio", "Basketball", "Estudios"])

# 2. Área central (Telaraña siempre visible)
st.markdown('<div class="spider-center">🕸️</div>', unsafe_allow_html=True)
st.markdown(f"<h1 style='text-align:center; color:white;'>{opcion}</h1>", unsafe_allow_html=True)

# 3. Lógica de Chat (Integrada para que funcione en todas las pestañas)
client = Groq(api_key=os.environ["GROQ_API_KEY"])

if "messages" not in st.session_state: st.session_state.messages = []

# Mostrar mensajes
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input de usuario (siempre abajo)
if prompt := st.chat_input(f"Escribe algo para {opcion}..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)
    
    with st.chat_message("assistant"):
        try:
            chat_completion = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="llama-3.1-8b-instant",
            )
            response = chat_completion.choices[0].message.content
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
        except Exception as e:
            st.error(f"Error: {e}")
