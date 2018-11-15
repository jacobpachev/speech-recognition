#!/usr/bin/env python3                                                                                
import os
import speech_recognition as sr  

# get audio from the microphone                                                                       
r = sr.Recognizer()                                                                                   
with sr.Microphone() as source:                                                                       
    print("Speak:")                                                                                   
    audio = r.listen(source)   
try:
    for i in range(0,len(r.recognize_google(audio))):
        if(r.recognize_google(audio)[i] == ' '):
            name = r.recognize_google(audio)[0:i]
            b = r.recognize_google(audio)[i:i + 4]
            x = r.recognize_google(audio)[i:i + 8]
            c = r.recognize_google(audio)[i:i + 5]
            if(x == "punched" and c == 'kicked'):
                a = (name + " don't " + b + " be nice")
                os.system("espeak -p 35 " + '"' + a + '"')
                break
            if(x != "punched"):
                x = r.recognize_google(audio)[i:i + 4]
                a = (name + " don't " + x + " be nice")
                os.system("espeak -p 35 " + '"' + a + '"')
                break
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))