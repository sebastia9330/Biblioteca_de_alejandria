BIBLIOTECA DE ALEJANDRIA: SISTEMA DE GESTION DE BIBLIOTECA

Michales Dayanna Rios Ruiz

Laura Valentina Bernal Palacios

Sebastián Felipe Carrero Ortiz

Juan Rigoberto Rojas Gacha

Facultad de ingeniería, Corporación Unificada Nacional de la educación Superior (CUN)

54465: Programación Avanzada

Ing. Verónica castro Munar

8 de noviembre de 2026

BIBLIOTECA DE ALEJANDRIA: SISTEMA DE GESTION DE BIBLIOTECA

Michales Dayanna Rios Ruiz

Laura Valentina Bernal Palacios

Sebastián Felipe Carrero Ortiz

Juan Rigoberto Rojas Gacha

Trabajo de curso para obtener indicador ACA

Asesor: Verónica castro Munar en ingeniería en Sistemas

Corporación Unificada Nacional de la educación Superior (CUN)

Facultad de ingeniería programa: programación avanzada

Bogotá D.C.

8 de noviembre de 2026

TABLA DE CONTENIDO

## INTRODUCCIÓN

La organización de la información es importante para que una biblioteca pueda administrar sus recursos de manera ordenada. Cuando los datos de los libros se registran o consultan manualmente, pueden presentarse dificultades para encontrar información, actualizar registros y controlar la disponibilidad de los ejemplares.

Por esta razón, se propone la Biblioteca de Alejandría, un sistema informático orientado a facilitar la gestión de la información bibliográfica. El proyecto permite trabajar en la organización de los registros y en el desarrollo de funciones que apoyen las actividades propias de una biblioteca.

Este trabajo también permite aplicar los conocimientos adquiridos durante la formación en Ingeniería de Sistemas, especialmente en análisis de requisitos, programación y desarrollo de software.

## OBJETIVOS

objetivo general

Desarrollar un sistema de gestión de biblioteca que facilite la organización, consulta y actualización de la información de los libros, contribuyendo a un manejo más ordenado de los datos.

objetivos específicos

Identificar las necesidades principales relacionadas con la administración de una biblioteca.

Definir los requisitos funcionales y no funcionales del sistema.

Organizar la información de los libros mediante registros estructurados.

Diseñar funciones que permitan agregar, consultar, modificar y eliminar registros.

Aplicar los conocimientos de programación y análisis de sistemas durante el desarrollo del proyecto.

## PLANTEAMIENTO DEL PROBLEMA

La administración de una biblioteca requiere mantener información organizada sobre los libros y facilitar su consulta. Cuando no se cuenta con una herramienta adecuada, actualizar los datos o localizar un registro puede convertirse en una tarea demorada y generar errores.

Ante esta situación, surge la necesidad de desarrollar una aplicación que permita gestionar la información bibliográfica de una manera más sencilla. La Biblioteca de Alejandría busca responder a esta necesidad mediante funciones que faciliten el registro, la búsqueda y la actualización de la información.

El sistema se plantea como una solución académica que puede fortalecerse a medida que se implementen y prueben sus diferentes funcionalidades.

## ANÁLISIS DE REQUISITOS

El análisis de requisitos permite identificar qué debe hacer el sistema y qué condiciones debe cumplir para que sea útil. Los siguientes requisitos corresponden a las funcionalidades previstas para el proyecto y deben contrastarse con la versión final de la aplicación.

Requisitos funcionales

Los requisitos funcionales describen las acciones que el sistema debe permitir.

RF01. Registrar libros con información como código, nombre, precio, cantidad disponible, autor, editorial, ISBN y tipo.

RF02. Consultar los libros registrados.

RF03. Buscar libros por un dato que permita identificarlos.

RF04. Modificar la información de un libro existente.

RF05. Eliminar registros cuando sea necesario.

RF06. Identificar los libros que tengan pocas unidades disponibles.

RF07. Guardar la información para conservar los cambios realizados.

RF08. Contemplar la administración de autores, editoriales, usuarios, préstamos y devoluciones, si estos módulos hacen parte del alcance aprobado del proyecto.

Requisitos no funcionales

Los requisitos no funcionales establecen condiciones de calidad para el funcionamiento del sistema.

RNF01. La interfaz debe ser sencilla y comprensible para el usuario.

RNF02. La información debe mostrarse de manera clara y organizada.

RNF03. Los datos ingresados deben validarse para reducir errores.

RNF04. El sistema debe permitir consultar y actualizar la información de manera práctica.

