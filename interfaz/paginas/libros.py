import streamlit as st
import pandas as pd
from datetime import date

from servicios.libros_servicio import LibrosServicio
from servicios.editoriales_servicio import EditorialesServicio
from servicios.autores_servicio import AutoresServicio



# SERVICIOS

libros_servicio = LibrosServicio()
editoriales_servicio = EditorialesServicio()
autores_servicio = AutoresServicio()

st.title("Gestión de libros")
st.write("Administra los libros, sus editoriales y sus autores.")
st.divider()



# CARGA DE INFORMACIÓN

try:
    libros = libros_servicio.listar_libros()
    editoriales = editoriales_servicio.listar_editoriales()
    autores = autores_servicio.listar_autores()

except Exception as error:
    st.error(f"No fue posible cargar la información: {error}")
    st.stop()


editoriales_por_id = {
    editorial["editorial_id"]: editorial["nombre"]
    for editorial in editoriales
}

autores_por_id = {
    autor["autor_id"]: autor
    for autor in autores
}

libros_por_id = {
    libro["libro_id"]: libro
    for libro in libros
}

ids_editoriales = list(editoriales_por_id.keys())
ids_autores = list(autores_por_id.keys())
ids_libros = list(libros_por_id.keys())


def mostrar_autor(autor_id):
    autor = autores_por_id[autor_id]
    return f'{autor["nombres"]} {autor["apellidos"]}'


def mostrar_libro(libro_id):
    libro = libros_por_id[libro_id]
    return f'{libro["titulo"]} (ID: {libro_id})'



# PESTAÑAS

tab_registrar, tab_editar, tab_eliminar = st.tabs(
    ["Registrar libro", "Editar libro", "Eliminar libro"]
)



# REGISTRAR LIBRO

with tab_registrar:

    st.subheader("Registrar un nuevo libro")

    if not ids_editoriales:
        st.warning("Primero debes registrar una editorial.")

    elif not ids_autores:
        st.warning("Primero debes registrar al menos un autor.")

    else:
        with st.form("form_registrar_libro"):

            titulo = st.text_input("Título")

            isbn = st.text_input("ISBN (opcional)")

            editorial_id = st.selectbox(
                "Editorial",
                options=ids_editoriales,
                format_func=lambda x: editoriales_por_id[x]
            )

            autores_ids = st.multiselect(
                "Autores",
                options=ids_autores,
                format_func=mostrar_autor
            )

            anio_publicacion = st.number_input(
                "Año de publicación (0 si no se conoce)",
                min_value=0,
                max_value=date.today().year,
                value=0,
                step=1
            )

            cantidad_total = st.number_input(
                "Cantidad total de ejemplares",
                min_value=1,
                value=1,
                step=1
            )

            cantidad_disponible = st.number_input(
                "Cantidad disponible",
                min_value=0,
                max_value=int(cantidad_total),
                value=int(cantidad_total),
                step=1
            )

            enviar = st.form_submit_button(
                "Registrar libro",
                type="primary"
            )

            if enviar:
                try:
                    libros_servicio.crear_libro(
                        titulo=titulo,
                        editorial_id=editorial_id,
                        autores_ids=autores_ids,
                        isbn=isbn or None,
                        anio_publicacion=(
                            int(anio_publicacion)
                            if anio_publicacion > 0
                            else None
                        ),
                        cantidad_total=int(cantidad_total),
                        cantidad_disponible=int(cantidad_disponible)
                    )

                    st.success("Libro registrado correctamente.")
                    st.rerun()

                except Exception as error:
                    st.error(f"No fue posible registrar el libro: {error}")



# EDITAR LIBRO

