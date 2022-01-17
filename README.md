# Virtual Assistant (Navillera)
<img src="https://github.com/Bayunova28/Navillera/blob/master/Benefits-of-Having-a-Virtual-Assistant.jpg" width="1000" height="450">

Virtual assistants are intelligent software agents that their performance is attributed to voice command. Some virtual assistants use synthesized voices to interpret the voice of 
human and response to the voice. The mundane activities and tasks perform by human waste time and energy that would have been expended on something meaningful. This is common in 
routine scenario that calls for immediate response as found in some of our everyday tasks. The technology behind virtual assistants allows users to: ask the virtual assistants 
questions, control home automation devices, play media playback through voice and manage other basic tasks such as email, to-do lists, and calendars. For example, virtual 
assistants help in the office activities in the sense that some hundreds of e-mail messages that need to be answered which could not be humanly attended to can be answered through
the hiring of virtual assistants. Any business owner can get the stress from their daily activities. There are many administrative tasks that could be solved during the day to 
free up time and relieve stress, an assistant is needed who will help in a difficult situation.

## Install Package
```python
pip install SpeechRecognition
pip install playsound
pip install gTTS
pip install random2
pip install pywin32
pip install pywhatkit
pip install DateTime
pip install wikipedia
pip install pyttsx3
```

## Setting up response of person and assistant
```python
class person:
    name = ''
    def setName(self, name):
        self.name = name

class assistant:
    name = ''
    def setName(self, name):
        self.name = name
```

## Setting up list of text message on audio
```python
def audio_exists(terms):
    for term in terms:
        if term in voice_db:
            return True
```

## Setting up audio to convert the text
```python
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
```

## Setting up to save the audio record
```python
def audio_speak(audio_string):
    audio_string = str(audio_string)
    google_text = gTTS(text = audio_string, lang = 'en')
    r = random.randint(1, 2000000)
    file = 'audio' + str(r) + '.mp3'
    google_text.save(file)
    playsound.playsound(file)
    print(assistantObj.name + ':', audio_string)
    os.remove(file)
```

## Setting up audio response the message
```python
def audio_response(voice_db):
    if audio_exists(['how old are you']):
        audio_speak('I am 21 years old')

    if audio_exists(['what time is it']):
        time = datetime.datetime.now().strftime('%I:%M %p')
        audio_speak('Current time is ' + time)
    
    if audio_exists(['are you single']):
        audio_speak('I am in relationship with wifi')

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
```
