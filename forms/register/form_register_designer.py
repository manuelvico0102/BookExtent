import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD
import util.generic as utl



class FormRegisterDesigner():

    def __init__(self, basedatos):
        self.ventana = tk.Toplevel()
        self.ventana.title("Registro")
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)   
        utl.centrar_ventana(self.ventana,600,480)

        logo = utl.leer_imagen("./imagenes/BE_sinfondo.png", (180, 180))

        # Panel izquierda logo
        frame_logo = tk.Frame(self.ventana, bd=0, width=200, relief=tk.SOLID, padx=10, pady=10, bg='#7ed957')
        frame_logo.pack(side="left", expand=tk.NO,fill=tk.BOTH)
        label = tk.Label(frame_logo, image=logo, bg='#7ed957')
        label.place(x=0, y=0, relwidth=1, relheight=1)

        # Panel derecha
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right", expand=tk.YES,fill=tk.BOTH)

        # Panel derecha arriba
        frame_form_top = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack(side="top", fill=tk.BOTH)
        title = tk.Label(frame_form_top, text="Registro de usuario", font=('Times', 30), fg="#666a88", bg="#fcfcfc", pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)

        # Panel derecha abajo
        frame_form_fill  = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)

        etiqueta_usuario = tk.Label(frame_form_fill, text="Usuario", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_usuario.pack(fill=tk.X, padx=20, pady=5)
        self.usuario = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.usuario.pack(fill=tk.X, padx=20, pady=10)

        etiqueta_password = tk.Label(frame_form_fill, text="Contraseña", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_password.pack(fill=tk.X, padx=20, pady=5)
        self.password = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.password.pack(fill=tk.X, padx=20, pady=10)
        self.password.config(show="*")

        etiqueta_confirmacion = tk.Label(frame_form_fill, text="Confirmación", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_confirmacion.pack(fill=tk.X, padx=20, pady=5)
        self.confirmacion = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.confirmacion.pack(fill=tk.X, padx=20, pady=10)
        self.confirmacion.config(show="*")
        self.confirmacion.bind("<Return>", (lambda event: self.verificar()))  # Si le das al enter tambien llama a la funcion

        register = tk.Button(frame_form_fill, text="Registrar", font=('Times', 15, BOLD), fg="#7ed957", bd=0, bg="#fcfcfc", command=self.register)
        register.pack(fill=tk.X, padx=20, pady=20)
        register.bind("<Return>", (lambda event: self.register()))  # Si le das al enter tambien llama a la funcion

        self.ventana.mainloop()
    
    def register():
        pass
