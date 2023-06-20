"""
    Archivo para ejecutar la aplicación.

    Autor: Manuel Vico Arboledas.
"""

from db.BD import BaseDatos
from forms.login.InicioLogin import inicioLogin

# Establezco conexion a la base de datos
bd = BaseDatos(usuario="x6520114", password="x6520114", dsn="oracle0.ugr.es:1521/practbd.oracle0.ugr.es")

if BaseDatos.conexion(self=bd):
    inicioLogin(basedatos=bd)

# Se cierra conexion a la base de datos
BaseDatos.desconexion(self=bd)

