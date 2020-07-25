import pyttsx3
import datetime
from modules.func import *
import speech_recognition as sp
import wikipedia




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

        elif "offline" in query:
            quit()


