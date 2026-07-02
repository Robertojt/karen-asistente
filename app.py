import streamlit as st
import google.generativeai as genai
import os

# Configuración de la API Key
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Configuración del modelo (Cambiado a gemini-pro)
model = genai.GenerativeModel('gemini-pro')

st.title("Karen AI")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("¿Qué necesitas, Isaac?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Error técnico: {e}")
