from forms.register.form_register_designer import FormRegisterDesigner
from db.BD import BaseDatos
from tkinter import messagebox
import util.encoding_decoding as end_dec
import tkinter as tk

class FormRegister(FormRegisterDesigner):
    def __init__(self, basedatos : BaseDatos):
        #self.BaseDatos = BaseDatos(usuario="x6520114", password="x6520114", dsn="oracle0.ugr.es:1521/practbd.oracle0.ugr.es")
        #BaseDatos.conexion(self=self.BaseDatos)
        self.bd = basedatos
        super().__init__(basedatos=self.bd)

    def register(self):
        #usuario_db = BaseDatos.obtenerUsuario(self=self.BaseDatos, username=self.usuario.get())
        usuario_db = self.bd.obtenerUsuario(username=self.usuario.get())
        if not (self.existeUsuario(usuario_db)):
            if(self.coincideContrasenia()):
                contra = end_dec.encrypted(self.password.get())
                usu = self.usuario.get()
                #BaseDatos.insertarUsuario(self=self.BaseDatos, username=usu, password=contra)
                self.bd.insertarUsuario(username=usu, password=contra)
                messagebox.showinfo(message="Se registro el usuario correctamente", title="Mensaje")
                self.ventana.destroy()
                #BaseDatos.desconexion(self=self.BaseDatos)

    def coincideContrasenia(self):
        estado: bool = True
        if(self.password.get() != self.confirmacion.get()):
            estado = False
            messagebox.showerror(message="La contraseña no coincide", title="Mensaje")
            self.password.delete(0, tk.END)
            self.confirmacion.delete(0, tk.END)
        return estado
    
    def existeUsuario(self, usuario):
        estado: bool = False
        if(usuario):
            estado = True
            messagebox.showerror(message="El usuario ya existe", title="Mensaje")
        return estado 
    
    
    