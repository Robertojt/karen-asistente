st.markdown("""
    <style>
    /* Fondo principal y sidebar en negro absoluto */
    .stApp, [data-testid="stSidebar"] { background-color: #000000 !important; }
    
    /* Ocultar elementos decorativos */
    header, #MainMenu, footer { visibility: hidden !important; }
    
    /* HACK PARA EL CHAT INPUT: Forzamos el fondo del contenedor a negro */
    [data-testid="stChatInputContainer"] {
        background-color: #000000 !important;
        border-top: 1px solid #333 !important;
    }
    
    /* El input mismo también en negro */
    [data-testid="stChatInput"] {
        background-color: #000000 !important;
        color: white !important;
    }
    
    /* Ajuste de colores para que el texto sea blanco */
    [data-testid="stSidebar"] *, .stMarkdown, p { color: #ffffff !important; }
    
    .spider-big { display: flex; justify-content: center; height: 60vh; font-size: 300px; align-items: center; }
    .spider-small { text-align: center; font-size: 100px; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)
