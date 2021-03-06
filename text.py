import pyttsx3
from googletrans import Translator
engine = pyttsx3.init()
sentence = str(input("Say ... > "))

""" RATE"""
rate = engine.getProperty('rate')  
print (rate)                        # printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate

"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
# engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

engine.say(sentence)
engine.runAndWait()
engine.stop()

translator = Translator()
sentence = translator.translate(sentence,dest='th')
print("แปลภาษา : " , sentence.text)