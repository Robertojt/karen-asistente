import streamlit as st
import os
from groq import Groq

# Configuración de diseño
st.set_page_config(page_title="Dashboard", layout="wide")

# CSS para el "Hack" total: Fondo, chat y todo en negro
st.markdown("""
    <style>
    /* Fondo principal y sidebar en negro absoluto */
    .stApp, [data-testid="stSidebar"] { background-color: #000000 !important; }
    
    /* Ocultar encabezados predeterminados y decoraciones */
    header, #MainMenu, footer { visibility: hidden !important; }
    
    /* Caja de chat en negro con texto blanco */
    [data-testid="stChatMessage"] { background-color: #000000 !important; border: 1px solid #333 !important; }
    
    /* Input de chat estilizado */
    .stChatInput { background-color: #000000 !important; }
    
    /* Telaraña central gigante */
    .spider-big { 
        display: flex; justify-content: center; align-items: center; 
        height: 60vh; font-size: 300px; 
    }
    
    /* Color de texto en el sidebar */
    [data-testid="stSidebar"] * { color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# Dashboard Lateral
with st.sidebar:
    st.markdown("## Dashboard")
    opcion = st.radio("Navegación:", ["Inicio", "Basketball", "Estudios"])

# Contenido Central
if opcion == "Inicio":
    st.markdown('<div class="spider-big">🕸️</div>', unsafe_allow_html=True)
else:
    # Telaraña un poco más pequeña al entrar en pestañas, pero centrada
    st.markdown('<div style="text-align:center; font-size:100px;">🕸️</div>', unsafe_allow_html=True)
    
    # Lógica de Groq
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    if "messages" not in st.session_state: st.session_state.messages = []
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]): st.markdown(message["content"])
        
    if prompt := st.chat_input("..."):
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
                st.error("Error técnico")
