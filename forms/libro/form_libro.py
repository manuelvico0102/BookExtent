from tkinter import messagebox
from db.BD import BaseDatos
from forms.libro.form_libro_designer import FormLibroDesigner
from tkinter import filedialog

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
    
