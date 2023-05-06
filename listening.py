import speech_recognition as sr
import say
from playsound import playsound
def speaking():
    global frase
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print('Diga alguma coisa: ')
        audio = microfone.listen(source)
    try:
        frase = microfone.recognize_google(audio,language='pt-BR')
        print('Você disse: '+frase)
    except sr.UnknownValueError:
        print('Não entendi')
        say.say('Não entendi senhor')
    return frase
speaking()