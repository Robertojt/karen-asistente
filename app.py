import streamlit as st
import google.generativeai as genai
import os

# Configuración de la API Key
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Usamos el modelo 1.0-pro, que es el más básico y compatible
model = genai.GenerativeModel('gemini-1.0-pro')

st.set_page_config(page_title="Karen AI", page_icon="🕸️")
st.title("Karen AI 🕸️")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar historial
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Entrada del usuario
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
            # Mostramos el error técnico exacto para diagnosticar
            st.error(f"Error técnico exacto: {type(e).__name__} - {e}")
