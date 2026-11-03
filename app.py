import streamlit as st

# Configuración general de la aplicación
st.set_page_config(
    page_title="Biblioteca de Alejandría",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título de la aplicación
st.title("📚 Biblioteca de Alejandría")

st.write(
    "Sistema de gestión y administración de una biblioteca."
)

# Navegación
paginas = {
    "Inicio": [],
    "Gestión": [
        st.Page("interfaz/paginas/autores.py", title="Autores"),
        st.Page("interfaz/paginas/editoriales.py", title="Editoriales"),
        st.Page("interfaz/paginas/libros.py", title="Libros"),
        st.Page("interfaz/paginas/usuarios.py", title="Usuarios"),
        st.Page("interfaz/paginas/prestamos.py", title="Préstamos"),
    ]
}

# Página principal
pagina_inicio = st.Page(
    "interfaz/inicio.py",
    title="Inicio",
    default=True
)

# Crear navegación
navegacion = st.navigation(
    [pagina_inicio] + paginas["Gestión"]
)

navegacion.run()