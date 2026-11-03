--insert datos tabla editoriales
INSERT INTO dbo.Editoriales (Nombre, Pais, Telefono, Correo) 
VALUES    
    ('Editorial Planeta Colombia', 'Colombia', '3102345678', 'colombia@planeta.es'),    
    ('Penguin Random House Grupo Editorial Colombia', 'Colombia', '3113456789', 'contacto@penguinrandomhouse.com'),    
    ('Editorial Norma', 'Colombia', '3124567890', 'servicioalcliente@norma.com'),    
    ('Panamericana Editorial', 'Colombia', '3135678901', 'clientes@panamericana.com.co'),    
    ('Editorial Universidad Nacional de Colombia', 'Colombia', '3146789012', 'direditorial@unal.edu.co'),    
    ('Editorial Universidad de Antioquia', 'Colombia', '3157890123', 'editorial@udea.edu.co'),    
    ('Villegas Editores', 'Colombia', '3168901234', 'info@villegaseditores.com'),    
    ('Editorial Universidad del Rosario', 'Colombia', '3179012345', 'editorial@urosario.edu.co'),    
    ('Sílaba Editores', 'Colombia', '3180123456', 'info@silabaeditores.com'),    
    ('Rey Naranjo Editores', 'Colombia', '3191234567', 'contacto@reynaranjo.com'),    
    ('Angosta Editores', 'Colombia', '3202345678', 'contacto@angosta.com'),    
    ('Tragaluz Editores', 'Colombia', '3213456789', 'contacto@tragaluzeditores.com'),    
    ('Editorial Universidad del Valle', 'Colombia', '3224567890', 'editorial@correounivalle.edu.co'),    
    ('Ediciones B Colombia', 'Colombia', '3235678901', 'atencionalcliente@edicionesb.com'),    
    ('Editorial Sudamericana', 'Argentina', '3246789012', 'contacto@megalink.com.ar'),    
    ('Editorial Anagrama', 'España', '3257890123', 'anagrama@anagrama-ed.es'),    
    ('Fondo de Cultura Económica', 'Mexico', '3268901234', 'fce@fondodeculturayes.com'),    
    ('Editorial Alfaguara', 'España', '3279012345', 'contacto@alfaguara.com'),    
    ('Editorial EAFIT', 'Colombia', '3280123456', 'editorial@eafit.edu.co'),    
    ('Editorial Universidad Javeriana', 'Colombia', '3291234567', 'editorial@javeriana.edu.co');


--insert datos tabla autores
INSERT INTO dbo.Autores (Nombres, Apellidos, Nacionalidad)
VALUES
    ('Gabriel', 'Garcia Marquez', 'Colombiana'),
    ('Jorge Luis', 'Borges', 'Argentina'),
    ('Isabel', 'Allende', 'Chilena'),
    ('Mario', 'Vargas Llosa', 'Peruana'),
    ('Julio', 'Cortazar', 'Argentina'),
    ('Pablo', 'Neruda', 'Chilena'),
    ('Rafael', 'Pombo', 'Colombiana'),
    ('Laura', 'Restrepo', 'Colombiana'),
    ('Carlos', 'Fuentes', 'Mexicana'),
    ('Octavio', 'Paz', 'Mexicana'),
    ('Miguel', 'de Cervantes', 'Espanola'),
    ('Federico', 'Garcia Lorca', 'Espanola'),
    ('Jane', 'Austen', 'Britanica'),
    ('William', 'Shakespeare', 'Britanica'),
    ('George', 'Orwell', 'Britanica'),
    ('Stephen', 'King', 'Estadounidense'),
    ('J.K.', 'Rowling', 'Britanica'),
    ('Paulo', 'Coelho', 'Brasilena'),
    ('Ernest', 'Hemingway', 'Estadounidense'),
    ('Franz', 'Kafka', 'Checa');


--insert datos tabla libros
INSERT INTO dbo.Libros (ISBN, Titulo, AnioPublicacion, EditorialID,CantidadTotal, CantidadDisponible)
VALUES
    ('9780307474728', 'Cien anos de soledad', 1967, 1, 5, 5),
    ('9788420471839', 'El amor en los tiempos del colera', 1985, 2, 3, 3),
    ('9789584281234', 'La voragine', 1924, 3, 4, 4),
    ('9789585112345', 'Maria', 1867, 4, 5, 5),
    ('9789584501234', 'Delirio', 2004, 5, 3, 3),
    ('9789587741234', 'Los ejercitos', 2007, 6, 4, 4),
    ('9789584212345', 'El olvido que seremos', 2006, 7, 5, 5),
    ('9789583812345', 'La tejedora de coronas', 1982, 8, 3, 3),
    ('9789585512345', 'Opio en las nubes', 1992, 9, 4, 4),
    ('9789584012345', 'Satanas', 2002, 10, 5, 5),
    ('9789584512345', 'La casa de las dos palmas', 1988, 11, 3, 3),
    ('9789585212345', 'El ruido de las cosas al caer', 2011, 12, 4, 4),
    ('9789585312345', 'La forma de las ruinas', 2015, 13, 5, 5),
    ('9789585412345', 'Que viva la musica', 1977, 14, 3, 3),
    ('9789875512345', 'Rayuela', 1963, 15, 4, 4),
    ('9788433912345', 'La sombra del viento', 2001, 16, 5, 5),
    ('9786071612345', 'Pedro Paramo', 1955, 17, 3, 3),
    ('9788426412345', 'La casa de los espiritus', 1982, 18, 4, 4),
    ('9789585612345', 'El coronel no tiene quien le escriba', 1961, 19, 5, 5),
    ('9789585712345', 'Cronica de una muerte anunciada', 1981, 20, 3, 3);


