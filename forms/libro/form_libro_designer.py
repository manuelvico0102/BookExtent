import tkinter as tk
from tkinter import messagebox
from tkinter.font import BOLD
import util.generic as utl
from db.BD import BaseDatos

class FormLibroDesigner:

    def __init__(self, basedatos : BaseDatos, id_libro=None, id_usuario=None):
        self.id_libro = id_libro
        self.bd = basedatos
        self.id_usuario = id_usuario
    
        if(BaseDatos.existeLibro(self=self.bd, id_libro=self.id_libro)):
            #Traemos el libro || cambiar esto por una funcion
            self.libro = BaseDatos.obtenerLibro(self=self.bd, id_libro=self.id_libro)
            self.titulo_libro = self.libro[0][1]
            self.autor_libro = self.libro[0][2]
            self.desc_libro = BaseDatos.obtenerDescripcion(self=self.bd, id_libro=self.id_libro)
            self.desc_libro = self.desc_libro[0][0]
            self.imagen_libro = BaseDatos.descargarImagen(self=self.bd, id_libro=self.id_libro)
           

            self.ventana = tk.Toplevel()
            self.ventana.title("Libro")
            self.ventana.geometry('800x600')
            self.ventana.config(bg='#fcfcfc')
            self.ventana.resizable(width=0, height=0)   
            utl.centrar_ventana(self.ventana,800,600)
            

            # Pasar la imagen de CV2 --> PIL --> Imagen compatible con tkinter || Cambiar esto por una funcion que englobe las dos
            self.imagen_libro = utl.convertirCV2aPIL(self.imagen_libro)
            portada = utl.imagenResize(self.imagen_libro, (200, 300))

            # Panel izquierda logo
            frame_libro = tk.Frame(self.ventana, bd=0, width=300, relief=tk.SOLID, bg='black')
            frame_libro.pack(side="left", expand=tk.NO,fill=tk.BOTH)

            #panel izquierdo arriba
            frame_libro_top = tk.Frame(frame_libro, height=350, width=300, bd=0, relief=tk.SOLID, bg='black')
            frame_libro_top.pack(side="top", expand=tk.NO, fill=tk.BOTH)
            label = tk.Label(frame_libro_top, image=portada, bg='black', padx=40, pady=40)
            label.place(x=0, y=0, relwidth=1, relheight=1)
            
            #panel izquierdo abajo  
            frame_libro_fill  = tk.Frame(frame_libro, height=50, bd=0, relief=tk.SOLID, bg='black')
            frame_libro_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)

            favorito = tk.Button(frame_libro_fill, text="Guardar en Favoritos", font=('Times', 15, BOLD), fg="#fff", bd=0, bg="#7ed957", command=lambda: self.guardarCategoria(id_usuario=self.id_usuario, id_libro=self.id_libro, id_categoria='1'))
            favorito.pack(fill=tk.X, padx=20, pady=10)
            favorito.bind("<Return>", (lambda event: self.guardarCategoria(id_usuario=self.id_usuario, id_libro=self.id_libro, id_categoria='1')))  # Si le das al enter tambien llama a la funcion

            siguiendo = tk.Button(frame_libro_fill, text="Guardar en Siguiendo", font=('Times', 15, BOLD), fg="#fff", bd=0, bg="#7ed957", command=lambda: self.guardarCategoria(id_usuario=self.id_usuario, id_libro=self.id_libro, id_categoria='2'))
            siguiendo.pack(fill=tk.X, padx=20, pady=10)
            siguiendo.bind("<Return>", (lambda event: self.guardarCategoria(id_usuario=self.id_usuario, id_libro=self.id_libro, id_categoria='2')))  # Si le das al enter tambien llama a la funcion

            leido = tk.Button(frame_libro_fill, text="Guardar en Finalizados", font=('Times', 15, BOLD), fg="#fff", bd=0, bg="#7ed957", command=lambda: self.guardarCategoria(id_usuario=self.id_usuario, id_libro=self.id_libro, id_categoria='3'))
            leido.pack(fill=tk.X, padx=20, pady=10)
            leido.bind("<Return>", (lambda event: self.guardarCategoria(id_usuario=self.id_usuario, id_libro=self.id_libro, id_categoria='3')))  # Si le das al enter tambien llama a la funcion

            pendiente = tk.Button(frame_libro_fill, text="Guardar en Pendientes", font=('Times', 15, BOLD), fg="#fff", bd=0, bg="#7ed957", command=lambda: self.guardarCategoria(id_usuario=self.id_usuario, id_libro=self.id_libro, id_categoria='4'))
            pendiente.pack(fill=tk.X, padx=20, pady=10)
            pendiente.bind("<Return>", (lambda event: self.guardarCategoria(id_usuario=self.id_usuario, id_libro=self.id_libro, id_categoria='4')))  # Si le das al enter tambien llama a la funcion

            # Panel derecha
            frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
            frame_form.pack(side="right", expand=tk.YES,fill=tk.BOTH)

            # Panel derecha arriba
            frame_form_top = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='black')
            frame_form_top.pack(side="top", fill=tk.BOTH)
            title = tk.Label(frame_form_top, text=self.titulo_libro, font=('Times', 30), fg="#666a88", bg="#fcfcfc", pady=50)
            title.pack(expand=tk.YES, fill=tk.BOTH)

            # Panel derecha abajo
            frame_form_fill  = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='#fcfcfc')
            frame_form_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)

            etiqueta_autor = tk.Label(frame_form_fill, text="Autor:", font=('Times', 14), fg="black", bg="#fcfcfc", anchor="w")
            etiqueta_autor.pack(fill=tk.X, padx=20, pady=5)
            etiqueta_autor_nombre = tk.Label(frame_form_fill, text=self.autor_libro, font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
            etiqueta_autor_nombre.pack(fill=tk.X, padx=40, pady=10)

            etiqueta_descripcion = tk.Label(frame_form_fill, text="Descripción:", font=('Times', 14), fg="black", bg="#fcfcfc", anchor="w")
            etiqueta_descripcion.pack(fill=tk.X, padx=20, pady=0)
            etiqueta_descripcion_texto = tk.Text(frame_form_fill, font=('Times', 14), fg="#666a88", bg="#fcfcfc", wrap="word", height=10, borderwidth=0, highlightthickness=0)
            etiqueta_descripcion_texto.pack(fill=tk.X, padx=40, pady=0, expand=tk.YES)
            etiqueta_descripcion_texto.insert(tk.END, self.desc_libro)
            etiqueta_descripcion_texto.configure(state='disabled')

            ar = tk.Button(frame_form_fill, text="Realidad Aumentada", font=('Times', 15, BOLD), fg="#fff", bd=0, bg="black", command=self.realidadAumentada)
            ar.pack(fill=tk.X, padx=20, pady=5)
            ar.bind("<Return>", (lambda event: self.realidadAumentada()))  # Si le das al enter tambien llama a la funcion
            
            b_imagen = tk.Button(frame_form_fill, text="Cambiar imagen", font=('Times', 15, BOLD), fg="#fff", bd=0, bg="black", command=self.subirImagen)
            b_imagen.pack(fill=tk.X, padx=20, pady=5)
            b_imagen.bind("<Return>", (lambda event: self.subirImagen()))  # Si le das al enter tambien llama a la funcion

            self.ventana.mainloop()
        else: 
            messagebox.showerror(message="El libro no existe", title="Mensaje")
    
    def guardarCategoria(self, id_usuario, id_libro, id_categoria):
        pass

    def realidadAumentada(self):
        pass

    def subirImagen(self):
        pass