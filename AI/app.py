import datetime
import random
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

prefixes = ["Sir", "Officer", "Sensei", "Lord", "Captain", "Creator"]
prefix = random.choice(prefixes)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 6 and hour < 12:
        wish = f"Good Morning {prefix}!"
        print(wish)
        speak(wish)
    elif hour >= 12 and hour < 17:
        wish = f"Good Afternoon {prefix}!"
        print(wish)
        speak(wish)
    elif hour >= 17 and hour < 21:
        wish = f"Good Evening {prefix}!"
        print(wish)
        speak(wish)
    else:
        wish = "It's night, I think you should sleep now."
        print(wish)
        speak(wish)


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source,duration=1)
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("recognizing")
        query = r.recognize_google(audio, language="en-in").lower()
        print(f"Command: {query}\n")
    except Exception:
        print("Please say again")
        return "None"
    return query


if __name__ == "__main__":
    greet()
    take_command()
