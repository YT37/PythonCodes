from tkinter import *

# TODO connect datatbase


def signUp():
    pass


win = Tk()
win.title("SignUp")
win.geometry("320x200")
win.config(bg="black")

el = Label(win, text="Email : ", bg="black", fg="white", font=("Helvetica", "11"))
el.grid(row=0, column=0, padx=5, pady=5)

email = Entry(win, bg="black", fg="white", font=("Helvetica", "9"))
email.grid(row=0, column=1, padx=5, pady=5)

pl = Label(win, text="Password : ", bg="black", fg="white", font=("Helvetica", "11"))
pl.grid(row=1, column=0, padx=5, pady=5)

pwd = Entry(win, show="*", bg="black", fg="white", font=("Helvetica", "9"))
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

logInb = Button(win, text="Log In", font=("Helvetica", "11"), command=logIn)
logInb.grid(row=2, column=1, padx=5, pady=5)

signUpLabel = Label(
    win, text="New User ? Sign Up", font=("Helvetica", "11"), bg="black", fg="white"
)
signUpLabel.grid(row=3, column=1)

signUpb = Button(win, text="Sign Up", font=("Helvetica", "11"), command=signUp)
signUpb.grid(row=4, column=1, padx=5, pady=5)

win.mainloop()
