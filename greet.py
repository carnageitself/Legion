import pyttsx3
import datetime

engine = pyttsx3.init("sap15")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <=12:
        speak("Good Morning Yash")
    elif hour > 12 and hour <= 18:
        speak("Good Afternoon Yash")
    else:
        speak("Good Night Yash")
        
    speak("Please tell me, How can I help you?")