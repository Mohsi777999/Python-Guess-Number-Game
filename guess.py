import random

randNum = random.randint(1, 100)

while True:
    userGuess = input("Guess a number between 1 and 100 or Quit (Q): ")
    if userGuess == "Q":
        print("You Quit The Game")
        print("----Game Over----")
        break
    userGuess = int(userGuess)
    if userGuess == randNum:
        print("Congratulations! You guessed the number correctly.")
        print("----Game Over----")
        break
    elif userGuess > randNum:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")
