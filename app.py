import streamlit as st
import os
from groq import Groq

# Configuración de página
st.set_page_config(page_title="Dashboard", layout="wide")

# CSS "Hacker Total"
st.markdown("""
    <style>
    /* Fondo absoluto para toda la aplicación */
    .stApp, [data-testid="stSidebar"], .stChatInputContainer {
        background-color: #000000 !important;
    }
    
    /* Forzar fondo negro en el contenedor de entrada y eliminar bordes blancos */
    div[data-testid="stChatInputContainer"] {
        background-color: #000000 !important;
        border: 1px solid #333 !important;
        border-radius: 5px !important;
    }
    
    /* Input de texto forzado a negro */
    [data-testid="stChatInput"] {
        background-color: #000000 !important;
        color: white !important;
    }

    /* Ocultar elementos predeterminados */
    header, #MainMenu, footer { visibility: hidden !important; }

    /* Estilo del sidebar */
    [data-testid="stSidebar"] * { color: white !important; }
    
    /* Telaraña centrada */
    .spider-center { display: flex; justify-content: center; font-size: 150px; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

# Dashboard Lateral
with st.sidebar:
    st.markdown("## Dashboard")
    opcion = st.radio("Navegación:", ["Inicio", "Basketball", "Estudios"])

# Estados independientes
if "messages_basketball" not in st.session_state: st.session_state.messages_basketball = []
if "messages_estudios" not in st.session_state: st.session_state.messages_estudios = []

# Área central
st.markdown('<div class="spider-center">🕸️</div>', unsafe_allow_html=True)

if opcion != "Inicio":
    key = "messages_basketball" if opcion == "Basketball" else "messages_estudios"
    
    # Historial (también forzado a oscuro)
    for message in st.session_state[key]:
        with st.chat_message(message["role"]): st.markdown(message["content"])
        
    # Input de usuario
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
                st.error("Error de conexión")