--insert datos tabla libroAutor
INSERT INTO dbo.LibroAutor (LibroID, AutorID)
VALUES
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 4),
    (6, 5),
    (7, 6),
    (8, 7),
    (9, 8),
    (10, 9),
    (11, 10),
    (12, 11),
    (13, 12),
    (14, 13),
    (15, 14),
    (16, 15),
    (17, 16),
    (18, 17),
    (19, 1),
    (20, 1),
    (1, 2),
    (5, 3),
    (10, 4),
    (15, 5),
    (20, 6);

--insert datos tabla usuarios
INSERT INTO dbo.Usuarios (Documento, Nombres, Apellidos, Correo, Telefono, Activo)
VALUES
    ('1001001001', 'Laura', 'Martinez', 'laura@alejandria.com', '3102345678', 1),
    ('1001001002', 'Carlos', 'Rodriguez', 'carlos@alejandria.com', '3113456789', 1),
    ('1001001003', 'Ana', 'Gomez', 'ana@alejandria.com', '3124567890', 1),
    ('1001001004', 'Andres', 'Lopez', 'andres@alejandria.com', '3135678901', 1),
    ('1001001005', 'Camila', 'Torres', 'camila@alejandria.com', '3146789012', 1),
    ('1001001006', 'Daniel', 'Ramirez', 'daniel@alejandria.com', '3157890123', 1),
    ('1001001007', 'Valentina', 'Castro', 'valentina@alejandria.com', '3168901234', 1),
    ('1001001008', 'Santiago', 'Herrera', 'santiago@alejandria.com', '3179012345', 1),
    ('1001001009', 'Maria', 'Fernandez', 'maria@alejandria.com', '3180123456', 1),
    ('1012402728', 'Sebastian', 'Carrero', 'mugssebastian@gmial.com', '3245864032', 1),
    ('1001001010', 'Lucia', 'Perez', 'lucia@alejandria.com', '3193456789', 1),
    ('1001001011', 'Mateo', 'Gomez', 'mateo@alejandria.com', '3204567890', 1),
    ('1001001012', 'Sofia', 'Rios', 'sofia@alejandria.com', '3215678901', 1),
    ('1001001013', 'David', 'Morales', 'david@alejandria.com', '3226789012', 1),
    ('1001001014', 'Isabella', 'Jimenez', 'isabella@alejandria.com', '3237890123', 1),
    ('1001001015', 'Lucas', 'Vargas', 'lucas@alejandria.com', '3248901234', 1),
    ('1001001016', 'Martina', 'Ortiz', 'martina@alejandria.com', '3259012345', 1),
    ('1001001017', 'Alejandro', 'Silva', 'alejandro@alejandria.com', '3260123456', 1),
    ('1001001018', 'Mariana', 'Rojas', 'mariana@alejandria.com', '3271234567', 1),
    ('1001001019', 'Gabriel', 'Mendoza', 'gabriel@alejandria.com', '3282345678', 1);



--insert datos tabla prestamos
INSERT INTO dbo.Prestamos (UsuarioID, LibroID, FechaPrestamo, FechaVencimiento, FechaDevolucion, Estado)
VALUES
    (1, 1, '2026-10-24', '2026-11-07', NULL, 'Prestado'),
    (2, 3, '2026-10-25', '2026-11-08', NULL, 'Prestado'),
    (3, 5, '2026-09-10', '2026-09-24', '2026-09-22', 'Devuelto'),
    (4, 2, '2026-10-27', '2026-11-10', NULL, 'Prestado'),
    (5, 7, '2026-09-15', '2026-09-29', '2026-09-28', 'Devuelto'),
    (6, 4, '2026-10-20', '2026-11-03', NULL, 'Prestado'),
    (7, 9, '2026-09-18', '2026-10-02', '2026-10-01', 'Devuelto'),
    (8, 6, '2026-10-15', '2026-10-29', NULL, 'Prestado'),
    (9, 8, '2026-09-20', '2026-10-04', '2026-10-03', 'Devuelto'),
    (10, 10, '2026-10-12', '2026-10-26', '2026-10-25', 'Devuelto'),
    (11, 11, '2026-10-29', '2026-11-12', NULL, 'Prestado'),
    (12, 12, '2026-09-25', '2026-10-09', '2026-10-08', 'Devuelto'),
    (13, 13, '2026-10-31', '2026-11-14', NULL, 'Prestado'),
    (14, 14, '2026-10-20', '2026-11-03', NULL, 'Prestado'),
    (15, 15, '2026-09-28', '2026-10-12', '2026-10-11', 'Devuelto'),
    (16, 16, '2026-10-22', '2026-11-05', NULL, 'Prestado'),
    (17, 17, '2026-09-30', '2026-10-14', '2026-10-13', 'Devuelto'),
    (18, 18, '2026-10-24', '2026-11-07', NULL, 'Prestado'),
    (19, 19, '2026-10-25', '2026-11-08', NULL, 'Prestado'),
    (20, 20, '2026-09-05', '2026-09-19', '2026-09-18', 'Devuelto');