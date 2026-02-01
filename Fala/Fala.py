import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('voice','roa/pt-br')
engine.setProperty('rate', 150)

rec = sr.Recognizer()
while True:
    with sr.Microphone() as fala:
        frase = rec.listen(fala, timeout=None, phrase_time_limit = 120)
    #print(rec.recognize_sphinx(frase))
    entrada = ''
    try:
        entrada = rec.recognize_google(frase, language='pt')
    except:
        pass
    print(entrada)
    engine.say(entrada)
    engine.runAndWait()
