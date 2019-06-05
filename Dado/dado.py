import numpy as np
# import only system from os
from os import system, name
import random

# import sleep to show output for some time period
from time import sleep


def clear():
    _ = system('clear')

def dado_pos1():
    print(" ______________________________")
    print("|                              |")
    print("|                              |")
    print("|                              |")
    print("|                              |")
    print("|                              |")
    print("|                              |")
    print("|             @@@@             |")
    print("|             @@@@             |")
    print("|                              |")
    print("|                              |")
    print("|                              |")
    print("|                              |")
    print("|                              |")
    print("|______________________________|")

def dado_pos2():
    print(" ______________________________")
    print("|                              |")
    print("|                              |")
    print("|                              |")
    print("|                    @@@@      |")
    print("|                    @@@@      |")
    print("|                              |")
    print("|                              |")
    print("|                              |")
    print("|                              |")
    print("|     @@@@                     |")
    print("|     @@@@                     |")
    print("|                              |")
    print("|                              |")
    print("|______________________________|")

def dado_pos3():
    print(" ______________________________")
    print("|                              |")
    print("|                              |")
    print("|                              |")
    print("|                    @@@@      |")
    print("|                    @@@@      |")
    print("|                              |")
    print("|             @@@@             |")
    print("|             @@@@             |")
    print("|                              |")
    print("|     @@@@                     |")
    print("|     @@@@                     |")
    print("|                              |")
    print("|                              |")
    print("|______________________________|")

def dado_pos4():
    print(" ______________________________")
    print("|                              |")
    print("|                              |")
    print("|                              |")
    print("|     @@@@           @@@@      |")
    print("|     @@@@           @@@@      |")
    print("|                              |")
    print("|                              |")
    print("|                              |")
    print("|                              |")
    print("|     @@@@           @@@@      |")
    print("|     @@@@           @@@@      |")
    print("|                              |")
    print("|                              |")
    print("|______________________________|")

def dado_pos5():
    print(" ______________________________")
    print("|                              |")
    print("|                              |")
    print("|                              |")
    print("|     @@@@           @@@@      |")
    print("|     @@@@           @@@@      |")
    print("|                              |")
    print("|             @@@@             |")
    print("|             @@@@             |")
    print("|                              |")
    print("|     @@@@           @@@@      |")
    print("|     @@@@           @@@@      |")
    print("|                              |")
    print("|                              |")
    print("|______________________________|")

def dado_pos6():
    print(" ______________________________")
    print("|                              |")
    print("|                              |")
    print("|                              |")
    print("|     @@@@    @@@@    @@@@     |")
    print("|     @@@@    @@@@    @@@@     |")
    print("|                              |")
    print("|                              |")
    print("|                              |")
    print("|                              |")
    print("|     @@@@    @@@@    @@@@     |")
    print("|     @@@@    @@@@    @@@@     |")
    print("|                              |")
    print("|                              |")
    print("|______________________________|")

def manejador_dado(num):
    if num == 1:
        dado_pos1()
    elif num == 2:
        dado_pos2()
    elif num == 3:
        dado_pos3()
    elif num == 4:
        dado_pos4()
    elif num == 5:
        dado_pos5()
    elif num == 6:
        dado_pos6()
    else:
        -1

clear()

a = random.randint(1,7)
manejador_dado(a)
