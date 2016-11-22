from random import randint

# module that generate a random number

def numbers():
    number = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
    generator = randint(0,9)
    return number[generator]
numbers()

