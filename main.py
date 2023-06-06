from forms.login.form_login import FormLogin
from db.BD import BaseDatos
from util.reconocimiento import reconocimientoFacial
from threading import Thread, Event, Lock
from util.speech import main
from forms.login.InicioLogin import inicioLogin

# Establezco conexion a la base de datos
bd = BaseDatos(usuario="x6520114", password="x6520114", dsn="oracle0.ugr.es:1521/practbd.oracle0.ugr.es")
BaseDatos.conexion(self=bd)
"""salir = Event()
matriz = [[None, None] for _ in range(10)]
h1 = Thread(target=FormLogin, args=[bd])
##h2 = Thread(target=main, args=[salir])

h1.start()
#h2.start()

h1.join()
salir.set()
#h2.join()"""
# Le paso la base de datos al login, y así sucesivamente con todo
#FormLogin(basedatos=bd)
inicioLogin(basedatos=bd)
#ids, nombres, rostrocod = bd.obtenerTodasCodificaciones()
#id = reconocimientoFacial(ids, rostrocod)
# Se cierra conexion a la base de datos
BaseDatos.desconexion(self=bd)



