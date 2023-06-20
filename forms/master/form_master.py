"""
    Archivo con la parte de la funcionalidad de la ventana principal.

    Autor: Manuel Vico Arboledas.
"""

from forms.master.form_master_designer import MasterPanelDesigner
from db.BD import BaseDatos
from forms.libro.form_libro import FormLibro

class MasterPanel(MasterPanelDesigner):
    """
    Clase que representa la ventana principal, parte de ejecución

    Atributos:
        ventana: ventana principal
        bd: objeto de la clase BaseDatos
        id_usuario: id del usuario
        nombre: nombre del usuario
        categoriaActual: categoria actual
        lcategoria: label de la categoria actual
        lista: lista de libros
        buscador: campo de texto para buscar libros
    """
    def __init__(self, basedatos : BaseDatos, id_usuario):
        """
        Constructor de la clase

        Args:
            basedatos (obj): Objeto de la clase BaseDatos
            id_usuario (int): Id del usuario
        """
        super().__init__(basedatos=basedatos, id_usuario=id_usuario)
    
    def obtenerNombre(self, id_usuario):
        """
        Método que obtiene el nombre del usuario

        Args:
            id_usuario (int): Id del usuario
        """
        return self.bd.obtenerUsername(id_usuario=id_usuario)

    def verLibros(self):
        """
        Método que muestra todos los libro
        """
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
        """
        Método que muestra los libros de una categoría

        Args:
            id_usuario (int): Id del usuario
            categoria (str): Categoría
        """
        self.categoriaActual = categoria
        self.lcategoria.config(text=self.categoriaActual)
        self.lista.delete(*self.lista.get_children())
        libros = self.bd.obtenerLibrosCategoria(id_usuario=id_usuario, categoria=categoria)
        for i in libros:
            self.lista.insert('', 'end', values=i)
    
    def buscar(self):
        """
        Método que busca libros, según el texto introducido en el buscador busca las coincidencias
        en el título y autor. La busqueda se hace sobre todos los libros.

        Args:
            id_usuario (int): Id del usuario
            categoria (str): Categoría
        """
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
        """
        Método que se ejecuta al hacer doble clic sobre un libro de la lista, abre la ventana del libro

        Args:
            event (obj): Evento
        """
        seleccion = self.lista.selection()
        if(seleccion):
            item = self.lista.item(seleccion[0])
            id_celda = item['values'][0]
            #self.hebraLibro = Thread(target=reconocimiento_voz, args=[self, ventana], daemon=True)
            #self.hebraLibro = Thread(target=FormLibro, args=[self.bd, str(id_celda), str(self.id_usuario)], daemon=True)
            #self.hebraLibro.start()
            FormLibro(basedatos=self.bd, id_libro=str(id_celda), id_usuario=str(self.id_usuario))

    





    
        