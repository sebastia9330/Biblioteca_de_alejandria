import streamlit as st
import pandas as pd
from servicios.autores_servicio import AutoresServicio


servicio = AutoresServicio()

st.title("Gestión de autores")
st.write("Administra los autores registrados en la biblioteca.")

st.divider()

# Consultar autores existentes
try:
    autores = servicio.listar_autores()

except Exception as error:
    st.error(f"No fue posible consultar los autores: {error}")
    st.stop()


# Organizar la información para los formularios
autores_por_id = {
    autor["autor_id"]: autor
    for autor in autores
}

ids_autores = list(autores_por_id.keys())



# PESTAÑAS
tab_registrar, tab_editar, tab_eliminar = st.tabs(
    ["Registrar autor", "Editar autor", "Eliminar autor"]
)



# REGISTRAR
with tab_registrar:

    st.subheader("Registrar nuevo autor")

    with st.form("formulario_registro_autor"):

        nombres = st.text_input("Nombres")
        apellidos = st.text_input("Apellidos")
        nacionalidad = st.text_input("Nacionalidad")

        guardar = st.form_submit_button("Registrar autor")

        if guardar:
            try:
                nuevo_id = servicio.crear_autor(
                    nombres,
                    apellidos,
                    nacionalidad
                )

                st.success(
                    f"Autor registrado correctamente. ID: {nuevo_id}"
                )

            except ValueError as error:
                st.warning(str(error))

            except Exception as error:
                st.error(f"Error al registrar el autor: {error}")



# EDITAR

with tab_editar:

    st.subheader("Actualizar información de un autor")

    if not autores:

        st.info("No hay autores disponibles para editar.")

    else:

        autor_seleccionado = st.selectbox(
            "Selecciona un autor",
            options=ids_autores,
            format_func=lambda autor_id: (
                f"{autores_por_id[autor_id]['nombres']} "
                f"{autores_por_id[autor_id]['apellidos']} "
                f"(ID: {autor_id})"
            ),
            key="autor_editar"
        )

        autor = autores_por_id[autor_seleccionado]

        with st.form("formulario_edicion_autor"):

            nuevos_nombres = st.text_input(
                "Nombres",
                value=autor["nombres"]
            )

            nuevos_apellidos = st.text_input(
                "Apellidos",
                value=autor["apellidos"]
            )

            nueva_nacionalidad = st.text_input(
                "Nacionalidad",
                value=autor["nacionalidad"] or ""
            )

            actualizar = st.form_submit_button("Guardar cambios")

            if actualizar:

                try:
                    resultado = servicio.actualizar_autor(
                        autor_seleccionado,
                        nuevos_nombres,
                        nuevos_apellidos,
                        nueva_nacionalidad
                    )

                    if resultado:
                        st.success("Autor actualizado correctamente.")
                    else:
                        st.warning("No se realizaron cambios.")

                except ValueError as error:
                    st.warning(str(error))

                except Exception as error:
                    st.error(f"Error al actualizar el autor: {error}")



# ELIMINAR

with tab_eliminar:

    st.subheader("Eliminar autor")

    if not autores:

        st.info("No hay autores disponibles para eliminar.")

    else:

        autor_a_eliminar = st.selectbox(
            "Selecciona el autor que deseas eliminar",
            options=ids_autores,
            format_func=lambda autor_id: (
                f"{autores_por_id[autor_id]['nombres']} "
                f"{autores_por_id[autor_id]['apellidos']} "
                f"(ID: {autor_id})"
            ),
            key="autor_eliminar"
        )

        autor = autores_por_id[autor_a_eliminar]

        st.warning(
            f"Vas a eliminar a {autor['nombres']} "
            f"{autor['apellidos']}."
        )

        confirmar = st.checkbox(
            "Confirmo que deseo eliminar este autor."
        )

        if st.button("Eliminar autor", type="primary"):

            if not confirmar:

                st.warning("Debes confirmar la eliminación.")

            else:

                try:
                    resultado = servicio.eliminar_autor(
                        autor_a_eliminar
                    )

                    if resultado:
                        st.success("Autor eliminado correctamente.")
                    else:
                        st.warning("No se encontró el autor.")

                except Exception as error:
                    st.error(
                        "No fue posible eliminar el autor. "
                        "Es posible que tenga libros asociados. "
                        f"Detalle: {error}"
                    )



# CONSULTAR AUTORES

st.divider()

st.subheader("Autores registrados")

# Volvemos a consultar para mostrar los cambios realizados
try:
    autores_actualizados = servicio.listar_autores()

    if autores_actualizados:

        df_autores = pd.DataFrame(autores_actualizados)

        df_autores = df_autores.rename(columns={
            "autor_id": "ID",
            "nombres": "Nombres",
            "apellidos": "Apellidos",
            "nacionalidad": "Nacionalidad"
        })

        st.dataframe(
            df_autores,
            use_container_width=True,
            hide_index=True
        )

        st.caption(
            f"Total de autores: {len(autores_actualizados)}"
        )

    else:

        st.info("Todavía no hay autores registrados.")

except Exception as error:

    st.error(f"No fue posible actualizar la tabla: {error}")
