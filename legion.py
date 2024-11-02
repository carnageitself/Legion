import pyttsx3
import speech_recognition
import datetime
# import mediapipe
# import cv2
# import pyautogui

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
        audio = r.listen(source, timeout=10)  # Will wait for 10 seconds

    try:
        print("Understanding...")
        query = r.recognize_google(audio, language='en-US')
        print(f"You Said: {query}\n")
        return query
    except speech_recognition.UnknownValueError:
        print("Sorry, I didn't understand that.")
        speak("Sorry, I didn't understand that.")
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

# capturehands = mediapipe.solutions.hands.Hands()
# drawing = mediapipe.solutions.drawing_utils
# screenWidth, screenHeight = pyautogui.size()

# camera = cv2.VideoCapture(0)  # No. of cameras

# while True:
#     _, image = camera.read()
#     imageheight, imagewidth, _ = image.shape
#     image = cv2.flip(image, 1)
#     rgbImage = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     output = capturehands.process(rgbImage)
#     allHands = output.multi_hand_landmarks
#     if allHands:
#         for hand in allHands:
#             drawing.draw_landmarks(image, hand)
#             onehand_landmark = hand.landmark
#             for id, lm in enumerate(onehand_landmark):
#                 x = int(lm.x * imagewidth)
#                 y = int(lm.y * imageheight)
#                 print(x, y)
#                 if id == 8:
#                     mouseX = int(screenWidth / imagewidth * x)
#                     mouseY = int(screenHeight / imageheight * x)
#                     cv2.circle(image, (x, y), 10, (0, 255, 255))  # 10 radius
#                     pyautogui.moveTo(mouseX, mouseY)
#                 # if id == 4:
#                 #     cv2.circle(image,(x,y),10,(0,255,255)) #10 radius
#     cv2.imshow("Hand movement video capture", image)
#     key = cv2.waitKey(100)  # 100 miliseconds
#     if key == 27:
#         break
# camera.release()
# cv2.destroyAllWindows()

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
