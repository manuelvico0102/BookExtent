# BookExtent
La idea principal de esta aplicación es proporcionar a los usuarios una plataforma para realizar un seguimiento personalizado de sus libros. El usuario podrá gestionar un catálogo de libros marcándolos como leídos, pendientes, en seguimiento o favoritos. Sin embargo, esta aplicación va más allá de un simple seguimiento; busca comprender al usuario para ofrecer una experiencia más personalizada. Además, la app contará con la capacidad de proyectar las portadas de los libros en el mundo real mediante realidad aumentada. Por último, los usuarios tendrán la opción de ser redirigidos a una playlist que mejore su experiencia de lectura.

## Funcionalidades
1. Base de Datos

- Uso de una base de datos Oracle proporcionada por la Universidad de Granada.
- Librería oracledb en Python para realizar operaciones en la base de datos.

2. Interfaz Gráfica

- Uso de la librería tkinter para implementar la interfaz gráfica.
- Código dividido en diseño y funciones para cada ventana.

3. Detección Facial y Registro

- Librería face_recognition y OpenCV para la detección de caras y reconocimiento facial.
- Al registrarse, se toma una foto del usuario y la contraseña se cifra antes de almacenarse en la base de datos.

4. Realidad Aumentada

- Implementación mediante OpenCV y un archivo camara.py para calibrar la cámara.
- Uso de marcadores aruco para proyectar la portada del libro en el mundo real.

5. Comandos por Voz

- Librería speech_recognition para implementar comandos por voz.
- Comandos disponibles para realizar acciones en las ventanas principal y del libro.

6. Hebras
- Uso de hebras para evitar la paralización de ventanas al abrir la cámara y para la implementación de comandos por voz.
