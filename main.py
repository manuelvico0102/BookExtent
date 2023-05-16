from forms.login.form_login import FormLogin
from db.BD import BaseDatos
# Establezco conexion a la base de datos
bd = BaseDatos(usuario="x6520114", password="x6520114", dsn="oracle0.ugr.es:1521/practbd.oracle0.ugr.es")
BaseDatos.conexion(self=bd)

# Le paso la base de datos al login, y así sucesivamente con todo
FormLogin(basedatos=bd)

# Se cierra conexion a la base de datos
BaseDatos.desconexion(self=bd)
"""
from forms.master.form_master import MasterPanel
MasterPanel(id_usuario='5')"""

"""
from db.BD import BaseDatos
from forms.libro.form_libro import FormLibro
bd = BaseDatos(usuario="x6520114", password="x6520114", dsn="oracle0.ugr.es:1521/practbd.oracle0.ugr.es")
BaseDatos.conexion(self=bd)
BaseDatos.cargarImagen(self=bd, ruta='C:/Users/Manuel Vico/Desktop/CUIA/Practicas/Proyecto/Interfaz/imagenes/laespadadeldestino.jpeg', id_libro='13')
BaseDatos.desconexion(self=bd)
FormLibro(id_libro='12')"""