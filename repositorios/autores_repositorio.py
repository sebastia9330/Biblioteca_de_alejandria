from database.connection import obtener_conexion


class AutoresRepositorio:
    #Gestiona las operaciones SQL de la tabla Autores.

    def listar_todos(self):
        conexion = None
        try:
            conexion = obtener_conexion()
            cursor = conexion.cursor()
            consulta = """
                SELECT AutorID, Nombres, Apellidos, Nacionalidad
                FROM dbo.Autores
                ORDER BY Apellidos, Nombres;
            """
            cursor.execute(consulta)
            filas = cursor.fetchall()

            return [
                {
                    "autor_id": fila[0],
                    "nombres": fila[1],
                    "apellidos": fila[2],
                    "nacionalidad": fila[3],
                }
                for fila in filas
            ]

        finally:
            if conexion is not None:
                conexion.close()

    def obtener_por_id(self, autor_id):
        conexion = None

        try:
            conexion = obtener_conexion()
            cursor = conexion.cursor()
            consulta = """
                SELECT AutorID, Nombres, Apellidos, Nacionalidad
                FROM dbo.Autores
                WHERE AutorID = ?;
            """
            cursor.execute(consulta, (autor_id,))
            fila = cursor.fetchone()

            if fila is None:
                return None

            return {
                "autor_id": fila[0],
                "nombres": fila[1],
                "apellidos": fila[2],
                "nacionalidad": fila[3],
            }

        finally:
            if conexion is not None:
                conexion.close()


    def crear(self, nombres, apellidos, nacionalidad=None):
        conexion = None

        try:
            conexion = obtener_conexion()
            cursor = conexion.cursor()
            consulta = """
                INSERT INTO dbo.Autores
                    (Nombres, Apellidos, Nacionalidad)
                OUTPUT INSERTED.AutorID
                VALUES (?, ?, ?);
            """
            cursor.execute(
                consulta,
                (nombres, apellidos, nacionalidad)
            )
            autor_id = cursor.fetchone()[0]
            conexion.commit()

            return autor_id

        except Exception:
            if conexion is not None:
                conexion.rollback()
            raise

        finally:
            if conexion is not None:
                conexion.close()

    def actualizar(self, autor_id, nombres, apellidos, nacionalidad=None):
        conexion = None

        try:
            conexion = obtener_conexion()
            cursor = conexion.cursor()
            consulta = """
                UPDATE dbo.Autores
                SET Nombres = ?,
                    Apellidos = ?,
                    Nacionalidad = ?
                WHERE AutorID = ?;
            """

            cursor.execute(
                consulta,
                (nombres, apellidos, nacionalidad, autor_id)
            )

            filas_afectadas = cursor.rowcount
            conexion.commit()

            return filas_afectadas > 0

        except Exception:
            if conexion is not None:
                conexion.rollback()
            raise

        finally:
            if conexion is not None:
                conexion.close()

    def eliminar(self, autor_id):
        conexion = None

        try:
            conexion = obtener_conexion()
            cursor = conexion.cursor()

            consulta = """
                DELETE FROM dbo.Autores
                WHERE AutorID = ?;
            """

            cursor.execute(consulta, (autor_id,))
            filas_afectadas = cursor.rowcount
            conexion.commit()

            return filas_afectadas > 0

        except Exception:
            if conexion is not None:
                conexion.rollback()
            raise

        finally:
            if conexion is not None:
                conexion.close()
