from tkinter import *

# TODO Font size and settings


def signUp():
    win = Tk()
    win.title("SignUp")
    win.geometry("300x300")
    win.config(bg="black")

    el = Label(win, text="Email : ", bg="black", fg="white")
    el.grid(row="0", column="0")

    email = Entry(win, bg="black", fg="white")
    email.grid(row="0", column="1")

    pl = Label(win, text="Password : ", bg="black", fg="white")
    pl.grid(row="1", column="0")

    pwd = Entry(win, show="*", bg="black", fg="white")
    pwd.grid(row="1", column="1")

    passShow = Button(
        win,
        text="Show",
        command=lambda: pwd.config(show=""),
        bg="black",
        fg="white",
        font=("Helvetica", "4"),
    )
    passShow.grid(row="1", column="2")

    passHide = Button(
        win, text="Hide", command=lambda: pwd.config(show="*"), bg="black", fg="white"
    )
    passHide.grid(row="1", column="3")

    logInb = Button(win, text="Log In")
    logInb.grid(row="2", column="1")

    signUpLabel = Label(
        win, text="New User ?", font=("Helvetica", "15"), bg="black", fg="white"
    )
    signUpLabel.grid(row="3", column="1")

    signUpb = Button(win, text="Sign Up", font=("Helvetica", "9"))
    signUpb.grid(row="4", column="1")

    win.mainloop()


signUp()

