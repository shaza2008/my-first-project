import pyttsx3
import datetime

# Engine initialize karna voice ke liye
engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Shaza!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Shaza!")
    else:
        speak("Good Evening Shaza!")
    
    speak("I am your virtual assistant. How can I help you today?")

    if _name_ == "_main_":
     wishMe()
