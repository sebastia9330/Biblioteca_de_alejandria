
-- 1. Tabla Autores
CREATE TABLE dbo.Autores (
    AutorID INT IDENTITY(1,1) NOT NULL,
    Nombres NVARCHAR(100) NOT NULL,
    Apellidos NVARCHAR(100) NOT NULL,
    Nacionalidad NVARCHAR(60) NULL
);


-- 2. Tabla Editoriales
CREATE TABLE dbo.Editoriales (
    EditorialID INT IDENTITY(1,1) NOT NULL,
    Nombre NVARCHAR(150) NOT NULL,
    Pais NVARCHAR(80) NULL,
    Telefono NVARCHAR(25) NULL,
    Correo NVARCHAR(150) NULL
);


-- 3. Tabla Libros
CREATE TABLE dbo.Libros (
    LibroID INT IDENTITY(1,1) NOT NULL,
    ISBN NVARCHAR(20) NULL,
    Titulo NVARCHAR(200) NOT NULL,
    AnioPublicacion SMALLINT NULL,
    EditorialID INT NOT NULL,
    CantidadTotal INT NOT NULL DEFAULT 1,
    CantidadDisponible INT NOT NULL DEFAULT 1
);


-- 4. Tabla intermedia LibroAutor
CREATE TABLE dbo.LibroAutor (
    LibroID INT NOT NULL,
    AutorID INT NOT NULL
);


-- 5. Tabla Usuarios
CREATE TABLE dbo.Usuarios (
    UsuarioID INT IDENTITY(1,1) NOT NULL,
    Documento NVARCHAR(30) NOT NULL,
    Nombres NVARCHAR(100) NOT NULL,
    Apellidos NVARCHAR(100) NOT NULL,
    Correo NVARCHAR(150) NULL,
    Telefono NVARCHAR(25) NULL,
    Activo BIT NOT NULL DEFAULT 1
);


-- 6. Tabla Prestamos
CREATE TABLE dbo.Prestamos (
    PrestamoID INT IDENTITY(1,1) NOT NULL,
    UsuarioID INT NOT NULL,
    LibroID INT NOT NULL,
    FechaPrestamo DATE NOT NULL DEFAULT CAST(GETDATE() AS DATE),
    FechaVencimiento DATE NOT NULL,
    FechaDevolucion DATE NULL,
    Estado NVARCHAR(15) NOT NULL DEFAULT 'Prestado'
);