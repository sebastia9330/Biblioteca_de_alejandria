
from database.connection import obtener_conexion


class PrestamosRepositorio:

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
                    P.PrestamoID,
                    P.UsuarioID,
                    U.Documento,
                    U.Nombres AS NombreUsuario,
                    U.Apellidos AS ApellidoUsuario,
                    P.LibroID,
                    L.Titulo AS TituloLibro,
                    P.FechaPrestamo,
                    P.FechaVencimiento,
                    P.FechaDevolucion,
                    P.Estado
                FROM Prestamos P
                INNER JOIN Usuarios U
                    ON P.UsuarioID = U.UsuarioID
                INNER JOIN Libros L
                    ON P.LibroID = L.LibroID
                ORDER BY P.FechaPrestamo DESC
            """)

            filas = cursor.fetchall()

            return [
                self._convertir_fila(cursor, fila)
                for fila in filas
            ]

        finally:
            conexion.close()

    def obtener_por_id(self, prestamo_id):
        conexion = obtener_conexion()

        try:
            cursor = conexion.cursor()

            cursor.execute("""
                SELECT
                    P.PrestamoID,
                    P.UsuarioID,
                    U.Documento,
                    U.Nombres AS NombreUsuario,
                    U.Apellidos AS ApellidoUsuario,
                    P.LibroID,
                    L.Titulo AS TituloLibro,
                    P.FechaPrestamo,
                    P.FechaVencimiento,
                    P.FechaDevolucion,
                    P.Estado
                FROM Prestamos P
                INNER JOIN Usuarios U
                    ON P.UsuarioID = U.UsuarioID
                INNER JOIN Libros L
                    ON P.LibroID = L.LibroID
                WHERE P.PrestamoID = ?
            """, (prestamo_id,))

            fila = cursor.fetchone()

            if fila is None:
                return None

            return self._convertir_fila(cursor, fila)

        finally:
            conexion.close()

    def crear(self, usuario_id, libro_id, fecha_vencimiento):
        conexion = obtener_conexion()

        try:
            cursor = conexion.cursor()

            # Verificar que el usuario exista y esté activo.
            cursor.execute("""
                SELECT Activo
                FROM Usuarios WITH (UPDLOCK, HOLDLOCK)
                WHERE UsuarioID = ?
            """, (usuario_id,))

            usuario = cursor.fetchone()

            if usuario is None:
                raise ValueError("El usuario no existe.")

            if not usuario[0]:
                raise ValueError("El usuario está inactivo.")

            # Bloquear el registro del libro durante la transacción.
            cursor.execute("""
                SELECT CantidadDisponible
                FROM Libros WITH (UPDLOCK, HOLDLOCK)
                WHERE LibroID = ?
            """, (libro_id,))

            libro = cursor.fetchone()

            if libro is None:
                raise ValueError("El libro no existe.")

            if libro[0] <= 0:
                raise ValueError(
                    "El libro no tiene ejemplares disponibles."
                )

            # Descontar un ejemplar.
            cursor.execute("""
                UPDATE Libros
                SET CantidadDisponible = CantidadDisponible - 1
                WHERE LibroID = ?
                  AND CantidadDisponible > 0
            """, (libro_id,))

            if cursor.rowcount != 1:
                raise ValueError(
                    "No fue posible reservar un ejemplar del libro."
                )

            # Registrar el préstamo.
            cursor.execute("""
                INSERT INTO Prestamos (
                    UsuarioID,
                    LibroID,
                    FechaVencimiento
                )
                OUTPUT INSERTED.PrestamoID
                VALUES (?, ?, ?)
            """, (
                usuario_id,
                libro_id,
                fecha_vencimiento
            ))

            prestamo_id = cursor.fetchone()[0]

            conexion.commit()

            return prestamo_id

        except Exception:
            conexion.rollback()
            raise

        finally:
            conexion.close()

    def registrar_devolucion(self, prestamo_id):
        conexion = obtener_conexion()

        try:
            cursor = conexion.cursor()

            # Consultar y bloquear el préstamo.
            cursor.execute("""
                SELECT LibroID, Estado
                FROM Prestamos WITH (UPDLOCK, HOLDLOCK)
                WHERE PrestamoID = ?
            """, (prestamo_id,))

            prestamo = cursor.fetchone()

            if prestamo is None:
                conexion.rollback()
                return False

            libro_id, estado = prestamo

            if estado != "Prestado":
                raise ValueError(
                    "El préstamo no se encuentra pendiente de devolución."
                )

            # Registrar la devolución.
            cursor.execute("""
                UPDATE Prestamos
                SET
                    FechaDevolucion = CAST(GETDATE() AS DATE),
                    Estado = 'Devuelto'
                WHERE PrestamoID = ?
                  AND Estado = 'Prestado'
            """, (prestamo_id,))

            if cursor.rowcount != 1:
                raise ValueError(
                    "No fue posible registrar la devolución."
                )

            # Recuperar el ejemplar.
            cursor.execute("""
                UPDATE Libros
                SET CantidadDisponible = CantidadDisponible + 1
                WHERE LibroID = ?
                  AND CantidadDisponible < CantidadTotal
            """, (libro_id,))

            if cursor.rowcount != 1:
                raise ValueError(
                    "No fue posible actualizar la disponibilidad del libro."
                )

            conexion.commit()

            return True

        except Exception:
            conexion.rollback()
            raise

        finally:
            conexion.close()
