import speech_recognition as sr
import pyttsx3

class OutIn:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('voice','roa/pt-br')
        self.engine.setProperty('rate', 150)
    def escuta(self):
        rec = sr.Recognizer()

        with sr.Microphone() as fala:
            frase = rec.listen(fala, timeout=None, phrase_time_limit = 120)
        #print(rec.recognize_sphinx(frase))
        entrada = ''
        try:
            entrada = rec.recognize_google(frase, language='pt')
            return entrada
        except:
            pass
        return entrada

    def fala(self,msg):
        if msg != '':
            self.engine.say(msg)
            self.engine.runAndWait()
