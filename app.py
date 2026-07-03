import streamlit as st
import os
from groq import Groq

# Configuración de página
st.set_page_config(page_title="Dashboard", layout="wide")

# CSS para el estilo hacker y forzar negro en todo
st.markdown("""
    <style>
    /* Fondo negro absoluto */
    .stApp, [data-testid="stSidebar"] { background-color: #000000 !important; }
    
    /* Ocultar elementos predeterminados */
    header, #MainMenu, footer { visibility: hidden !important; }
    
    /* El contenedor del chat input: FORZADO A NEGRO */
    [data-testid="stChatInputContainer"] {
        background-color: #000000 !important;
        border-top: 1px solid #333 !important;
    }
    
    /* Input interior */
    textarea { background-color: #000000 !important; color: white !important; }
    
    /* Sidebar y texto */
    [data-testid="stSidebar"] * { color: white !important; }
    
    .spider-center { display: flex; justify-content: center; font-size: 150px; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

# Dashboard Lateral
with st.sidebar:
    st.markdown("## Dashboard")
    opcion = st.radio("Navegación:", ["Inicio", "Basketball", "Estudios"])

# Lógica de estados independientes
if "messages_basketball" not in st.session_state: st.session_state.messages_basketball = []
if "messages_estudios" not in st.session_state: st.session_state.messages_estudios = []

# Área central
st.markdown('<div class="spider-center">🕸️</div>', unsafe_allow_html=True)

if opcion != "Inicio":
    key = "messages_basketball" if opcion == "Basketball" else "messages_estudios"
    
    for message in st.session_state[key]:
        with st.chat_message(message["role"]): st.markdown(message["content"])
        
    if prompt := st.chat_input("Escribe aquí..."):
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
                st.error("Error de conexión con Groq")
