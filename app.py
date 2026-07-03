st.markdown("""
    <style>
    /* Fondo oscuro absoluto */
    .stApp, [data-testid="stSidebar"] { background-color: #000000 !important; }
    
    /* HACEMOS EL INPUT MINIMALISTA */
    /* Eliminamos el fondo blanco y el tamaño gigante */
    [data-testid="stChatInputContainer"] {
        background-color: transparent !important;
        border: none !important;
        padding: 0 !important;
    }
    
    /* Dejamos solo la rayita de escritura */
    div[data-testid="stChatInput"] {
        background-color: #111111 !important;
        border: 1px solid #333 !important;
        border-radius: 5px !important;
        margin-bottom: 10px !important;
    }
    
    /* Ocultar elementos sobrantes */
    header, #MainMenu, footer { visibility: hidden !important; }
    [data-testid="stSidebar"] * { color: white !important; }
    
    .spider-center { display: flex; justify-content: center; font-size: 150px; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)
