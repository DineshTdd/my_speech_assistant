import speech_recognition as sr
import webbrowser
import time
from playsound import playsound
import random
from gtts import gTTS
import os
from time import ctime

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            td_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            td_speak('Sorry, I did not get that')
        except sr.RequestError:
            td_speak('Sorry, my speech service is down')
        return voice_data
    
def td_speak(audio_string):
    tts = gTTS(text = audio_string, lang = 'en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'what is your name' in voice_data:
        td_speak('My name is 3000!')
    if 'what time is it' in voice_data:
        td_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        if search is not '':
            url = 'https://google.com/search?q=' + search
            webbrowser.get().open(url)
            td_speak('Here is what I found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        if location is not '':
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get().open(url)
            td_speak('Here is the location of ' + location)
    if 'exit' in voice_data:
        exit()
time.sleep(1)
td_speak('How can I help you?')
while 1:
    voice_data = record_audio()
    if not voice_data:
        continue
    respond(voice_data)