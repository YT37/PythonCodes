import json
import time
import random
import tkinter as tk
import random

# TODO implement Check

score = 0


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


def check(opt, ans):
    global score
    global root

    if score <= 5:
        if opt == ans:
            score = score + 1
            root.destroy()
            main()

        else:
            root.destroy()
            main()


def main():
    global score
    global root

    root = tk.Tk()
    root.iconbitmap("Quiz.ico")
    root.title("Quiz")
    root.config(bg="black")

    quesText, ansText = loadData()

    ques = tk.Label(root, text=quesText, bg="black", fg="white", font=("Calbri", "21"))
    ques.grid(row=0, column=3, padx=3, pady=3)

    true = tk.Button(
        root,
        text=u"\u2714 True",
        bg="black",
        fg="white",
        font=("Calbri", "14"),
        command=lambda: check(True, ansText),
    )
    true.grid(row=2, column=1, padx=10, pady=3)

    false = tk.Button(
        root,
        text=u"\u2718 False",
        bg="black",
        fg="white",
        font=("Calbri", "14"),
        command=lambda: check(False, ansText),
    )
    false.grid(row=2, column=5, padx=3, pady=3)

    root.mainloop()


if __name__ == "__main__":
    main()
