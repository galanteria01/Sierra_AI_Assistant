import pyttsx3
import datetime
import speech_recognition as sp

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    tim = datetime.datetime.now().strftime("%I:%M:%S")
    speak(tim)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak(day)
    speak(month)
    speak(year)


def wish_me():
    speak("Welcome back sir")
    speak("the current time is")
    time()
    speak("the current date is")
    date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <= 12:
        speak("good morning sir")
    elif hour > 12 and hour <= 18:
        speak("good afternoon sir")
    elif hour > 18 and hour <= 24:
        speak("good evening sir")
    else:
        speak("its night! You must sleep sir")
    speak("sierra at your service Please tell me how to help you")


def takeCommand():
    r = sp.Recognizer()
    with sp.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognising...")
        query = r.recognize_google(audio,language="en-in")
        print(query)
    except Exception as e:
        print(e)
        speak("say that again please")
        return None

    return query
