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

    
    def test_obtener_autor_por_id(self):
        autor = {
            "autor_id": 1,
            "nombres": "Gabriel",
            "apellidos": "Garcia Marquez",
            "nacionalidad": "Colombiana",
        }

        self.repositorio_mock.return_value.obtener_por_id.return_value = autor

        resultado = self.servicio.obtener_autor(1)

        self.assertEqual(resultado, autor)
        self.repositorio_mock.return_value.obtener_por_id.assert_called_once_with(1)

    def test_rechaza_id_invalido(self):
        with self.assertRaises(ValueError):
            self.servicio.obtener_autor(0)

        self.repositorio_mock.return_value.obtener_por_id.assert_not_called()

    def test_actualizar_autor_valido(self):
        self.repositorio_mock.return_value.actualizar.return_value = True

        resultado = self.servicio.actualizar_autor(
            1,
            " Gabriel ",
            " Garcia Marquez ",
            "Colombiana"
        )

        self.assertTrue(resultado)
        self.repositorio_mock.return_value.actualizar.assert_called_once_with(
            1,
            "Gabriel",
            "Garcia Marquez",
            "Colombiana"
        )

    def test_eliminar_autor_valido(self):
        self.repositorio_mock.return_value.eliminar.return_value = True

        resultado = self.servicio.eliminar_autor(1)

        self.assertTrue(resultado)
        self.repositorio_mock.return_value.eliminar.assert_called_once_with(1)

    def test_rechaza_id_invalido_al_eliminar(self):
        with self.assertRaises(ValueError):
            self.servicio.eliminar_autor(-1)

        self.repositorio_mock.return_value.eliminar.assert_not_called()



if __name__ == "__main__":
    unittest.main()
