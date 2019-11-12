import json
import time
import random
import tkinter as tk
import random

# TODO implement Check


def loadData():
    ques = {}
    ans = {}

    pickedQues = []
    pickedAns = []

    with open("Questions.json") as data:
        result = json.load(data)["results"]
        for no, quesAns in enumerate(result):
            ques.update({no: quesAns["question"]})
            ans.update({no: quesAns["answer"]})

    for _ in range(0, 5):
        no = random.randint(0, 49)
        pickedQues.append(ques[no])
        pickedAns.append(ans[no])
        ques.pop(no)
        ans.pop(no)

    return pickedQues, pickedAns


def check(opt, ques):
    if opt:
        print(True)
        ques.config(text="hi")
    else:
        print("False")


def main():
    root = tk.Tk()
    root.iconbitmap("Quiz.ico")
    root.title("Quiz")
    root.config(bg="black")

    ques = tk.Label(root, text="Hi", bg="black", fg="white", font=("Calbri", "21"))
    ques.grid(row=0, column=3, padx=3, pady=3)

    true = tk.Button(
        root,
        text=u"\u2714 True",
        bg="black",
        fg="white",
        font=("Calbri", "14"),
        command=lambda: check(True, ques),
    )
    true.grid(row=2, column=1, padx=10, pady=3)

    false = tk.Button(
        root,
        text=u"\u2718 False",
        bg="black",
        fg="white",
        font=("Calbri", "14"),
        command=lambda: check(False, ques),
    )
    false.grid(row=2, column=5, padx=3, pady=3)

    root.mainloop()


if __name__ == "__main__":
    main()
