from __future__ import print_function

import datetime
import os.path
import pickle
import subprocess
import time

import playsound as ps
import pyaudio as pa
import pyttsx3
import pytz
import speech_recognition as sr
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

scopes = ["https://www.googleapis.com/auth/calendar.readonly"]
months = [
    "January",
    "Febuary",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
days = ["Monday", "Tuesday", "Wednesday", "Thurday", "Friday", "Saturday", "Sunday"]
daysExt = ["st", "nd", "rd", "th"]
calStrs = ["What do i have", "do i have plans", "busy"]
noteStrs = ["make a note", "write this down", "remember this"]


def authenticate():
    creds = None

    if os.path.exists("Token.pickle"):
        with open("Token.pickle", "rb") as Token:
            creds = pickle.load(Token)

    if not creds or not creds.valid:

        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        else:
            flow = InstalledAppFlow.from_client_secrets_file("Cred.json", scopes)
            creds = flow.run_local_server(port=0)

        with open("Token.pickle", "wb") as Token:
            pickle.dump(creds, Token)

    service = build("calendar", "v3", credentials=creds)

    return service


def getevent(days, s):
    date = datetime.datetime.combine(days, datetime.datetime.min.time())
    end = datetime.datetime.combine(days, datetime.datetime.max.time())

    utc = pytz.UTC

    date = date.astimezone(utc)
    end = end.astimezone(utc)

    eventResult = (
        s.events()
        .list(
            calendarId="primary",
            timeMin=date.isoformat(),
            timeMax=end.isoformat(),
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )

    events = eventResult.get("items", [])

    if not events:
        print("No upcoming events found.")

    else:
        speak(f"You have {len(events)} Events On This Day.")

        for event in events:
            start = event["start"].get("dateTime", event["start"].get("date"))
            print(start, event["summary"])
            startTime = str(start.split("T")[1].split("-")[0])

            if int(startTime.split(":")[0]) < 12:
                startTime = startTime + "AM"

            else:
                startTime = (
                    str(int(startTime.split(":")[0]) - 12) + startTime.split(":")[1]
                )
                startTime = startTime + "PM"

            speak(event["summary"] + "At" + startTime)


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


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

    return said.lower()


def getDate(text):
    text = text.lower()
    today = datetime.date.today()

    if text.count("today") > 0:
        return today

    day = -1
    dayWeek = -1
    mon = -1
    year = today.year

    for word in text.split():
        if word in months:
            mon = months.index(word) + 1

        elif word in days:
            dayWeek = days.index(word)

        elif word.isdigit():
            day = int(word)

        else:
            for ext in daysExt:
                found = word.find(ext)

                if found > 0:
                    try:
                        day = int(word[:found])

                    except:
                        pass

    if mon < today.month and mon != -1:
        year = year + 1

    if mon == -1 and day != -1:
        if day < today.day:
            mon = today.month + 1

        else:
            mon = today.month

    if mon == -1 and day == -1 and dayWeek != -1:
        currentDayWeek = today.weekday()
        dif = dayWeek - currentDayWeek

        if dif < 0:
            dif += 7

            if text.count("next") >= 1:
                dif += 7

        return today + datetime.timedelta(dif)
    if day != -1:
        return datetime.date(month=mon, day=day, year=year)


def note(text):
    date = datetime.datetime.now()
    fileName = str(date).replace(":", "-") + "-note.txt"

    with open(fileName, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", fileName])


wake = "max"
service = authenticate()
print("Start")
while True:
    text = audio()

    if text.count(wake) > 0:
        speak("I Am Ready")
        text = audio()

    for phrase in calStrs:
        if phrase in text:
            date = getDate(text)

            if date:
                getevent(date, service)

            else:
                speak("Please Try Again")

    for phrase in noteStrs:
        if phrase in text:
            speak("What Would You Like Me To Write Down ?")
            noteText = audio()
            note(noteText)
            speak("I've Made A Note Of That.")
