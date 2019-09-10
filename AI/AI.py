from __future__ import print_function

import datetime
import os.path
import pickle
import time

import playsound as ps
import pyaudio as pa
import speech_recognition as sr
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from gtts import gTTS as t

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


def getevent(n, s):
    now = datetime.datetime.utcnow().isoformat() + "Z"
    print(f"Getting the upcoming {n} events")
    events_result = (
        s.events()
        .list(
            calendarId="primary",
            timeMin=now,
            maxResults=n,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )
    events = events_result.get("items", [])

    if not events:
        print("No upcoming events found.")
    for event in events:
        start = event["start"].get("dateTime", event["start"].get("date"))
        print(start, event["summary"])


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


def getDate(text):
    text = text.lower()
    today = datetime.date.today()

    if text.count("today") > 0:
        return today

    day = -1
    dayWeek = -1
    month = -1
    year = today.year

    for word in text.split():
        if word in months:
            month = months.index(word) + 1

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

    if month < today.month and month != -1:
        year += 1

    if day < today.day and month == -1 and day != -1:
        month += 1

    if month == -1 and day == -1 and dayWeek != -1:
        currentDayWeek = today.weekday()
        dif = dayWeek - currentDayWeek

        if dif < 0:
            dif += 7

            if text.count("next") >= 1:
                dif += 7

        return today + datetime.timedelta(dif)

    return datetime.date(month=month, day=day, year=year)


text = audio().lower()
print(getDate(text))