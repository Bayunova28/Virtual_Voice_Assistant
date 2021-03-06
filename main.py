#import library
import sys
import time
import psutil
import speedtest
import speech_recognition as sr 
import playsound  
from gtts import gTTS  
import random
import win32api
import pywhatkit
import datetime
import webbrowser
import pyautogui
import os   
import wikipedia
import json
import pyttsx3
import smtplib
import requests

#define function class person
class person:
    name = ''
    #define function name of person 
    def setName(self, name):
        self.name = name

#define function class assistant
class assistant:
    name = ''
    #define function name of person 
    def setName(self, name):
        self.name = name

#define function to list text message on audio speak
def audio_exists(terms):
    for term in terms:
        if term in voice_db:
            return True

#define function engine audio speak
def audio_speak(text):
    txt = str(text)
    engine.say(txt)
    engine.runAndWait()

#generate speech recognition
recognition = sr.Recognizer()

#define function for listen audio to convert text
def audio_record(ask = False):
    with sr.Microphone() as source:
        print('Listening...')
        audio_listen = recognition.listen(source, 5, 5)
        voice_db = ''

        try:
            voice_db = recognition.recognize_google(audio_listen)
        except sr.UnknownValueError:
            print('I am sorry Sir, I did not understand what you said. Can you please repeat again!')
        except sr.RequestError:
            print('I am sorry Sir, my server is going down')
        print(voice_db)
        return voice_db


#define function for get string of audio file 
def audio_speak(audio_string):
    audio_string = str(audio_string)
    google_text = gTTS(text = audio_string, lang = 'en')
    r = random.randint(1, 2000000)
    file = 'audio' + str(r) + '.mp3'
    google_text.save(file)
    playsound.playsound(file)
    print(assistantObj.name + ':', audio_string)
    os.remove(file)

#define function to send email
def audio_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

#define function to start the conversation
def audio_greet():
    hour = datetime.datetime.now().hour
    if hour >= 1 and hour < 12:
        audio_speak('Good morning!')
    elif hour >= 12 and hour < 18:
        audio_speak('Good afternoon!')
    elif hour >= 18 and hour < 24:
        audio_speak('Good evening!')
    audio_speak('Nova is online. Please tell me how can i help you Sir!')

#define function to present about news
def audio_news():
    api_key = 'your-api-key'
    news_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=' + api_key
    news_json = requests.get(news_url).json()
    news = []

    for i in range(5):
        news.append('Headline ' + str(i + 1) + ', ' + news_json['articles'][i]['title'] + '.')
    return news

#generate function class person and assistant
personObj = person()
assistantObj = assistant()
assistantObj.name = 'Nova'
engine = pyttsx3.init()

#define function to response the audio
def audio_response(voice_db):
    if audio_exists(['Nova search weather for']):
        api_key = 'your-api-key'
        base_url = 'https://api.openweathermap.org/data/2.5/weather?'
        audio_speak('Where is the city?')
        city_name = audio_record()
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()

        if x['cod'] != '404':
            y = x['main']
            temp = round(y['temp'] - 273)
            humidity = y['humidity']
            z = x['weather']
            description = z[0]['description']
            audio_speak('Currently in ' + city_name + ' temperature is ' + str(temp) + ' degrees celcius' + '\n humidity in percentage is ' + 
                        str(humidity) + ' percent' + '\n the condition is ' + str(description))
            print('Currently in ' + city_name + ' temperature is ' + str(temp) + ' degrees celcius' + '\n humidity in percentage is ' + 
                  str(humidity) + ' percent' + '\n the condition is ' + str(description))
    
    elif audio_exists(['Nova current news']):
        arr_news = audio_news()
        for i in range(len(arr_news)):
            audio_speak(arr_news[i])
            print(arr_news[i])
            
    elif audio_exists(['Nova what time is it']):
        time = datetime.datetime.now().strftime('%I:%M %p')
        audio_speak('Current time is ' + time)
    
    elif audio_exists(['Nova tell me the location']):
        audio_speak('What is the location?')
        location = audio_record()
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        audio_speak('Here is the location ' + location)
        
    elif audio_exists(['Nova show my system']):
        system_path = "C:\Program Files (x86)\MSI\Dragon Center\Dragon Center.exe"
        audio_speak('starting monitoring system')
        os.startfile(system_path)
    
    elif audio_exists(['Nova show internet speed']):
        speed_test = speedtest.Speedtest()
        dowload = round(speed_test.download(), 2)
        upload = round(speed_test.upload(), 2)
        audio_speak(f'The internet have {dowload} bit per second downloading speed and {upload} bit per second uploading speed')

    elif audio_exists(['Nova show power battery']):
        power_battery = psutil.sensors_battery()
        battery_percentage = power_battery.percent
        audio_speak(f'The system have {battery_percentage} percent battery')
    
    elif audio_exists(['Nova send email for']):
        try:
            audio_speak('What should I say Sir?')
            content = audio_record()
            to = 'youremail@gmail.com'    
            audio_email(to, content)
            audio_speak('Email has been sent Sir')
        except Exception as e:
            print(e)
            audio_speak('Sorry your friend willi bayu. I am not able to send this email') 
    
    elif audio_exists(['Nova play music']):
        music_dir = "C:\\Users\\bayu\\Music\\music"
        songs = os.listdir(music_dir)
        print(songs)    
        audio_speak('Yes Sir! please wait')
        os.startfile(os.path.join(music_dir, songs[0]))
    
    elif audio_exists(['Nova play movie']):
        movie_dir = "C:\\Users\\bayu\\Videos\\Captures\\movie"
        movies = os.listdir(movie_dir)
        print(movies)
        audio_speak('Yes Sir! please wait')
        os.startfile(os.path.join(movie_dir, movies[0]))
        
    elif audio_exists(['Nova open Discord']):
        discord = "C:\\Users\\bayu\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\\Discord.lnk"
        audio_speak('starting discord app')
        os.startfile(discord)

    elif audio_exists(['Nova open Spotify']):
        spotify = "C:\\Users\\bayu\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Spotify.lnk"
        audio_speak('starting spotify app')
        os.startfile(spotify)
        
    elif audio_exists(['Nova volume up']):
        pyautogui.press('volumeup')

    elif audio_exists(['Nova volume down']):
        pyautogui.press('volumedown')

    elif audio_exists(['Nova mute']):
        pyautogui.press('volumemute')

    elif audio_exists(['Nova who is']):
        person = voice_db.split('for')[-1]
        info = wikipedia.summary(person, sentences = 5)
        audio_speak(info)
    
    elif audio_exists(['Nova search for']):
        search = voice_db.split('for')[-1]
        url = 'http://www.google.com/search?q=' + search
        webbrowser.get().open(url)
        audio_speak('Hello Sir Here is what I found for ' + search + 'on google!')
    
    elif audio_exists(['thank you']):
        audio_speak('you are welcome Sir. See you later!')
        sys.exit(0)

#generate function start the conversation
audio_greet()

#define function to record the audio
while (1):
    time.sleep(2)
    voice_db = audio_record('Recording...')
    print('Q:', voice_db)
    audio_response(voice_db)
