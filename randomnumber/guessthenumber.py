import random

Guesses = 3

name = ("Hello, what is your name? ")
print(name)

myname =input("")

number = random.randint(1, 20)
print(myname + ", Let's play a game! I'm thinking of a number between 1 - 20. "
               "You have 3 attempts to guess the right number!\n")

while Guesses > 0:
    print("Take a guess! ")
    guess = input()
    guess = int(guess)

    Guesses = Guesses - 1

    if guess > number:
        print("Lower...")
    elif guess < number:
        print("Higher...")
    elif guess == number:
        break

if guess == number:
    Guesses = str(Guesses)
    print("Congratulations " + myname + ", you guessed the correct number with " + Guesses + " guesses left!")

if guess != number:
    number = str(number)
    print("Sorry, but you have used all your chances. The correct number that i was thinking of was " + number + ".")

