from repositorios.autores_repositorio import AutoresRepositorio


class AutoresServicio:
    #Aplica validaciones antes de operar sobre los autores.

    def __init__(self):
        self.repositorio = AutoresRepositorio()

    def listar_autores(self):
        return self.repositorio.listar_todos()

    def obtener_autor(self, autor_id):
        if not isinstance(autor_id, int) or isinstance(autor_id, bool):
            raise ValueError("El ID del autor debe ser un número entero.")

        if autor_id <= 0:
            raise ValueError("El ID del autor debe ser mayor que cero.")

        return self.repositorio.obtener_por_id(autor_id)

    def crear_autor(self, nombres, apellidos, nacionalidad=None):
        nombres = self._validar_texto(nombres, "Los nombres")
        apellidos = self._validar_texto(apellidos, "Los apellidos")

        if nacionalidad is not None:
            nacionalidad = nacionalidad.strip() or None

        return self.repositorio.crear(
            nombres,
            apellidos,
            nacionalidad
        )

    def actualizar_autor(
        self, autor_id, nombres, apellidos, nacionalidad=None
    ):
        self._validar_id(autor_id)
        nombres = self._validar_texto(nombres, "Los nombres")
        apellidos = self._validar_texto(apellidos, "Los apellidos")

        if nacionalidad is not None:
            nacionalidad = nacionalidad.strip() or None

        return self.repositorio.actualizar(
            autor_id,
            nombres,
            apellidos,
            nacionalidad
        )

    def eliminar_autor(self, autor_id):
        self._validar_id(autor_id)
        return self.repositorio.eliminar(autor_id)

    @staticmethod
    def _validar_id(autor_id):
        if (
            not isinstance(autor_id, int)
            or isinstance(autor_id, bool)
            or autor_id <= 0
        ):
            raise ValueError("El ID debe ser un entero mayor que cero.")

    @staticmethod
    def _validar_texto(valor, campo):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError(f"{campo} son obligatorios.")

        valor = valor.strip()

        if len(valor) > 100:
            raise ValueError(f"{campo} no pueden superar 100 caracteres.")

        return valor
