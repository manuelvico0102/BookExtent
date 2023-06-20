"""
    Archivo con las funciones para el manejo de imagenes
    Autor: Manuel Vico Arboledas.
"""

from PIL import ImageTk, Image
import cv2

def convertirCV2aPIL(imagen):
    """
    Método que convierte una imagen de OpenCV a PIL

    Args:
        imagen (obj): Imagen de OpenCV
    
    Returns:
        obj: Imagen de PIL
    """
    imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    return Image.fromarray(imagen)

def leer_imagen(path, size):
    """
    Método que lee una imagen y la redimensiona

    Args:
        path (str): Ruta de la imagen
        size (tuple): Tamaño de la imagen
    
    Returns:
        obj: Imagen de PIL
    """
    return ImageTk.PhotoImage(Image.open(path).resize(size, Image.ANTIALIAS))

def imagenResize(imagen, size):
    """
    Método que redimensiona una imagen

    Args:
        imagen (obj): Imagen de PIL
        size (tuple): Tamaño de la imagen
    """
    return ImageTk.PhotoImage(imagen.resize(size, Image.ANTIALIAS))

def centrar_ventana(ventana, aplicacion_ancho, aplicacion_largo):
    """
    Método que centra la ventana

    Args:
        ventana (obj): Ventana
        aplicacion_ancho (int): Ancho de la aplicación
        aplicacion_largo (int): Largo de la aplicación
    
    Returns:
        str: Posición de la ventana
    """
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_largo = ventana.winfo_screenheight()
    x = int((pantalla_ancho/2) - (aplicacion_ancho/2))
    y = int((pantalla_largo/2) - (aplicacion_largo/2))
    return ventana.geometry(f"{aplicacion_ancho}x{aplicacion_largo}+{x}+{y}")