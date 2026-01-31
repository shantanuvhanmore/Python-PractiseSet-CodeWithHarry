import pyttsx3
import time


def speak(text):
    print(f"Assistant: {text}")
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    del engine


# Test multiple calls
speak("Test one")
time.sleep(1)
speak("Test two")
time.sleep(1)
speak("Test three")