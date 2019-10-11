from tkinter import *
import mysql.connector
from datetime import datetime
from functools import partial
from passlib.context import CryptContext
import re
from tkinter import messagebox

pwdHash = CryptContext(
    schemes=["pbkdf2_sha256"],
    default="pbkdf2_sha256",
    pbkdf2_sha256__default_rounds=30000,
)
# TODO LogIn And Welcome And Delete

db = mysql.connector.connect(
    host="localhost", user="root", passwd="Agasthya4572$:my", database="Users"
)

cursor = db.cursor()
global win
global pwdVal
global emailval


def welcome():
    pass


def logIn():
    pass


def delete():
    pass


def signUp():
    if re.search("^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$", emailVal.get()):
        if any(char.isalnum() for char in pwdVal.get()):
            cursor.execute(
                "INSERT INTO userInfo (Username,Created,Password) VALUES (%s,%s,%s)",
                (emailVal.get(), datetime.now(), pwdHash.hash(pwdVal.get())),
            )

            db.commit()
            win.destroy()

        elif not any(char.isalnum() for char in pwdVal.get()):
            messagebox.showinfo(
                "Weak Password",
                "The Password Sould Contain Atleast One Uppercase And Lowercase Letter, One Digit",
            )

    else:
        messagebox.showinfo(
            "Incorrect Email", "Check Email Format (abc01exp.abc) And Renter"
        )


win = Tk()
win.title("SignUp")
win.geometry("320x200")
win.config(bg="black")

emailVal = StringVar()
pwdVal = StringVar()

el = Label(win, text="Email : ", bg="black", fg="white", font=("Helvetica", "11"))
el.grid(row=0, column=0, padx=5, pady=5)

email = Entry(
    win, textvariable=emailVal, bg="black", fg="white", font=("Helvetica", "9")
)
email.grid(row=0, column=1, padx=5, pady=5)

pl = Label(win, text="Password : ", bg="black", fg="white", font=("Helvetica", "11"))
pl.grid(row=1, column=0, padx=5, pady=5)

pwd = Entry(
    win, textvariable=pwdVal, show="*", bg="black", fg="white", font=("Helvetica", "9")
)
pwd.grid(row=1, column=1, padx=5, pady=5)

passShow = Button(
    win,
    text="Show",
    bg="black",
    fg="white",
    font=("Helvetica", "7"),
    command=lambda: pwd.config(show=""),
)
passShow.grid(row=1, column=2)

passHide = Button(
    win,
    text="Hide",
    bg="black",
    fg="white",
    font=("Helvetica", "7"),
    command=lambda: pwd.config(show="*"),
)
passHide.grid(row=1, column=3)

logInb = Button(win, text="Log In", font=("Helvetica", "11"))
logInb.grid(row=2, column=1, padx=5, pady=5)

signUpLabel = Label(
    win, text="New User ? Sign Up", font=("Helvetica", "11"), bg="black", fg="white"
)
signUpLabel.grid(row=3, column=1)

signUpb = Button(win, text="Sign Up", font=("Helvetica", "11"), command=signUp)
signUpb.grid(row=4, column=1, padx=5, pady=5)

win.mainloop()

cursor.execute("DELETE FROM userInfo WHERE Username = ' '")
db.commit()
cursor.execute("SELECT Username,Password,ID FROM userInfo ORDER BY ID ASC")

for x in cursor:
    print(x)
