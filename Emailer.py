import os
import smtplib
import imghdr
from email.message import EmailMessage


def send(email, pwd, reciver, subject=None, content=None):
    msg = EmailMessage()
    msg["Subject"] = str(subject)
    msg["From"] = str(email)
    msg["To"] = str(reciver)
    msg.set_content(str(content))
    msg.add_alternative(
        f"\<!DOCTYPE html><html><body><h1 style='color:SlateGray;''>{content}</h1></body></html>",
        subtype="html",
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(str(email), str(pwd))
        smtp.send_message(msg)
