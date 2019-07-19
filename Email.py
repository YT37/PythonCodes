import os
import smtplib
import imghdr
from email.message import EmailMessage
Add = os.environ.get('Email')
Pass = os.environ.get('Password')
contacts = ['yugthapar37@gmail.com', 'test@example.com']
msg = EmailMessage()
msg['Subject'] = 'Check out Max as a puppy!'
msg['From'] = Add
msg['To'] = 'yugthapar37@gmail.com'
msg.set_content('This is a plain text email')
msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">This is an HTML Email!</h1>
    </body>
</html>
""", subtype='html')
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(Add, Pass)
    smtp.send_message(msg)