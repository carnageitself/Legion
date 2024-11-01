import pyttsx3
import speech_recognition
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # Pause time
        r.energy_threshold = 300  # Sensitivity for background noise
        audio = r.listen(source, timeout = 10)  # Will wait for 10 seconds

    try:
        print("Understanding...")
        query = r.recognize_google(audio, language='en-US')
        print(f"You Said: {query}\n")
        return query
    except speech_recognition.UnknownValueError:
        print("Sorry, I did not understand that.")
        speak("Sorry, I did not understand that.")
        return None
    except speech_recognition.RequestError as e:
        print(f"Could not request results; {e}")
        speak(f"Sorry, I could not request results; {e}")
        return None


def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning Sir")
    elif hour > 12 and hour <= 18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Night Sir")

    speak("What can I do for you today?")

if __name__ == "__main__":
    while True:
        query = takeCommand()

        if query:
            query = query.lower()

            if "wake up" in query:
                greet()

            if "go to sleep" in query:
                speak("Going offline")
                break
            
                
