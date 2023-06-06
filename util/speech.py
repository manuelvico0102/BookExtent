import speech_recognition as sr
import pyttsx3

def texto_a_audio(texto):
    engine=pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

def transcribir_audio():
    # Crear un objeto de reconocimiento de voz
    rec = sr.Recognizer()
    mic = sr.Microphone()

    # Capturar el audio del altavoz
    with mic as source:
        print("Escuchando...")
        # Ajustar automáticamente el umbral de energía del ruido de fondo
        rec.adjust_for_ambient_noise(source)

        # Escuchar el audio del altavoz
        audio = rec.listen(source, timeout=2)

    try:
        # Transcribir el audio a texto utilizando la API de Google
        texto = rec.recognize_google(audio, language='es-ES')
        return texto
    except sr.RequestError:
        print("API no disponible")
        return None
    except sr.UnknownValueError:
        print("No se pudo reconocer el audio")
        return None  


def main(salir):
    global matriz
    palabra_objetivo = "descripción"
    while not salir.is_set():
        texto = transcribir_audio()

        if texto is not None and palabra_objetivo in texto.lower():
            print("Se ha detectado la palabra")
        print(texto)
        
if __name__=="__main__":
    main()