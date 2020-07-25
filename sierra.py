import pyttsx3
import datetime
from modules.func import *
import speech_recognition as sp
import wikipedia
import smtplib
import webbrowser as wb


if __name__ == '__main__':
    wish_me()
    while True:
        query = takeCommand().lower()
        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "wikipedia" in query:
            speak("Searching on wiki")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)
        elif "send email" in query:
            try:
                speak("What should i convey?")
                content = takeCommand()
                speak("whom must i send email")
                to = takeCommand()
                sendEmail(to,content)
                speak("Email has been sent succesfully")
            except Exception as e:
                print(e)
                speak("sorry! unable to send mail")
        elif "search in chrome" in query:
            speak("what should i search sir")


        elif "offline" in query:
            quit()


