
import streamlit as st
from servicios.libros_servicio import LibrosServicio
from servicios.usuarios_servicio import UsuariosServicio
from servicios.prestamos_servicio import PrestamosServicio


st.title("Panel principal")

st.write(
    "Bienvenido al sistema de gestión de la Biblioteca de Alejandría."
)

st.divider()



# CONSULTAR INFORMACIÓN DE LA BASE DE DATOS

try:

    libros = LibrosServicio().listar_libros()

    usuarios = UsuariosServicio().listar_usuarios()

    prestamos = PrestamosServicio().listar_prestamos()


    # CALCULAR INDICADORES

    total_libros = len(libros)

    total_usuarios = len(usuarios)

    prestamos_activos = sum(
        1 for prestamo in prestamos
        if str(prestamo.get("Estado", "")).strip().lower() == "prestado"
    )

    devoluciones = sum(
        1 for prestamo in prestamos
        if str(prestamo.get("Estado", "")).strip().lower() == "devuelto"
    )


    # MOSTRAR INDICADORES

    st.subheader("Indicadores generales")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Libros registrados",
            total_libros
        )

    with col2:
        st.metric(
            "Usuarios registrados",
            total_usuarios
        )

    with col3:
        st.metric(
            "Préstamos activos",
            prestamos_activos
        )

    with col4:
        st.metric(
            "Devoluciones",
            devoluciones
        )

    st.divider()

    st.subheader("Información del sistema")

    st.success(
        "Conexión con SQL Server establecida. "
        "Los indicadores corresponden a los registros actuales."
    )

except Exception as error:

    st.error(
        f"No fue posible cargar los indicadores desde la base de datos: {error}"
    )
