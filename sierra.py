import pyttsx3
import datetime
from modules.func import *
import speech_recognition as sp




if __name__ == '__main__':
    wish_me()
    while True:
        query = takeCommand().lower()
        if "time" in query:
            time()
        elif "date" in query:
            date()
