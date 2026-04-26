from voice import speak, listen
from brain import ask_ollama
from config import EXIT_WORDS
def main():
    speak("Hi ,am your Assistant , please let know how can i help you Jamal ")
    
    while True:
        user_input = listen()
        if not user_input:
            continue
        if any(word in user_input for word in EXIT_WORDS):
            speak("Goodbye")
            break
        response=ask_ollama(user_input)
        speak(response)
        
if __name__ == "__main__":
    main()