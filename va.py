#will be the wrapper function that will act as main
from pathlib import Path
from openai import OpenAI
import assist
import audio
from openai import OpenAI
from gpiozero import Button
import os
import subprocess
import pyaudio
import wave
from pydub import AudioSegment
from pydub.playback import play
client = OpenAI()  #Creates the variables needed to communicate with GPT. Needs a key set up in bashrc file
thread,assistant = assist.intAssist(client)   #Calls a script to create a new assistant
x = 1  #used to retrieve messages later from an array that holds messages in the assistant API
while 1: 
    msg = audio.Butmain(client)  #Calls the button main function, and returns a string, which will be our input to GPT
    assist.addmsg(msg,thread,assistant,client,x) #Adds a message to our assistant, runs, then converts the output into an audio file
    sound = AudioSegment.from_mp3('speech.mp3') #Opens the audiofile that was generated in the previous call
    play(sound) #Plays the file
    x = x+2     #Increments the counter used for retrieving the message



