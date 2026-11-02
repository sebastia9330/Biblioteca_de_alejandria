
from database.connection import obtener_conexion


class UsuariosRepositorio:

    @staticmethod
    def _convertir_fila(cursor, fila):
        columnas = [columna[0] for columna in cursor.description]
        return dict(zip(columnas, fila))

    def listar_todos(self):
        conexion = obtener_conexion()

        try:
            cursor = conexion.cursor()

            cursor.execute("""
                SELECT
                    UsuarioID,
                    Documento,
                    Nombres,
                    Apellidos,
                    Correo,
                    Telefono,
                    Activo
                FROM Usuarios
                ORDER BY Apellidos, Nombres
            """)

            filas = cursor.fetchall()

            return [
                self._convertir_fila(cursor, fila)
                for fila in filas
            ]

        finally:
            conexion.close()

    def obtener_por_id(self, usuario_id):
        conexion = obtener_conexion()

        try:
            cursor = conexion.cursor()

            cursor.execute("""
                SELECT
                    UsuarioID,
                    Documento,
                    Nombres,
                    Apellidos,
                    Correo,
                    Telefono,
                    Activo
                FROM Usuarios
                WHERE UsuarioID = ?
            """, (usuario_id,))

            fila = cursor.fetchone()

            if fila is None:
                return None

            return self._convertir_fila(cursor, fila)

        finally:
            conexion.close()

    def crear(self, documento, nombres, apellidos, correo, telefono):
        conexion = obtener_conexion()

        try:
            cursor = conexion.cursor()

            cursor.execute("""
                INSERT INTO Usuarios (
                    Documento,
                    Nombres,
                    Apellidos,
                    Correo,
                    Telefono
                )
                OUTPUT INSERTED.UsuarioID
                VALUES (?, ?, ?, ?, ?)
            """, (
                documento,
                nombres,
                apellidos,
                correo,
                telefono
            ))

            usuario_id = cursor.fetchone()[0]

            conexion.commit()

            return usuario_id

        except Exception:
            conexion.rollback()
            raise

        finally:
            conexion.close()

    def actualizar(
        self,
        usuario_id,
        documento,
        nombres,
        apellidos,
        correo,
        telefono
    ):
        conexion = obtener_conexion()

        try:
            cursor = conexion.cursor()

            cursor.execute("""
                UPDATE Usuarios
                SET
                    Documento = ?,
                    Nombres = ?,
                    Apellidos = ?,
                    Correo = ?,
                    Telefono = ?
                WHERE UsuarioID = ?
            """, (
                documento,
                nombres,
                apellidos,
                correo,
                telefono,
                usuario_id
            ))

            actualizado = cursor.rowcount > 0

            if actualizado:
                conexion.commit()
            else:
                conexion.rollback()

            return actualizado

        except Exception:
            conexion.rollback()
            raise

        finally:
            conexion.close()

    def cambiar_estado(self, usuario_id, activo):
        conexion = obtener_conexion()

        try:
            cursor = conexion.cursor()

            cursor.execute("""
                UPDATE Usuarios
                SET Activo = ?
                WHERE UsuarioID = ?
            """, (activo, usuario_id))

            actualizado = cursor.rowcount > 0

            if actualizado:
                conexion.commit()
            else:
                conexion.rollback()

            return actualizado

        except Exception:
            conexion.rollback()
            raise

        finally:
            conexion.close()
