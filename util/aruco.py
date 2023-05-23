import cv2
import numpy as np
import sys
import os

def proyectar(imagen):
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
                if len(corners)>0:
                    for i in range(len(corners)):
                        # Obtener las dimensiones del marcador detectado
                        x, y, w, h = cv2.boundingRect(corners[i])

                        # Ajustar la imagen al tamaño del marcador
                        imagen_resized = cv2.resize(imagen, (w, h))

                        # Superponer la imagen en el fotograma
                        framerecortado[y:y + h, x:x + w] = imagen_resized

                cv2.imshow("RECORTADO", framerecortado)
                if cv2.waitKey(1) == ord(' '):
                    final = True
            else:
                final = True
    else:
        print("No se pudo acceder a la cámara.")
