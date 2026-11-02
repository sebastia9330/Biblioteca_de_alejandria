
from datetime import date

from repositorios.libros_repositorio import LibrosRepositorio


class LibrosServicio:
    """Valida los datos y gestiona las operaciones de libros."""

    def __init__(self):
        self.repositorio = LibrosRepositorio()

    def listar_libros(self):
        return self.repositorio.listar_todos()

    def obtener_libro(self, libro_id):
        self._validar_id(libro_id, "El ID del libro")
        return self.repositorio.obtener_por_id(libro_id)

    def crear_libro(
        self,
        titulo,
        editorial_id,
        autores_ids,
        isbn=None,
        anio_publicacion=None,
        cantidad_total=1,
        cantidad_disponible=1
    ):
        titulo = self._validar_texto(titulo, "El título", 200)
        isbn = self._validar_opcional(isbn, "El ISBN", 20)

        self._validar_id(editorial_id, "El ID de la editorial")
        autores_ids = self._validar_autores(autores_ids)

        self._validar_anio(anio_publicacion)
        self._validar_cantidades(
            cantidad_total, cantidad_disponible
        )

        return self.repositorio.crear(
            isbn,
            titulo,
            anio_publicacion,
            editorial_id,
            cantidad_total,
            cantidad_disponible,
            autores_ids
        )

    def actualizar_libro(
        self,
        libro_id,
        titulo,
        editorial_id,
        autores_ids,
        isbn=None,
        anio_publicacion=None,
        cantidad_total=1,
        cantidad_disponible=1
    ):
        self._validar_id(libro_id, "El ID del libro")
        titulo = self._validar_texto(titulo, "El título", 200)
        isbn = self._validar_opcional(isbn, "El ISBN", 20)

        self._validar_id(editorial_id, "El ID de la editorial")
        autores_ids = self._validar_autores(autores_ids)

        self._validar_anio(anio_publicacion)
        self._validar_cantidades(
            cantidad_total, cantidad_disponible
        )

        return self.repositorio.actualizar(
            libro_id,
            isbn,
            titulo,
            anio_publicacion,
            editorial_id,
            cantidad_total,
            cantidad_disponible,
            autores_ids
        )

    def eliminar_libro(self, libro_id):
        self._validar_id(libro_id, "El ID del libro")
        return self.repositorio.eliminar(libro_id)

    @staticmethod
    def _validar_id(valor, campo):
        if (
            isinstance(valor, bool)
            or not isinstance(valor, int)
            or valor <= 0
        ):
            raise ValueError(f"{campo} debe ser un entero positivo.")

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

    @staticmethod
    def _validar_autores(autores_ids):
        if not isinstance(autores_ids, (list, tuple)):
            raise ValueError("Los autores deben enviarse en una lista.")

        if not autores_ids:
            raise ValueError("El libro debe tener al menos un autor.")

        for autor_id in autores_ids:
            LibrosServicio._validar_id(
                autor_id, "El ID del autor"
            )

        if len(autores_ids) != len(set(autores_ids)):
            raise ValueError("No se permiten autores duplicados.")

        return list(autores_ids)

    @staticmethod
    def _validar_anio(anio):
        if anio is None:
            return

        if (
            isinstance(anio, bool)
            or not isinstance(anio, int)
            or not 1 <= anio <= date.today().year
            or anio > 32767
        ):
            raise ValueError("El año de publicación no es válido.")

    @staticmethod
    def _validar_cantidades(total, disponible):
        for valor, campo in (
            (total, "La cantidad total"),
            (disponible, "La cantidad disponible")
        ):
            if (
                isinstance(valor, bool)
                or not isinstance(valor, int)
                or valor < 0
            ):
                raise ValueError(
                    f"{campo} debe ser un entero no negativo."
                )

        if total < 1:
            raise ValueError(
                "La cantidad total debe ser al menos 1."
            )

        if disponible > total:
            raise ValueError(
                "La cantidad disponible no puede superar "
                "la cantidad total."
            )
