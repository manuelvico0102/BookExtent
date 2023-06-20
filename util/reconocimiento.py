"""
    Archivo con las funciones necesarias para el reconocimiento facial.

    Autor: Manuel Vico Arboledas.
"""
import cv2
import numpy as np
import face_recognition as fr
from db.BD import BaseDatos
import time

def capturarFoto():
    """
    Función que captura una foto

    Returns:
        img: imagen capturada
    """
    cam = cv2.VideoCapture(0)
    ret, imagen = cam.read()
    cam.release()
    return imagen

def CrearUsuarioConFoto(bd, usuario, contra, img):
    """
    Función que crea un usuario con una foto

    Args:
        bd (obj): Objeto de la clase BaseDatos
        usuario (str): Nombre de usuario
        contra (str): Contraseña
        img (obj): Imagen capturada
    
    Returns:
        bool: True si se ha creado el usuario, False si no se ha creado
    """
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
    """
    Función que codifica una foto

    Args:
        bd (obj): Objeto de la clase BaseDatos
        idusuario (int): Id del usuario
        ruta (str): Ruta de la foto
    """
    img = cv2.imread(ruta)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cod = fr.face_encodings(img)[0]
    # Convertir la codificación de la imagen a bytes
    imagen_codificada = np.array(cod).tobytes()
    BaseDatos.subirImagenCodificada(self=bd, idusuario=idusuario, cod=imagen_codificada)


def reconocimientoFacial(ids, rostroscod):
    """
    Función que realiza el reconocimiento facial
    
    Args:
        ids (list): Lista de ids
        rostroscod (list): Lista de codificaciones de rostros

    Returns:
        id: Id del usuario
    """
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

    
