"""
$ pip install google-generativeai
"""
import os
import time
from pydub.playback import play
from pydub import AudioSegment
import pyttsx3
import google.generativeai as genai

genai.configure(api_key="AIzaSyBnEQMl-hbEuOY6Mn6hnpHgzmP9uU4AY0E")

engine = pyttsx3.init()
engine.setProperty("rate", 145)
        
with open("instructions.txt","r") as F1,open("teachers.txt","r") as F2:
    instructions = F1.read()
    teachers = F2.read()

# Create the model
generation_config = {
  "temperature": 2,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 100,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
  system_instruction=instructions

)

history=[
    {
      "role": "user",
      "parts": [
        teachers,
      ],
    }
  ]

chat_session = model.start_chat(
  history=history
)

# message = "Welcome!  I'm Rishi, the virtual assistant for Maria Assumpta Convent School. How can I help you today?"
# print(message)
# engine.say(message)
# engine.runAndWait()

def playthis(file):
    sound = AudioSegment.from_file(file)
    play(sound)

def capture():
  os.system("libcamera-jpeg --rotation 180 -o ~/Desktop/new/image_file/test.jpg -n")


flag = False

while True:

  text=input("Enter what you want to ask Rishi: ")

  if 'hello rishi' in text and not flag:
    ac = "(Rishi Activation Sound)"
    print(f"\r{ac}",end="") # print("\r(Rishi Activation Sound)",end='')
    playthis('activation_sound.mp3')
    wb = "Hello! How can I help you today?"
    print(f"\r{wb}")
    engine.say(wb)
    engine.runAndWait()
    flag = True
    continue

  if 'listen rishi' in text and not flag:
    
    ac = "(Rishi Activation Sound)"
    print(f"\r{ac}",end="") # print("\r(Rishi Activation Sound)",end='')
    playthis('activation_sound.mp3')
    wb = "welcome back             "
    print(f"\r{wb}")
    engine.say(wb)
    engine.runAndWait()
    flag = True
    continue
  
  if 'capture' in text and flag:
    print("Processing...")
    capture()
    myfile = genai.upload_file("image_file/test.jpg")
    print("Processing")
    result = model.generate_content([myfile, "\n\n", "Can you tell me about this photo?"])
    a = result.text
    a = a.replace("*","")
    print(a)
    engine.say(a)

    engine.runAndWait()
    continue

  if 'details' and 'photo' in text:
    myfile = genai.upload_file("image_file/test.jpg")
    print("Processing")
    d = input("Enter what you want to ask about the photo: ")
    result = model.generate_content([myfile, "\n\n", d])
    a = result.text
    a = a.replace("*","")
    print(a)
    engine.say(a)

    engine.runAndWait()
    continue


  if 'please wait' in text and flag:
    print("Of course! Take your time, and let me know when you're ready.")
    engine.say("Of course! Take your time, and let me know when you're ready.")
    engine.runAndWait()
    flag = False
    continue
   
  if 'stop' in text and flag:
    response = chat_session.send_message(text)
    a=response.text
    a = a.replace("*","")
    print("Rishi: ",a)
    print("Goodbye, shutting down the system.")
    engine.say("Goodbye, shutting down the system.")
    engine.runAndWait()
    time.sleep(2.5)
    playthis('deactivation.mp3')
    break



  if flag:
    response = chat_session.send_message(text)
    a=response.text
    a = a.replace("*","")
    print("You:",text)
    print("Rishi:",a)
    # engine.setProperty('rate',400)
    engine.say(a)
    engine.runAndWait()