import json
import time
import random
import tkinter as tk
import random

# TODO implement Check


def loadData():
    ques = []
    ans = []

    with open("Questions.json") as data:
        result = json.load(data)["results"]

        for quesAns in result:
            ques.append(quesAns["question"])
            ans.append(quesAns["answer"])

    no = random.randint(0, 49)
    ques.pop(no)
    ans.pop(no)

    return ques[no], ans[no]


def check(opt, ans, ques):
    quesText, ansText = loadData()

    if opt == ans:
        ques.config(text=quesText)

    else:
        ques.config(text=quesText)


def main():
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
        command=lambda: check(True, ansText, ques),
    )
    true.grid(row=2, column=1, padx=10, pady=3)

    false = tk.Button(
        root,
        text=u"\u2718 False",
        bg="black",
        fg="white",
        font=("Calbri", "14"),
        command=lambda: check(False, ansText, ques),
    )
    false.grid(row=2, column=5, padx=3, pady=3)

    root.mainloop()


if __name__ == "__main__":
    main()
