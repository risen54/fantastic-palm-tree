import psutil
import wikipedia
import datetime
import random
from subprocess import run
import webbrowser
import speech_recognition as sr
import pyttsx3
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

prefixes = ['Sir', 'Officer', 'Captain']
prefix = random.choice(prefixes)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 6 and hour < 12:
        greeting = f"Good Morning {prefix}!"
        print(greeting)
        speak(greeting)
    elif hour >= 12 and hour < 17:
        greeting = f"Good Afternoon {prefix}!"
        print(greeting)
        speak(greeting)
    elif hour >= 17 and hour < 21:
        greeting = f"Good Evening {prefix}!"
        print(greeting)
        speak(greeting)
    else:
        greeting = "It's night, I think you should sleep now."
        print(greeting)
        speak(greeting)


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.adjust_for_ambient_noise(source,duration=1)
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print('recognizing')
        query = r.recognize_google(audio, language='en-in').lower()
        print(f'Command: {query}\n')
        # Functions

        if 'open youtube' in query:
            webbrowser.Chrome.open('www.youtube.com')
        elif 'open google' in query:
            google_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
            run(google_path)
        elif 'exit' in query or 'close' in query or 'quit' in query:
            exit()
        elif 'stats' in query or 'health' in query:
            heat = int()
            usage = int(psutil.cpu_percent())
            stats = f"your cpu is running at {heat} with {usage} percent of the cpu being utilized"
        elif "wikipedia" in query:
            search_thing = query.replace("wikipedia", "")
            rezults = wikipedia.search(search_thing, 3)
            print(rezults)
            speak(rezults)
    except Exception:
        speak("Please say again")
        print("Please say again")
        return 'None'

    return query


if __name__ == '__main__':
    greet()
    while True:
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source,duration=1)
                r.pause_threshold = 0.8
                audio = r.listen(source)
            query = r.recognize_google(audio, language='en-in').lower()
            if 'hello' in query:
                take_command()
            else:
                continue
        except Exception as e:
            print("Please say again")
            speak("Please say again")
            print(e)