Built for a Class. Works via a few different open AI API’s to allow for a GPT chatbot. Attached are some pictures of the final project. 

Assembly Instructions:

Connect a speaker and USB Microphone to Rasberry Pi. Make sure they are the default sound device
Connect a push button on pin 16 and ground. 
Verify that all needed python packages are installed
Verify that a GPT API key is inside the .bashrc file of the pi
Run va.py

Running Instructions:

Hold push button, and talk. Maximum time is 20 seconds. 
Release button when done talking
Wait for response from GPT, might take upwards of 20+ seconds depending on prompt. 
Can edit personality in the assist.py function
