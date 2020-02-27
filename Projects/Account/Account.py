import os
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
db = connector.connect(host="localhost",
                       user="root",
                       passwd=os.environ.get("Password"),
                       database="Users")

cursor = db.cursor(buffered=True)


def enterUser(email, pwd, win):
    cursor.execute(
        """INSERT INTO userInfo (Username,Password) VALUES ('%s','%s')""" %
        (email.lower(), pwdHash.hash(pwd)))
    emVal = email.lower()
    db.commit()
    welcome(emVal, win)


def delete(email, win):
    cursor.execute("""DELETE FROM userInfo WHERE Username = '%s'""" % (email))
    db.commit()
    win.destroy()


def welcome(email, oldWin):
    oldWin.destroy()
    win = t.Tk()
    win.title("Account")
    win.geometry("320x200")
    win.config(bg="black")

    emailSt = str(email).split("@")

    welLabel = t.Label(
        win,
        text=f"Welcome, {emailSt[0].capitalize()}",
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
        command=lambda: delete(email.lower(), win),
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


def logIn(email, pwd, win):
    cursor.execute("""SELECT Username FROM userInfo""")

    for user in cursor:
        if email == str(user)[2:-3]:
            cursor.execute(
                """SELECT Password FROM userInfo WHERE Username = '%s'""" %
                (email))

            for passwd in cursor:
                if pwdHash.verify(str(pwd), str(passwd)[2:-3]):
                    emVal = email
                    welcome(emVal, win)
                else:
                    messagebox.showinfo(
                        "Wrong Password",
                        "The Password You Entered Is Wrong, Try Again")
        else:
            messagebox.showinfo(
                "Not Registered",
                "The Email You Entered Is Wrong Or Either Not Registered",
            )


def signUp(email, pwd, win):
    win.title("Sign Up")
    win.iconbitmap("SignUp.ico")

    if re.search(r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$", email):
        if all(char.isalnum() for char in pwd):
            cursor.execute("""SELECT count(*) as tot FROM userInfo""")

            if (str(cursor.fetchone())[1]) == "0":
                enterUser(email, pwd, win)

            else:
                cursor.execute(
                    """SELECT Username FROM userInfo WHERE Username = '%s'""" %
                    (email))
                for user in cursor:
                    if (str(type(user))[8:-2]) == "tuple":
                        messagebox.showinfo(
                            "User Already Registered",
                            "Email Is In Use For An Account Use Another One",
                        )
                        win.title("Log In")
                        win.iconbitmap("LogIn.ico")

                    else:
                        enterUser(email, pwd, win)

        elif not any(char.isalnum() for char in pwd):
            messagebox.showinfo(
                "Weak Password",
                "The Password Should Contain At least One Uppercase And Lowercase Letter, One Digit",
            )

    else:
        messagebox.showinfo("Incorrect Email",
                            "Email Format Should Be (abc01@exp.abc)")


def main():
    win = t.Tk()
    win.iconbitmap("LogIn.ico")
    win.title("Log In")
    win.geometry("320x200")
    win.config(bg="black")

    emailVal = t.StringVar()
    pwdVal = t.StringVar()

    emailLabel = t.Label(win,
                         text="Email : ",
                         bg="black",
                         fg="white",
                         font=("Helvetica", "11"))
    emailLabel.grid(row=0, column=0, padx=5, pady=5)

    email = t.Entry(win,
                    textvariable=emailVal,
                    bg="black",
                    fg="white",
                    font=("Helvetica", "9"))
    email.grid(row=0, column=1, padx=5, pady=5)

    pwdLabel = t.Label(win,
                       text="Password : ",
                       bg="black",
                       fg="white",
                       font=("Helvetica", "11"))
    pwdLabel.grid(row=1, column=0, padx=5, pady=5)

    pwd = t.Entry(
        win,
        textvariable=pwdVal,
        show="*",
        bg="black",
        fg="white",
        font=("Helvetica", "9"),
    )
    pwd.grid(row=1, column=1, padx=5, pady=5)

    passShow = t.Button(
        win,
        text="Show",
        bg="black",
        fg="white",
        font=("Helvetica", "7"),
        command=lambda: pwd.config(show=""),
    )
    passShow.grid(row=1, column=2)

    passHide = t.Button(
        win,
        text="Hide",
        bg="black",
        fg="white",
        font=("Helvetica", "7"),
        command=lambda: pwd.config(show="*"),
    )
    passHide.grid(row=1, column=3)

    logInb = t.Button(
        win,
        text="Log In",
        font=("Helvetica", "11"),
        command=lambda: logIn(emailVal.get().lower(), pwdVal.get(), win),
    )
    logInb.grid(row=2, column=1, padx=5, pady=5)

    signUpLabel = t.Label(win,
                          text="New User ? Sign Up",
                          font=("Helvetica", "11"),
                          bg="black",
                          fg="white")
    signUpLabel.grid(row=3, column=1)

    signUpb = t.Button(
        win,
        text="Sign Up",
        font=("Helvetica", "11"),
        command=lambda: signUp(emailVal.get().lower(), pwdVal.get(), win),
    )
    signUpb.grid(row=4, column=1, padx=5, pady=5)

    win.mainloop()


if __name__ == "__main__":
    main()
    # db = connector.connect(host="localhost",
    #                        user="root",
    #                        passwd=os.environ.get("Password"),
    #                        database="Users")
    # cursor = db.cursor(buffered=True)
    # cursor.execute("CREATE DATABASE Users")
    # cursor.execute("CREATE TABLE userInfo (Username VARCHAR(50),Password VARCHAR(300))")
