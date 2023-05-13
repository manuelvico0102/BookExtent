import tkinter as tk
from tkinter.font import BOLD
import util.generic as utl

class MasterPanelDesigner:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('BookExtent')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()
        
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        logo = utl.leer_imagen("./imagenes/BE_sinfondo.png", (40, 40))

        # Panel superior 
        frame_top = tk.Frame(self.ventana, height=50, bd=0, relief=tk.SOLID, bg='gray')
        frame_top.pack(side="top", fill=tk.BOTH)

        frame_top_left = tk.Frame(frame_top, bd=0, relief=tk.SOLID, bg='gray')
        frame_top_left.pack(side="left", fill=tk.BOTH, expand=tk.NO)
        lLogo = tk.Label(frame_top_left, image=logo, bg='gray')
        lLogo.grid(row=0, column=0, sticky='w', padx=10)

        self.lUsuario = tk.Label(frame_top_left, text="username", font=('Times', 14), fg="black", bg="gray")
        self.lUsuario.grid(row=0, column=1, sticky='e')
 
        frame_top_left.grid_columnconfigure(0, minsize=50)
        frame_top_left.grid_columnconfigure(1,minsize=150)

        # Panel izquierdo menu
        frame_menu = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='black')
        frame_menu.pack(side="left", expand=tk.NO,fill=tk.BOTH)
        
        bLibros = tk.Button(frame_menu, text="Libros", font=('Times', 15, BOLD), fg="#fff", bd=0, bg="black", anchor="w", padx=20, command=self.verLibros)
        bLibros.grid(row=0, column=0, pady=10, sticky='nsew')
        bLibros.bind("<Return>", (lambda event: self.verLibros()))  # Si le das al enter tambien llama a la funcion

        bFavoritos = tk.Button(frame_menu, text="Favoritos", font=('Times', 15, BOLD), fg="#fff", bd=0, bg="black", anchor="w", padx=20, command=self.verLibros)
        bFavoritos.grid(row=1, column=0, pady=10, sticky='nsew')
        bFavoritos.bind("<Return>", (lambda event: self.verLibros()))  # Si le das al enter tambien llama a la funcion

        bSiguiendo = tk.Button(frame_menu, text="Siguiendo", font=('Times', 15, BOLD), fg="#fff", bd=0, bg="black", anchor="w", padx=20, command=self.verLibros)
        bSiguiendo.grid(row=2, column=0, pady=10, sticky='nsew')
        bSiguiendo.bind("<Return>", (lambda event: self.verLibros()))  # Si le das al enter tambien llama a la funcion

        bPendientes = tk.Button(frame_menu, text="Pendientes", font=('Times', 15, BOLD), fg="#fff", bd=0, bg="black", anchor="w", padx=20, command=self.verLibros)
        bPendientes.grid(row=3, column=0, pady=10, sticky='nsew')
        bPendientes.bind("<Return>", (lambda event: self.verLibros()))  # Si le das al enter tambien llama a la funcion

        bFinalizados = tk.Button(frame_menu, text="Finalizados", font=('Times', 15, BOLD), fg="#fff", bd=0, bg="black", anchor="w", padx=20, command=self.verLibros)
        bFinalizados.grid(row=4, column=0, pady=10, sticky='nsew')
        bFinalizados.bind("<Return>", (lambda event: self.verLibros()))  # Si le das al enter tambien llama a la funcion

        frame_menu.grid_columnconfigure(0, minsize=220)
        
        """
        bFavoritos = tk.Button(frame_menu, text="Favoritos", font=('Times', 15, BOLD), fg="#fff", bd=0, bg="black", command=self.verLibros)
        bFavoritos.pack(fill=tk.X,padx=20, pady=20)
        bFavoritos.bind("<Return>", (lambda event: self.verLibros()))  # Si le das al enter tambien llama a la funcion
        """
        # Panel derecha
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right", expand=tk.YES,fill=tk.BOTH)
        
        self.ventana.mainloop()
    
    def verLibros(self):
        self.lUsuario.config(text="holaaaa")

    def conexion(self):
        pass

    def desconexion(self):
        pass