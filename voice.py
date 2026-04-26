import speech_recognition as sr
import pyttsx3
from config import VOICE_RATE

engine = pyttsx3.init()
engine.setProperty('rate', VOICE_RATE)

def speak(text):
    print(f"{text}")
    engine.say(text)
    engine.runAndWait()
    
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='en-US')
            print(f"User: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")