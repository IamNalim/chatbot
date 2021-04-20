# Author: Milan Matoušek
# Date: July 2020
# Update: March 2021
# Description: Module for chatbot

import datetime
import webbrowser
import pygame
from gtts import gTTS
from io import BytesIO
from time import sleep


# text into floating point audio
# input:    "text", string, command that will our chatbot say (default is answer to waking up chatbot)
# output:   None
# Desc:     In this function we gonna create FP audio from text that is gonna be played.
def text_to_fp(text='Copak je Milane?'):
    global mp3_fp # make var. mp3_fp global (its gonna be used in play_audio())
    mp3_fp = BytesIO()
    tts = gTTS(text=text, lang='cs', slow=False)
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)


# play audio/answer from chatbot
# input:    None  
# output:   print, function, its indicate that we can again wait for user command and for debugging 
# Desc:     Function is only for playing chatbot answer and waiting till we can again make a new command.
def play_audio():
    if not pygame.mixer.init(): # inicialization mixer for playing sound without store file
        pygame.mixer.init()

    pygame.mixer.music.load(mp3_fp) # load audio into mixer
    pygame.mixer.music.play() # playing audio

    # wait till audio is playing
    while pygame.mixer.music.get_busy():
        print('cekam') # Debugging
    
    return print('Jdu zpet') # Debug message


# Find out time
# input:    None  
# output:   None
# Desc:     Simple function say current time
def kolik_je_hodin():
    now = datetime.datetime.now()
    answer = 'Je právě {} hodin a {} minut'.format(now.hour, now.minute)
    text_to_fp(answer)
    play_audio()


# Google searching
# input:    "prikaz", string, command what we should searching for
# output:   None
# Desc:     Simple function that will replace command word and searching on google input from user
def searching(prikaz):
    term = prikaz.replace('vyhledej', '') # cut off command
    url = 'https://www.google.com.tr/search?q={}'.format(term)
    webbrowser.open_new_tab(url)
    answer = 'Vyhledávám {}'.format(term)
    text_to_fp(answer)
    play_audio()


# Opening some webpages
# input:    "prikaz", string, command what we should opened
# output:   None or error message from bot that user input invalid command
# Desc:     Simple function to open a few of the famous webpages
def open(prikaz):
    term = prikaz.replace('otevři', '') # cut off command
    if 'facebook' in term:
        url = 'https://www.facebook.com/'
    elif 'twitter' in term:
        url = 'https://www.twitter.com/'
    elif 'instagram' in term:
        url = 'https://www.instagram.com/'
    elif 'zing' in term:
        url = 'https://zing.cz/'
    else:
        return text_to_fp('Příkaz se nepodařilo rozeznat'), play_audio()
    
    webbrowser.open_new_tab(url)
    answer = 'Otevírám {}'.format(term)
    text_to_fp(answer)
    play_audio()

# Opening random playlist on youtube
# input:    "prikaz", string, command for opening youtube, playlist, closing app
# output:   None
# Desc:     Function to open youtube or open playlist (or open playlist and close app)
def zapni(prikaz):
    term = prikaz.replace('zapni', '')
    vypnout = False
    if 'random' in term:
        url = 'https://www.youtube.com/watch?v=p9asRPqPbjo&list=RDp9asRPqPbjo&start_radio=1'
        if 'vypni se' in term:
            term = term.replace('vypni se', 'vypínám se')
            vypnout = True

    else:
        url = 'https://www.youtube.com/'
    
    webbrowser.open_new_tab(url)
    answer = 'Zapínám {}'.format(term)
    text_to_fp(answer)
    play_audio()
    if vypnout:
        konec()
    else:
        pass

# Simple echo
# input:    "prikaz", string, what should chatbot say
# output:   None
# Desc:     Simple function to echo input and cut off "řekni"
def say(prikaz):
    term = prikaz.replace('řekni', '')
    text_to_fp(term)
    play_audio()

# Closing app
# input:    None
# output:   Closed app
# Desc:     Function for closing chatbot
def konec():
    text_to_fp('Měj se hezky')
    play_audio()
    sleep(2)
    quit()