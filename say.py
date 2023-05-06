import pyttsx3
def say(x):
    engine = pyttsx3.init()
    engine.getProperty('rate')
    engine.setProperty('rate',250)
    engine.say(x)
    engine.runAndWait()