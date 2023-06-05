

# ROCK    PAPER     SCISSORS

import random

userWins = 0
compWins = 0

getMsg = input("Do you want to play type Y for yes or N: ")

options = ["rock", "paper", "scissors"]


if getMsg == "n":
    print("we are leaving")
    quit()
else:
    while True:
        userInput = input("Type rock/paper/scissors or q to quit: ")
        randomNum = random.randint(0, 2)

        compPick = options[randomNum]

        if userInput == "q":

            print("CONGRATULATION!")
            print("You won", userWins, "times")
            print("Computer won", compWins, "times")

            quit()

        else:
            if userInput not in options:
                continue
            else:
                if userInput == compPick:
                    print("Match Draw")
                    print("OOPs! \n " + "[ you=" +
                          userInput, "comp="+compPick, "]")

                elif userInput == "rock" and compPick == "scissors":
                    print("Yeah! you won\n " + "[ you=" +
                          userInput, "comp="+compPick, "]")
                    userWins = userWins+1

                elif userInput == "paper" and compPick == "rock":
                    print("Yeah! you won\n " + "you=" +
                          userInput, "comp="+compPick)
                    userWins = userWins+1

                elif userInput == "rock" and compPick == "scissors":
                    print("Yeah! you won\n " + "[ you=" +
                          userInput, "comp="+compPick, "]")
                    userWins = userWins+1

                elif userInput == "rock" and compPick == "scissors":
                    print("Yeah! you won\n " + "[ you=" +
                          userInput, "comp="+compPick, "]")
                    userWins += 1

                else:
                    print("[ you="+userInput, "comp="+compPick, "]")
                    print("Oo you lost ,computer wins")
                    compWins += 1
