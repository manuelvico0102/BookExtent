from forms.master.form_master_designer import MasterPanelDesigner
from db.BD import BaseDatos

class MasterPanel(MasterPanelDesigner):
    def __init__(self, id_usuario):
        super().__init__(id_usuario=id_usuario)
    
    def obtenerNombre(self, id_usuario):
        return self.bd.obtenerUsername(id_usuario=id_usuario)

    def verLibros(self):
        self.lista.delete(*self.lista.get_children())
        libros = self.bd.obtenerLibros()
        for i in libros:
            self.lista.insert('', 'end', values=i)
    
    
    def verFavoritos(self, id_usuario):
        self.lista.delete(*self.lista.get_children())
        libros = self.bd.obtenerLibrosFavoritos(id_usuario=id_usuario)
        for i in libros:
            self.lista.insert('', 'end', values=i)
    
    def verSiguiendo(self, id_usuario):
        self.lista.delete(*self.lista.get_children())
        libros = self.bd.obtenerLibrosSiguiendo(id_usuario=id_usuario)
        for i in libros:
            self.lista.insert('', 'end', values=i)
    
    def verPendientes(self, id_usuario):
        self.lista.delete(*self.lista.get_children())
        libros = self.bd.obtenerLibrosPendiente(id_usuario=id_usuario)
        for i in libros:
            self.lista.insert('', 'end', values=i)
    
    def verLeido(self, id_usuario):
        self.lista.delete(*self.lista.get_children())
        libros = self.bd.obtenerLibrosLeido(id_usuario=id_usuario)
        for i in libros:
            self.lista.insert('', 'end', values=i)



    
        