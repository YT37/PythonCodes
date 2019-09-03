import speech_recognition as sr
from gtts import gTTS as t
import playsound as ps
import pyaudio as pa
import time
import os


def speak(text):
    tts = t(text=text, lang="en")
    fn = "voice.mp3"
    tts.save(fn)
    ps.playsound(fn)


def audio():
    r = sr.Recognizer()

    print("Listening....")

    with sr.Microphone() as source:
        aud = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(aud)
            print(said)

        except Exception as e:
            print("Exception : " + str(e))

    return said


text = audio()
if "hello" in text:
    speak("Hi,How Are You?")
