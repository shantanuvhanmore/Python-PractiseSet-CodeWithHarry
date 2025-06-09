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
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")



def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
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


def get_latest_news(num_articles=3, country='us'):
    url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={NEWS_API_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        if data['status'] == 'ok':
            articles = data['articles'][:num_articles]
            for i, article in enumerate(articles, 1):
                speak(f"Headline {i}: {article['title']}")
        else:
            speak("Couldn't fetch news.")
    except Exception:
        speak("Error while getting news.")


def get_time():

def date():

def get_weather(city):
    try:
        geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={WEATHER_API_KEY}"
        geo_data = requests.get(geo_url).json()
        if not geo_data:
            speak(f"Couldn't find location {city}.")
            return
        lat, lon = geo_data[0]['lat'], geo_data[0]['lon']
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}&units=metric"
        weather_data = requests.get(weather_url).json()
        temp = weather_data['main']['temp']
        condition = weather_data['weather'][0]['description']
        speak(f"The current temperature in {city} is {temp}°C with {condition}.")
    except:
        speak("Couldn't retrieve weather data.")

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
        speak("hi there how can i help you!")

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


            


