import os
import webbrowser
import pyttsx3
import speech_recognition as sr


'''
pip install pyttsx3
pip install SpeechRecognition
pip install PyAudio

'''
# initialisation
engine = pyttsx3.init()



def speak(text):

    # testing
    engine.say(f"{text}")
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print(f"You: {command}")
        return command.lower()
    except sr.UnknownValueError:
        #speak("Sorry, I didn’t get that.")
        return ""
    except sr.RequestError:
        #speak("Speech service is unavailable.")
        return ""
    
def greeting():


def get_latest_news():


def get_time():

def date():

def get_weather():

def play_song():

def open_webbrowser():

def play_song():

    
# main function for logic
def main():
    
    input_text = listen()
    print(input_text)
    words = input_text.split()
    print(words)

    if any(keyword in words for keyword in ["hello","hi","hey","what's up"]):
        greeting()

    elif any(keyword in words for keyword in ["headlines","news","articles"]):
        get_latest_news()

    elif "time" in words:
        get_time()
    
    elif "date" in words:
        date()
    
    elif any(keyword in words for keyword in ["weather","whether"]):
        get_weather(city)

    elif "open" in words:
        open_webbrowser()

    elif any(keyword in words for keyword in ["play","music","song"]):
        play_song(song)
        
    else:
        openai_logic()





if __name__ == "__main__":
    main()