RNF05. El código debe mantenerse organizado para facilitar su comprensión y futuras mejoras.

RNF06. El almacenamiento debe permitir conservar y recuperar los registros de acuerdo con la tecnología utilizada en la versión final.

## CASOS DE USO

Los casos de uso describen la interacción entre el usuario y el sistema para realizar una tarea determinada.

Caso de uso 1. registrar un libro

Actor principal: usuario del sistema.

Descripción: permite ingresar la información de un libro para incorporarlo al inventario.

Flujo principal:

El usuario selecciona la opción para agregar un libro.

Ingresa los datos solicitados.

El sistema verifica la información.

Si los datos son válidos, registra el libro y muestra el resultado.

Resultado esperado: el libro queda registrado y disponible para su consulta, siempre que la funcionalidad esté implementada correctamente.

Caso de uso 2. buscar un libro

Actor principal: usuario del sistema.

Descripción: permite localizar un libro registrado.

Flujo principal:

El usuario selecciona la opción de búsqueda.

Introduce el dato de consulta.

El sistema busca coincidencias.

Presenta la información encontrada o informa que no hay resultados.

Resultado esperado: el usuario puede identificar el libro que necesita.

Caso de uso 3. modificar un libro

Actor principal: usuario del sistema.

Descripción: permite actualizar la información de un registro existente.

Flujo principal:

El usuario busca el libro.

Selecciona el registro que desea modificar.

Actualiza los datos necesarios.

El sistema valida y guarda los cambios.

Resultado esperado: la información queda actualizada si la operación se completa correctamente.

Caso de uso 4. eliminar un libro

Actor principal: usuario del sistema.

Descripción: permite retirar un registro que ya no debe permanecer en el inventario.

Flujo principal:

El usuario localiza el libro.

Selecciona la opción para eliminarlo.

El sistema solicita confirmar la acción, si esa opción está implementada.

Se elimina el registro y se informa el resultado.

Resultado esperado: el libro deja de aparecer en el inventario después de una eliminación exitosa.

Caso de uso 5. consultar libros con bajo stock

Actor principal: usuario del sistema.

Descripción: permite identificar los libros cuya cantidad disponible está por debajo del nivel establecido.

Flujo principal:

El usuario abre la opción de bajo stock.

El sistema revisa las cantidades registradas.

Presenta los libros que cumplen la condición.

Resultado esperado: el usuario puede identificar los registros que requieren revisión o reposición.

## DIAGRAMA DE CLASES

| Campo | Función |

| --- | --- |

| IdUsuario | Clave primaria |

| Nombre | Nombre del usuario |

| Apellido | Apellido |

| Documento | Documento de identificación |

| Teléfono | Número telefónico |

| Correo | Correo electrónico |

en el siguiente diagrama de relaciones podemos analizar el aplicativo de una biblioteca para gestionar funciones como:

Guarda la información de las personas que utilizan la biblioteca de manera digital Id usuario identifica de una única manera a cada usuario

Tabla prestamos podemos ver los libros que se han prestado a cada usuario esta tabla es importante ya que relaciona a los usuarios con los libros

| Campo | Función |

| --- | --- |

| IdPrestamo 🔑 | Clave primaria |

| IdUsuario | Clave foránea hacia Usuarios |

| ISBN | Clave foránea hacia Libros |

| FechaPrestamo | Fecha en que se realiza el préstamo |

| FechaDevolucion | Fecha de devolución |

| Estado | Esituación del préstamo, por ejemplo, activo o devuelto |

La relación usuarios → prestamos es:
usuarios – N prestamosesto quiere decir que un usuario puede solicitar varios prestamos pero cada préstamo que se realiza corresponde a un único usuario:

USUARIO

IdUsuario = 1
│
└──Libro 001
└──Libro 002
└── Libro 003

En este caso préstamos y id usuario trabajaría como clave foránea (FK)

RELACION LIBROS PRESTAMOS
el diagrama también nos muestra

Libros – N PRESTAMOS 
esto quiere decir que un libro puede aparecer en varios o muchos registros de préstamos
la relación seria:

Libros.ISBN 
↓
Prestamos.ISBN

LIBROS

| Campo | Función |

| --- | --- |

| ISBN 🔑 | Clave primaria |

| Titulo | Título del libro |

| IdAutor | Clave foránea hacia Autores |

| IdEditorial | Clave foránea hacia Editoriales |

| Categoria | Categoría del libro |

| Anio | Año de publicación |

| Existencias | Cantidad disponible |

