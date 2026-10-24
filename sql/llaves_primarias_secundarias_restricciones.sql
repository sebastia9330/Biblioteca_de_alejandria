-- CLAVES PRIMARIAS

ALTER TABLE dbo.Autores
ADD CONSTRAINT PK_Autores
PRIMARY KEY (AutorID);


ALTER TABLE dbo.Editoriales
ADD CONSTRAINT PK_Editoriales
PRIMARY KEY (EditorialID);


ALTER TABLE dbo.Libros
ADD CONSTRAINT PK_Libros
PRIMARY KEY (LibroID);


ALTER TABLE dbo.LibroAutor
ADD CONSTRAINT PK_LibroAutor
PRIMARY KEY (LibroID, AutorID);


ALTER TABLE dbo.Usuarios
ADD CONSTRAINT PK_Usuarios
PRIMARY KEY (UsuarioID);


ALTER TABLE dbo.Prestamos
ADD CONSTRAINT PK_Prestamos
PRIMARY KEY (PrestamoID);


-- CLAVES FORANEAS

ALTER TABLE dbo.Libros
ADD CONSTRAINT FK_Libros_Editoriales
FOREIGN KEY (EditorialID)
REFERENCES dbo.Editoriales (EditorialID);


ALTER TABLE dbo.LibroAutor
ADD CONSTRAINT FK_LibroAutor_Libros
FOREIGN KEY (LibroID)
REFERENCES dbo.Libros (LibroID);


ALTER TABLE dbo.LibroAutor
ADD CONSTRAINT FK_LibroAutor_Autores
FOREIGN KEY (AutorID)
REFERENCES dbo.Autores (AutorID);


ALTER TABLE dbo.Prestamos
ADD CONSTRAINT FK_Prestamos_Usuarios
FOREIGN KEY (UsuarioID)
REFERENCES dbo.Usuarios (UsuarioID);


ALTER TABLE dbo.Prestamos
ADD CONSTRAINT FK_Prestamos_Libros
FOREIGN KEY (LibroID)
REFERENCES dbo.Libros (LibroID);


-- UNICIDAD

ALTER TABLE dbo.Usuarios
ADD CONSTRAINT UQ_Usuarios_Documento
UNIQUE (Documento);



-- RESTRICCIONES CHECK: PRESTAMOS

ALTER TABLE dbo.Prestamos
ADD CONSTRAINT CK_Prestamos_Estado
CHECK (Estado IN ('Prestado', 'Devuelto'));


ALTER TABLE dbo.Prestamos
ADD CONSTRAINT CK_Prestamos_Fechas
CHECK (FechaVencimiento >= FechaPrestamo);


ALTER TABLE dbo.Prestamos
ADD CONSTRAINT CK_Prestamos_Devolucion
CHECK (
    (Estado = 'Prestado' AND FechaDevolucion IS NULL)
    OR
    (Estado = 'Devuelto'
        AND FechaDevolucion IS NOT NULL
        AND FechaDevolucion >= FechaPrestamo)
);



