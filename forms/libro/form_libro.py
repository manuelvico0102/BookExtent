from tkinter import messagebox
from db.BD import BaseDatos
from forms.libro.form_libro_designer import FormLibroDesigner
from tkinter import filedialog
import util.aruco as ar

class FormLibro(FormLibroDesigner):
    def __init__(self, basedatos : BaseDatos, id_libro=None, id_usuario=None):
        super().__init__(basedatos=basedatos, id_libro=id_libro, id_usuario=id_usuario)

    def subirImagen(self):
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
        if not (self.bd.existeEnBiblioteca(id_usuario=id_usuario, id_libro=id_libro, id_categoria=id_categoria)):
            self.bd.insertarEnBiblioteca(id_usuario=id_usuario, id_libro=id_libro, id_categoria=id_categoria)
            messagebox.showinfo(title="Libro añadido", message="Se ha añadido el libro a la sección correspondiente")
        else:
            messagebox.showinfo(title="Libro eliminado", message="Se ha eliminado el libro de la sección correspondiente")
    
    def realidadAumentada(self, imagen):
        ar.proyectar(imagen)