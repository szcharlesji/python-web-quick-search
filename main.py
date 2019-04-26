import speech_recognition as sr
import pygame as pg
from gtts import gTTS
import requests
import sys
import webbrowser
import bs4
from requests import get

r = sr.Recognizer()
speech_result = ''

with sr.Microphone() as source:
    audio = r.listen(source)
try:
    print("System predicts: "+r.recognize_google(audio))
    speech_result = r.recognize_google(audio)

except Exception:
    print("Something went wrong")


link_number = 0
working = False


while not working:
    res = requests.get('https://google.com/search?q='+speech_result)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,'html5lib')
    linktoscrape = soup.select('.r a')[link_number].get("href")[7:].split('&sa=U&ved=0')[0]

    content = get('http://api.smmry.com/&SM_API_KEY=B2A2EEA4A2&SM_URL=' + linktoscrape).json()
    print(content)

    try:
        _ = content['sm_api_error']
    except KeyError:
        working = True
        content = content['sm_api_content']
        break

    link_number += 1

    print(content)


speech = gTTS(content)

speech.save("happy.mp3")


def play_music(music_file, volume=0.8):
    '''
    stream music with mixer.music module in a blocking manner
    this will stream the sound from disk while playing
    '''
    
    # set up the mixer
    freq = 30000     # audio CD quality
    bit_size = -16    # unsigned 16 bit
    channels = 2     # 1 is mono, 2 is stereo
    buffer = 2048    # number of samples (experiment to get best sound)
    pg.mixer.init(freq, bit_size, channels, buffer)
    # volume value 0.0 to 1.0
    pg.mixer.music.set_volume(volume)
    clock = pg.time.Clock()
    try:
        pg.mixer.music.load(music_file)
        print("Music file {} loaded!".format(music_file))
    except pg.error:
        print("File {} not found! ({})".format(music_file, pg.get_error()))
        return
    pg.mixer.music.play()
    while pg.mixer.music.get_busy():
        # check if playback has finished
        clock.tick(30)
# pick a MP3 music file you have in the working folder
# otherwise give the full file path
# (try other sound file formats too)


music_file = "happy.mp3"
# optional volume 0 to 1.0
volume = 0.8
play_music(music_file, volume)