with tab_editar:

    st.subheader("Editar un libro")

    if not ids_libros:
        st.info("No hay libros registrados para editar.")

    elif not ids_editoriales:
        st.warning("No hay editoriales registradas.")

    elif not ids_autores:
        st.warning("No hay autores registrados.")

    else:
        libro_id = st.selectbox(
            "Selecciona el libro",
            options=ids_libros,
            format_func=mostrar_libro,
            key="libro_editar"
        )

        libro = libros_por_id[libro_id]

        autores_actuales = [
            autor["autor_id"]
            for autor in libro["autores"]
        ]

        with st.form("form_editar_libro"):

            titulo = st.text_input(
                "Título",
                value=libro["titulo"]
            )

            isbn = st.text_input(
                "ISBN (opcional)",
                value=libro["isbn"] or ""
            )

            editorial_id = st.selectbox(
                "Editorial",
                options=ids_editoriales,
                index=(
                    ids_editoriales.index(libro["editorial_id"])
                    if libro["editorial_id"] in ids_editoriales
                    else 0
                ),
                format_func=lambda x: editoriales_por_id[x]
            )

            autores_ids = st.multiselect(
                "Autores",
                options=ids_autores,
                default=[
                    autor_id
                    for autor_id in autores_actuales
                    if autor_id in ids_autores
                ],
                format_func=mostrar_autor
            )

            anio_publicacion = st.number_input(
                "Año de publicación (0 si no se conoce)",
                min_value=0,
                max_value=date.today().year,
                value=int(libro["anio_publicacion"] or 0),
                step=1
            )

            cantidad_total = st.number_input(
                "Cantidad total de ejemplares",
                min_value=1,
                value=int(libro["cantidad_total"]),
                step=1
            )

            cantidad_disponible = st.number_input(
                "Cantidad disponible",
                min_value=0,
                max_value=int(cantidad_total),
                value=min(
                    int(libro["cantidad_disponible"]),
                    int(cantidad_total)
                ),
                step=1
            )

            actualizar = st.form_submit_button(
                "Guardar cambios",
                type="primary"
            )

            if actualizar:
                try:
                    libros_servicio.actualizar_libro(
                        libro_id=libro_id,
                        titulo=titulo,
                        editorial_id=editorial_id,
                        autores_ids=autores_ids,
                        isbn=isbn or None,
                        anio_publicacion=(
                            int(anio_publicacion)
                            if anio_publicacion > 0
                            else None
                        ),
                        cantidad_total=int(cantidad_total),
                        cantidad_disponible=int(cantidad_disponible)
                    )

                    st.success("Libro actualizado correctamente.")
                    st.rerun()

                except Exception as error:
                    st.error(f"No fue posible actualizar el libro: {error}")



# ELIMINAR LIBRO

with tab_eliminar:

    st.subheader("Eliminar un libro")

    if not ids_libros:
        st.info("No hay libros registrados para eliminar.")

    else:
        libro_id = st.selectbox(
            "Selecciona el libro que deseas eliminar",
            options=ids_libros,
            format_func=mostrar_libro,
            key="libro_eliminar"
        )

        libro = libros_por_id[libro_id]

        st.write(f"**Título:** {libro['titulo']}")
        st.write(f"**ISBN:** {libro['isbn'] or 'No registrado'}")

        confirmar = st.checkbox(
            "Confirmo que deseo eliminar este libro."
        )

        if st.button("Eliminar libro", type="primary"):

            if not confirmar:
                st.warning("Debes confirmar la eliminación.")

            else:
                try:
                    libros_servicio.eliminar_libro(libro_id)

                    st.success("Libro eliminado correctamente.")
                    st.rerun()

                except Exception as error:
                    st.error(
                        "No fue posible eliminar el libro. "
                        "Es posible que tenga préstamos asociados. "
                        f"Detalle: {error}"
                    )



# CONSULTAR LIBROS

st.divider()
st.subheader("Libros registrados")

if libros:

    filas = []

    for libro in libros:

        nombres_autores = ", ".join(
            f'{autor["nombres"]} {autor["apellidos"]}'
            for autor in libro["autores"]
        )

        filas.append({
            "ID": libro["libro_id"],
            "ISBN": libro["isbn"] or "",
            "Título": libro["titulo"],
            "Año": libro["anio_publicacion"] or "",
            "Editorial": libro["editorial"],
            "Autores": nombres_autores,
            "Cantidad total": libro["cantidad_total"],
            "Disponibles": libro["cantidad_disponible"]
        })

    st.dataframe(
        pd.DataFrame(filas),
        use_container_width=True,
        hide_index=True
    )

else:
    st.info("Todavía no hay libros registrados.")
