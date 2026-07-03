import streamlit as st
import os
from groq import Groq

# Configuración de diseño
st.set_page_config(page_title="Dashboard", layout="wide")

# CSS para el estilo "Hacker" y la telaraña gigante
st.markdown("""
    <style>
    /* Fondo negro absoluto en todo */
    .stApp, [data-testid="stSidebar"] { background-color: #000000 !important; }
    
    /* Ocultar elementos predeterminados */
    header, #MainMenu, footer { visibility: hidden !important; }
    
    /* Input de chat: minimalista y discreto */
    [data-testid="stChatInputContainer"] {
        background-color: transparent !important;
        border: none !important;
        padding: 0 !important;
    }
    div[data-testid="stChatInput"] {
        background-color: #111111 !important;
        border: 1px solid #333 !important;
        border-radius: 5px !important;
    }

    /* Sidebar y texto blanco */
    [data-testid="stSidebar"] *, .stMarkdown, p { color: #ffffff !important; }
    
    /* TELARAÑA GIGANTE CENTRAL */
    .spider-super-big { 
        display: flex; 
        justify-content: center; 
        align-items: center; 
        height: 60vh; 
        font-size: 400px; 
    }
    </style>
    """, unsafe_allow_html=True)

# Dashboard Lateral
with st.sidebar:
    st.markdown("## Dashboard")
    opcion = st.radio("Navegación:", ["Inicio", "Basketball", "Estudios"])

# Estados independientes para cada chat
if "messages_basketball" not in st.session_state: st.session_state.messages_basketball = []
if "messages_estudios" not in st.session_state: st.session_state.messages_estudios = []

# Área central con la telaraña gigante
st.markdown('<div class="spider-super-big">🕸️</div>', unsafe_allow_html=True)

if opcion != "Inicio":
    key = "messages_basketball" if opcion == "Basketball" else "messages_estudios"
    
    # Historial de mensajes
    for message in st.session_state[key]:
        with st.chat_message(message["role"]): st.markdown(message["content"])
        
    # Input de chat
    if prompt := st.chat_input("..."):
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
