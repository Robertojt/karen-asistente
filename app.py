import streamlit as st
import os
from groq import Groq

# Configuración inicial
st.set_page_config(page_title="Karen Key", page_icon="🕸️", layout="wide")

# CSS para el estilo oscuro total
st.markdown("""
    <style>
    /* Fondo general */
    .stApp { background-color: #000000; }
    
    /* Panel lateral (donde iría el dashboard) */
    [data-testid="stSidebar"] { background-color: #000000; border-right: 1px solid #333; }
    
    /* Encabezado */
    h1 { color: #ffffff; text-align: center; font-family: 'Arial'; }
    
    /* Telaraña central */
    .spider-web {
        display: flex;
        justify-content: center;
        margin-top: 50px;
        font-size: 200px;
    }
    
    /* Ajuste de los mensajes */
    .stChatMessage { background-color: #111111; border: 1px solid #222; }
    </style>
    """, unsafe_allow_html=True)

# Dashboard lateral
with st.sidebar:
    st.title("🕸️ Dashboard")
    st.write("---")
    st.subheader("🏀 Basketball")
    st.subheader("📚 Estudios")
    st.write("---")

# Contenido Principal
st.markdown('<div class="spider-web">🕸️</div>', unsafe_allow_html=True)
st.title("KAREN KEY")

# Inicializar Groq
client = Groq(api_key=os.environ["GROQ_API_KEY"])

if "messages" not in st.session_state:
    st.session_state.messages = []

# Historial
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input
if prompt := st.chat_input("¿Qué necesitas, Isaac?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

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
