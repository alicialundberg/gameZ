import random

# Attribut för tärningens lägsta och högsta värde
min = 1
max = 6

rolldice = input("Want to roll dices? (Y/N)")

# Loop för att kasta tärning
while rolldice.lower() == "y":
    print("Rolling dices...")
    print("You received following values: ")
    print(random.randint(min, max))
    print(random.randint(min, max))

    rolldice = input("Want to roll dices again? (Y/N)")


