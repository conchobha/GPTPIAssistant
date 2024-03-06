#Will hold functions to

#Initialze the assistant
#Add a message to the thread
#send the output to the TTS and return it to main to play
from pathlib import Path
from openai import OpenAI
import time
x = 0
def intAssist(client): #Creates the assistant thread. could be improved by instead always refrencing an existing assistant. 
    assistant = client.beta.assistants.create(
    name="Pai", #Just the name of the AI, has no effect
    instructions="You are to answer the questions asked to the best of your ability. Answer as if you are speaking directly to a person. Keep your answers under three paragraphs. You act friendly to whoever asks a question.", #Here we can adjust the personality of the AI
    tools=[{"type": "code_interpreter"}], #If we want to add math/code functionality
    model="gpt-4-1106-preview" #to change the model if we desire
) #In the future, it might be best to instead import an already existing assistant. As of now, it creates a new one every time. 
    thread = client.beta.threads.create()
    return thread,assistant

def addmsg(msg,thread,assistant,client,x):
    message = client.beta.threads.messages.create( #sends a message to the assistant thread
    thread_id=thread.id,
    role="user",
    content=msg
)
    run = client.beta.threads.runs.create(thread_id=thread.id,assistant_id=assistant.id,) #runs the assistant to process our input
    while run.status == "queued" or run.status == "in_progress": #Waits until GPT is done processing, and is ready to output
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id,
        )
        time.sleep(0.5)
    messages = client.beta.threads.messages.list(thread_id=thread.id, order="asc") #grab the message
#messages in assistants are stored in these 2d arrays
#under data, even numbers are our input, and odd numbers are the output. This is why x starts at 1, and increases by 2
    print(messages.data[x].content[0].text.value) 
    speech_file_path = Path(__file__).parent / "speech.mp3"  #Creates a voice file to output
    response = client.audio.speech.create(model="tts-1",voice="alloy",input=messages.data[x].content[0].text.value) #Converts the Output into an Audio File
    response.stream_to_file(speech_file_path) #uses GPT to generate it from the output
    return 



