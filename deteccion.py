#importamos las librerias
import cv2 
import numpy as np
import face_recognition as fr
import os
import random
from datetime import datetime

# Accedemos a la carpeta
path = 'Personal'
images = []
clases = []
lista = os.listdir(path)
#print(lista)

#Variables
comp1 = 100

# Leemos los rostros
for lis in lista:
    #leemos las imagenes de los rostros
    imgdb = cv2.imread(f'{path}/{lis}')
    #almacenamos imagen
    images.append(imgdb)
    #almacenamos nombre
    clases.append(os.path.splitext(lis)[0])

print(clases)

# Funcion para codificar los rostros
def codrostros(images):
    listacod = []

    # Iteramos
    for img in images:
        # Correcion de color
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # codificamos la imagen
        cod = fr.face_encodings(img)[0]
        # almacenamos la codificacion
        listacod.append(cod)
    
    return listacod

# llamamos la funcion 
rostroscod = codrostros(images)

# Realizamos video captura
cap = cv2.VideoCapture(0)

# Empezamos
while True:
    # Leemos los fotogramas
    ret, frame = cap.read()
    
    #Reducimos las imagenes para mejorar el procesamiento
    frame2 = cv2.resize(frame, (0,0), None, 0.25, 0.25)

    #Convertimos de color 
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
            nombre = clases[min].upper()
            print(nombre)
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
                cv2.rectangle(frame, (xi, yi), (xf, yf), (r, g, b), 3)
                cv2.rectangle(frame, (xi, yf-35), (xf, yf), (r, g, b), cv2.FILLED)
                cv2.putText(frame, nombre, (xi+6, yf-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)


    # Mostramos frames
    cv2.imshow('Video', frame)

    # Leemos el teclado
    t = cv2.waitKey(5)
    if t == 27:
        break

