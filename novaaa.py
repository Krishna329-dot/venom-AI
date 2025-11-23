import pyttsx3
import speech_recognition as sr

# Initialize TTS engine globally
engine = pyttsx3.init()

def say(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def takecommand():
    """Capture and recognize speech input."""
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=2)  # Adjust for noise
            print("Listening...")
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            try:
                query = r.recognize_google(audio, language='en-in')
                print(f"User said: {query}")
                return query
            except sr.UnknownValueError:
                print("Sorry, could not understand audio.")
                return None
            except sr.RequestError as e:
                print(f"Could not connect to Google API; {e}")
                return 0
    except Exception as e:
        print(f"Microphone error: {e}")
        return ""

if __name__ == "__main__":
    say("Hello, I am Venom AI. How can I help you?")
    text = takecommand()
    if text:  # Only speak if valid input is received
        say(text)