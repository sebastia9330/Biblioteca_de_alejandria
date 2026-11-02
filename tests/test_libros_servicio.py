
import unittest
from unittest.mock import patch

from servicios.libros_servicio import LibrosServicio


class TestLibrosServicio(unittest.TestCase):

    def setUp(self):
        self.parche = patch("servicios.libros_servicio.LibrosRepositorio")
        self.mock_repositorio = self.parche.start()
        self.addCleanup(self.parche.stop)

        self.servicio = LibrosServicio()
        self.repositorio = self.servicio.repositorio

    def test_listar_libros(self):
        self.repositorio.listar_todos.return_value = []

        resultado = self.servicio.listar_libros()

        self.assertEqual(resultado, [])
        self.repositorio.listar_todos.assert_called_once()

    def test_obtener_libro(self):
        self.repositorio.obtener_por_id.return_value = {"libro_id": 1}

        resultado = self.servicio.obtener_libro(1)

        self.assertEqual(resultado, {"libro_id": 1})
        self.repositorio.obtener_por_id.assert_called_once_with(1)

    def test_obtener_libro_id_invalido(self):
        with self.assertRaises(ValueError):
            self.servicio.obtener_libro(0)

    def test_crear_libro_valido(self):
        self.repositorio.crear.return_value = 1

        resultado = self.servicio.crear_libro(
            titulo="  Cien años de soledad  ",
            editorial_id=1,
            autores_ids=[1, 2],
            isbn="  9781234567890  ",
            anio_publicacion=1967,
            cantidad_total=5,
            cantidad_disponible=5
        )

        self.assertEqual(resultado, 1)

        self.repositorio.crear.assert_called_once_with(
            "9781234567890",
            "Cien años de soledad",
            1967,
            1,
            5,
            5,
            [1, 2]
        )

    def test_crear_libro_sin_autores(self):
        with self.assertRaises(ValueError):
            self.servicio.crear_libro(
                "Libro de prueba", 1, []
            )

        self.repositorio.crear.assert_not_called()

    def test_crear_libro_con_autores_duplicados(self):
        with self.assertRaises(ValueError):
            self.servicio.crear_libro(
                "Libro de prueba", 1, [1, 1]
            )

        self.repositorio.crear.assert_not_called()

    def test_crear_libro_con_autor_invalido(self):
        with self.assertRaises(ValueError):
            self.servicio.crear_libro(
                "Libro de prueba", 1, [0]
            )

    def test_crear_libro_sin_titulo(self):
        with self.assertRaises(ValueError):
            self.servicio.crear_libro(
                "   ", 1, [1]
            )

    def test_crear_libro_con_titulo_largo(self):
        with self.assertRaises(ValueError):
            self.servicio.crear_libro(
                "A" * 201, 1, [1]
            )

    def test_crear_libro_con_anio_futuro(self):
        from datetime import date

        with self.assertRaises(ValueError):
            self.servicio.crear_libro(
                "Libro de prueba",
                1,
                [1],
                anio_publicacion=date.today().year + 1
            )

    def test_crear_libro_con_cantidad_invalida(self):
        with self.assertRaises(ValueError):
            self.servicio.crear_libro(
                "Libro de prueba",
                1,
                [1],
                cantidad_total=2,
                cantidad_disponible=3
            )

    def test_actualizar_libro(self):
        self.repositorio.actualizar.return_value = True

        resultado = self.servicio.actualizar_libro(
            libro_id=1,
            titulo="Libro actualizado",
            editorial_id=1,
            autores_ids=[1, 2],
            cantidad_total=4,
            cantidad_disponible=3
        )

        self.assertTrue(resultado)
        self.repositorio.actualizar.assert_called_once()

    def test_eliminar_libro(self):
        self.repositorio.eliminar.return_value = True

        resultado = self.servicio.eliminar_libro(1)

        self.assertTrue(resultado)
        self.repositorio.eliminar.assert_called_once_with(1)

    def test_eliminar_libro_id_invalido(self):
        with self.assertRaises(ValueError):
            self.servicio.eliminar_libro(-1)

        self.repositorio.eliminar.assert_not_called()


if __name__ == "__main__":
    unittest.main()