Las siglas isbn es el que identifica de una única manera cada libro

RELACIÓN AUTORES – LIBROS

Según el diagrama 
Autores 1 – N libros

Esto quiere decir que un autor puede varios libros registrados mientras que cada libro está asociado a un autor

Editoriales

Presenta la informacion que las editoriales publican acerca de los libros 

id editorial - clave primaria
nombre –nombre de la editorial

relaciones y cardinalidades

Según las conexiones presentadas en el anterior diagrama, las relaciones principales son las siguientes:

| Relación | Cardinalidad | Explicación |

| --- | --- | --- |

| Usuarios – Prestamos | Uno a muchos (1:N) | Un usuario puede realizar varios préstamos, pero cada préstamo pertenece a un usuario. |

| Libros – Prestamos | Uno a muchos (1:N) | Un libro puede aparecer en diferentes préstamos a lo largo del tiempo, y cada registro de préstamo corresponde a un libro. |

| Autores – Libros | Uno a muchos (1:N) | Un autor puede tener varios libros registrados, y cada libro referencia un autor. |

| Editoriales – Libros | Uno a muchos (1:N) | Una editorial puede publicar varios libros, y cada libro referencia una editorial. |

Las claves primarias (PK) identifican de manera única cada registro. En el diagrama son IdPrestamo, IdUsuario, ISBN, IdAutor e IdEditorial.

Las claves foráneas (FK) establecen las relaciones entre las tablas:

Cuando un usuario solicita un libro, se registra un préstamo con el identificador del usuario y el ISBN del libro para consultar detalles del préstamo.

## MODELO ENTIDAD RELACIÓN

Ventajas

La información se organiza en tablas según su función.

Las claves foráneas evitan referencias a usuarios o libros inexistentes.

Reducción de duplicidad de datos almacenados por separado.

Controlar fechas y estados de préstamos.

SQL permite obtener informes sobre libros, usuarios y préstamos.

Recomendaciones

Configurar Documento y Correo con restricciones UNIQUE.

Definir restricciones para que Fecha Devolución no sea anterior a Fecha Préstamo.

Comprobar que los préstamos actualicen disponibilidad libros.

Si un libro puede tener varios autores, crear una tabla intermedia, por ejemplo, Libro Autor, para representar esa relación muchos a muchos.

Si se necesita registrar varios ejemplares físicos de un mismo título, considerar una tabla adicional de ejemplares

## DICCIONARIO DE DATOS

El sistema de Biblioteca de Alejandría utiliza una base de datos relacional en Microsoft SQL Server. En el script compartido se identifican las tablas Autores, Editoriales, Libros, LibroAutor, Usuarios y Prestamos. Los campos y tipos de datos descritos a continuación se transcriben de las instrucciones CREATE TABLE que aparecen en el material compartido.

Nota: los nombres de las columnas que terminan en ID se describen como identificadores. Las relaciones que se indican como claves foráneas corresponden al uso de los campos en el código de repositorios; se debe verificar que el script definitivo incluya las restricciones PRIMARY KEY y FOREIGN KEY.

1.1. Tabla Autores

| Campo | Tipo de dato | Descripción |

| --- | --- | --- |

| AutorID | INT IDENTITY(1,1) NOT NULL | Identificador del autor; generado automáticamente. (PK prevista) |

| Nombres | NVARCHAR(100) NOT NULL | Nombres del autor. |

| Apellidos | NVARCHAR(100) NOT NULL | Apellidos del autor. |

| Nacionalidad | NVARCHAR(60) NULL | Nacionalidad del autor; dato opcional. |

1.2. Tabla Editoriales

| Campo | Tipo de dato | Descripción |

| --- | --- | --- |

| EditorialID | INT IDENTITY(1,1) NOT NULL | Identificador de la editorial; generado automáticamente. (PK prevista) |

| Nombre | NVARCHAR(150) NOT NULL | Nombre de la editorial. |

| Pais | NVARCHAR(80) NULL | País de la editorial; opcional. |

| Telefono | NVARCHAR(25) NULL | Número de teléfono de contacto; opcional. |

| Correo | NVARCHAR(150) NULL | Correo electrónico de contacto; opcional. |

1.3. Tabla Libros

| Campo | Tipo de dato | Descripción |

| --- | --- | --- |

| LibroID | INT IDENTITY(1,1) NOT NULL | Identificador del libro; generado automáticamente. (PK prevista) |

| ISBN | NVARCHAR(20) NULL | Código ISBN del libro; opcional. |

| Titulo | NVARCHAR(200) NOT NULL | Título del libro. |

