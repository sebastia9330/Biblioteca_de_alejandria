
import streamlit as st
import pandas as pd

from servicios.usuarios_servicio import UsuariosServicio



# SERVICIO

servicio = UsuariosServicio()

st.title("Gestión de usuarios")
st.write("Administra los usuarios registrados en la biblioteca.")
st.divider()



# CARGA DE INFORMACIÓN

try:
    usuarios = servicio.listar_usuarios()

except Exception as error:
    st.error(f"No fue posible consultar los usuarios: {error}")
    st.stop()


usuarios_por_id = {
    usuario["UsuarioID"]: usuario
    for usuario in usuarios
}

ids_usuarios = list(usuarios_por_id.keys())


def mostrar_usuario(usuario_id):
    usuario = usuarios_por_id[usuario_id]
    nombre = f'{usuario["Nombres"]} {usuario["Apellidos"]}'
    return f'{nombre} - Documento: {usuario["Documento"]}'



# PESTAÑAS

tab_registrar, tab_editar, tab_estado = st.tabs(
    ["Registrar usuario", "Editar usuario", "Activar / desactivar"]
)



# REGISTRAR USUARIO

with tab_registrar:

    st.subheader("Registrar un nuevo usuario")

    with st.form("form_registrar_usuario"):

        documento = st.text_input("Documento")

        nombres = st.text_input("Nombres")

        apellidos = st.text_input("Apellidos")

        correo = st.text_input("Correo electrónico (opcional)")

        telefono = st.text_input("Teléfono (opcional)")

        enviar = st.form_submit_button(
            "Registrar usuario",
            type="primary"
        )

        if enviar:

            try:
                servicio.crear_usuario(
                    documento=documento,
                    nombres=nombres,
                    apellidos=apellidos,
                    correo=correo or None,
                    telefono=telefono or None
                )

                st.success("Usuario registrado correctamente.")
                st.rerun()

            except Exception as error:
                st.error(f"No fue posible registrar el usuario: {error}")



# EDITAR USUARIO

with tab_editar:

    st.subheader("Editar información del usuario")

    if not ids_usuarios:
        st.info("No hay usuarios registrados para editar.")

    else:

        usuario_id = st.selectbox(
            "Selecciona el usuario",
            options=ids_usuarios,
            format_func=mostrar_usuario,
            key="usuario_editar"
        )

        usuario = usuarios_por_id[usuario_id]

        with st.form("form_editar_usuario"):

            documento = st.text_input(
                "Documento",
                value=usuario["Documento"]
            )

            nombres = st.text_input(
                "Nombres",
                value=usuario["Nombres"]
            )

            apellidos = st.text_input(
                "Apellidos",
                value=usuario["Apellidos"]
            )

            correo = st.text_input(
                "Correo electrónico (opcional)",
                value=usuario["Correo"] or ""
            )

            telefono = st.text_input(
                "Teléfono (opcional)",
                value=usuario["Telefono"] or ""
            )

            actualizar = st.form_submit_button(
                "Guardar cambios",
                type="primary"
            )

            if actualizar:

                try:
                    servicio.actualizar_usuario(
                        usuario_id=usuario_id,
                        documento=documento,
                        nombres=nombres,
                        apellidos=apellidos,
                        correo=correo or None,
                        telefono=telefono or None
                    )

                    st.success("Usuario actualizado correctamente.")
                    st.rerun()

                except Exception as error:
                    st.error(
                        f"No fue posible actualizar el usuario: {error}"
                    )



# ACTIVAR / DESACTIVAR USUARIO

with tab_estado:

    st.subheader("Cambiar estado del usuario")

    if not ids_usuarios:
        st.info("No hay usuarios registrados.")

    else:

        usuario_id = st.selectbox(
            "Selecciona el usuario",
            options=ids_usuarios,
            format_func=mostrar_usuario,
            key="usuario_estado"
        )

        usuario = usuarios_por_id[usuario_id]

        activo = bool(usuario["Activo"])

        st.write(
            f'**Usuario:** {usuario["Nombres"]} {usuario["Apellidos"]}'
        )

        st.write(
            f'**Estado actual:** {"Activo" if activo else "Inactivo"}'
        )

        if activo:

            st.warning(
                "Al desactivar este usuario, no podrá realizar nuevos "
                "préstamos. Su historial se conservará."
            )

            confirmar = st.checkbox(
                "Confirmo que deseo desactivar este usuario.",
                key="confirmar_desactivar"
            )

            if st.button("Desactivar usuario", type="primary"):

                if not confirmar:
                    st.warning("Debes confirmar la operación.")

                else:
                    try:
                        servicio.cambiar_estado_usuario(
                            usuario_id=usuario_id,
                            activo=False
                        )

                        st.success("Usuario desactivado correctamente.")
                        st.rerun()

                    except Exception as error:
                        st.error(
                            f"No fue posible desactivar el usuario: {error}"
                        )

        else:

            st.info(
                "Este usuario está inactivo. Puedes volver a habilitarlo."
            )

            confirmar = st.checkbox(
                "Confirmo que deseo activar este usuario.",
                key="confirmar_activar"
            )

            if st.button("Activar usuario", type="primary"):

                if not confirmar:
                    st.warning("Debes confirmar la operación.")

                else:
                    try:
                        servicio.cambiar_estado_usuario(
                            usuario_id=usuario_id,
                            activo=True
                        )

                        st.success("Usuario activado correctamente.")
                        st.rerun()

                    except Exception as error:
                        st.error(
                            f"No fue posible activar el usuario: {error}"
                        )



# CONSULTAR USUARIOS

st.divider()
st.subheader("Usuarios registrados")

if usuarios:

    filas = []

    for usuario in usuarios:

        filas.append({
            "ID": usuario["UsuarioID"],
            "Documento": usuario["Documento"],
            "Nombres": usuario["Nombres"],
            "Apellidos": usuario["Apellidos"],
            "Correo": usuario["Correo"] or "",
            "Teléfono": usuario["Telefono"] or "",
            "Estado": "Activo" if usuario["Activo"] else "Inactivo"
        })

    st.dataframe(
        pd.DataFrame(filas),
        use_container_width=True,
        hide_index=True
    )

else:
    st.info("Todavía no hay usuarios registrados.")
