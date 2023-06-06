import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD
import util.generic as utl
from threading import Thread
import cv2

class FormLoginDesigner:

    def __init__(self, basedatos):   
        self.ventana = tk.Tk()
        self.ventana.title("Inicio de sesión")
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)   
        utl.centrar_ventana(self.ventana,800,500)

        logo = utl.leer_imagen("./imagenes/BE_sinfondo.png", (200, 200))

        # Panel izquierda logo
        frame_logo = tk.Frame(self.ventana, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10, bg='black')
        frame_logo.pack(side="left", expand=tk.NO,fill=tk.BOTH)
        label = tk.Label(frame_logo, image=logo, bg='black')
        label.place(x=0, y=0, relwidth=1, relheight=1)

        # Panel derecha
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right", expand=tk.YES,fill=tk.BOTH)

        # Panel derecha arriba
        frame_form_top = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack(side="top", fill=tk.BOTH)
        title = tk.Label(frame_form_top, text="Inicio de sesión", font=('Times', 30), fg="#666a88", bg="#fcfcfc", pady=50)
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
        self.password.bind("<Return>", (lambda event: self.verificar()))  # Si le das al enter tambien llama a la funcion

        faceid = tk.Button(frame_form_fill, text="Face ID", font=('Times', 10, BOLD), fg="black", bd=0, bg="#fcfcfc", command=self.inicioFaceid)
        faceid.pack(fill=tk.X, padx=20, pady=0)
        faceid.bind("<Return>", (lambda event: self.inicioFaceid()))  # Si le das al enter tambien llama a la funcion

        inicio = tk.Button(frame_form_fill, text="Iniciar Sesión", font=('Times', 15, BOLD), fg="#fff", bd=0, bg="black", command=self.verificar)
        inicio.pack(fill=tk.X, padx=20, pady=20)
        inicio.bind("<Return>", (lambda event: self.verificar()))  # Si le das al enter tambien llama a la funcion

        registro = tk.Button(frame_form_fill, text="Registrar usuario", font=('Times', 15, BOLD), fg="black", bd=0, bg="#fcfcfc", command=self.userRegister)
        registro.pack(fill=tk.X, padx=20, pady=20)
        registro.bind("<Return>", (lambda event: self.userRegister()))  # Si le das al enter tambien llama a la funcion

        self.ventana.mainloop()
    
    def verificar(self):
        pass

    def userRegister(self):
        pass

    def inicioFaceid(self):
        pass
