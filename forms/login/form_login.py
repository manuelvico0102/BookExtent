import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from forms.master.form_master import MasterPanel
from forms.login.form_login_designer import FormLoginDesigner
from db.BD import BaseDatos
import util.encoding_decoding as end_dec
from forms.register.form_register import FormRegister


class FormLogin(FormLoginDesigner):

    def __init__(self):
        self.BaseDatos = BaseDatos(usuario="x6520114", password="x6520114", dsn="oracle0.ugr.es:1521/practbd.oracle0.ugr.es")
        BaseDatos.conexion(self=self.BaseDatos)
        super().__init__()
    
    def verificar(self):
        usuario_db = BaseDatos.obtenerUsuario(self=self.BaseDatos, username=self.usuario.get())
        if(self.existeUsuario(usuario_db)):
            self.existeContraseña(self.password.get(), usuario_db)
    
    def existeUsuario(self, usuario):
        estado: bool = True
        if(not usuario):
            estado = False
            messagebox.showerror(message="El usuario no existe, por favor registrese", title="Mensaje")
        return estado 
    
    def userRegister(self):
        FormRegister().mainloop()

    def existeContraseña(self, password, usuario):
        #usuario es una lista de usuarios aunque solo tenga un usuario por lo que 0, y 2 porque es la columna de la contraseña
        b_password = end_dec.decrypt(usuario[0][2])
        if(password == b_password):
           self.ventana.destroy()
           BaseDatos.desconexion(self=self.BaseDatos)
           MasterPanel(usuario[0][0])
        else: 
            messagebox.showerror(message="El usuario y la contraseña no coincide", title="Mensaje")
