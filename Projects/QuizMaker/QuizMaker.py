import json
import time
import random
import tkinter as tk
import random

# TODO Implement Title Screen And Ending

score = 0
answeredQues = -1


def loadData():
    quesAns = {}

    with open("Questions.json") as data:
        for no, dataset in enumerate(json.load(data)["results"], start=1):
            quesAns.update({no: {dataset["question"]: dataset["answer"]}})

    no = random.randint(1, 50)
    ques = quesAns[no]
    quesAns.pop(no)
    for k, v in dict(ques).items():
        return k, v


def check(root, opt, ans):
    global score
    global answeredQues

    if answeredQues <= 4:
        if opt == ans:
            score = score + 1
            root.destroy()
            boolQuiz()

        else:
            root.destroy()
            boolQuiz()
    else:
        root.destroy()


def titleMenu():
    root = tk.Tk()
    bg = tk.PhotoImage(file="Quiz.gif")
    root.geometry("%dx%d+500+200" % (bg.width(), bg.height()))
    root.iconbitmap("Quiz.ico")
    root.title("QuizMaker")
    root.config(bg="black")
    root.resizable(False, False)

    cv = tk.Canvas(width=bg.width(), height=bg.height())
    cv.pack(side="top", fill="both", expand="yes")

    cv.create_image(0, 0, image=bg, anchor="nw")

    root.mainloop()


def boolQuiz():
    global answeredQues

    answeredQues += 1

    root = tk.Tk()
    root.geometry("1400x100+75+300")
    root.iconbitmap("Quiz.ico")
    root.title("BoolQuiz")
    root.config(bg="black")
    root.resizable(False, False)

    topFrame = tk.Frame(root)
    topFrame.pack()

    bottomFrame = tk.Frame(root)
    bottomFrame.pack(side=tk.BOTTOM)

    quesText, ansText = loadData()

    ques = tk.Label(
        topFrame, text=quesText, bg="black", fg="white", font=("Calbri", "18")
    )
    ques.pack()

    true = tk.Button(
        bottomFrame,
        text=u"         \u2714 True         ",
        bg="black",
        fg="white",
        font=("Calbri", "18"),
        command=lambda: check(root, "True", ansText),
    )
    true.pack(side=tk.LEFT)

    false = tk.Button(
        bottomFrame,
        text=u"         \u2718 False        ",
        bg="black",
        fg="white",
        font=("Calbri", "18"),
        command=lambda: check(root, "False", ansText),
    )
    false.pack(fill=tk.BOTH, side=tk.RIGHT)

    root.mainloop()


if __name__ == "__main__":
    titleMenu()