| AnioPublicacion | SMALLINT NULL | Año de publicación; opcional. |

| EditorialID | INT NOT NULL | Editorial relacionada con el libro. (FK prevista) |

| CantidadTotal | INT NOT NULL DEFAULT 1 | Cantidad total de ejemplares registrados; valor inicial 1. |

| CantidadDisponible | INT NOT NULL DEFAULT 1 | Cantidad de ejemplares disponibles; valor inicial 1. |

1.4. Tabla LibroAutor

| Campo | Tipo de dato | Descripción |

| --- | --- | --- |

| LibroID | INT NOT NULL | Identificador del libro relacionado. (FK prevista; parte de la clave compuesta prevista) |

| AutorID | INT NOT NULL | Identificador del autor relacionado. (FK prevista; parte de la clave compuesta prevista) |

1.5. Tabla Usuarios

| Campo | Tipo de dato | Descripción |

| --- | --- | --- |

| UsuarioID | INT IDENTITY(1,1) NOT NULL | Identificador del usuario; generado automáticamente. (PK prevista) |

| Documento | NVARCHAR(30) NOT NULL | Número de documento del usuario. |

| Nombres | NVARCHAR(100) NOT NULL | Nombres del usuario. |

| Apellidos | NVARCHAR(100) NOT NULL | Apellidos del usuario. |

| Correo | NVARCHAR(150) NULL | Correo electrónico del usuario; opcional. |

| Telefono | NVARCHAR(25) NULL | Teléfono del usuario; opcional. |

| Activo | BIT NOT NULL DEFAULT 1 | Estado del usuario: activo (1) o inactivo (0); valor inicial 1. |

1.6. Tabla Prestamos

| Campo | Tipo de dato | Descripción |

| --- | --- | --- |

| PrestamoID | INT IDENTITY(1,1) NOT NULL | Identificador del préstamo; generado automáticamente. (PK prevista) |

| UsuarioID | INT NOT NULL | Usuario que realiza el préstamo. (FK prevista) |

| LibroID | INT NOT NULL | Libro asociado al préstamo. (FK prevista) |

| FechaPrestamo | DATE NOT NULL DEFAULT CAST(GETDATE() AS DATE) | Fecha en la que se registra el préstamo; por defecto la fecha actual. |

| FechaVencimiento | DATE NOT NULL | Fecha límite para devolver el libro. |

| FechaDevolucion | DATE NULL | Fecha efectiva de devolución; puede estar vacía mientras siga prestado. |

| Estado | NVARCHAR(15) NOT NULL DEFAULT 'Prestado' | Estado del préstamo; por defecto 'Prestado'. |

1.7. Relaciones identificadas en el código

Editoriales — Libros: un registro de editorial puede relacionarse con varios libros mediante EditorialID.

Libros — Autores: relación de muchos a muchos implementada mediante la tabla intermedia LibroAutor.

Usuarios — Prestamos: un usuario puede tener registros de préstamos mediante UsuarioID.

Libros — Prestamos: un libro puede aparecer en diferentes registros de préstamo mediante LibroID.

Estas relaciones se describen según las consultas y la estructura funcional presentes en el código. El equipo debe confirmar las restricciones de integridad referencial en el script SQL final.

## ARQUITECTURA DEL SISTEMA

La aplicación está organizada en una arquitectura por capas. La interfaz gráfica está desarrollada con Streamlit; los servicios contienen la lógica y validaciones de las operaciones; los repositorios ejecutan las consultas SQL; y el módulo de conexión permite acceder a SQL Server. El archivo app.py configura la aplicación y su navegación.

Representación lógica preliminar:

Usuario
↓
Interfaz Streamlit (app.py e interfaz/)
↓
Servicios (servicios/)
↓
Repositorios (repositorios/)
↓
Módulo de conexión (database/)
↓
Base de datos Microsoft SQL Server

La navegación principal se define en app.py y contempla una página de Inicio y páginas de gestión para Autores, Editoriales, Libros, Usuarios y Préstamos. El archivo interfaz/inicio.py muestra indicadores generales consultando los servicios de libros, usuarios y préstamos.

Pendiente de completar: insertar el diagrama gráfico definitivo y comprobar si la estructura de carpetas o el flujo cambia en la versión integrada por el equipo.

## EXPLICACIÓN DE LOS MÓDULOS DESARROLLADOS

Módulo de interfaz

