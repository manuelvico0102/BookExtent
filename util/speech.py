"""
    Archivo con las funciones para escuchar y hablar.

    Autor: Manuel Vico Arboledas.
"""
import speech_recognition as sr
import pyttsx3
from threading import Thread
import webbrowser

def texto_a_audio(texto):
    """
        Función para convertir un texto a audio y lo reproduce

        Args:
            texto (str): Texto a convertir a audio
    """
    engine=pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()


def inicio_reconocimiento_voz(self, ventana):
    """
        Función para iniciar el reconocimiento de voz en una hebra

        Args:
            self (obj): Objeto de la clase que utiliza la función
            ventana (str): Ventana en la que se encuentra
    """
    self.r = sr.Recognizer()

    self.hebraVoz = Thread(target=reconocimiento_voz, args=[self, ventana], daemon=True)
    self.hebraVoz.start()


def reconocimiento_voz(self, ventana):
    """
        Función para reconocer el audio y procesarlo

        Args:
            self (obj): Objeto de la clase que utiliza la función
            ventana (str): Ventana en la que se encuentra
    """
    
    with sr.Microphone() as source:
        print("Puedes hablar")
        # Ajusta el ruido de fondo
        self.r.adjust_for_ambient_noise(source)
        # Ajusta el umbral de energia
        self.r.energy_threshold = 4000
        while not self.eventoStop.is_set():
            audio = self.r.listen(source)
            procesar_audio(self, audio, ventana)


def procesar_audio(self, audio, ventana):
    """
        Función para procesar el audio dependiendo de la ventana en la que se encuentre

        Args:
            self (obj): Objeto de la clase que utiliza la función
            audio (obj): Audio a procesar
            ventana (str): Ventana en la que se encuentra
    """
    if not self.eventoStop.is_set():  #Compruebo que no se haya cerrado la ventana
        try:
            texto = self.r.recognize_google(audio, language="es-ES")
            print("Has dicho: ", texto)
            if(ventana == "principal"):
                if "música" in texto.lower():
                    abrir_playlist()
                elif "libros" in texto.lower() and "favoritos" in texto.lower():
                    self.verCategoria(id_usuario=self.id_usuario, categoria="Favoritos")
                elif "libros" in texto.lower() and "siguiendo" in texto.lower():
                    self.verCategoria(id_usuario=self.id_usuario, categoria="Siguiendo")
                elif "libros" in texto.lower() and "finalizados" in texto.lower():
                    self.verCategoria(id_usuario=self.id_usuario, categoria="Finalizado")
                elif "libros" in texto.lower() and "pendientes" in texto.lower():
                    self.verCategoria(id_usuario=self.id_usuario, categoria="Pendiente")
                elif "libros" in texto.lower():
                    self.verLibros()
                        
            elif(ventana == "libro"):
                if "guardar" in texto.lower() and "favoritos" in texto.lower():
                    self.guardarCategoria(id_usuario=self.id_usuario, id_libro=self.id_libro, id_categoria='1')
                elif "guardar" in texto.lower() and "siguiendo" in texto.lower():
                    self.guardarCategoria(id_usuario=self.id_usuario, id_libro=self.id_libro, id_categoria='2')
                elif "guardar" in texto.lower() and "finalizados" in texto.lower():
                    self.guardarCategoria(id_usuario=self.id_usuario, id_libro=self.id_libro, id_categoria='3')
                elif "guardar" in texto.lower() and "pendientes" in texto.lower():
                    self.guardarCategoria(id_usuario=self.id_usuario, id_libro=self.id_libro, id_categoria='4')
                elif "leer" in texto.lower():
                    self.leerDescripcion(texto=self.desc_libro)
                elif "aumentada" in texto.lower():
                    self.realidadAumentada(imagen=self.imagen_libro)    
        except sr.UnknownValueError:
            print("No te he entendido")
        except sr.RequestError as e:
            print("Error al procesar el audio; {0}".format(e))
        finally:
            self.comando_ejecutandose = False

def cerrar_ventana(self):
    """
        Función para cerrar la hebra de reconocimiento de voz

        Args:
            self (obj): Objeto de la clase que utiliza la función
    """
    if self.hebraVoz:
        self.eventoStop.set()
        #self.hebraVoz.join() # Espera a que termine la hebra
        #No espero a que termine la hebra para que no tarde la ventana en cerrarse


def abrir_playlist():
    """
        Función para abrir la playlist de spotify
    """

    # Enlace para la lista de spotify
    url = "https://open.spotify.com/playlist/2XQ2h5FLnEeG5cYbzJRiba"
    webbrowser.open_new(url)
