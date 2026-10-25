from repositorios.editoriales_repositorio import EditorialesRepositorio


class EditorialesServicio:
    #"Valida los datos y gestiona las operaciones de editoriales

    def __init__(self):
        self.repositorio = EditorialesRepositorio()

    def listar_editoriales(self):
        return self.repositorio.listar_todas()

    def obtener_editorial(self, editorial_id):
        self._validar_id(editorial_id)
        return self.repositorio.obtener_por_id(editorial_id)

    def crear_editorial(self, nombre, pais=None, telefono=None, correo=None):
        nombre = self._validar_texto(nombre, "El nombre", 150)

        pais = self._validar_opcional(pais, "El país", 80)
        telefono = self._validar_opcional(telefono, "El teléfono", 25)
        correo = self._validar_opcional(correo, "El correo", 150)

        return self.repositorio.crear(
            nombre, pais, telefono, correo
        )

    def actualizar_editorial(
        self, editorial_id, nombre, pais=None, telefono=None, correo=None
    ):
        self._validar_id(editorial_id)
        nombre = self._validar_texto(nombre, "El nombre", 150)

        pais = self._validar_opcional(pais, "El país", 80)
        telefono = self._validar_opcional(telefono, "El teléfono", 25)
        correo = self._validar_opcional(correo, "El correo", 150)

        return self.repositorio.actualizar(
            editorial_id, nombre, pais, telefono, correo
        )

    def eliminar_editorial(self, editorial_id):
        self._validar_id(editorial_id)
        return self.repositorio.eliminar(editorial_id)

    @staticmethod
    def _validar_id(editorial_id):
        if (
            isinstance(editorial_id, bool)
            or not isinstance(editorial_id, int)
            or editorial_id <= 0
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
        if valor is None or (
            isinstance(valor, str) and not valor.strip()
        ):
            return None

        if not isinstance(valor, str):
            raise ValueError(f"{campo} debe ser texto.")

        valor = valor.strip()

        if len(valor) > longitud_maxima:
            raise ValueError(
                f"{campo} no puede superar "
                f"{longitud_maxima} caracteres."
            )

        return valor
