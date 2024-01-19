"""
    Archivo para ejecutar la aplicación.

    Autor: Manuel Vico Arboledas.
"""

from db.BD import BaseDatos
from forms.login.InicioLogin import inicioLogin
import os
from dotenv import load_dotenv

load_dotenv()
# Establezco conexion a la base de datos
usuario = os.environ.get("usuario")
password = os.environ.get("password")
dsn = os.environ.get("dsn")
bd = BaseDatos(usuario=usuario, password=password, dsn=dsn)

if BaseDatos.conexion(self=bd):
    inicioLogin(basedatos=bd)

# Se cierra conexion a la base de datos
BaseDatos.desconexion(self=bd)

