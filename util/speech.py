import speech_recognition as sr
import pyttsx3
from threading import Thread


def texto_a_audio(texto):
    engine=pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

def inicio_reconocimiento_voz(self):
        self.r = sr.Recognizer()

        self.hebraVoz = Thread(target=reconocimiento_voz, args=[self], daemon=True)
        self.hebraVoz.start()

def reconocimiento_voz(self):
        with sr.Microphone() as source:
            print("Puedes hablar")
            self.r.adjust_for_ambient_noise(source)
            while not self.eventoStop.is_set():
                audio = self.r.listen(source, timeout=5)
                procesar_audio(self, audio)
    
def procesar_audio(self, audio):
        try:
            texto = self.r.recognize_google(audio, language="es-ES")
            print("Has dicho: ", texto)
            if "favoritos" in texto.lower():
                self.guardarCategoria(id_usuario=self.id_usuario, id_libro=self.id_libro, id_categoria='1')
            elif "siguiendo" in texto.lower():
                self.guardarCategoria(id_usuario=self.id_usuario, id_libro=self.id_libro, id_categoria='2')
            elif "finalizados" in texto.lower():
                self.guardarCategoria(id_usuario=self.id_usuario, id_libro=self.id_libro, id_categoria='3')
            elif "pendientes" in texto.lower():
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
    if self.hebraVoz:
        self.eventoStop.set()
        self.hebraVoz.join()
