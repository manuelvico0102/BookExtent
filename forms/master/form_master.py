from forms.master.form_master_designer import MasterPanelDesigner
from db.BD import BaseDatos

class MasterPanel(MasterPanelDesigner):
    def __init__(self, basedatos : BaseDatos, id_usuario):
        super().__init__(basedatos=basedatos, id_usuario=id_usuario)
    
    def obtenerNombre(self, id_usuario):
        return self.bd.obtenerUsername(id_usuario=id_usuario)

    def verLibros(self):
        self.lista.delete(*self.lista.get_children())
        libros = self.bd.obtenerLibros()
        for i in libros:
            self.lista.insert('', 'end', values=i)
    
    
    def verFavoritos(self, id_usuario):
        self.lista.delete(*self.lista.get_children())
        libros = self.bd.obtenerLibrosCategoria(id_usuario=id_usuario, categoria='Favoritos')
        for i in libros:
            self.lista.insert('', 'end', values=i)
    
    def verSiguiendo(self, id_usuario):
        self.lista.delete(*self.lista.get_children())
        libros = self.bd.obtenerLibrosCategoria(id_usuario=id_usuario, categoria='Siguiendo')
        for i in libros:
            self.lista.insert('', 'end', values=i)
    
    def verPendientes(self, id_usuario):
        self.lista.delete(*self.lista.get_children())
        libros = self.bd.obtenerLibrosCategoria(id_usuario=id_usuario, categoria='Pendiente')
        for i in libros:
            self.lista.insert('', 'end', values=i)
    
    def verFinalizados(self, id_usuario):
        self.lista.delete(*self.lista.get_children())
        libros = self.bd.obtenerLibrosCategoria(id_usuario=id_usuario, categoria='Leido')
        for i in libros:
            self.lista.insert('', 'end', values=i)



    
        