La interfaz utiliza Streamlit para presentar títulos, formularios, pestañas, tablas y mensajes al usuario. En los fragmentos compartidos se observa una página de gestión de autores con opciones para registrar, editar y eliminar información. También se identifica una página principal que presenta indicadores de libros registrados, usuarios registrados, préstamos activos y devoluciones.

Módulo de servicios

Los servicios actúan como capa intermedia entre la interfaz y los repositorios. En el código se observan clases como AutoresServicio, LibrosServicio, UsuariosServicio y PrestamosServicio. Sus responsabilidades incluyen validar datos antes de enviarlos al repositorio. Entre las validaciones identificadas están la comprobación de identificadores positivos, campos de texto obligatorios, longitudes máximas, fechas y cantidades.

Módulo de repositorios

Los repositorios encapsulan las operaciones de acceso a datos. En los fragmentos revisados se observan consultas SELECT para listar y consultar registros, INSERT para crear, UPDATE para actualizar y DELETE para eliminar. Las consultas parametrizadas utilizan signos de interrogación como marcadores de parámetros. En las operaciones de escritura se observan confirmaciones mediante commit y manejo de errores con rollback.

Módulo de base de datos y SQL

La carpeta database contiene el módulo de conexión referenciado por los repositorios mediante la función obtener_conexion(). La carpeta sql incluye el script de creación y carga de datos de las entidades de la biblioteca. El detalle definitivo de configuración y restricciones debe verificarse con el archivo de conexión y el script SQL que entregue el equipo.

Módulo de pruebas

En la carpeta tests se incluyen pruebas unitarias sobre los servicios. Un fragmento de pruebas de préstamos verifica, entre otros casos, el rechazo de fechas de tipo datetime, la fecha actual y fechas pasadas para el registro, así como la validación de identificadores al registrar una devolución. El resultado de ejecución de la suite completa queda pendiente.

Pendiente: revisar y documentar individualmente todos los módulos y sus funciones con el código final integrado.

## DESCRIPCIÓN DE LA CONEXIÓN CON SQL SERVER

El proyecto utiliza Microsoft SQL Server como motor de base de datos. Los repositorios importan la función obtener_conexion desde database.connection y la utilizan para abrir una conexión, crear un cursor y ejecutar instrucciones SQL. De acuerdo con los fragmentos revisados, el código realiza consultas y operaciones de inserción, actualización y eliminación sobre tablas del esquema dbo.

Flujo general de acceso:

El usuario realiza una acción desde la interfaz Streamlit.

La interfaz invoca el método correspondiente de un servicio.

El servicio valida la información recibida.

El repositorio llama a obtener_conexion() y ejecuta la consulta SQL.

En operaciones de escritura se confirma la transacción con commit; ante una excepción se realiza rollback cuando corresponde.

La conexión se cierra al terminar la operación.

Datos técnicos por confirmar en el archivo database/connection.py:

Nombre exacto del servidor o instancia SQL Server.

Nombre exacto de la base de datos.

Driver ODBC instalado y versión.

Método de autenticación configurado.

Configuración de seguridad y manejo de credenciales.

No se incluye una cadena de conexión textual en este borrador porque no se ha confirmado su configuración completa. Se recomienda no incluir contraseñas, tokens ni credenciales en la documentación.

## CAPTURAS DE PANTALLA DEL SISTEMA

## PRUEBAS DE FUNCIONAMIENTO

## RECOMENDACIONES

Configurar Documento y Correo con restricciones UNIQUE.

Definir restricciones para que Fecha Devolución no sea anterior a Fecha Préstamo.

Comprobar que los préstamos actualicen disponibilidad libros.

Si un libro puede tener varios autores, crear una tabla intermedia, por ejemplo, Libro Autor, para representar esa relación muchos a muchos.

Si se necesita registrar varios ejemplares físicos de un mismo título, considerar una tabla adicional de ejemplares

## CONCLUSIONES

El diagrama describe una estructura relacional para gestionar operaciones de una biblioteca con cinco tablas que organizan datos de usuarios, libros, autores, editoriales y préstamos. Las claves primarias y foráneas conectan la información. Las relaciones uno a muchos permiten que un usuario solicite varios libros y mejoran la gestión del inventario y los préstamos según las restricciones y controles.

## REFERENCIAS

https://dbschema.com/blog/tutorials/sql-what-is-a-primary-key/

https://www.ibm.com/docs/es/db2-for-zos/12.0.0?topic=integrity-defining-foreign-key

https://universidadeuropea.com/blog/modelo-entidad-relacion/

https://www.ilerna.es/blog/modelo-entidad-relacion-base-datos
