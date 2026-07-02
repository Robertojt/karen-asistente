import streamlit as st
import google.generativeai as genai
import os

# Configuración de la API Key
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Usamos el modelo más actual y compatible
model = genai.GenerativeModel('gemini-1.5-flash')

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
            st.error("Karen está teniendo un problema técnico. Verifica tu API Key en los Settings de Streamlit.")
