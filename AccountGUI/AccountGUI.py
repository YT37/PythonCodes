import re
import tkinter as t
from tkinter import messagebox
from mysql import connector
from passlib.context import CryptContext

pwdHash = CryptContext(
    schemes=["pbkdf2_sha256"],
    default="pbkdf2_sha256",
    pbkdf2_sha256__default_rounds=30000,
)

db = connector.connect(
    host="localhost", user="root", passwd="Agasthya4572$:my", database="Users"
)

cursor = db.cursor(buffered=True)


global mainWin
global pwdVal
global emailVal


def enterUser():
    cursor.execute(
        "INSERT INTO userInfo (Username,Password) VALUES ('%s','%s')"
        % ((emailVal.get().lower()), (pwdHash.hash(pwdVal.get())))
    )
    emVal = emailVal.get().lower()
    db.commit()
    welcome(emVal)


def delete(email, win):
    cursor.execute("DELETE FROM userInfo WHERE Username = '%s'" % (email))
    db.commit()
    win.destroy()


def welcome(email):
    mainWin.destroy()
    win = t.Tk()
    win.title("Account")
    win.geometry("320x200")
    win.config(bg="black")
    em = str(email).split("@")
    welLabel = t.Label(
        win,
        text=f"Welcome, {em[0].capitalize()}",
        bg="black",
        fg="white",
        font=("Helvetica", "11"),
    )
    welLabel.grid(row=0, column=0, padx=5, pady=5)

    deleteUser = t.Button(
        win,
        text="Delete User",
        bg="white",
        fg="black",
        font=("Helvetica", "11"),
        command=lambda: delete(email, win),
    )
    deleteUser.grid(row=1, column=0, padx=5, pady=5)

    logOut = t.Button(
        win,
        text="Log Out",
        bg="white",
        fg="black",
        font=("Helvetica", "11"),
        command=lambda: win.destroy(),
    )
    logOut.grid(row=2, column=0, padx=5, pady=5)


def logIn():
    cursor.execute("SELECT Username FROM userInfo")

    for user in cursor:
        if emailVal.get().lower() == str(user)[2:-3]:
            cursor.execute(
                f"SELECT Username,Password FROM userInfo WHERE Username = '{emailVal.get().lower()}'"
            )

            for passwd in cursor:
                if pwdHash.verify(pwdVal.get(), str(passwd)[17:-2]):
                    emVal = emailVal.get().lower()
                    welcome(emVal)
                else:
                    messagebox.showinfo(
                        "Wrong Password", "The Password You Entered Is Wrong, Try Again"
                    )
        else:
            messagebox.showinfo(
                "Not Registered",
                "The Email You Entered Is Wrong Or Either Not Registered",
            )


def signUp():
    mainWin.title("Sign Up")
    mainWin.iconbitmap("SignUp.ico")
    if re.search(r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$", emailVal.get()):
        if all(char.isalnum() for char in pwdVal.get()):
            cursor.execute("SELECT count(*) as tot FROM userInfo")

            if (str(cursor.fetchone())[1]) == "0":
                enterUser()

            else:
                cursor.execute("SELECT Username FROM userInfo")

                for user in cursor:
                    if str(user)[2:-3] == str(emailVal.get()):
                        messagebox.showinfo(
                            "User Already Registered",
                            "Email Is In Use For An Account Use Another One",
                        )
                        mainWin.title("Log In")
                        mainWin.iconbitmap("LogIn.ico")

                    else:
                        enterUser()

        elif not any(char.isalnum() for char in pwdVal.get()):
            messagebox.showinfo(
                "Weak Password",
                "The Password Should Contain At least One Uppercase And Lowercase Letter, One Digit",
            )

    else:
        messagebox.showinfo("Incorrect Email", "Email Format Should Be (abc01@exp.abc)")


mainWin = t.Tk()
mainWin.iconbitmap("LogIn.ico")
mainWin.title("Log In")
mainWin.geometry("320x200")
mainWin.config(bg="black")


emailVal = t.StringVar()
pwdVal = t.StringVar()

emailLabel = t.Label(
    mainWin, text="Email : ", bg="black", fg="white", font=("Helvetica", "11")
)
emailLabel.grid(row=0, column=0, padx=5, pady=5)

email = t.Entry(
    mainWin, textvariable=emailVal, bg="black", fg="white", font=("Helvetica", "9")
)
email.grid(row=0, column=1, padx=5, pady=5)

pwdLabel = t.Label(
    mainWin, text="Password : ", bg="black", fg="white", font=("Helvetica", "11")
)
pwdLabel.grid(row=1, column=0, padx=5, pady=5)

pwd = t.Entry(
    mainWin,
    textvariable=pwdVal,
    show="*",
    bg="black",
    fg="white",
    font=("Helvetica", "9"),
)
pwd.grid(row=1, column=1, padx=5, pady=5)

passShow = t.Button(
    mainWin,
    text="Show",
    bg="black",
    fg="white",
    font=("Helvetica", "7"),
    command=lambda: pwd.config(show=""),
)
passShow.grid(row=1, column=2)

passHide = t.Button(
    mainWin,
    text="Hide",
    bg="black",
    fg="white",
    font=("Helvetica", "7"),
    command=lambda: pwd.config(show="*"),
)
passHide.grid(row=1, column=3)

logInb = t.Button(mainWin, text="Log In", font=("Helvetica", "11"), command=logIn)
logInb.grid(row=2, column=1, padx=5, pady=5)

signUpLabel = t.Label(
    mainWin, text="New User ? Sign Up", font=("Helvetica", "11"), bg="black", fg="white"
)
signUpLabel.grid(row=3, column=1)

signUpb = t.Button(mainWin, text="Sign Up", font=("Helvetica", "11"), command=signUp)
signUpb.grid(row=4, column=1, padx=5, pady=5)

mainWin.mainloop()
