"""
    Archivo para el reconocimiento facial para ingresar a la aplicación.

    Autor: Manuel Vico Arboledas.
"""

from forms.login.form_login import FormLogin
from forms.master.form_master import MasterPanel
from util.reconocimiento import reconocimientoFacial
from db.BD import BaseDatos
import cv2

class inicioLogin():
    """
    Clase que representa el inicio de sesión por faceID al iniciar la aplicación
    Al iniciair la aplicación se ejecuta el reconocimiento facial, si el usuario existe se abre la ventana principal,
    si no existe o no se reconoce se abre la ventana de inicio de sesión

    Atributos:
        bd: objeto de la clase BaseDatos
    """
    def __init__(self, basedatos : BaseDatos):
        """
        Constructor de la clase

        Args:
            basedatos (obj): Objeto de la clase BaseDatos
        """
        self.bd = basedatos
        ids, nombres, rostrocod = self.bd.obtenerTodasCodificaciones()
        id = reconocimientoFacial(ids, rostrocod)
        cv2.destroyAllWindows()    
        if id is not None:
            MasterPanel(basedatos=self.bd, id_usuario=id)
        else:
            FormLogin(basedatos=self.bd)

