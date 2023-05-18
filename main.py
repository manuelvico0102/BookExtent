from forms.login.form_login import FormLogin
from db.BD import BaseDatos

# Establezco conexion a la base de datos
bd = BaseDatos(usuario="x6520114", password="x6520114", dsn="oracle0.ugr.es:1521/practbd.oracle0.ugr.es")
BaseDatos.conexion(self=bd)

# Le paso la base de datos al login, y así sucesivamente con todo
FormLogin(basedatos=bd)

# Se cierra conexion a la base de datos
BaseDatos.desconexion(self=bd)
