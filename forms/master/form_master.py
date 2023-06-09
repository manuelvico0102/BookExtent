from forms.master.form_master_designer import MasterPanelDesigner
from db.BD import BaseDatos
from forms.libro.form_libro import FormLibro

class MasterPanel(MasterPanelDesigner):
    def __init__(self, basedatos : BaseDatos, id_usuario):
        super().__init__(basedatos=basedatos, id_usuario=id_usuario)
    
    def obtenerNombre(self, id_usuario):
        return self.bd.obtenerUsername(id_usuario=id_usuario)

    def verLibros(self):
        self.categoriaActual = "Libros"
        self.lcategoria.config(text=self.categoriaActual)
        self.lista.delete(*self.lista.get_children())
        libros = self.bd.obtenerLibros()
        
        contador = 0
        for i in libros:
            etiqueta = "FilaPar.Treeview" if contador % 2 == 0 else "FilaImpar.Treeview"
            self.lista.insert('', 'end', values=i, tags=(etiqueta,))
            contador += 1
    
    def verCategoria(self, id_usuario, categoria):
        self.categoriaActual = categoria
        self.lcategoria.config(text=self.categoriaActual)
        self.lista.delete(*self.lista.get_children())
        libros = self.bd.obtenerLibrosCategoria(id_usuario=id_usuario, categoria=categoria)
        for i in libros:
            self.lista.insert('', 'end', values=i)
    
    def buscar(self):
        self.categoriaActual = "Libros"
        self.lcategoria.config(text=self.categoriaActual)
        where = " where 1=1 "
        if(len(self.buscador.get()) > 0):
            texto = self.buscador.get().upper()
            where = where + " and (titulo LIKE '%" + texto +"%' or autor LIKE '%" + texto +"%') "

        self.lista.delete(*self.lista.get_children())
        libros = self.bd.obtenerLibros(where)

        for i in libros:
            self.lista.insert('', 'end', values=i)

    def doble_clic(self, event):
        seleccion = self.lista.selection()
        if(seleccion):
            item = self.lista.item(seleccion[0])
            id_celda = item['values'][0]
            FormLibro(basedatos=self.bd, id_libro=str(id_celda), id_usuario=str(self.id_usuario))     
    





    
        