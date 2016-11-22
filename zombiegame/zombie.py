from random import randint

def zombieattack():
    zombies = ("One lonely Zombie", "Three running Zombies", "A group of hungry Zombies")
    meetzombie = randint(0, 2)
    return zombies[meetzombie]