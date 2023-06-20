"""
    Archivo con la parte de la funcionalidad de la ventana de inicio de sesión.

    Autor: Manuel Vico Arboledas.
"""

from tkinter import messagebox
from forms.master.form_master import MasterPanel
from forms.login.form_login_designer import FormLoginDesigner
from db.BD import BaseDatos
import util.encoding_decoding as end_dec
from forms.register.form_register import FormRegister
from util.reconocimiento import reconocimientoFacial
import cv2

class FormLogin(FormLoginDesigner):
    """
    Clase que representa la ventana de inicio de sesión
    
    Atributos:
        ventana: ventana de inicio de sesión
        usuario: campo de texto para introducir el usuario
        password: campo de texto para introducir la contraseña
        bd: objeto de la clase BaseDatos
    """
    def __init__(self, basedatos : BaseDatos):
        """
        Constructor de la clase
        
        Args:
            basedatos (obj): Objeto de la clase BaseDatos
        """
        self.ventana = None
        self.bd = basedatos
        super().__init__(basedatos=self.bd)
    
    def verificar(self):
        """
        Método que verifica si el usuario existe y si la contraseña es correcta
        """
        usuario_db = self.bd.obtenerUsuario(username=self.usuario.get())
        if(self.existeUsuario(usuario_db)):
            self.existeContraseña(self.password.get(), usuario_db)
    
    def existeUsuario(self, usuario):
        """
        Método que verifica si el usuario existe

        Args:
            usuario (list): Lista de usuarios
        
        Returns:
            bool: True si el usuario existe, False si no existe
        """
        estado: bool = True
        if(not usuario):
            estado = False
            messagebox.showerror(message="El usuario no existe, por favor registrese", title="Mensaje")
        return estado 
    
    def userRegister(self):
        """
        Método que abre la ventana de registro
        """
        self.ventana.destroy()
        FormRegister(basedatos=self.bd)

    def existeContraseña(self, password, usuario):
        """
        Método que verifica si la contraseña es correcta

        Args:
            password (str): Contraseña introducida por el usuario
            usuario (list): Lista de usuarios
        """
        #usuario es una lista de usuarios aunque solo tenga un usuario por lo que 0, y 2 porque es la columna de la contraseña
        b_password = end_dec.decrypt(usuario[0][2])
        if(password == b_password):
           self.ventana.destroy()
           MasterPanel(basedatos=self.bd, id_usuario=usuario[0][0])
        else: 
            messagebox.showerror(message="El usuario y la contraseña no coincide", title="Mensaje")
    
    def inicioFaceid(self):
        """
        Método que inicia el reconocimiento facial
        """
        ids, nombres, rostrocod = self.bd.obtenerTodasCodificaciones()
        id = reconocimientoFacial(ids, rostrocod)
        
        if id is not None:
            if self.ventana is not None:
                self.ventana.destroy()
            MasterPanel(basedatos=self.bd, id_usuario=id)
        else: 
            cv2.destroyAllWindows()
        
        
