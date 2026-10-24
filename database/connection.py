import pyodbc


def obtener_conexion():
    cadena_conexion = (
        "DRIVER={ODBC Driver 18 for SQL Server};"
        r"SERVER=.\SQLEXPRESS;"
        "DATABASE=Biblioteca_de_alejandria;"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )

    return pyodbc.connect(cadena_conexion, timeout=5)
