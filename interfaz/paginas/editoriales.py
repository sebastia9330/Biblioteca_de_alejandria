import streamlit as st
import pandas as pd

from servicios.editoriales_servicio import EditorialesServicio


servicio = EditorialesServicio()

st.title("Gestión de editoriales")
st.write("Administra las editoriales asociadas a los libros de la biblioteca.")

st.divider()



# CONSULTAR EDITORIALES

try:
    editoriales = servicio.listar_editoriales()

except Exception as error:
    st.error(f"No fue posible consultar las editoriales: {error}")
    st.stop()


editoriales_por_id = {
    editorial["editorial_id"]: editorial
    for editorial in editoriales
}

ids_editoriales = list(editoriales_por_id.keys())



# PESTAÑAS

tab_registrar, tab_editar, tab_eliminar = st.tabs(
    ["Registrar editorial", "Editar editorial", "Eliminar editorial"]
)



# REGISTRAR

with tab_registrar:

    st.subheader("Registrar nueva editorial")

    with st.form("formulario_registro_editorial"):

        nombre = st.text_input("Nombre *")
        pais = st.text_input("País")
        telefono = st.text_input("Teléfono")
        correo = st.text_input("Correo electrónico")

        guardar = st.form_submit_button("Registrar editorial")

        if guardar:

            try:
                nuevo_id = servicio.crear_editorial(
                    nombre,
                    pais,
                    telefono,
                    correo
                )

                st.success(
                    f"Editorial registrada correctamente. ID: {nuevo_id}"
                )

                st.rerun()

            except ValueError as error:
                st.warning(str(error))

            except Exception as error:
                st.error(f"No fue posible registrar la editorial: {error}")



# EDITAR

with tab_editar:

    st.subheader("Actualizar información de una editorial")

    if not editoriales:

        st.info("No hay editoriales disponibles para editar.")

    else:

        editorial_seleccionada = st.selectbox(
            "Selecciona una editorial",
            options=ids_editoriales,
            format_func=lambda editorial_id: (
                f"{editoriales_por_id[editorial_id]['nombre']} "
                f"(ID: {editorial_id})"
            ),
            key="editorial_editar"
        )

        editorial = editoriales_por_id[editorial_seleccionada]

        with st.form("formulario_edicion_editorial"):

            nuevo_nombre = st.text_input(
                "Nombre *",
                value=editorial["nombre"]
            )

            nuevo_pais = st.text_input(
                "País",
                value=editorial["pais"] or ""
            )

            nuevo_telefono = st.text_input(
                "Teléfono",
                value=editorial["telefono"] or ""
            )

            nuevo_correo = st.text_input(
                "Correo electrónico",
                value=editorial["correo"] or ""
            )

            actualizar = st.form_submit_button("Guardar cambios")

            if actualizar:

                try:
                    resultado = servicio.actualizar_editorial(
                        editorial_seleccionada,
                        nuevo_nombre,
                        nuevo_pais,
                        nuevo_telefono,
                        nuevo_correo
                    )

                    if resultado:
                        st.success("Editorial actualizada correctamente.")
                        st.rerun()
                    else:
                        st.warning("No se encontró la editorial.")

                except ValueError as error:
                    st.warning(str(error))

                except Exception as error:
                    st.error(f"No fue posible actualizar la editorial: {error}")



# ELIMINAR

with tab_eliminar:

    st.subheader("Eliminar editorial")

    if not editoriales:

        st.info("No hay editoriales disponibles para eliminar.")

    else:

        editorial_a_eliminar = st.selectbox(
            "Selecciona la editorial que deseas eliminar",
            options=ids_editoriales,
            format_func=lambda editorial_id: (
                f"{editoriales_por_id[editorial_id]['nombre']} "
                f"(ID: {editorial_id})"
            ),
            key="editorial_eliminar"
        )

        editorial = editoriales_por_id[editorial_a_eliminar]

        st.warning(
            f"Vas a eliminar la editorial: {editorial['nombre']}."
        )

        st.caption(
            "Una editorial asociada a libros no podrá eliminarse "
            "si la relación está protegida por una llave foránea."
        )

        confirmar = st.checkbox(
            "Confirmo que deseo eliminar esta editorial."
        )

        if st.button("Eliminar editorial", type="primary"):

            if not confirmar:

                st.warning("Debes confirmar la eliminación.")

            else:

                try:
                    resultado = servicio.eliminar_editorial(
                        editorial_a_eliminar
                    )

                    if resultado:
                        st.success("Editorial eliminada correctamente.")
                        st.rerun()
                    else:
                        st.warning("No se encontró la editorial.")

                except Exception as error:
                    st.error(
                        "No fue posible eliminar la editorial. "
                        "Puede estar asociada a uno o varios libros. "
                        f"Detalle: {error}"
                    )



# CONSULTAR Y MOSTRAR EDITORIALES

st.divider()

st.subheader("Editoriales registradas")

try:

    editoriales_actualizadas = servicio.listar_editoriales()

    if editoriales_actualizadas:

        df_editoriales = pd.DataFrame(editoriales_actualizadas)

        df_editoriales = df_editoriales.rename(columns={
            "editorial_id": "ID",
            "nombre": "Nombre",
            "pais": "País",
            "telefono": "Teléfono",
            "correo": "Correo electrónico"
        })

        st.dataframe(
            df_editoriales,
            use_container_width=True,
            hide_index=True
        )

        st.caption(
            f"Total de editoriales: {len(editoriales_actualizadas)}"
        )

    else:

        st.info("Todavía no hay editoriales registradas.")

except Exception as error:

    st.error(f"No fue posible actualizar la tabla: {error}")
