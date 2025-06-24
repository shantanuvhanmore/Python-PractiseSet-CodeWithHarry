import os
import webbrowser
import pyttsx3
import speech_recognition as sr
import urllib.parse
import requests
import yt_dlp
import vlc
import time
from datetime import datetime
import openai
'''
pip install pyttsx3
pip install SpeechRecognition
pip install PyAudio
pip install openai==0.28
pip install requests
pip install yt-dlp
pip install python-vlc

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
        speak("Sorry, I didn’t get that.")
        return ""
    except sr.RequestError:
        speak("Speech service is unavailable.")
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
    speak(f"It's {datetime.now().strftime('%I:%M %p')}")

def date():
    speak(f"Today is {datetime.now().strftime('%A, %B %d')}")


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

def open_webbrowser(input_text):
    if "open youtube" in input_text.lower():
        webbrowser.open("https://www.youtube.com/")
    elif "open google" in input_text.lower():
        webbrowser.open("https://www.google.com/")
    elif "open instagram" in input_text.lower():
        webbrowser.open("https://www.instagram.com/")
    elif "open linkdin" in input_text.lower():
        webbrowser.open("https://www.linkdin.com/")
    elif "open facebook" in input_text.lower():
        webbrowser.open("https://www.facebook.com/")
    elif "open chatgpt" in input_text.lower():
        webbrowser.open("https://www.chatgpt.com/")

def play_song(song_name):
    try:
        speak(f"Playing {song_name} , to Stop music press ctrl + c")
        ydl_opts = {
            'format': 'bestaudio/best',
            'quiet': True,
            'noplaylist': True
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch:{song_name}", download=False)
            video = info['entries'][0]
            url = video['url']

        instance = vlc.Instance('--no-xlib')
        player = instance.media_player_new()
        media = instance.media_new(url)
        player.set_media(media)
        player.play()

        while True:
            state = player.get_state()
            if state in (vlc.State.Ended, vlc.State.Error):
                break
            time.sleep(1)

    except KeyboardInterrupt:
        speak("Song interrupted.")
        player.stop()
    except Exception:
        speak("Could not play the song.")

def search_on_yt(input_text):
    query = input_text[len("play "):-len(" on youtube")]
    search_url = "https://www.youtube.com/results?search_query=" + urllib.parse.quote(query)
    webbrowser.open(search_url)

def get_openai_response(prompt):
     # Make sure your API key is set in environment variables
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # Define your assistant's personality here
    personality = ("skips hi hello and give short reply"
        "You're a funny, witty AI assistant who always explains things in an easy and simple way, "
        "like a chill friend who’s a tech genius. Your replies are short, sharp, and packed with insight, "
        "but you're not afraid to add some humor and light roasting when needed. Keep things fun and helpful."
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use "gpt-4" if you have access
            messages=[
                {"role": "system", "content": personality},
                {"role": "user", "content": prompt}
            ],
            max_tokens=100,
            temperature=0.8  # Slightly more creative
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {e}"

def command_handler(command):
    input_text = command
    words = input_text.split()
    
    if any(keyword in words for keyword in ["hello","how are you","hi","yo","hey","what's up"]):
        speak("hi there how can i help you!")

    elif any(keyword in words for keyword in ["headlines","news","articles"]):
        get_latest_news()        

    elif "time" in words:
        get_time()
    
    elif "date" in words:
        date()
    
    elif any(keyword in words for keyword in ["weather","whether"]):
        city = command[len("weather in "):].strip()
        get_weather(city)

    elif "open" in words:
        open_webbrowser(input_text)

    elif "play" in command and not "youtube" in command:
        song = input_text.split("play ", 1)[1]
        if song:
            play_song(song)
        else:
            speak("Tell me which song to play.")

    elif "play" in input_text and "youtube" in input_text :
        if input_text.startswith("play ") and input_text.endswith(" on youtube"):
           search_on_yt(input_text) 
        else:
            print("Invalid input format")

    else:
        speak(get_openai_response(command))


# main function for logic
def main():
    start = True
    speak("Say 'moto' to activate me")

    while start:
        command = listen()

        if "moto" in command:
            speak("Listening...")
            
            while True:
                try:
                    
                    in_txt = listen().lower()

                    if any(word in in_txt for word in ["chup", "shut up", "pause", "stop", "wait"]):
                        speak("Okay, pausing...")
                        break

                    if any(word in in_txt for word in ["band ho", "quit", "exit", "terminate"]):
                        speak("Shutting down...")
                        start = False
                        break

                    command_handler(in_txt)

                except KeyboardInterrupt:
                    speak("Interrupted by user. Exiting gracefully...")

        elif any(word in command for word in ["band ho", "quit", "exit", "terminal"]):
            speak("Shutting down...")
            break            

            
if __name__ == "__main__":
    main()
