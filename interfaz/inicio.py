import streamlit as st

st.title("Panel principal")

st.write(
    "Bienvenido al sistema de gestión de la Biblioteca de Alejandría."
)

st.divider()

# Indicadores generales
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Libros registrados", 0)

with col2:
    st.metric("Usuarios registrados", 0)

with col3:
    st.metric("Préstamos activos", 0)

with col4:
    st.metric("Devoluciones", 0)

st.divider()

st.subheader("Información del sistema")

st.info(
    "Los indicadores se actualizarán cuando conectemos "
    "la interfaz con los servicios y la base de datos."
)