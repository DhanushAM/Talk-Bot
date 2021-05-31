# TalkBot using Machine Learning in Python
#Installing Neccesary Libraries
pip install --user chatterbot==0.8.6

pip install pyttsx3

pip install SpeechRecognition

!apt install libasound2-dev portaudio19-dev libportaudio2 libportaudiocpp0 ffmpeg

!pip install PyAudio

#importing library as 'sp' to Recognize User input
import speech_recognition as sp

#Function To Taking the input from user
def takeQuery():
  sr=sp.Recognizer()
  sr.pause_threshold=1
  print("Your Bot is Listening Try to Speak")
  with sp.Microphone() as m:
    try:
      audio=sr.listen(m)
      query=sr.recognize_google(audio,language='eng-in')
      print(query)
      ask_from_talkbot()
    except Exception as e:
      print(e)
      print("Not Getting Your Words, Try To Speak properly")

import pyttsx3 
engine = pyttsx3.init('dummy')

#Used to choosing Voice to Speak-Out

voices=engine.getProperty("voices")
print(voices)

#Setting the Voice sound Male Voice Property

engine.setProperty("voice",voices[0].id)

def speak(word):
  engine.say(word)
  engine.runAndWait()

#Importing ChatBot Function From chatterbot Library 
    
from chatterbot import ChatBot
bot = ChatBot("My Bot")

#Training to the bot using chatterbot.trainers function

from chatterbot.trainers import ChatterBotCorpusTrainer

bot.set_trainer(ChatterBotCorpusTrainer)

bot.train('chatterbot.corpus.english')

#A function to asking Queries From bot

def ask_from_talkbot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert("You : " + query)
    msgs.insert("TalkBot : " + str(answer_from_bot))
    speak(answer_from_bot)
    
    print("Clicked")

  #function for A Loop to Take Repeated Queries And Gives The Proper Outputs  
    
def repeatL():    
  while(True):
    takeQuery()
    msgs = input('You: ')
    if((msgs == 'bye') or (msgs == 'Bye')):
        reply = speak('Nice Talking. See You Later')
        print(bot.name,':',speak(reply))
        print(' {} : {} '.format(bot.name, reply))
        break
    else:
      takeQuery()
      reply =speak(bot.get_response(msgs))
      print(' {} : {} '.format(bot.name, speak(reply)))

import threading

t=threading.Thread(target=repeatL)

#Calling speak Function to start The Conversation

t.start()


#calling takeQueries Fuction To take the inputs from the  user

takeQuery()
