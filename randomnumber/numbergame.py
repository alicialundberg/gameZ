import random
from randomnumber import numbers

# "Guess the right number" -game.

def playerpick():
    picknumber = str(input("Pick a number between 1 - 10: "))
    print(picknumber)

    luckynumber = numbers()
    print("Following number was generated: \n" + luckynumber)

    if picknumber in luckynumber:
        print("Congratulations!)

    else:
        print("Sorry, but your number was not one of the generated numbers.")
        time.sleep(1)
        play = input("Want to pick a new number? (Y/N)")
        if play == "Y":
            print("Awesome! Let\'s try again.")
            playerpick()
        else:
            print("Game Over.")
            sys.exit()


# Another "Guess the right number" -game
def generator():
    randomnumber = str(input("Pick a number between 1 - 5 "))
    print(randomnumber)

    number = random.choice(['1', '2', '3', '4', '5'])
    print("Following number was generated: \n" + number)

    if randomnumber in number:
        print("Congratulations!")
    else:
        print("Sorry, but your number was not the generated number.")
        time.sleep(1)
        play = input("Try again? (Y/N)")
        if play == "Y":
            generator()
        else:
        print("Game Over.")
            sys.exit()

generator()