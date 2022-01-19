# Virtual Voice Assistant (Ace)
<img src="https://github.com/Bayunova28/Navillera/blob/master/Benefits-of-Having-a-Virtual-Assistant.jpg" width="1000" height="450">

Virtual assistants are intelligent software agents that their performance is attributed to voice command. Some virtual assistants use synthesized voices to interpret the voice of 
human and response to the voice. The mundane activities and tasks perform by human waste time and energy that would have been expended on something meaningful. This is common in 
routine scenario that calls for immediate response as found in some of our everyday tasks. The technology behind virtual assistants allows users to: ask the virtual assistants 
questions, control home automation devices, play media playback through voice and manage other basic tasks such as email, to-do lists, and calendars. For example, virtual 
assistants help in the office activities in the sense that some hundreds of e-mail messages that need to be answered which could not be humanly attended to can be answered through
the hiring of virtual assistants. Any business owner can get the stress from their daily activities. There are many administrative tasks that could be solved during the day to 
free up time and relieve stress, an assistant is needed who will help in a difficult situation.

## Control accesss to less secure apps
If you ran the program and got a gmail SMTP authentication error but your username or password was correct, check your problem [here](https://support.google.com/accounts/answer/6010255). This is step if you're using smtp.gmail.com :
* Turn on the less secure apps in [recent security activity](https://myaccount.google.com/u/1/security?utm_source=OGB&utm_medium=act)
* You'll get the security mail in your gmail inbox, Click 'Yes,it's me' in that.
* Now run your code again.

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
pip install json
pip install weathercom
pip install smtplib
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

## Setting up to present the weather
```python
def audio_weather(city):
    weather = weathercom.getCityWeatherDetails(city)
    humidity = json.loads(weather)['vt1observation']['humidity']
    temp = json.loads(weather)['vt1observation']['temperature']
    phrase = json.loads(weather)['vt1observation']['phrase']
    return humidity, temp, phrase
```

## Setting up start the conversation
```python
def audio_greet():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        audio_speak('Good morning, Sir!')
    elif hour >= 12 and hour < 18:
        audio_speak('Good afternoon, Sir!')
    elif hour >= 19 and hour < 24:
        audio_speak('Good evening, Sir!')
    audio_speak('Ace at your service. Please tell me how can i help you, Sir?')
```

## Setting up to send the email
```python
def audio_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()
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
    if audio_exists(['Ace search weather for']):
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

    elif audio_exists(['Ace what time is it']):
        time = datetime.datetime.now().strftime('%I:%M %p')
        audio_speak('Current time is ' + time)
    
    elif audio_exists(['Ace show my system']):
        system_path = "C:\Program Files (x86)\MSI\Dragon Center\Dragon Center.exe"
        audio_speak('starting monitoring system')
        os.startfile(system_path)
    
    elif audio_exists(['Ace send email for']):
        try:
            audio_speak("What should I say? Sir")
            content = audio_record()
            to = 'youremail@gmail.com'    
            audio_email(to, content)
            audio_speak('Email has been sent Sir')
        except Exception as e:
            print(e)
            audio_speak('Sorry your friend willi bayu. I am not able to send this email') 
    
    elif audio_exists(['Ace play music']):
        music_dir = "C:\\Users\\bayu\\Music\\music"
        songs = os.listdir(music_dir)
        print(songs)    
        audio_speak('Yes Sir! please wait')
        os.startfile(os.path.join(music_dir, songs[0]))

    elif audio_exists(['Ace open Discord']):
        discord = "C:\\Users\\bayu\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\\Discord.lnk"
        audio_speak('starting discord app')
        os.startfile(discord)

    elif audio_exists(['Ace open Spotify']):
        spotify = "C:\\Users\\bayu\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Spotify.lnk"
        audio_speak('starting spotify app')
        os.startfile(spotify)

    elif audio_exists(['Ace tell me about']):
        person = voice_db.split('for')[-1]
        info = wikipedia.summary(person, 1)
        audio_speak(info)
    
    elif audio_exists(['Ace search for']):
        search = voice_db.split('for')[-1]
        url = 'http://www.google.com/search?q=' + search
        webbrowser.get().open(url)
        audio_speak('Hello Sir Here is what I found for ' + search + 'on google!')
    
    elif audio_exists(['thank you']):
        audio_speak('you are welcome Sir. See you later!')
        sys.exit(0)
```
