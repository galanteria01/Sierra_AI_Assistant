# Imported libraries essential
import pyttsx3
import datetime
from modules.func import *
import speech_recognition as sp
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui as pag
from instapy import InstaPy
from selenium import webdriver


# DEFINED main function,Its where everything starts
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
            speak("logging out")
            os.system('shutdown -l')

        elif 'restart' in query:
            speak("restarting the desktop sir")
            os.system('shutdown /r /t 1')

        elif 'shutdown' in query:
            speak("shutting down, hope you saved your data")
            os.system('shutdown /s /t 1')

        elif 'play songs' in query:
            speak("playing songs now")
            songsDir = '/home/shanu/Documents'
            songs = os.listdir(songsDir)
            os.startfile(os.path.join(songsDir,songs[0]))

        elif 'remember that' in query:
            speak("what should i remember sir")
            rememberMessage = takeCommand()
            speak("you said me to remember"+rememberMessage)
            remember = open('data.txt', 'w')
            remember.write(rememberMessage)
            remember.close()

        elif 'do you know anything' in query:
            remember = open('data.txt', 'r')
            speak("you said me to remember that" + remember.read())

        elif 'about you' in query:
            speak('''i am sierra! an Artificial intelligence assistant by galanteria!
             i can do some basic stuff uptill now,but definately do more with time, As i am AI''')

        elif 'screenshot' in query:
            speak("taking a screenshot")
            screenshot()
            speak("screenshot has been took and saved to Documents")

        elif 'update linux' in query:
            speak("do you want to update or upgrade")
            commandInput = takeCommand()
            if 'update' in commandInput:
                speak("updating the repository")
                os.system('sudo apt update')
            elif 'upgrade' in commandInput:
                speak("upgrading the repository")
                os.system('sudo apt upgrade')

        elif 'install app' in query:
            speak("tell the name of app you want to install sir")
            app = takeCommand()
            speak("installing app now")
            os.system('sudo apt-get install'+app)

        elif 'tell a story' in query:
            speak("telling a story")
            tellStory()

        elif "tell about developer" in query:
            speak("i am developed by shanu and written in python, thanks to developer for giving life")

        elif "tell a factorial" in query:
            speak("what number")
            num = int(takeCommand())
            sum=1
            for i in range(num+1):
                sum = sum*i
            speak(sum)

        elif "motivate me" in query:
            speak('you will be best,someday,somehow, NEVER STOP TRYING')

        elif "open instagram" in query:
            speak("Tell you're username sir")
            username = takeCommand()
            speak("Tell your password sir")
            password = takeCommand()
            session = InstaPy(username,password)
            # Can make modifications to automate things
            speak("You are logged in")

        elif "search on google" in query:
            speak("tell about what to search sir")
            searchText = takeCommand()
            browser = webdriver.Firefox()
            browser.implicitly_wait(5)
            browser.get('https://www.google.com')
            search = browser.find_element_by_css_selector("input[name='text']")
            search.send_keys(searchText)
            button = browser.find_element_by_css_selector("//button[name='btnK']")
            speak("Here are the relevant results sir")

        elif "offline" in query:
            speak("going offline, goodbye!")
            quit()


