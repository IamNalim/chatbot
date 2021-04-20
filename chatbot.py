# Author: Milan Matoušek
# Date: July 2020
# Update: March 2021
# Description: Easy chatbot specially made for me

import speech_recognition as sr # speech recognition
import pygame # mixer for work with playing audio
from gtts import gTTS # google text to speech
from io import BytesIO # audio into bytes for mixer
from time import sleep # always handly

import chatbot_module as chatm # our module with chat functions

# variables for working with mic
r = sr.Recognizer()
r2 = sr.Recognizer()

# python "switch" for choosing correct command
# input:    "prikaz", string, command from user
# output:   1 or 0, int, 1 signal that command was correct, 0 that command was not valid
# desc:     Python dont have switch, so we using if statement for choosing correct command and calling function from module
def make_prikaz(prikaz):
    if prikaz == 'kolik je hodin':
        chatm.kolik_je_hodin()

    elif 'vyhledej' in prikaz:
        chatm.searching(prikaz)

    elif 'otevři' in prikaz:
        chatm.open(prikaz)

    elif 'řekni' in prikaz:
        chatm.say(prikaz)

    elif 'vypni se' == prikaz or prikaz == 'konec':
        chatm.konec()

    elif 'zapni' in prikaz:
        chatm.zapni(prikaz)

    else:
        return 0

    return 1


# Prikaz mode
# Input:    "text", string, default is empty
# Return:   None
# Desc:     brain of chatbot, from here chatbot is answer for calling and waiting for command and calling "switch" function (make_prikaz)
def prikaz_mode(text=''):
    # Chatbot is answering for calling or saying invalid command
    print('Prikaz MODE') # Debugging
    if text == '':
        chatm.text_to_fp()
    else:
        chatm.text_to_fp(text)

    chatm.play_audio()

    # waiting for command from user
    try:
        with sr.Microphone() as source3:
            r2.adjust_for_ambient_noise(source3, duration=0.5) # filtering
            audio3 = r2.listen(source3)
            prikaz = r2.recognize_google(audio3, language='cs') # audio into string
            hotovo = make_prikaz(prikaz.lower()) # give command to switch function

            # make_prikaz() return 0 so command was not valid
            if hotovo == 0:
                prikaz_mode('Příkaz se nepodařilo rozeznat')

    # some error handling
    except sr.RequestError as e:
        print('Could not request results; {}'.format(e))
        prikaz_mode('Příkaz se nepodařilo rozeznat')

    except sr.UnknownValueError:
        print('Unknown error occured')
        prikaz_mode('Příkaz se nepodařilo rozeznat')


# main loop
# Desc: Mic is always trying to analyze text and find out if its calling for chatbot ("hej báro, báro")
while True:
    try:
        with sr.Microphone() as source2:
            # little bit filtering and recording of audio
            r.adjust_for_ambient_noise(source2, duration=0.5)
            audio2 = r.listen(source2)

            # audio into text and text into lower
            task_text = r.recognize_google(audio2, language='cs')
            task_text = task_text.lower()

            print('Slyseno: {}'.format(task_text)) # Debugging

            # find out if user want to wake up chatbot
            if task_text == 'hej báro' or task_text == 'báro':
                prikaz_mode() # main function for analyse command
            else:
                continue # Not talking to chatbot, continue loop
    
    # handle some errors that could create
    except sr.RequestError as e:
        print('Could not request results; {0}'.format(e))

    except sr.UnknownValueError:
        print('Unknown error occured')

    except OSError as err:
        print('No mic detected; {0}'.format(err))
        break