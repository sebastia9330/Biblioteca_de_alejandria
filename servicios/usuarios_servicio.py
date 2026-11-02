
from repositorios.usuarios_repositorio import UsuariosRepositorio


class UsuariosServicio:

    def __init__(self):
        self.repositorio = UsuariosRepositorio()

    def listar_usuarios(self):
        return self.repositorio.listar_todos()

    def obtener_usuario(self, usuario_id):
        self._validar_id(usuario_id)
        return self.repositorio.obtener_por_id(usuario_id)

    def crear_usuario(
        self,
        documento,
        nombres,
        apellidos,
        correo=None,
        telefono=None
    ):
        documento = self._validar_texto(
            documento, "El documento", 30
        )
        nombres = self._validar_texto(
            nombres, "Los nombres", 100
        )
        apellidos = self._validar_texto(
            apellidos, "Los apellidos", 100
        )
        correo = self._validar_opcional(
            correo, "El correo", 150
        )
        telefono = self._validar_opcional(
            telefono, "El teléfono", 25
        )

        return self.repositorio.crear(
            documento,
            nombres,
            apellidos,
            correo,
            telefono
        )

    def actualizar_usuario(
        self,
        usuario_id,
        documento,
        nombres,
        apellidos,
        correo=None,
        telefono=None
    ):
        self._validar_id(usuario_id)

        documento = self._validar_texto(
            documento, "El documento", 30
        )
        nombres = self._validar_texto(
            nombres, "Los nombres", 100
        )
        apellidos = self._validar_texto(
            apellidos, "Los apellidos", 100
        )
        correo = self._validar_opcional(
            correo, "El correo", 150
        )
        telefono = self._validar_opcional(
            telefono, "El teléfono", 25
        )

        return self.repositorio.actualizar(
            usuario_id,
            documento,
            nombres,
            apellidos,
            correo,
            telefono
        )

    def cambiar_estado_usuario(self, usuario_id, activo):
        self._validar_id(usuario_id)

        if not isinstance(activo, bool):
            raise ValueError("El estado debe ser verdadero o falso.")

        return self.repositorio.cambiar_estado(
            usuario_id, activo
        )

    @staticmethod
    def _validar_id(valor):
        if (
            isinstance(valor, bool)
            or not isinstance(valor, int)
            or valor <= 0
        ):
            raise ValueError("El ID debe ser un entero positivo.")

    @staticmethod
    def _validar_texto(valor, campo, longitud_maxima):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError(f"{campo} es obligatorio.")

        valor = valor.strip()

        if len(valor) > longitud_maxima:
            raise ValueError(
                f"{campo} no puede superar "
                f"{longitud_maxima} caracteres."
            )

        return valor

    @staticmethod
    def _validar_opcional(valor, campo, longitud_maxima):
        if valor is None:
            return None

        if not isinstance(valor, str):
            raise ValueError(f"{campo} debe ser texto.")

        valor = valor.strip()

        if not valor:
            return None

        if len(valor) > longitud_maxima:
            raise ValueError(
                f"{campo} no puede superar "
                f"{longitud_maxima} caracteres."
            )

        return valor
