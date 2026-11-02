
import unittest
from datetime import date, datetime, timedelta
from unittest.mock import patch

from servicios.prestamos_servicio import PrestamosServicio


class TestPrestamosServicio(unittest.TestCase):

    def setUp(self):
        self.parche = patch(
            "servicios.prestamos_servicio.PrestamosRepositorio"
        )
        self.mock_repositorio = self.parche.start()
        self.addCleanup(self.parche.stop)

        self.servicio = PrestamosServicio()
        self.repositorio = self.servicio.repositorio

        self.fecha_vencimiento = date.today() + timedelta(days=7)

    def test_listar_prestamos(self):
        self.repositorio.listar_todos.return_value = []

        resultado = self.servicio.listar_prestamos()

        self.assertEqual(resultado, [])
        self.repositorio.listar_todos.assert_called_once()

    def test_obtener_prestamo(self):
        self.repositorio.obtener_por_id.return_value = {
            "PrestamoID": 1
        }

        resultado = self.servicio.obtener_prestamo(1)

        self.assertEqual(resultado, {"PrestamoID": 1})
        self.repositorio.obtener_por_id.assert_called_once_with(1)

    def test_rechaza_id_invalido_al_consultar(self):
        with self.assertRaises(ValueError):
            self.servicio.obtener_prestamo(0)

        self.repositorio.obtener_por_id.assert_not_called()

    def test_crear_prestamo_valido(self):
        self.repositorio.crear.return_value = 1

        resultado = self.servicio.crear_prestamo(
            1, 2, self.fecha_vencimiento
        )

        self.assertEqual(resultado, 1)
        self.repositorio.crear.assert_called_once_with(
            1, 2, self.fecha_vencimiento
        )

    def test_rechaza_usuario_invalido(self):
        with self.assertRaises(ValueError):
            self.servicio.crear_prestamo(
                0, 2, self.fecha_vencimiento
            )

        self.repositorio.crear.assert_not_called()

    def test_rechaza_libro_invalido(self):
        with self.assertRaises(ValueError):
            self.servicio.crear_prestamo(
                1, -2, self.fecha_vencimiento
            )

        self.repositorio.crear.assert_not_called()

    def test_rechaza_id_booleano(self):
        with self.assertRaises(ValueError):
            self.servicio.crear_prestamo(
                True, 2, self.fecha_vencimiento
            )

        self.repositorio.crear.assert_not_called()

    def test_rechaza_fecha_nula(self):
        with self.assertRaises(ValueError):
            self.servicio.crear_prestamo(1, 2, None)

        self.repositorio.crear.assert_not_called()

    def test_rechaza_fecha_con_tipo_invalido(self):
        with self.assertRaises(ValueError):
            self.servicio.crear_prestamo(
                1, 2, "2026-12-15"
            )

        self.repositorio.crear.assert_not_called()

    def test_rechaza_fecha_tipo_datetime(self):
        with self.assertRaises(ValueError):
            self.servicio.crear_prestamo(
                1, 2, datetime.now()
            )

        self.repositorio.crear.assert_not_called()

    def test_rechaza_fecha_de_hoy(self):
        with self.assertRaises(ValueError):
            self.servicio.crear_prestamo(
                1, 2, date.today()
            )

        self.repositorio.crear.assert_not_called()

    def test_rechaza_fecha_pasada(self):
        fecha_pasada = date.today() - timedelta(days=1)

        with self.assertRaises(ValueError):
            self.servicio.crear_prestamo(
                1, 2, fecha_pasada
            )

        self.repositorio.crear.assert_not_called()

    def test_registrar_devolucion(self):
        self.repositorio.registrar_devolucion.return_value = True

        resultado = self.servicio.registrar_devolucion(1)

        self.assertTrue(resultado)
        self.repositorio.registrar_devolucion.assert_called_once_with(1)

    def test_rechaza_id_invalido_al_devolver(self):
        with self.assertRaises(ValueError):
            self.servicio.registrar_devolucion(-1)

        self.repositorio.registrar_devolucion.assert_not_called()


if __name__ == "__main__":
    unittest.main()
