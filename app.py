import streamlit as st
import google.generativeai as genai

# Configuración básica
st.set_page_config(page_title="Karen AI", layout="wide")

# Configurar API con la llave de los Secrets
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# CSS para tu diseño
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    [data-testid="stSidebar"] { background-color: #000000; border-right: none !important; }
    h1, h2, h3, p, label { color: #ffffff !important; }
    .jarvis-vibrar { font-size: 150px; text-align: center; margin-top: 50px; user-select: none; }
    </style>
""", unsafe_allow_html=True)

# Personalidades
system_prompts = {
    "Dashboard": "Eres Karen, un sistema de asistencia general, eficiente y profesional.",
    "Estudios": "Eres Karen, una experta académica. Explicas conceptos complejos de forma clara, didáctica y estructurada.",
    "Basket: Entrenamiento Intensivo": "Eres Karen, Coach de baloncesto. Tu enfoque es técnico, táctico y de alto rendimiento."
}

# Sidebar
st.sidebar.markdown("### 🕸️ SISTEMAS")
menu = st.sidebar.selectbox("Selecciona un protocolo", list(system_prompts.keys()))
st.markdown('<div class="jarvis-vibrar">🕸️</div>', unsafe_allow_html=True)

# Lógica del Chat
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("¿Qué necesitas, Isaac?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # MODELO ESTÁNDAR COMPATIBLE
    model = genai.GenerativeModel('gemini-1.0-pro')
    
    instruccion = system_prompts.get(menu, "Eres Karen.")
    full_prompt = f"{instruccion}\n\nPregunta: {prompt}"
    
    try:
        response = model.generate_content(full_prompt)
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"Error técnico: {e}. Si esto persiste, verifica que tu API Key sea correcta y tenga permisos en Google AI Studio.")
