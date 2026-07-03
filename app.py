import streamlit as st
import os
from groq import Groq

st.set_page_config(page_title="Dashboard", layout="wide")

st.markdown("""
    <style>
    .stApp, [data-testid="stSidebar"] { background-color: #000000 !important; }
    header, #MainMenu, footer { visibility: hidden !important; }
    
    [data-testid="stChatInputContainer"] {
        background-color: transparent !important;
        border: none !important;
        padding: 0 !important;
    }
    div[data-testid="stChatInput"] {
        background-color: #111111 !important;
        border: 1px solid #333 !important;
        border-radius: 5px !important;
        margin-bottom: 10px !important;
    }

    [data-testid="stSidebar"] * { color: white !important; }
    
    /* TELARAÑA MÁXIMA */
    .spider-max { 
        display: flex; 
        justify-content: center; 
        align-items: center; 
        height: 70vh; 
        font-size: 600px; 
        margin-top: -20px;
    }
    </style>
    """, unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## Dashboard")
    opcion = st.radio("Navegación:", ["Inicio", "Basketball", "Estudios"])

if "messages_basketball" not in st.session_state: st.session_state.messages_basketball = []
if "messages_estudios" not in st.session_state: st.session_state.messages_estudios = []

# Telaraña al máximo tamaño
st.markdown('<div class="spider-max">🕸️</div>', unsafe_allow_html=True)

if opcion != "Inicio":
    key = "messages_basketball" if opcion == "Basketball" else "messages_estudios"
    for message in st.session_state[key]:
        with st.chat_message(message["role"]): st.markdown(message["content"])
        
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
