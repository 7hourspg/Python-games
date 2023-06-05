# GUESS     THE     NUMBER

import random

randomNumber = random.randint(1, 5)

getMsg = input("Do you want to play type Y for yes or N: ")

guessTimes = 1


if getMsg == "n":
    print("we are leaving")
    quit()
else:

    while True:
        guess = int(input("Guess the number (between 1 and 5): "))
        if randomNumber == guess:
            print("Congratulations! You guessed the correct number.",
                  "In", guessTimes, "Times")
            break

        elif guess < randomNumber:
            print("Low! Try guessing a higher number.")
            guessTimes += 1
        else:
            print("High! Try guessing a lower number.")
            guessTimes += 1
