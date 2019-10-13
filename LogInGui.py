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
# TODO Welcome And Delete

db = connector.connect(
    host="localhost", user="root", passwd="Agasthya4572$:my", database="Users"
)

cursor = db.cursor(buffered=True)
global main
global pwdVal
global emailVal


def enterUser():
    cursor.execute(
        "INSERT INTO userInfo (Username,Password) VALUES (%s,%s,%s)",
        (emailVal.get().lower(), pwdHash.hash(pwdVal.get())),
    )
    db.commit()
    main.destroy()


def welcome():
    pass


def logIn():
    cursor.execute("SELECT Username FROM userInfo")

    for user in cursor:
        if emailVal.get().lower() == str(user)[2:-3]:
            cursor.execute(
                "SELECT Password FROM userInfo WHERE Username = '%s'"
                % (emailVal.get().lower())
            )

            for passwd in cursor:
                print(str(passwd)[2:-3])
                print(pwdVal.get())
                if pwdHash.verify(str(pwdVal.get()), str(passwd)[2:89]):
                    welcome()


def delete():
    cursor.execute("DELETE FROM userInfo WHERE Username = 'b@a.aaa'")
    db.commit()


def signUp():
    main.title("Sign Up")
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

                    else:
                        enterUser()

        elif not any(char.isalnum() for char in pwdVal.get()):
            messagebox.showinfo(
                "Weak Password",
                "The Password Should Contain At least One Uppercase And Lowercase Letter, One Digit",
            )

    else:
        messagebox.showinfo("Incorrect Email", "Email Format Should Be (abc01@exp.abc)")


main = t.Tk()
main.title("Log In")
main.geometry("320x200")
main.config(bg="black")

emailVal = t.StringVar()
pwdVal = t.StringVar()

el = t.Label(main, text="Email : ", bg="black", fg="white", font=("Helvetica", "11"))
el.grid(row=0, column=0, padx=5, pady=5)

email = t.Entry(
    main, textvariable=emailVal, bg="black", fg="white", font=("Helvetica", "9")
)
email.grid(row=0, column=1, padx=5, pady=5)

pl = t.Label(main, text="Password : ", bg="black", fg="white", font=("Helvetica", "11"))
pl.grid(row=1, column=0, padx=5, pady=5)

pwd = t.Entry(
    main, textvariable=pwdVal, show="*", bg="black", fg="white", font=("Helvetica", "9")
)
pwd.grid(row=1, column=1, padx=5, pady=5)

passShow = t.Button(
    main,
    text="Show",
    bg="black",
    fg="white",
    font=("Helvetica", "7"),
    command=lambda: pwd.config(show=""),
)
passShow.grid(row=1, column=2)

passHide = t.Button(
    main,
    text="Hide",
    bg="black",
    fg="white",
    font=("Helvetica", "7"),
    command=lambda: pwd.config(show="*"),
)
passHide.grid(row=1, column=3)

logInb = t.Button(main, text="Log In", font=("Helvetica", "11"), command=logIn)
logInb.grid(row=2, column=1, padx=5, pady=5)

signUpLabel = t.Label(
    main, text="New User ? Sign Up", font=("Helvetica", "11"), bg="black", fg="white"
)
signUpLabel.grid(row=3, column=1)

signUpb = t.Button(main, text="Sign Up", font=("Helvetica", "11"), command=signUp)
signUpb.grid(row=4, column=1, padx=5, pady=5)

main.mainloop()

# cursor.execute("DELETE FROM userInfo WHERE Username = 'b@a.aaa'")
# db.commit()
cursor.execute("SELECT Username,Password,ID FROM userInfo ORDER BY ID ASC")

for x in cursor:
    print(x)

# cursor.execute("ALTER TABLE userInfo AUTO_INCREMENT = 0")
# db.commit()
