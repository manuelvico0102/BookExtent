"""
    Archivo con la parte de la funcionalidad de la ventana libro.

    Autor: Manuel Vico Arboledas.
"""

from tkinter import messagebox
from db.BD import BaseDatos
from forms.libro.form_libro_designer import FormLibroDesigner
from tkinter import filedialog
import util.aruco as ar
import util.speech as speech
from threading import Thread

class FormLibro(FormLibroDesigner):
    """
        Clase que representa la ventana de un libro, parte de funcionalidad
    """
    def __init__(self, basedatos : BaseDatos, id_libro=None, id_usuario=None):
        """
            Constructor de la clase

            Args:
                basedatos (obj): Objeto de la clase BaseDatos
                id_libro (int): Id del libro
                id_usuario (int): Id del usuario
        """
        super().__init__(basedatos=basedatos, id_libro=id_libro, id_usuario=id_usuario)

    def obtenerInformacionLibro(self):
        #Traemos el libro
        self.libro = BaseDatos.obtenerLibro(self=self.bd, id_libro=self.id_libro)
        self.titulo_libro = self.libro[0][1]
        self.autor_libro = self.libro[0][2]
        self.desc_libro = BaseDatos.obtenerDescripcion(self=self.bd, id_libro=self.id_libro)
        self.desc_libro = self.desc_libro[0][0]
        self.imagen_libro = BaseDatos.descargarImagen(self=self.bd, id_libro=self.id_libro)

    def subirImagen(self):
        """
            Método para subir una imagen
        """
        ruta = None
        try:
            ruta = filedialog.askopenfilename(title="Abrir")
            if not ruta:
                raise FileNotFoundError("No se seleccionó ningún archivo")
            print(ruta)
            self.bd.cargarImagen(ruta=ruta, id_libro=self.id_libro)
        except FileNotFoundError as e:
            messagebox.showerror(message=str(e), title="Error")
        except Exception as e:
            messagebox.showerror(message=str(e), title="Mensaje")
    
    def guardarCategoria(self, id_usuario, id_libro, id_categoria):
        """
            Método para guardar una categoría

            Args:
                id_usuario (int): Id del usuario
                id_libro (int): Id del libro
                id_categoria (int): Id de la categoría
        """
        if not self.comando_ejecutandose:
            self.comando_ejecutandose = True
            if not (self.bd.existeEnBiblioteca(id_usuario=id_usuario, id_libro=id_libro, id_categoria=id_categoria)):
                self.bd.insertarEnBiblioteca(id_usuario=id_usuario, id_libro=id_libro, id_categoria=id_categoria)
                messagebox.showinfo(title="Libro añadido", message="Se ha añadido el libro a la sección correspondiente", parent=self.ventana)
            else:
                self.bd.eliminarDeBiblioteca(id_usuario=id_usuario, id_libro=id_libro, id_categoria=id_categoria)
                messagebox.showinfo(title="Libro eliminado", message="Se ha eliminado el libro de la sección correspondiente", parent=self.ventana)
    
    def realidadAumentada(self, imagen):
        """
            Método para proyectar una imagen en realidad aumentada

            Args:
                imagen (obj): Imagen a proyectar
        """
        print(ar.camaraEjecutandose)
        if not ar.camaraEjecutandose:
            ar.camaraEjecutandose = True
            h1 = Thread(target=ar.proyectar, args=[imagen], daemon=True)
            h1.start()

    def leerDescripcion(self, texto):
        """
            Método para leer una descripción

            Args:
                texto (str): Texto a leer
        """
        speech.texto_a_audio(texto=texto)
    
    
