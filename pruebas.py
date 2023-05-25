import cv2
import numpy as np
import sys
import os

imagen = cv2.imread("imagenes\ElUltimoDeseo.jpeg")

if os.path.exists('camara.py'):
    import camara
else:
    print("Es necesario realizar la calibración de la cámara")
    exit()

DIC = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
parametros = cv2.aruco.DetectorParameters()

cap = cv2.VideoCapture(0)
if cap.isOpened():
    hframe = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    wframe = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    print("Tamaño del frame de la cámara: ", wframe, "x", hframe)

    matrix, roi = cv2.getOptimalNewCameraMatrix(camara.cameraMatrix, camara.distCoeffs, (wframe,hframe), 1, (wframe,hframe))
    roi_x, roi_y, roi_w, roi_h = roi

    final = False
    while not final:
        ret, framebgr = cap.read()
        if ret:
            # Aquí procesamos el frame
            framerectificado = cv2.undistort(framebgr, camara.cameraMatrix, camara.distCoeffs, None, matrix)
            framerecortado = framerectificado[roi_y : roi_y + roi_h, roi_x : roi_x + roi_w]

            (corners, ids, rejected) = cv2.aruco.detectMarkers(framerecortado, DIC, parameters=parametros)
    
            if np.all(ids != None):    
                #aruco = cv2.aruco.drawDetectedMarkers(framerecortado, corners)

                #Guardamos las esquinas del marcador
                c1 = (corners[0][0][0][0], corners[0][0][0][1])
                c2 = (corners[0][0][1][0], corners[0][0][1][1])
                c3 = (corners[0][0][2][0], corners[0][0][2][1])
                c4 = (corners[0][0][3][0], corners[0][0][3][1])

                #Creamos una copiar para luego superponer dos imagenes
                copy = framerecortado
                #Extraemos el tamaño de la imagen
                tamaño = imagen.shape
                #Organizamos las coordenadas del aruco en una matriz
                puntos_aruco = np.array([c1,c2,c3,c4])
                
                #Organizamos las coordenadas de la imagen en una matriz
                puntos_imagen = np.array([
                    [0,0],
                    [tamaño[1] - 1, 0],
                    [tamaño[1] - 1, tamaño[0] - 1],
                    [0, tamaño[0] - 1]
                ], dtype= float)

                #Realizamos la superposición de la imagen (Homografia)
                h, estado = cv2.findHomography(puntos_imagen, puntos_aruco)

                #Realizamos la transformación de perspectiva
                perspectiva = cv2.warpPerspective(imagen, h, (copy.shape[1], copy.shape[0]))
                cv2.fillConvexPoly(copy, puntos_aruco.astype(int), 0, 16)
                copy = copy + perspectiva


                cv2.imshow("RECORTADO", copy)
            else:
                cv2.imshow("RECORTADO", framerecortado)
                    
            if cv2.waitKey(1) == ord(' '):
                final = True
        else:
            final = True
else:
    print("No se pudo acceder a la cámara.")
