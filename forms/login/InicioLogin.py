from forms.login.form_login import FormLogin
from forms.master.form_master import MasterPanel
from util.reconocimiento import reconocimientoFacial
from db.BD import BaseDatos
import cv2

class inicioLogin():
    def __init__(self, basedatos : BaseDatos):
        self.bd = basedatos
        ids, nombres, rostrocod = self.bd.obtenerTodasCodificaciones()
        id = reconocimientoFacial(ids, rostrocod)
        cv2.destroyAllWindows()    
        if id is not None:
            MasterPanel(basedatos=self.bd, id_usuario=id)
        else:
            FormLogin(basedatos=self.bd)

