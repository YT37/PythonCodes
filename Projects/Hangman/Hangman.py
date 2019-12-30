import random


def getGuess(secret, guessed):
    string = ""

    for key in secret:
        if key in guessed:
            string += key

        else:
            string += " _ "

    return string


def availableAlphas(guessed):
    string = ""
    count = 0

    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for letter in alpha:
        if letter.lower() in guessed:
            count += 1
        else:
            string += letter

    return string


def main(secret):
    chances = 2*len(secret)
    guessed = []

    print("Welcome To Hangman!")
    print(f"The Word Is {len(secret)} Letters Long.")

    while (chances != 0):
        print("_"*50)
        if secret != getGuess(secret, guessed):
            print(f"You have {chances} guesses left.")

            print(f"Available Letters: {availableAlphas(guessed)}")
            try:
                guess = input("Guess A Letter: ").lower()[0]
            except:
                guess = "a"

            if guess in guessed:
                print(
                    f"You've Already Guessed That Letter: {guess.upper()}")

            if guess not in secret:
                print(
                    f"Oops! That Letter Is Not In The Word: {getGuess(secret, guessed)}")
                chances -= 1
            else:
                guessed.append(guess)
                print("Good guess: ", getGuess(
                    secret, guessed))

            guessed.append(guess)
        elif secret == getGuess(secret, guessed):
            print("Congratulations, you won!")
            break
    else:
        print("_"*50)
        print(
            f"Sorry, You Ran Out Of Guesses. The Word Was {secret}.")


if __name__ == "__main__":
    with open("words.txt") as wordFile:
        line = wordFile.readline()
        wordlist = line.split()

    main(random.choice(wordlist).lower())
