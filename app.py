import streamlit as st
import google.generativeai as genai

# 1. Configuración de página
st.set_page_config(page_title="Karen AI", layout="wide")

# Conexión con tu llave guardada en los Secrets de Streamlit
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# 2. Estilos CSS
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    [data-testid="stSidebar"] { background-color: #000000; border-right: none !important; }
    h1, h2, h3, p, label { color: #ffffff !important; }
    .jarvis-vibrar { font-size: 150px; text-align: center; margin-top: 50px; user-select: none; }
    </style>
""", unsafe_allow_html=True)

# 3. Personalidades
system_prompts = {
    "Dashboard": "Eres Karen, un sistema de asistencia general, eficiente y profesional.",
    "Estudios": "Eres Karen, una experta académica. Explicas conceptos complejos de forma clara, didáctica y estructurada.",
    "Basket: Entrenamiento Intensivo": "Eres Karen, Coach de baloncesto. Tu enfoque es técnico, táctico y de alto rendimiento."
}

# 4. Sidebar
st.sidebar.markdown("### 🕸️ SISTEMAS")
menu = st.sidebar.selectbox("Selecciona un protocolo", list(system_prompts.keys()))
st.markdown('<div class="jarvis-vibrar">🕸️</div>', unsafe_allow_html=True)

# 5. Lógica del Chat
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("¿Qué necesitas, Isaac?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # El modelo corregido (gemini-1.5-flash)
    model = genai.GenerativeModel('gemini-1.5-flash')
    instruccion = system_prompts.get(menu, "Eres Karen, una asistente útil.")
    full_prompt = f"{instruccion}\n\nPregunta: {prompt}"
    
    try:
        response = model.generate_content(full_prompt)
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"Error al conectar con el cerebro: {e}")
