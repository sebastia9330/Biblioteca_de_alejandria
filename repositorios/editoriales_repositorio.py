from database.connection import obtener_conexion


class EditorialesRepositorio:
    #Gestiona las operaciones SQL de la tabla Editoriales

    def listar_todas(self):
        conexion = None

        try:
            conexion = obtener_conexion()
            cursor = conexion.cursor()
            consulta = """
                SELECT EditorialID, Nombre, Pais, Telefono, Correo
                FROM dbo.Editoriales
                ORDER BY Nombre;
            """
            cursor.execute(consulta)
            filas = cursor.fetchall()

            return [
                {
                    "editorial_id": fila[0],
                    "nombre": fila[1],
                    "pais": fila[2],
                    "telefono": fila[3],
                    "correo": fila[4],
                }
                for fila in filas
            ]

        finally:
            if conexion is not None:
                conexion.close()

    def obtener_por_id(self, editorial_id):
        conexion = None

        try:
            conexion = obtener_conexion()
            cursor = conexion.cursor()
            consulta = """
                SELECT EditorialID, Nombre, Pais, Telefono, Correo
                FROM dbo.Editoriales
                WHERE EditorialID = ?;
            """
            cursor.execute(consulta, (editorial_id,))
            fila = cursor.fetchone()

            if fila is None:
                return None

            return {
                "editorial_id": fila[0],
                "nombre": fila[1],
                "pais": fila[2],
                "telefono": fila[3],
                "correo": fila[4],
            }

        finally:
            if conexion is not None:
                conexion.close()

    def crear(self, nombre, pais=None, telefono=None, correo=None):
        conexion = None

        try:
            conexion = obtener_conexion()
            cursor = conexion.cursor()
            consulta = """
                INSERT INTO dbo.Editoriales
                    (Nombre, Pais, Telefono, Correo)
                OUTPUT INSERTED.EditorialID
                VALUES (?, ?, ?, ?);
            """
            cursor.execute(
                consulta,
                (nombre, pais, telefono, correo)
            )
            editorial_id = cursor.fetchone()[0]
            conexion.commit()

            return editorial_id

        except Exception:
            if conexion is not None:
                conexion.rollback()
            raise

        finally:
            if conexion is not None:
                conexion.close()

    def actualizar(self, editorial_id, nombre, pais=None, telefono=None, correo=None):
        conexion = None

        try:
            conexion = obtener_conexion()
            cursor = conexion.cursor()
            consulta = """
                UPDATE dbo.Editoriales
                SET Nombre = ?,
                    Pais = ?,
                    Telefono = ?,
                    Correo = ?
                WHERE EditorialID = ?;
            """
            cursor.execute(
                consulta,
                (nombre, pais, telefono, correo, editorial_id)
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

    def eliminar(self, editorial_id):
        conexion = None

        try:
            conexion = obtener_conexion()
            cursor = conexion.cursor()

            consulta = """
                DELETE FROM dbo.Editoriales
                WHERE EditorialID = ?;
            """
            cursor.execute(consulta, (editorial_id,))
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
