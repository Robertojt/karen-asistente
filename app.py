import streamlit as st
import os
from groq import Groq

# Configuración de página - Estilo Oscuro
st.set_page_config(page_title="Karen Key", page_icon="🕸️", layout="wide")

# Estilos CSS para el look de "Dashboard"
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #00ff00; }
    .css-1d391kg { background-color: #0e1117; }
    h1 { text-align: center; color: #ff4b4b; font-family: 'Courier New', monospace; }
    .stChatMessage { border: 1px solid #333; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🕸️ KAREN KEY 🕸️")

# Inicializar Groq
client = Groq(api_key=os.environ["GROQ_API_KEY"])

if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar historial
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input del usuario
if prompt := st.chat_input("¿Qué necesitas, Isaac?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # Llamada al modelo Llama 3.1
            chat_completion = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="llama-3.1-8b-instant",
            )
            response = chat_completion.choices[0].message.content
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
        except Exception as e:
            st.error(f"Error técnico: {e}")
