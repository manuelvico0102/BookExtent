import speech_recognition as sr
import cv2
import numpy as np
import face_recognition as fr
import os
import random
from db.BD import BaseDatos
from forms.master.form_master import MasterPanel
import time

# Necesito una hebra para el microfono
def capturarFoto():
    cam = cv2.VideoCapture(0)
    ret, imagen = cam.read()
    cam.release()
    return imagen

# Llamar a la función para capturar una foto cuando se diga "foto"
# capturarFoto()

def CrearUsuarioConFoto(bd, usuario, contra, img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    caras_detectadadas = fr.face_locations(img)
    if len(caras_detectadadas) > 0:
        cod = fr.face_encodings(img)[0]
        # Convertir la codificación de la imagen a bytes
        imagen_codificada = np.array(cod).tobytes()
        BaseDatos.insertarUsuarioFoto(self=bd, username=usuario, password=contra, imagen=imagen_codificada)
        return True
    else:
        return False

def codificarFoto(bd, idusuario, ruta):
    img = cv2.imread(ruta)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cod = fr.face_encodings(img)[0]
    # Convertir la codificación de la imagen a bytes
    imagen_codificada = np.array(cod).tobytes()
    BaseDatos.subirImagenCodificada(self=bd, idusuario=idusuario, cod=imagen_codificada)


"""
# Establezco conexion a la base de datos
bd = BaseDatos(usuario="x6520114", password="x6520114", dsn="oracle0.ugr.es:1521/practbd.oracle0.ugr.es")
BaseDatos.conexion(self=bd)

codificarFoto(bd=bd, idusuario="1", ruta="Personal\FOTO.jpg")

# Se cierra conexion a la base de datos
BaseDatos.desconexion(self=bd)"""


def reconocimientoFacial(ids, rostroscod):
    # Variables
    id = None
    comp1 = 100
    fin = False

    # Realizamos video captura
    cap = cv2.VideoCapture(0)

    tiempo_inicio = time.time()
    tiempo_limite = 5  # 5 segundos
    # Empezamos
    while True:

        tiempo_actual = time.time()
        tiempo_transcurrido = tiempo_actual - tiempo_inicio
        if tiempo_transcurrido >= tiempo_limite:
            break
        # Leemos los fotogramas
        ret, frame = cap.read()

        # Reducimos las imagenes para mejorar el procesamiento
        frame2 = cv2.resize(frame, (0, 0), None, 0.25, 0.25)

        # Convertimos de color
        rgb = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)

        # Buscamos los rostros
        faces = fr.face_locations(rgb)
        facescod = fr.face_encodings(rgb, faces)

         # Iteramos
        for facecod, faceloc in zip(facescod, faces):
            
            # Comparamos rostro de DB con rostro en tiempo real
            comparacion = fr.compare_faces(rostroscod, facecod)

            # Calculamos la similitud
            simi = fr.face_distance(rostroscod, facecod)
            #print(simi)
            # Buscamos el valor más bajo
            min = np.argmin(simi)

            if comparacion[min]:
                id = ids[min]
                """nombre = nombres[min].upper()
                # Extraemos las coordenadas
                yi, xf, yf, xi = faceloc
                # Escalamos las coordenadas
                yi, xf, yf, xi = yi*4, xf*4, yf*4, xi*4

                indice = comparacion.index(True)

                # Comparamos
                if comp1 != indice:
                    # Para dibujar cambiamos colores
                    r = random.randrange(0, 255, 50)
                    g = random.randrange(0, 255, 50)
                    b = random.randrange(0, 255, 50)   

                    comp1 = indice
                
                if comp1 == indice:
                    # Dibujamos
                    #cv2.rectangle(frame, (xi, yi), (xf, yf), (r, g, b), 3)
                    #cv2.rectangle(frame, (xi, yf-35), (xf, yf), (r, g, b), cv2.FILLED)
                    #cv2.putText(frame, nombre, (xi+6, yf-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)"""
                cv2.destroyAllWindows()
                fin = True
                print(id)
                
                break
        
        if not fin:
            # Mostramos frames
            cv2.imshow('Video', frame)

            # Leemos el teclado
            t = cv2.waitKey(5)
            if t == 27:
                break
        else:
            break

    return id

    
