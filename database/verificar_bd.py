
from database.connection import obtener_conexion


def verificar_tablas():
    conexion = None

    try:
        conexion = obtener_conexion()

        consulta = """
            SELECT TABLE_NAME
            FROM INFORMATION_SCHEMA.TABLES
            WHERE TABLE_TYPE = 'BASE TABLE'
                AND TABLE_SCHEMA = 'dbo'
            ORDER BY TABLE_NAME;
        """

        cursor = conexion.cursor()
        cursor.execute(consulta)

        tablas = [fila[0] for fila in cursor.fetchall()]

        tablas_esperadas = {
            "Autores",
            "Editoriales",
            "Libros",
            "LibroAutor",
            "Usuarios",
            "Prestamos",
        }

        print("Conexión a SQL Server: correcta")
        print("\nTablas encontradas:")

        for tabla in tablas:
            print(f"- {tabla}")

        faltantes = tablas_esperadas - set(tablas)

        if faltantes:
            print("\nFaltan estas tablas:")
            for tabla in sorted(faltantes):
                print(f"- {tabla}")
            return False

        print("\nVerificación completada: todas las tablas existen.")
        return True

    except Exception as error:
        print(f"Error al verificar la base de datos: {error}")
        return False

    finally:
        if conexion is not None:
            conexion.close()


if __name__ == "__main__":
    verificar_tablas()
