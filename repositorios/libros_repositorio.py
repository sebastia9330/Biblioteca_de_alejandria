
from database.connection import obtener_conexion


class LibrosRepositorio:
    """Gestiona libros y sus asociaciones con autores."""

    def _consultar_libros(self, condicion="", parametros=()):
        conexion = None

        try:
            conexion = obtener_conexion()
            cursor = conexion.cursor()

            consulta = f"""
                SELECT
                    L.LibroID,
                    L.ISBN,
                    L.Titulo,
                    L.AnioPublicacion,
                    L.EditorialID,
                    E.Nombre AS Editorial,
                    L.CantidadTotal,
                    L.CantidadDisponible,
                    A.AutorID,
                    A.Nombres,
                    A.Apellidos
                FROM dbo.Libros AS L
                INNER JOIN dbo.Editoriales AS E
                    ON L.EditorialID = E.EditorialID
                LEFT JOIN dbo.LibroAutor AS LA
                    ON L.LibroID = LA.LibroID
                LEFT JOIN dbo.Autores AS A
                    ON LA.AutorID = A.AutorID
                {condicion}
                ORDER BY L.Titulo, A.Apellidos, A.Nombres;
            """

            cursor.execute(consulta, parametros)
            filas = cursor.fetchall()

            libros = {}

            for fila in filas:
                libro_id = fila[0]

                if libro_id not in libros:
                    libros[libro_id] = {
                        "libro_id": fila[0],
                        "isbn": fila[1],
                        "titulo": fila[2],
                        "anio_publicacion": fila[3],
                        "editorial_id": fila[4],
                        "editorial": fila[5],
                        "cantidad_total": fila[6],
                        "cantidad_disponible": fila[7],
                        "autores": []
                    }

                if fila[8] is not None:
                    libros[libro_id]["autores"].append({
                        "autor_id": fila[8],
                        "nombres": fila[9],
                        "apellidos": fila[10]
                    })

            return list(libros.values())

        finally:
            if conexion is not None:
                conexion.close()

    def listar_todos(self):
        return self._consultar_libros()

    def obtener_por_id(self, libro_id):
        libros = self._consultar_libros(
            "WHERE L.LibroID = ?",
            (libro_id,)
        )

        return libros[0] if libros else None

    def _validar_referencias(self, cursor, editorial_id, autores_ids):
        # Comprobar que la editorial exista.
        cursor.execute(
            """
            SELECT COUNT(*)
            FROM dbo.Editoriales
            WHERE EditorialID = ?;
            """,
            (editorial_id,)
        )

        if cursor.fetchone()[0] != 1:
            raise ValueError("La editorial seleccionada no existe.")

        # Comprobar que todos los autores existan.
        marcadores = ", ".join("?" for _ in autores_ids)

        consulta = f"""
            SELECT COUNT(*)
            FROM dbo.Autores
            WHERE AutorID IN ({marcadores});
        """

        cursor.execute(consulta, tuple(autores_ids))
        cantidad_encontrada = cursor.fetchone()[0]

        if cantidad_encontrada != len(autores_ids):
            raise ValueError(
                "Uno o varios autores seleccionados no existen."
            )

    def crear(
        self,
        isbn,
        titulo,
        anio_publicacion,
        editorial_id,
        cantidad_total,
        cantidad_disponible,
        autores_ids
    ):
        conexion = None

        try:
            conexion = obtener_conexion()
            cursor = conexion.cursor()

            self._validar_referencias(
                cursor, editorial_id, autores_ids
            )

            consulta = """
                INSERT INTO dbo.Libros (
                    ISBN,
                    Titulo,
                    AnioPublicacion,
                    EditorialID,
                    CantidadTotal,
                    CantidadDisponible
                )
                OUTPUT INSERTED.LibroID
                VALUES (?, ?, ?, ?, ?, ?);
            """

            cursor.execute(
                consulta,
                (
                    isbn,
                    titulo,
                    anio_publicacion,
                    editorial_id,
                    cantidad_total,
                    cantidad_disponible
                )
            )

            libro_id = cursor.fetchone()[0]

            for autor_id in autores_ids:
                cursor.execute(
                    """
                    INSERT INTO dbo.LibroAutor (LibroID, AutorID)
                    VALUES (?, ?);
                    """,
                    (libro_id, autor_id)
                )

            conexion.commit()
            return libro_id

        except Exception:
            if conexion is not None:
                conexion.rollback()
            raise

        finally:
            if conexion is not None:
                conexion.close()

    def actualizar(
        self,
        libro_id,
        isbn,
        titulo,
        anio_publicacion,
        editorial_id,
        cantidad_total,
        cantidad_disponible,
        autores_ids
    ):
        conexion = None

        try:
            conexion = obtener_conexion()
            cursor = conexion.cursor()

            self._validar_referencias(
                cursor, editorial_id, autores_ids
            )

            consulta = """
                UPDATE dbo.Libros
                SET ISBN = ?,
                    Titulo = ?,
                    AnioPublicacion = ?,
                    EditorialID = ?,
                    CantidadTotal = ?,
                    CantidadDisponible = ?
                WHERE LibroID = ?;
            """

            cursor.execute(
                consulta,
                (
                    isbn,
                    titulo,
                    anio_publicacion,
                    editorial_id,
                    cantidad_total,
                    cantidad_disponible,
                    libro_id
                )
            )

            if cursor.rowcount == 0:
                conexion.rollback()
                return False

            # Reemplazar las asociaciones anteriores.
            cursor.execute(
                """
                DELETE FROM dbo.LibroAutor
                WHERE LibroID = ?;
                """,
                (libro_id,)
            )

            for autor_id in autores_ids:
                cursor.execute(
                    """
                    INSERT INTO dbo.LibroAutor (LibroID, AutorID)
                    VALUES (?, ?);
                    """,
                    (libro_id, autor_id)
                )

            conexion.commit()
            return True

        except Exception:
            if conexion is not None:
                conexion.rollback()
            raise

        finally:
            if conexion is not None:
                conexion.close()

    def eliminar(self, libro_id):
        conexion = None

        try:
            conexion = obtener_conexion()
            cursor = conexion.cursor()

            # Eliminar primero las asociaciones.
            cursor.execute(
                """
                DELETE FROM dbo.LibroAutor
                WHERE LibroID = ?;
                """,
                (libro_id,)
            )

            cursor.execute(
                """
                DELETE FROM dbo.Libros
                WHERE LibroID = ?;
                """,
                (libro_id,)
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
