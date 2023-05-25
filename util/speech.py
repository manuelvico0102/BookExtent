import pyttsx3

def texto_a_audio(texto):
    engine=pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()