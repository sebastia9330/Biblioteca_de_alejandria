import unittest
from unittest.mock import patch
from servicios.autores_servicio import AutoresServicio


class TestAutoresServicio(unittest.TestCase):

    def setUp(self):
        self.parche = patch(
            "servicios.autores_servicio.AutoresRepositorio"
        )
        self.repositorio_mock = self.parche.start()
        self.addCleanup(self.parche.stop)

        self.servicio = AutoresServicio()

    def test_listar_autores(self):
        autores = [
            {
                "autor_id": 1,
                "nombres": "Gabriel",
                "apellidos": "Garcia Marquez",
                "nacionalidad": "Colombiana",
            }
        ]

        self.repositorio_mock.return_value.listar_todos.return_value = autores

        resultado = self.servicio.listar_autores()

        self.assertEqual(resultado, autores)

    def test_rechaza_nombres_vacios(self):
        with self.assertRaises(ValueError):
            self.servicio.crear_autor(" ", "Prueba")

        self.repositorio_mock.return_value.crear.assert_not_called()

    def test_rechaza_apellidos_vacios(self):
        with self.assertRaises(ValueError):
            self.servicio.crear_autor("Gabriel", "")

        self.repositorio_mock.return_value.crear.assert_not_called()

    def test_crear_autor_valido(self):
        self.repositorio_mock.return_value.crear.return_value = 2

        resultado = self.servicio.crear_autor(
            "  Mario ",
            " Mendoza ",
            "Colombiano"
        )

        self.assertEqual(resultado, 2)

        self.repositorio_mock.return_value.crear.assert_called_once_with(
            "Mario",
            "Mendoza",
            "Colombiano"
        )


if __name__ == "__main__":
    unittest.main()
