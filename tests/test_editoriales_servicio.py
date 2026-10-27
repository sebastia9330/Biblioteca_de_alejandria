import unittest
from unittest.mock import patch
from servicios.editoriales_servicio import EditorialesServicio


class TestEditorialesServicio(unittest.TestCase):
    def setUp(self):
        self.parche = patch(
            "servicios.editoriales_servicio.EditorialesRepositorio"
        )
        self.repositorio_mock = self.parche.start()
        self.addCleanup(self.parche.stop)

        self.servicio = EditorialesServicio()
        self.repositorio = self.servicio.repositorio

    def test_listar_editoriales(self):
        self.repositorio.listar_todas.return_value = [
            {"editorial_id": 1, "nombre": "Editorial Prueba"}
        ]

        resultado = self.servicio.listar_editoriales()

        self.assertEqual(len(resultado), 1)
        self.repositorio.listar_todas.assert_called_once()

    def test_obtener_editorial_por_id(self):
        self.repositorio.obtener_por_id.return_value = {
            "editorial_id": 1,
            "nombre": "Editorial Prueba",
        }

        resultado = self.servicio.obtener_editorial(1)

        self.assertEqual(resultado["editorial_id"], 1)
        self.repositorio.obtener_por_id.assert_called_once_with(1)

    def test_rechaza_id_invalido(self):
        for editorial_id in (0, -1, "1", True):
            with self.subTest(editorial_id=editorial_id):
                with self.assertRaises(ValueError):
                    self.servicio.obtener_editorial(editorial_id)

    def test_crear_editorial_valida(self):
        self.repositorio.crear.return_value = 1

        resultado = self.servicio.crear_editorial(
            "  Editorial Prueba  ",
            "  Colombia  ",
            "  6011234567  ",
            "  prueba@example.com  ",
        )

        self.assertEqual(resultado, 1)
        self.repositorio.crear.assert_called_once_with(
            "Editorial Prueba",
            "Colombia",
            "6011234567",
            "prueba@example.com",
        )

    def test_rechaza_nombre_vacio(self):
        with self.assertRaises(ValueError):
            self.servicio.crear_editorial("   ")

        self.repositorio.crear.assert_not_called()

    def test_rechaza_nombre_demasiado_largo(self):
        with self.assertRaises(ValueError):
            self.servicio.crear_editorial("A" * 151)

        self.repositorio.crear.assert_not_called()

    def test_actualizar_editorial_valida(self):
        self.repositorio.actualizar.return_value = True

        resultado = self.servicio.actualizar_editorial(
            1, "Editorial Actualizada"
        )

        self.assertTrue(resultado)
        self.repositorio.actualizar.assert_called_once_with(
            1, "Editorial Actualizada", None, None, None
        )

    def test_eliminar_editorial_valida(self):
        self.repositorio.eliminar.return_value = True

        resultado = self.servicio.eliminar_editorial(1)

        self.assertTrue(resultado)
        self.repositorio.eliminar.assert_called_once_with(1)

    def test_rechaza_id_invalido_al_eliminar(self):
        with self.assertRaises(ValueError):
            self.servicio.eliminar_editorial(0)

        self.repositorio.eliminar.assert_not_called()


if __name__ == "__main__":
    unittest.main()
