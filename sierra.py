import pyttsx3
import datetime


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


if __name__ == '__main__':
    wish_me()