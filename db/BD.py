"""
    Archivo con todos los métodos necesarios para hacer uso de la base de datos.

    Autor: Manuel Vico Arboledas.
"""
import oracledb
import numpy as np
import cv2

class BaseDatos:
    """
        Clase que representa la Base de Datos

        Attributes:
            usuario (str): Usuario de la Base de Datos
            password (str): Contraseña del usuario de la Base de Datos
            dsn (str): DSN de la Base de Datos
            connection (obj): Conexión a la Base de Datos
            cursor (obj): Cursor de la Base de Datos
    """
    def __init__(self, usuario, password, dsn):
        """
            Constructor de la clase BaseDatos

            Args:
                usuario (str): Usuario de la Base de Datos
                password (str): Contraseña del usuario de la Base de Datos
                dsn (str): DSN de la Base de Datos
        """
        self.usuario = usuario
        self.password = password
        self.dsn = dsn
        self.connection = None
        self.cursor = None
    
    def conexion(self):
        """
            Función para conectarse a la Base de Datos

            Returns:
                bool: True si se ha conectado correctamente, False en caso contrario
        """

        try:
            self.connection = oracledb.connect(user=self.usuario, password=self.password, dsn=self.dsn)
            self.cursor = self.connection.cursor()
            print("Se ha conectado a la Base de Datos")
            return True
        except Exception as e:
            print("Error al conectarse con la Base de Datos")
            return False
    
    def desconexion(self):
        """
            Función para desconectarse de la Base de Datos
        """
        try:
            if self.cursor is not None:
                self.cursor.close()
            if self.connection is not None:
                self.connection.close()
            print("Se ha desconectado de la Base de Datos")
        except Exception as e:
            print("Error al desconectarse de la Base de Datos")

    def mostrar_tabla(self, tabla):
        """
            Función para mostrar una tabla de la Base de Datos

            Args:
                tabla (str): Nombre de la tabla a mostrar
        """

        self.cursor.execute("SELECT * FROM " + tabla)
        resultado = self.cursor.fetchall()

        for row in resultado:
            print(row)

    def obtenerUsuario(self, username):
        """
            Función para obtener un usuario de la Base de Datos

            Args:
                username (str): Nombre de usuario a obtener
            
            Returns:
                obj: Usuario obtenido de la Base de Datos
        """
        user = None
        self.cursor.execute("SELECT * FROM USUARIO WHERE NOMBRE_USUARIO='" + username +"'")
        user = self.cursor.fetchall()
        return user

    def insertarUsuario(self, username, password):
        """
            Función para insertar un usuario en la Base de Datos

            Args:
                username (str): Nombre de usuario a insertar
                password (str): Contraseña del usuario a insertar
        """
        self.cursor.execute("INSERT INTO USUARIO (NOMBRE_USUARIO, PASSWORD_USUARIO) VALUES ('"+username+"','"+password+"')")
        self.connection.commit()

    def obtenerUsername(self, id_usuario):
        """
            Función para obtener el nombre de usuario de un usuario de la Base de Datos

            Args:
                id_usuario (str): ID del usuario a obtener
            
            Returns:
                str: Nombre de usuario obtenido de la Base de Datos
        """
        query = "SELECT nombre_usuario FROM usuario WHERE id= :id"
        self.cursor.execute(query, {"id": id_usuario})
        username = self.cursor.fetchone()
        return username

    def existeLibro(self, id_libro):
        """
            Función para comprobar si existe un libro en la Base de Datos

            Args:
                id_libro (str): ID del libro a comprobar
            
            Returns:
                bool: True si existe, False en caso contrario
        """
        existe : bool = False
        libro = self.obtenerLibro(id_libro=id_libro)
        if(libro):
            existe = True
        return existe

    def obtenerLibro(self, id_libro):
        """
            Función para obtener un libro de la Base de Datos

            Args:
                id_libro (str): ID del libro a obtener
            
            Returns:
                obj: Libro obtenido de la Base de Datos
        """
        libro = None
        self.cursor.execute("SELECT * FROM LIBRO WHERE ID='" + id_libro +"'")
        libro = self.cursor.fetchall()
        return libro

    def obtenerDescripcion(self, id_libro):
        """
            Función para obtener la descripción de un libro de la Base de Datos

            Args:
                id_libro (str): ID del libro a obtener
            
            Returns:
                str: Descripción del libro obtenido de la Base de Datos
        """
        texto = ""
        self.cursor.execute("SELECT DBMS_LOB.SUBSTR(descripcion, 2000) FROM LIBRO WHERE id='" + id_libro +"'")
        texto = self.cursor.fetchall()
        return texto

    def cargarImagen(self, ruta, id_libro):
        """
            Función para cargar una imagen en la Base de Datos

            Args:
                ruta (str): Ruta de la imagen a cargar
                id_libro (str): ID del libro al que pertenece la imagen
        """
        with open(ruta, "rb") as f:
            imagen = f.read()

        ##self.cursor.execute("INSERT INTO tabla_imagen (id_img, imagen) VALUES (1, :blobImagen)", blobImagen=imagen)
        self.cursor.execute("UPDATE libro SET imagen=:blobImagen WHERE id=:id", blobImagen=imagen, id=id_libro)

        self.connection.commit()
    
    def descargarImagen(self, id_libro):
        """
            Función para descargar una imagen de la Base de Datos

            Args:
                id_libro (str): ID del libro al que pertenece la imagen
            
            Returns:
                obj: Imagen descargada de la Base de Datos
        """
        query = "SELECT imagen FROM libro WHERE id= :id"
        
        self.cursor.execute(query, {"id": id_libro})
        
        #Resultados de la consulta
        result = self.cursor.fetchone()
        if result is not None and result[0] is not None:
            imagen = result[0].read()

            #Decodificamos la imagen
            imagen_np = np.frombuffer(imagen, dtype=np.uint8)
            img = cv2.imdecode(imagen_np, cv2.IMREAD_UNCHANGED)
        else:
            img = cv2.imread('./imagenes/BE_sinfondo.png')
        return img
    
    def obtenerLibros(self):
        """
            Función para obtener todos los libros de la Base de Datos

            Returns:
                obj: Libros obtenidos de la Base de Datos
        """
        query = "SELECT libro.id, libro.titulo, libro.autor FROM libro"
        self.cursor.execute(query)
        libros = self.cursor.fetchall()
        return libros

    def obtenerLibrosCategoria(self, id_usuario, categoria):
        """
            Función para obtener los libros de una categoría de la Base de Datos

            Args:
                id_usuario (str): ID del usuario al que pertenecen los libros
                categoria (str): Categoría de los libros a obtener

            Returns:
                obj: Libros obtenidos de la Base de Datos
        """
        query = "SELECT libro.id, libro.titulo, libro.autor FROM libro INNER JOIN biblioteca_usuario ON libro.ID = biblioteca_usuario.id_libro INNER JOIN seccion ON biblioteca_usuario.id_seccion = seccion.ID WHERE biblioteca_usuario.id_usuario = :id AND seccion.NOMBRE_SECCION = :categoria ORDER BY libro.id"
        self.cursor.execute(query, {"id": id_usuario, "categoria": categoria})
        libros = self.cursor.fetchall()
        return libros
    
    def obtenerLibros(self, where=""):
        """
            Función para obtener los libros de la Base de Datos que cumplan una condición

            Args:
                where (str): Condición de los libros a obtener
            
            Returns:
                obj: Libros obtenidos de la Base de Datos
        """
        if(len(where)>0):
            query = "SELECT libro.id, libro.titulo, libro.autor FROM libro " + where
        else:
            query = "SELECT libro.id, libro.titulo, libro.autor FROM libro"
        
        self.cursor.execute(query)
        libros = self.cursor.fetchall()
        return libros

    def insertarEnBiblioteca(self, id_usuario, id_libro, id_categoria):
        """
            Función para insertar un libro en la biblioteca de un usuario

            Args:
                id_usuario (str): ID del usuario al que pertenece el libro
                id_libro (str): ID del libro a insertar
                id_categoria (str): ID de la categoría del libro a insertar
        """
        query = "INSERT INTO biblioteca_usuario (id_usuario, id_libro, id_seccion) VALUES (:id_u, :id_l, :id_c)"
        self.cursor.execute(query, {"id_u": id_usuario, "id_l": id_libro, "id_c": id_categoria})
        self.connection.commit()

    def eliminarDeBiblioteca(self, id_usuario, id_libro, id_categoria):
        """
            Función para eliminar un libro de la biblioteca de un usuario

            Args:
                id_usuario (str): ID del usuario al que pertenece el libro
                id_libro (str): ID del libro a eliminar
                id_categoria (str): ID de la categoría del libro a eliminar
        """
        query = "DELETE FROM biblioteca_usuario WHERE id_usuario = :id_u AND id_libro = :id_l AND id_seccion = :id_c"
        self.cursor.execute(query, {"id_u": id_usuario, "id_l": id_libro, "id_c": id_categoria})
        self.connection.commit()


    def existeEnBiblioteca(self, id_usuario, id_libro, id_categoria):
        """
            Función para comprobar si un libro existe en la biblioteca de un usuario

            Args:
                id_usuario (str): ID del usuario al que pertenece el libro
                id_libro (str): ID del libro a comprobar
                id_categoria (str): ID de la categoría del libro a comprobar
            
            Returns:
                bool: True si existe, False en caso contrario
        """
        query = "SELECT COUNT(*) FROM biblioteca_usuario WHERE id_usuario = :id_u AND id_libro = :id_l AND id_seccion = :id_c"
        self.cursor.execute(query, {"id_u": id_usuario, "id_l": id_libro, "id_c": id_categoria})
        resultado = self.cursor.fetchone()
        
        existe = False
        if(resultado[0] > 0):
            existe = True
        
        return existe

    def subirImagenCodificada(self, idusuario, cod):
        """
            Método para subir una imagen codificada a la Base de Datos

            Args:
                idusuario (str): ID del usuario al que pertenece la imagen
                cod (obj): Imagen codificada
        """
        query = "UPDATE usuario SET imagen_codificada = :blobImagen WHERE id = :id"
        values = {"blobImagen": cod, "id": idusuario}

        # Ejecutar la consulta SQL
        self.cursor.execute(query, values)
        self.connection.commit()
    
    def obtenerTodasCodificaciones(self):
        """
            Método para obtener todas las codificaciones de la Base de Datos

            Returns:
                obj: Codificaciones obtenidas de la Base de Datos
        """
        query = "SELECT id, NOMBRE_USUARIO, imagen_codificada FROM usuario"
        self.cursor.execute(query)
        codificaciones = self.cursor.fetchall()
        ids = []
        nombres = []
        rostroscod = []
        for id, nombre, imagen_codificada in codificaciones:
            if imagen_codificada is not None: 
                # Leer los datos de la columna imagen_codificada
                buffer = imagen_codificada.read()

                # Convertir los datos en un arreglo NumPy
                codificacion = np.frombuffer(buffer, dtype=np.float64)

                ids.append(id)
                nombres.append(nombre)
                rostroscod.append(codificacion)

        return ids, nombres, rostroscod
    
    def insertarUsuarioFoto(self, username, password, imagen):
        """
            Método para insertar un usuario en la Base de Datos

            Args:
                username (str): Nombre de usuario a insertar
                password (str): Contraseña del usuario a insertar
                imagen (obj): Imagen del usuario a insertar
        """
        self.cursor.execute("INSERT INTO USUARIO (NOMBRE_USUARIO, PASSWORD_USUARIO, IMAGEN_CODIFICADA) VALUES (:usuario, :password, :imagen)", usuario=username, password=password, imagen=imagen)
        self.connection.commit()

