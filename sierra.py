import pyttsx3
import datetime
from modules.func import *
import speech_recognition as sp
import wikipedia
import smtplib
import webbrowser as wb
import os


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
        elif 'logout' in query:
            os.system('shutdown -l')
        elif 'restart' in query:
            os.system('shutdown /r /t 1')
        elif 'shutdown' in query:
            os.system('shutdown /s /t 1')
        elif 'play songs' in query:
            songsDir = '/home/shanu/Documents'
            songs = os.listdir(songsDir)
            os.startfile(os.path.join(songsDir,songs[0]))

        elif "offline" in query:
            quit()


