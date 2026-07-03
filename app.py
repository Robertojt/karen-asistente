import streamlit as st
import os
from groq import Groq

# Configuración de diseño
st.set_page_config(page_title="Dashboard", layout="wide")

# CSS para el "Hack" del modo oscuro total
st.markdown("""
    <style>
    /* Fondo oscuro absoluto */
    .stApp { background-color: #000000 !important; }
    
    /* Ocultar elementos predeterminados de Streamlit */
    header { visibility: hidden !important; }
    #MainMenu { visibility: hidden !important; }
    footer { visibility: hidden !important; }
    
    /* Estilo de la barra lateral */
    [data-testid="stSidebar"] { background-color: #000000 !important; border-right: 1px solid #333; }
    
    /* Estilo para que los tabs parezcan botones seleccionables */
    .stTabs [data-baseweb="tab-list"] { background-color: #111; }
    .stTabs [data-baseweb="tab"] { color: #888; }
    .stTabs [aria-selected="true"] { color: #fff !important; }
    </style>
    """, unsafe_allow_html=True)

# Dashboard Lateral
with st.sidebar:
    st.markdown("<h2 style='color:white;'>Dashboard</h2>", unsafe_allow_html=True)
    opcion = st.radio("Navegación:", ["Inicio", "Basketball", "Estudios"])

# Contenido Central
if opcion == "Inicio":
    st.markdown("<div style='text-align:center; font-size:300px;'>🕸️</div>", unsafe_allow_html=True)
else:
    st.title(opcion)
    
    # Lógica de Groq
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    if "messages" not in st.session_state: st.session_state.messages = []
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]): st.markdown(message["content"])
        
    if prompt := st.chat_input(f"Consulta sobre {opcion}..."):
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
