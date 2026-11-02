
from datetime import date

from repositorios.prestamos_repositorio import PrestamosRepositorio


class PrestamosServicio:

    def __init__(self):
        self.repositorio = PrestamosRepositorio()

    def listar_prestamos(self):
        return self.repositorio.listar_todos()

    def obtener_prestamo(self, prestamo_id):
        self._validar_id(prestamo_id, "El ID del préstamo")
        return self.repositorio.obtener_por_id(prestamo_id)

    def crear_prestamo(
        self,
        usuario_id,
        libro_id,
        fecha_vencimiento
    ):
        self._validar_id(usuario_id, "El ID del usuario")
        self._validar_id(libro_id, "El ID del libro")
        self._validar_fecha_vencimiento(fecha_vencimiento)

        return self.repositorio.crear(
            usuario_id,
            libro_id,
            fecha_vencimiento
        )

    def registrar_devolucion(self, prestamo_id):
        self._validar_id(prestamo_id, "El ID del préstamo")

        return self.repositorio.registrar_devolucion(
            prestamo_id
        )

    @staticmethod
    def _validar_id(valor, campo):
        if (
            isinstance(valor, bool)
            or not isinstance(valor, int)
            or valor <= 0
        ):
            raise ValueError(
                f"{campo} debe ser un entero positivo."
            )

    @staticmethod
    def _validar_fecha_vencimiento(fecha):
        if type(fecha) is not date:
            raise ValueError(
                "La fecha de vencimiento debe ser una fecha válida."
            )

        if fecha <= date.today():
            raise ValueError(
                "La fecha de vencimiento debe ser posterior a hoy."
            )
