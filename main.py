#import library
import speech_recognition as sr 
import playsound  
from gtts import gTTS  
import random
import win32api
import pywhatkit
import datetime
import webbrowser
import os   
import wikipedia
import pyttsx3

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
def audio_record(ask = ''):
    with sr.Microphone() as source:
        if ask:
            audio_speak(ask)

        audio_listen = recognition.listen(source, 5, 5)
        print('finding at database')
        voice_db = ''

        try:
            voice_db = recognition.recognize_google(audio_listen)

        except sr.UnknownValueError:
            audio_speak('I am sorry Sir, I did not understand what you said. Can you please repeat again!')
        except sr.RequestError:
            audio_speak('I am sorry Sir, my server is going down')
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

#generate function class person and assistant
personObj = person()
assistantObj = assistant()
assistantObj.name = 'Navy'
engine = pyttsx3.init()

#define function to response the audio
def audio_response(voice_db):
    if audio_exists(['hello Navy']):
        audio_speak('hello, can i help you Sir?')

    if audio_exists(['how old are you']):
        audio_speak('I am 21 years old')

    if audio_exists(['what time is it']):
        time = datetime.datetime.now().strftime('%I:%M %p')
        audio_speak('Current time is ' + time)
    
    if audio_exists(['are you single']):
        audio_speak('I am in relationship with bruno')

    if audio_exists(['play for']):
        song = voice_db.split('for')[-1]
        url = 'http://www.youtube.com/results?search_query=' + song
        pywhatkit.playonyt(url)

    if audio_exists(['who is']):
        person = voice_db.split('for')[-1]
        info = wikipedia.summary(person, 1)
        audio_speak(info)
    
    if audio_exists(['search for']):
        search = voice_db.split('for')[-1]
        url = 'http://www.google.com/search?q=' + search
        webbrowser.get().open(url)
        audio_speak('Hello Bayu, Here is what I found for ' + search + 'on google!')
    
    if audio_exists(['thank you']):
        audio_speak('you are welcome Sir. See you later!')
        exit()

#define function to record the audio
while (1):
    voice_db = audio_record()
    print('Succesfully Recorded')
    print('Q:', voice_db)
    audio_response(voice_db)
