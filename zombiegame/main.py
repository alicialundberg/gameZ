import random
import sys
import time

from zombiegame.weapon import randomweapon
from zombiegame.zombie import zombieattack


def play():
    startgame = input("Start Game? (y/n) ")

    while startgame != "y" and startgame != "y":
        startgame = input("Invalid choice. Please try with Y or N ")

        # Loop för att starta spelet
    while startgame == "y" not in "n":
        name = input("What's your name? ")
        print("Loading...\n")
        time.sleep(1)
        print("Hello", name + ".", "The Apocalypse is here. If you want to survive,"
                             "you have to enter the spaceship and leave planet Earth.\n")
        time.sleep(1)
        print("Problem is that the spaceship is on the other side of the city...")
        time.sleep(1)
        print("...And there are zombies everywhere!\n")
        time.sleep(1)

        print("Before we start our travel, we will need a weapon for self-protection.")
        time.sleep(1.5)

        def weapons():
            protection = ("Would you like to have some kind of weapon to protect yourself with? (Y/N)")
            print(protection)

            decision = input("")

            if decision == "n":
                saftey = input("Are you sure? Have you ever tried to fight zombies with your bare hands before? (Y/N)")
                if saftey == "n":
                    print("Didn\'t think so. now choose a weapon! \n")
                    time.sleep(1)
                    print("*Grabbing something randomly from the mystery box* \n")
                    time.sleep(2)
                    weapon = randomweapon() # Importerar från modul weapon
                    print("--> You have been given a " + weapon)
                    time.sleep(2)
                else:
                    print("That\'s a risky decision. Good luck my friend.\n")
            elif decision == "y":
                print("You have to be quick, just grab something from that box over there!\n ")
                time.sleep(2)
                print("*Grabbing something randomly from the mystery box* \n")
                time.sleep(2)
                weapon = randomweapon()
                print("--> You have been given a " + weapon)
                time.sleep(2)
            else:
                print("Invalid choice, try again! You can choose between y and n")
                weapons()
        weapons()

        print("\n Loading...\n")
        time.sleep(2)
        print ("Oh my... It was even worse than i thought. \nThe town has totally collapse and the zombies has taken over.")
        time.sleep(2)
        print("\nKeep your eyes and ears open....\n")
        time.sleep(3)


        meetzombies = zombieattack()
        print("Look out, there is " + meetzombies + " over there!")

        def attack():
            fight = ("Do you want to kill " + meetzombies + "? Kill = Y Avoid = N")
            print(fight)

            question = input("")

            if meetzombies == "One lonely Zombie" and question == "y":
                print("Start the zombieslaying!")
                time.sleep(2)
            elif meetzombies == "Three running Zombies" and question == "y":
                print("Just aim for the head and kill those bastards!")
                time.sleep(2)
            elif meetzombies == "A group of hungry Zombies" and question == "y":
                print("The hungry Zombies are reeeeally hungry... There is no escape!")
                time.sleep(2)
                print("Game Over.")
                sys.exit()
            elif question == "n":
                print("Just like a ninja, you avoided " + meetzombies)
                time.sleep(2)
            else:
                print("Invalid choice, try again! You can choose between y and n")
                attack()
        attack()

    # code is under construction, more will be added!
play()
