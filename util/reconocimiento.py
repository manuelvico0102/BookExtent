import speech_recognition as sr
import cv2 
import numpy as np
import face_recognition as fr
import os
import random
from db.BD import BaseDatos

#Necesito una hebra para el microfono
def capturarFoto():
    cap = cv2.VideoCapture(0)
    # Inicializar el reconocimiento de voz
    r = sr.Recognizer()

    if not cap.isOpened():
        print("No se puede abrir la cámara")
        exit()
    while True:
        ret, frame = cap.read()

        if not ret:
            print("No he podido leer el frame")
            break

        cv2.imshow('WEBCAM', frame)

        with sr.Microphone() as source:
            print("Escuchando...")
            audio = r.listen(source)

        try:
            comando = r.recognize_google(audio)
            if comando == "foto":
                # Guardar la imagen capturada en un archivo
                cv2.imshow("foto_webcam.jpg", frame)
                print("¡Foto capturada con éxito!")
            else:
                print("Comando no reconocido")
        except sr.UnknownValueError:
            print("No se pudo reconocer el audio")
        except sr.RequestError as e:
            print(f"No se pudo completar la solicitud: {e}")

        if cv2.waitKey(1) == ord(' '):
            break

    cap.release()
    cv2.destroyWindow('WEBCAM')

# Llamar a la función para capturar una foto cuando se diga "foto"
# capturarFoto()

def codificarFoto(bd, idusuario, ruta):
    img = cv2.imread(ruta)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cod = fr.face_encodings(img)[0]
    # Convertir la codificación de la imagen a bytes
    imagen_codificada = np.array(cod).tobytes()
    BaseDatos.subirImagenCodificada(self=bd, idusuario=idusuario, cod=imagen_codificada)


# Establezco conexion a la base de datos
bd = BaseDatos(usuario="x6520114", password="x6520114", dsn="oracle0.ugr.es:1521/practbd.oracle0.ugr.es")
BaseDatos.conexion(self=bd)

codificarFoto(bd=bd, idusuario="1", ruta="Personal\FOTO.jpg")

# Se cierra conexion a la base de datos
BaseDatos.desconexion(self=bd)
