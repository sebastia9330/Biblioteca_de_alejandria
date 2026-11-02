**BIBLIOTECA DE ALEJANDRÍA: SISTEMA DE GESTIÓN DE BIBLIOTECA**

Sebastián Felipe Carrero Ortiz  
Juan Rigoberto Rojas Gacha  
Laura Valentina Bernal Palacios  
MIchaels Dayanna Ríos Ruiz 

Facultad de ingenieria, Corporación Unificada Nacional de Educación Superior (CUN)  

54465: Programacion avanzada

ing. veronica castro Munar 

 8 de noviembre de 2026

---

**BIBLIOTECA DE ALEJANDRÍA: SISTEMA DE GESTIÓN DE BIBLIOTECA**

Sebastián Felipe Carrero Ortiz  
Juan Rigoberto Rojas Gacha  
Laura Valentina Bernal Palacios  
MIchaels Dayanna Ríos Ruiz 

Trabajo de curso para obtener la calificacion del indicador ACA 

Asesor: Veronica Castro Munar en Ingenieria en Sistemas 

Corporación Unificada Nacional de Educación Superior (CUN)  
Facultad de ingenieria 
Programa: Programacion avanzada 
Bogotá D. C.  
8 de noviembre de 2026

---

**TABLA DE CONTENIDO**

1. Introducción
2. Objetivos
   2.1. Objetivo general
   2.2. Objetivos específicos
3. Planteamiento del problema
4. Análisis de requisitos
   4.1. Requisitos funcionales
   4.2. Requisitos no funcionales
5. Casos de uso
6. Referencias

---

**1. INTRODUCCIÓN**

La organización de la información es importante para que una biblioteca pueda administrar sus recursos de manera ordenada. Cuando los datos de los libros se registran o consultan manualmente, pueden presentarse dificultades para encontrar información, actualizar registros y controlar la disponibilidad de los ejemplares.

Por esta razón, se propone la Biblioteca de Alejandría, un sistema informático orientado a facilitar la gestión de la información bibliográfica. El proyecto permite trabajar en la organización de los registros y en el desarrollo de funciones que apoyen las actividades propias de una biblioteca.

Este trabajo también permite aplicar los conocimientos adquiridos durante la formación en Ingeniería de Sistemas, especialmente en análisis de requisitos, programación y desarrollo de software.

---

**2. OBJETIVOS**

**2.1. OBJETIVO GENERAL**

Desarrollar un sistema de gestión de biblioteca que facilite la organización, consulta y actualización de la información de los libros, contribuyendo a un manejo más ordenado de los datos.

**2.2. OBJETIVOS ESPECÍFICOS**

- Identificar las necesidades principales relacionadas con la administración de una biblioteca.
- Definir los requisitos funcionales y no funcionales del sistema.
- Organizar la información de los libros mediante registros estructurados.
- Diseñar funciones que permitan agregar, consultar, modificar y eliminar registros.
- Aplicar los conocimientos de programación y análisis de sistemas durante el desarrollo del proyecto.

---

**3. PLANTEAMIENTO DEL PROBLEMA**

La administración de una biblioteca requiere mantener información organizada sobre los libros y facilitar su consulta. Cuando no se cuenta con una herramienta adecuada, actualizar los datos o localizar un registro puede convertirse en una tarea demorada y generar errores.

Ante esta situación, surge la necesidad de desarrollar una aplicación que permita gestionar la información bibliográfica de una manera más sencilla. La Biblioteca de Alejandría busca responder a esta necesidad mediante funciones que faciliten el registro, la búsqueda y la actualización de la información.

El sistema se plantea como una solución académica que puede fortalecerse a medida que se implementen y prueben sus diferentes funcionalidades.

---

**4. ANÁLISIS DE REQUISITOS**

El análisis de requisitos permite identificar qué debe hacer el sistema y qué condiciones debe cumplir para que sea útil. Los siguientes requisitos corresponden a las funcionalidades previstas para el proyecto y deben contrastarse con la versión final de la aplicación.

**4.1. REQUISITOS FUNCIONALES**

Los requisitos funcionales describen las acciones que el sistema debe permitir.

