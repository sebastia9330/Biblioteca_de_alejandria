import streamlit as st
import pandas as pd
from datetime import date, timedelta

from servicios.prestamos_servicio import PrestamosServicio
from servicios.usuarios_servicio import UsuariosServicio
from servicios.libros_servicio import LibrosServicio



# SERVICIOS

prestamos_servicio = PrestamosServicio()
usuarios_servicio = UsuariosServicio()
libros_servicio = LibrosServicio()

st.title("Gestión de préstamos")
st.write("Administra los préstamos y las devoluciones de la biblioteca.")
st.divider()



# CARGA DE INFORMACIÓN

try:
    prestamos = prestamos_servicio.listar_prestamos()
    usuarios = usuarios_servicio.listar_usuarios()
    libros = libros_servicio.listar_libros()

except Exception as error:
    st.error(f"No fue posible cargar la información: {error}")
    st.stop()


# Los usuarios se devuelven con claves en mayúsculas.
usuarios_activos = {
    usuario["UsuarioID"]: usuario
    for usuario in usuarios
    if usuario["Activo"]
}

# Los libros se devuelven con claves en minúsculas.
libros_disponibles = {
    libro["libro_id"]: libro
    for libro in libros
    if libro["cantidad_disponible"] > 0
}

prestamos_activos = {
    prestamo["PrestamoID"]: prestamo
    for prestamo in prestamos
    if prestamo["Estado"] == "Prestado"
}


def mostrar_usuario(usuario_id):
    usuario = usuarios_activos[usuario_id]
    return (
        f'{usuario["Nombres"]} {usuario["Apellidos"]} '
        f'- Documento: {usuario["Documento"]}'
    )


def mostrar_libro(libro_id):
    libro = libros_disponibles[libro_id]
    return (
        f'{libro["titulo"]} '
        f'- Disponibles: {libro["cantidad_disponible"]}'
    )


def mostrar_prestamo(prestamo_id):
    prestamo = prestamos_activos[prestamo_id]
    return (
        f'{prestamo["NombreUsuario"]} '
        f'{prestamo["ApellidoUsuario"]} - '
        f'{prestamo["TituloLibro"]} '
        f'(ID: {prestamo_id})'
    )



# INDICADORES

col1, col2, col3 = st.columns(3)

col1.metric("Préstamos registrados", len(prestamos))
col2.metric("Préstamos activos", len(prestamos_activos))
col3.metric(
    "Devoluciones realizadas",
    sum(1 for p in prestamos if p["Estado"] == "Devuelto")
)

st.divider()



# PESTAÑAS

tab_registrar, tab_devolver = st.tabs(
    ["Registrar préstamo", "Registrar devolución"]
)



# REGISTRAR PRÉSTAMO

with tab_registrar:

    st.subheader("Registrar un nuevo préstamo")

    if not usuarios_activos:
        st.warning("No hay usuarios activos disponibles.")

    elif not libros_disponibles:
        st.warning("No hay libros con ejemplares disponibles.")

    else:

        with st.form("form_registrar_prestamo"):

            usuario_id = st.selectbox(
                "Selecciona el usuario",
                options=list(usuarios_activos.keys()),
                format_func=mostrar_usuario
            )

            libro_id = st.selectbox(
                "Selecciona el libro",
                options=list(libros_disponibles.keys()),
                format_func=mostrar_libro
            )

            fecha_vencimiento = st.date_input(
                "Fecha de vencimiento",
                value=date.today() + timedelta(days=14),
                min_value=date.today() + timedelta(days=1)
            )

            enviar = st.form_submit_button(
                "Registrar préstamo",
                type="primary"
            )

            if enviar:

                try:
                    prestamo_id = prestamos_servicio.crear_prestamo(
                        usuario_id=usuario_id,
                        libro_id=libro_id,
                        fecha_vencimiento=fecha_vencimiento
                    )

                    st.success(
                        f"Préstamo registrado correctamente. "
                        f"Identificador: {prestamo_id}"
                    )

                    st.rerun()

                except Exception as error:
                    st.error(
                        f"No fue posible registrar el préstamo: {error}"
                    )



# REGISTRAR DEVOLUCIÓN

with tab_devolver:

    st.subheader("Registrar devolución de un libro")

    if not prestamos_activos:

        st.info("No hay préstamos pendientes de devolución.")

    else:

        prestamo_id = st.selectbox(
            "Selecciona el préstamo",
            options=list(prestamos_activos.keys()),
            format_func=mostrar_prestamo
        )

        prestamo = prestamos_activos[prestamo_id]

        st.write(f'**Libro:** {prestamo["TituloLibro"]}')
        st.write(
            f'**Usuario:** {prestamo["NombreUsuario"]} '
            f'{prestamo["ApellidoUsuario"]}'
        )
        st.write(
            f'**Fecha de vencimiento:** '
            f'{prestamo["FechaVencimiento"]}'
        )

        confirmar = st.checkbox(
            "Confirmo que deseo registrar la devolución."
        )

        if st.button("Registrar devolución", type="primary"):

            if not confirmar:
                st.warning("Debes confirmar la devolución.")

            else:

                try:
                    prestamos_servicio.registrar_devolucion(
                        prestamo_id=prestamo_id
                    )

                    st.success(
                        "Devolución registrada correctamente. "
                        "El ejemplar volvió a estar disponible."
                    )

                    st.rerun()

                except Exception as error:
                    st.error(
                        f"No fue posible registrar la devolución: {error}"
                    )



# CONSULTAR HISTORIAL DE PRÉSTAMOS

st.divider()
st.subheader("Historial de préstamos")

if prestamos:

    filas = []

    for prestamo in prestamos:

        filas.append({
            "ID": prestamo["PrestamoID"],
            "Documento": prestamo["Documento"],
            "Usuario": (
                f'{prestamo["NombreUsuario"]} '
                f'{prestamo["ApellidoUsuario"]}'
            ),
            "Libro": prestamo["TituloLibro"],
            "Fecha préstamo": prestamo["FechaPrestamo"],
            "Fecha vencimiento": prestamo["FechaVencimiento"],
            "Fecha devolución": prestamo["FechaDevolucion"] or "",
            "Estado": prestamo["Estado"]
        })

    st.dataframe(
        pd.DataFrame(filas),
        use_container_width=True,
        hide_index=True
    )

else:
    st.info("Todavía no hay préstamos registrados.")
