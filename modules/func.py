import pyttsx3
import datetime
import speech_recognition as sp
import smtplib
import pyautogui as pag

engine = pyttsx3.init()
engine.setProperty('rate',160)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    tim = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(tim)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(day)
    speak(month)
    speak(year)


def wish_me():
    speak("Welcome back sir")
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
    with sp.Microphone(device_index=0) as source:
        r.adjust_for_ambient_noise(source, duration=1)
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
        takeCommand()
        return None

    return query


def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('laddoo22032001@gmail.com','baatcheet',)
    server.sendmail('laddoo22032001@gmail.com',to,content)
    server.close()

def screenshot():
    img = pag.screenshot()
    img.save('/home/shanu/Documents')

def tellStory():
    speak('''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et
     dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip
      ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat
       nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit
        anim id est laborum.''')