- RF01. Registrar libros con información como código, nombre, precio, cantidad disponible, autor, editorial, ISBN y tipo.
- RF02. Consultar los libros registrados.
- RF03. Buscar libros por un dato que permita identificarlos.
- RF04. Modificar la información de un libro existente.
- RF05. Eliminar registros cuando sea necesario.
- RF06. Identificar los libros que tengan pocas unidades disponibles.
- RF07. Guardar la información para conservar los cambios realizados.
- RF08. Contemplar la administración de autores, editoriales, usuarios, préstamos y devoluciones, si estos módulos hacen parte del alcance aprobado del proyecto.

**4.2. REQUISITOS NO FUNCIONALES**

Los requisitos no funcionales establecen condiciones de calidad para el funcionamiento del sistema.

- RNF01. La interfaz debe ser sencilla y comprensible para el usuario.
- RNF02. La información debe mostrarse de manera clara y organizada.
- RNF03. Los datos ingresados deben validarse para reducir errores.
- RNF04. El sistema debe permitir consultar y actualizar la información de manera práctica.
- RNF05. El código debe mantenerse organizado para facilitar su comprensión y futuras mejoras.
- RNF06. El almacenamiento debe permitir conservar y recuperar los registros de acuerdo con la tecnología utilizada en la versión final.

---

**5. CASOS DE USO**

Los casos de uso describen la interacción entre el usuario y el sistema para realizar una tarea determinada.

**CASO DE USO 1. REGISTRAR UN LIBRO**

Actor principal: usuario del sistema.

Descripción: permite ingresar la información de un libro para incorporarlo al inventario.

Flujo principal:
1. El usuario selecciona la opción para agregar un libro.
2. Ingresa los datos solicitados.
3. El sistema verifica la información.
4. Si los datos son válidos, registra el libro y muestra el resultado.

Resultado esperado: el libro queda registrado y disponible para su consulta, siempre que la funcionalidad esté implementada correctamente.

**CASO DE USO 2. BUSCAR UN LIBRO**

Actor principal: usuario del sistema.

Descripción: permite localizar un libro registrado.

Flujo principal:
1. El usuario selecciona la opción de búsqueda.
2. Introduce el dato de consulta.
3. El sistema busca coincidencias.
4. Presenta la información encontrada o informa que no hay resultados.

Resultado esperado: el usuario puede identificar el libro que necesita.

**CASO DE USO 3. MODIFICAR UN LIBRO**

Actor principal: usuario del sistema.

Descripción: permite actualizar la información de un registro existente.

Flujo principal:
1. El usuario busca el libro.
2. Selecciona el registro que desea modificar.
3. Actualiza los datos necesarios.
4. El sistema valida y guarda los cambios.

Resultado esperado: la información queda actualizada si la operación se completa correctamente.

**CASO DE USO 4. ELIMINAR UN LIBRO**

Actor principal: usuario del sistema.

Descripción: permite retirar un registro que ya no debe permanecer en el inventario.

Flujo principal:
1. El usuario localiza el libro.
2. Selecciona la opción para eliminarlo.
3. El sistema solicita confirmar la acción, si esa opción está implementada.
4. Se elimina el registro y se informa el resultado.

Resultado esperado: el libro deja de aparecer en el inventario después de una eliminación exitosa.

**CASO DE USO 5. CONSULTAR LIBROS CON BAJO STOCK**

Actor principal: usuario del sistema.

Descripción: permite identificar los libros cuya cantidad disponible está por debajo del nivel establecido.

Flujo principal:
1. El usuario abre la opción de bajo stock.
2. El sistema revisa las cantidades registradas.
3. Presenta los libros que cumplen la condición.

Resultado esperado: el usuario puede identificar los registros que requieren revisión o reposición.

---

**6. REFERENCIAS**

Corporación Unificada Nacional de Educación Superior. (s. f.). *Información institucional*. https://www.cun.edu.co/


Streamlit. (s. f.). *Streamlit documentation*. https://docs.streamlit.io/

Sommerville, I. (2016). *Software engineering* (10th ed.). Pearson.

---


