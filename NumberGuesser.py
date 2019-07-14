secretNumber = 7;
while True:
    guessedNumber = int(input("Guess A Number Between 1 & 10 : "))
    if guessedNumber == secretNumber:
        print("You Guessed The Right Number")
        break