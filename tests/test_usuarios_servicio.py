
import unittest
from unittest.mock import patch

from servicios.usuarios_servicio import UsuariosServicio


class TestUsuariosServicio(unittest.TestCase):

    def setUp(self):
        self.parche = patch("servicios.usuarios_servicio.UsuariosRepositorio")
        self.mock_repositorio = self.parche.start()
        self.addCleanup(self.parche.stop)

        self.servicio = UsuariosServicio()
        self.repositorio = self.servicio.repositorio

    def test_listar_usuarios(self):
        self.repositorio.listar_todos.return_value = []

        resultado = self.servicio.listar_usuarios()

        self.assertEqual(resultado, [])
        self.repositorio.listar_todos.assert_called_once()

    def test_obtener_usuario(self):
        self.repositorio.obtener_por_id.return_value = {
            "UsuarioID": 1
        }

        resultado = self.servicio.obtener_usuario(1)

        self.assertEqual(resultado, {"UsuarioID": 1})
        self.repositorio.obtener_por_id.assert_called_once_with(1)

    def test_rechaza_id_invalido(self):
        with self.assertRaises(ValueError):
            self.servicio.obtener_usuario(0)

        self.repositorio.obtener_por_id.assert_not_called()

    def test_crear_usuario_valido(self):
        self.repositorio.crear.return_value = 1

        resultado = self.servicio.crear_usuario(
            documento="  123456  ",
            nombres="  Sebastian  ",
            apellidos="  Carrero  ",
            correo="  correo@ejemplo.com  ",
            telefono="  3001234567  "
        )

        self.assertEqual(resultado, 1)

        self.repositorio.crear.assert_called_once_with(
            "123456",
            "Sebastian",
            "Carrero",
            "correo@ejemplo.com",
            "3001234567"
        )

    def test_rechaza_documento_vacio(self):
        with self.assertRaises(ValueError):
            self.servicio.crear_usuario(
                "", "Sebastian", "Carrero"
            )

        self.repositorio.crear.assert_not_called()

    def test_rechaza_nombres_vacios(self):
        with self.assertRaises(ValueError):
            self.servicio.crear_usuario(
                "123456", "   ", "Carrero"
            )

    def test_rechaza_apellidos_vacios(self):
        with self.assertRaises(ValueError):
            self.servicio.crear_usuario(
                "123456", "Sebastian", ""
            )

    def test_rechaza_documento_demasiado_largo(self):
        with self.assertRaises(ValueError):
            self.servicio.crear_usuario(
                "1" * 31, "Sebastian", "Carrero"
            )

    def test_rechaza_correo_demasiado_largo(self):
        with self.assertRaises(ValueError):
            self.servicio.crear_usuario(
                "123456",
                "Sebastian",
                "Carrero",
                correo="a" * 151
            )

    def test_rechaza_telefono_demasiado_largo(self):
        with self.assertRaises(ValueError):
            self.servicio.crear_usuario(
                "123456",
                "Sebastian",
                "Carrero",
                telefono="1" * 26
            )

    def test_campos_opcionales_vacios_se_guardan_como_none(self):
        self.repositorio.crear.return_value = 1

        self.servicio.crear_usuario(
            "123456",
            "Sebastian",
            "Carrero",
            correo="   ",
            telefono=""
        )

        self.repositorio.crear.assert_called_once_with(
            "123456",
            "Sebastian",
            "Carrero",
            None,
            None
        )

    def test_actualizar_usuario_valido(self):
        self.repositorio.actualizar.return_value = True

        resultado = self.servicio.actualizar_usuario(
            1,
            "123456",
            "Sebastian",
            "Carrero"
        )

        self.assertTrue(resultado)
        self.repositorio.actualizar.assert_called_once_with(
            1,
            "123456",
            "Sebastian",
            "Carrero",
            None,
            None
        )

    def test_cambiar_estado_usuario(self):
        self.repositorio.cambiar_estado.return_value = True

        resultado = self.servicio.cambiar_estado_usuario(1, False)

        self.assertTrue(resultado)
        self.repositorio.cambiar_estado.assert_called_once_with(
            1, False
        )

    def test_rechaza_estado_invalido(self):
        with self.assertRaises(ValueError):
            self.servicio.cambiar_estado_usuario(1, "inactivo")

        self.repositorio.cambiar_estado.assert_not_called()


if __name__ == "__main__":
    unittest.main()
