# Python Jarvis

# modules which need installation
import psutil  # pip install psutil
import pyttsx3  # pip install pyttsx3
import wikipedia  # pip install wikipedia
from gpiozero import CPUTemperature  # pip install gpiozero
import speech_recognition as sr  # pip install speechRecognition

# modules which do not need installation
import datetime
import random
import subprocess
import webbrowser
import os


# voice setup
engine = pyttsx3.init('sapi5')
engine.setProperty('rate',205)  #speed of speech
engine.setProperty('volume', 1)  #volume low(0) and high(1) 
engine.setProperty('voice', 'en')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# Some variables
pronouns = ['Sir', 'Officer', 'Captain']
pronoun = random.choice(pronouns)
# Paths
google_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
vsc_path = r'C:\Users\admin\AppData\Local\Programs\Microsoft VS Code\Code.exe'
yt_path = r'https://www.youtube.com'
github_path = r'https://www.github.com/Risen54'



# Funtion to let the bot speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greet():  # Makes the bot greet you according to the time
    hour = int(datetime.datetime.now().hour)
    if hour >= 6 and hour < 12:
        greeting = f"Good Morning {pronoun}!"
        print(greeting)
        speak(greeting)
    elif hour >= 12 and hour < 17:
        greeting = f"Good Afternoon {pronoun}!"
        print(greeting)
        speak(greeting)
    elif hour >= 17 and hour < 21:
        greeting = f"Good Evening {pronoun}!"
        print(greeting)
        speak(greeting)
    else:
        greeting = "It's night, I think you should sleep now."
        print(greeting)
        speak(greeting)


def take_command():  # Receives and evaluates the given command
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening...')
            r.adjust_for_ambient_noise(source, duration=1)
            r.pause_threshold = 0.8
            audio = r.listen(source)
            
            print('recognizing')
            query = r.recognize_google(audio, language='en-in').lower()
            print(f'Command: {query}\n')
            
            # Functions
            # Add Emotions!!!!!!!!!!!!! 🤖
            try:

                if 'open youtube' in query:
                    webbrowser.WindowsDefault().open(yt_path)

                elif 'open google' in query:
                    subprocess.run(google_path)

                elif 'exit' in query or 'close' in query or 'quit' in query:
                    exit()

                elif 'stats' in query \
                or 'health' in query \
                or 'statistics' in query:
                    heat = CPUTemperature()
                    usage = int(psutil.cpu_percent())
                    stats = f"""your cpu is running at {heat} \
                    with {usage} percent of the cpu being utilized"""
                    print(stats)
                    speak(stats)

                elif 'wikipedia' in query:
                    speak("Searching...")
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=3)
                    speak("According  to Wikipedia...")
                    print(results)
                    speak(results)

                elif 'open main folder' in query \
                or 'open blizzard' in query \
                or 'open my main folder' in query \
                or 'open my folder' in query:

                    subprocess.Popen(r'explorer /open,"G:\Blizzard\"')

                elif 'open code' in query or \
                'open visual studio code' in query:
                    speak("Opening VSC")
                    subprocess.run(vsc_path)

                elif 'introduce yourself' in query\
                or 'what can you do':
                    intro = """
                    I am you personal voice assistant.
                    I can help you with stuff like reminding your tasks,
                    give information about something,
                    helping you with small things and
                    making your work fast"""
                    print(intro)
                    speak(intro)

                # Tell time function
                elif 'the time' in query:
                    time = datetime.datetime.now().strftime("%H:%M:%S")
                    print(time)
                    speak(time)
                
                # Tell date function
                elif 'the date' in query:
                    date = datetime.datetime.now().strftime("%d/%m/%Y")
                    print(date)
                    speak(date)
                
                # Tell day function
                elif 'the day' in query:
                    day = datetime.datetime.now().strftime("%A")
                    print(day)
                    speak(day)
                
                # Flip coin function
                elif 'flip coin' in query:
                    flip = random.choice(['heads', 'tails'])
                    print(flip)
                    speak(flip)

                # Open Github function
                elif 'open github' in query:
                    webbrowser.WindowsDefault().open(github_path)

                else:
                    continue
            except Exception:
                print("Please say again")
                return 'None'
            return query


if __name__ == '__main__':
    greet()
    take_command()
