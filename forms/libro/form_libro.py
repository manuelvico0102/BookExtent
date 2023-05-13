import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from forms.master.form_master_designer import MasterPanel
from db.BD import BaseDatos
import util.encoding_decoding as end_dec
from forms.libro.form_libro_designer import FormLibroDesigner
from tkinter import filedialog

class FormLibro(FormLibroDesigner):
    def __init__(self, id_libro=None):
        super().__init__(id_libro)

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
    
