from random import randint

def randomweapon():
    weaponlist = ["Pistol", "Baseball bat", "Machete"]
    selectweapon = randint(0, 2)
    return weaponlist[selectweapon]
