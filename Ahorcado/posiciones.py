# import only system from os
from os import system, name

# import sleep to show output for some time period
from time import sleep


class posiciones:

    def __init__(self):
        return

    # define our clear function
    def clear(self):
        _ = system('clear')

    def pos_inicial(self):
        print("   ---------------     ")
        print("   |             |     ")
        print("   |                   ")
        print("   |                   ")
        print("   |                   ")
        print("   |                   ")
        print("   |                   ")
        print("   |                   ")
        print("-------                ")

        return

    def pos_1(self):
        print("   ---------------     ")
        print("   |             |     ")
        print("   |             0     ")
        print("   |                   ")
        print("   |                   ")
        print("   |                   ")
        print("   |                   ")
        print("   |                   ")
        print("-------                ")


        return

    def pos_2(self):
        print("   ---------------     ")
        print("   |             |     ")
        print("   |             0     ")
        print("   |             |     ")
        print("   |                   ")
        print("   |                   ")
        print("   |                   ")
        print("   |                   ")
        print("-------                ")


        return

    def pos_3(self):
        print("   ---------------     ")
        print("   |             |     ")
        print("   |             0     ")
        print("   |             |     ")
        print("   |            /      ")
        print("   |                   ")
        print("   |                   ")
        print("   |                   ")
        print("-------                ")

        return

    def pos_4(self):
        print("   ---------------     ")
        print("   |             |     ")
        print("   |             0     ")
        print("   |             |     ")
        print("   |            / \    ")
        print("   |                   ")
        print("   |                   ")
        print("   |                   ")
        print("-------                ")

        return

    def pos_5(self):
        print("   ---------------     ")
        print("   |             |     ")
        print("   |             0 /   ")
        print("   |             |     ")
        print("   |            / \    ")
        print("   |                   ")
        print("   |                   ")
        print("   |                   ")
        print("-------                ")

        return

    def pos_final(self):
        print("   ---------------     ")
        print("   |             |     ")
        print("   |           \ 0 /   ")
        print("   |             |     ")
        print("   |            / \    ")
        print("   |                   ")
        print("   |                   ")
        print("   |                   ")
        print("-------                ")


        return

    def manejador(self, i):

        if(i == 0):
            self.pos_inicial()
        elif(i == 1):
            self.pos_1()
        elif(i == 2):
            self.pos_2()
        elif(i == 3):
            self.pos_3()
        elif(i == 4):
            self.pos_4()
        elif(i == 5):
            self.pos_5()
        else:
            self.pos_final()

    def guiones(self, palabra):

        palabras = palabra.split(" ")
        
        for item in palabras:
            longitud = len(item)
            print("_"*longitud, end='')
            print(" ", end='')

        return

    def imprimir_palabra(self, palabra, letras):
        for i in range(len(palabra)):
            if(palabra[i] in letras):
                print(palabra[i].upper(), end='')
            else:
                print(" ", end='')

        return
