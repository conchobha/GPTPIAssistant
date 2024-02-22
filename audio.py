from openai import OpenAI
from gpiozero import Button
import os
import subprocess
import pyaudio
import wave
def mp3totext(client): #Returns a string, converted from the speech.wav file
    audio_file = open("speech.wav", "rb")
    transcript = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file
) 
    print(transcript.text)
    return transcript.text
#This function creates a bunch of nasty error messages in the terminal, but doesn't actually halt, and works correctly. 
#Most likely an issue with the implementation of the pyaudio function. 
def Butmain(client):
    button = Button(16)  #Creates a button on pin 16 (Otherside connected to ground)
    button.wait_for_press()  #Halts the function until it detects a button press                     
    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    seconds = 20
    filename = "speech.wav"   #Will be our input audio file

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    while button.value == 1:
        data = stream.read(chunk)
        frames.append(data)
     #Halts the program until the button is released. 
    # Stop and close the stream 
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    return mp3totext(client)  #Calls mp3totext to convert the recorded file into text, then returns the string  
    