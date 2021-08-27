import requests
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


url = 'http://google.com/'

timeout = 6
try:
    request = requests.get(url, timeout=timeout)
    internet = True
except (requests.ConnectionError, requests.Timeout) as exception:
    internet = False

if internet == True:
    pass
elif internet == False:
    print("JARVIS: No Internet! Please check your router or your internet connection and try again.")
    talk("No Internet! Please check your router or your internet connection and try again.")
    exit()
else:
    print("JARVIS: Error! Please run the right command.")
    talk("Error! Please run the right command.")
    exit()

import random
import os
from playsound import playsound
import pywhatkit
import webbrowser
import wikipedia
import json
import time

def take_input():
    try:
        print("Lestening...")
        command = str(input("You: "))
        if 'jarvis' in command:
            command = command.replace('jarvis', '')
    except:
        pass
    return command


def jarvis_run():
    command = take_input()

    with open('data.json') as json_file:
        data = json.load(json_file)

        for code in data['code']:
            if code['question'] in command:
                print("JARVIS: " + code['answer'])
                talk(code['answer'])

    if 'bye' in command:
        print("JARVIS: Goodbye, Sir")
        talk("Goodbye, Sir")
        exit()
    elif 'who the heck is' in command:
        get_info = command.replace('who the heck is ', '')
        info = wikipedia.summary(get_info, 1)
        print("JARVIS: " + info)
        talk(info)
    elif 'open browser' == command:
        print("JARVIS: Opening Browser")
        talk("Opening Browser")
        webbrowser.open("http://google.com/")
    elif 'search for' in command:
        search = command.replace('search for ', '')
        print("JARVIS: Searching for " + search)
        talk("Searching for " + search)
        webbrowser.open("http://google.com/search?q=" + search)
    elif 'play' in command:
        song = command.replace('play ', '')
        print("JARVIS: Playing " + song)
        talk("Playing " + song)
        pywhatkit.playonyt(song)
    elif 'song' == command:
        random_song = random.choice(os.listdir("audio"))
        print("JARVIS: Playing Song...")
        talk("Playing Song...")
        playsound('audio/' + random_song)
    elif 'cls' == command:
        def clear(): 
            return os.system('cls')
        clear()

if '__main__' == __name__:
    while True:
        jarvis_run()
