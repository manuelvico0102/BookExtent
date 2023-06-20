"""
    Archivo con la parte de la funcionalidad de la ventana de registro.

    Autor: Manuel Vico Arboledas.
"""

from forms.register.form_register_designer import FormRegisterDesigner
from db.BD import BaseDatos
from tkinter import messagebox
import util.encoding_decoding as end_dec
import tkinter as tk
from forms.master.form_master import MasterPanel
from util.reconocimiento import capturarFoto, CrearUsuarioConFoto

class FormRegister(FormRegisterDesigner):
    """
    Clase que representa la ventana de registro

    Atributos:
        ventana: ventana de registro
        usuario: campo de texto para introducir el usuario
        password: campo de texto para introducir la contraseña
        confirmacion: campo de texto para introducir la confirmación de la contraseña
        bd: objeto de la clase BaseDatos
    """
    def __init__(self, basedatos : BaseDatos):
        """
        Constructor de la clase

        Args:
            basedatos (obj): Objeto de la clase BaseDatos
        """
        self.bd = basedatos
        super().__init__(basedatos=self.bd)

    def register(self):
        """
        Método que registra un usuario
        """
        usuario_db = self.bd.obtenerUsuario(username=self.usuario.get())
        if not (self.existeUsuario(usuario_db)):
            if(self.coincideContrasenia()):
                contra = end_dec.encrypted(self.password.get())
                usu = self.usuario.get()
                imagen = capturarFoto()
                #Faltaria hacer una comprobacion de que la foto es una cara
                if(CrearUsuarioConFoto(bd=self.bd, usuario=usu, contra=contra, img=imagen)):
                    #self.bd.insertarUsuario(username=usu, password=contra)
                    messagebox.showinfo(message="Se registro el usuario correctamente", title="Mensaje")
                    self.ventana.destroy()
                    usuario_db = self.bd.obtenerUsuario(username=usu)
                    MasterPanel(basedatos=self.bd, id_usuario=usuario_db[0][0])
                else:
                    messagebox.showerror(message="No se ha detectado ninguna cara", title="Mensaje")

    def coincideContrasenia(self):
        """
        Método que verifica si la contraseña coincide

        Returns:
            bool: True si la contraseña coincide, False si no coincide
        """
        estado: bool = True
        if(self.password.get() != self.confirmacion.get()):
            estado = False
            messagebox.showerror(message="La contraseña no coincide", title="Mensaje")
            self.password.delete(0, tk.END)
            self.confirmacion.delete(0, tk.END)
        return estado
    
    def existeUsuario(self, usuario):
        """
        Método que verifica si el usuario existe
        
        Args:
            usuario (list): Lista de usuarios
        
        Returns:
            bool: True si el usuario existe, False si no existe
        """
        estado: bool = False
        if(usuario):
            estado = True
            messagebox.showerror(message="El usuario ya existe", title="Mensaje")
        return estado 
    
    
    