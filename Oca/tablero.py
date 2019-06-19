# import only system from os
from os import system, name
import math


ocas = [5,9,14,18,23,27,32,36,41,45,50,54,59]

def clear():
        _ = system('clear')

def rellenar_posicion(fila, pos, pos1, pos2):
    if pos1 == pos and pos2 == pos:
        fila = fila + "  X O"
    elif pos1 == pos:
        fila = fila + "  X  "
    elif pos2 == pos:
        fila = fila + "   O "
    else:
        fila = fila + "     "

    return fila

def imprimir_tablero(pos1, pos2):
    print("----------------------------------------------------------")
    print("| Leyenda:                                               |")
    print("| Ocas: 5, 9, 14, 18, 23, 27, 32, 36, 41, 45, 50, 54, 59 |")
    print("| Puentes: 6, 12 -> Avanzas a la casilla 19              |")
    print("| Posada: 19 -> Estas un turno sin tirar                 |")
    print("| Laberinto: 42 -> Retrocedes a la casilla 30            |")
    print("| Carcel: 56 -> Estas dos turnos sin tirar               |")
    print("| Calavera: 58 -> Retrocedes a la casilla 1              |")
    print("----------------------------------------------------------")
    
    #Fila1
    print(" ________________________________________________")

    #Fila 2
    fila = "|"
    for i in range(22,14,-1):
        fila = rellenar_posicion(fila,i,pos1, pos2)
        fila = fila + " "
    fila = fila + "|"
    print(fila)

    print("|      ____________________________________      |") #Fila 3

    #Fila 4
    fila = "|"

    #Imprimir posicion 23
    fila = rellenar_posicion(fila, 23, pos1, pos2)
    fila = fila + "|"

    for i in range(44,38,-1):
        fila = rellenar_posicion(fila, i, pos1, pos2)
        if i == 39:
            fila = fila + " |"
        else:
            fila = fila + " "

    #Imprimir posicion 14
    fila = rellenar_posicion(fila, 14, pos1, pos2)
    fila = fila + "|"
    print(fila)

    #Fila 5
    print("|     |      ________________________      |     |")

    #Fila 6
    fila = "|"
    #Imprimir posicion 24
    fila = rellenar_posicion(fila, 24, pos1, pos2)
    fila = fila + "|"

    #Imprimir posicion 45
    fila = rellenar_posicion(fila, 45, pos1, pos2)
    fila = fila + "|"

    for i in range(58,54,-1):
        fila = rellenar_posicion(fila, i, pos1, pos2)
        if i == 55:
            fila = fila + " |"
        else:
            fila = fila + " "
    #Imprimir posicion 38
    fila = rellenar_posicion(fila, 38, pos1, pos2)
    fila = fila + "|"

    #Imprimir posicion 13
    fila = rellenar_posicion(fila, 13, pos1, pos2)
    fila = fila + "|"

    print(fila)

    #Fila 7
    print("|     |     |      ____________      |     |     |")
    #Fila 8
    print("|     |     |     |            |     |     |     |")
    #Fila 9

    #Imprimir posicion 25
    fila = "|"
    fila = rellenar_posicion(fila, 25, pos1, pos2)
    fila = fila + "|"

    #Imprimir posicion 46
    fila = rellenar_posicion(fila, 46, pos1, pos2)
    fila = fila + "|"

    #Imprimir posicion 59
    fila = rellenar_posicion(fila, 59, pos1, pos2)
    fila = fila + "|"

    #Imprimir posicion 64
    fila = rellenar_posicion(fila, 64, pos1, pos2)
    fila = fila + "  "

    #Imprimir posicion 63
    fila = rellenar_posicion(fila, 63, pos1, pos2)
    fila = fila + "|"

    #Imprimir posicion 54
    fila = rellenar_posicion(fila, 54, pos1, pos2)
    fila = fila + "|"

    #Imprimir posicion 37
    fila = rellenar_posicion(fila, 37, pos1, pos2)
    fila = fila + "|"

    #Imprimir posicion 12
    fila = rellenar_posicion(fila, 12, pos1, pos2)
    fila = fila + "|"

    print(fila)

    #Fila 10
    print("|     |     |     |_____       |     |     |     |")

    #Fila 11
    fila = "|"
    #Imprimir posicion 26
    fila = rellenar_posicion(fila, 26, pos1, pos2)
    fila = fila + "|"

    #Imprimir posicion 47
    fila = rellenar_posicion(fila, 47, pos1, pos2)
    fila = fila + "|"

    #Imprimir posiciones 60-62
    for i in range(60,63):
        fila = rellenar_posicion(fila, i, pos1, pos2)
        if i == 62:
            fila = fila + " |"
        else:
            fila = fila + " "
    #Imprimir posicion 53
    fila = rellenar_posicion(fila, 53, pos1, pos2)
    fila = fila + "|"

    #Imprimir posicion 36
    fila = rellenar_posicion(fila, 36, pos1, pos2)
    fila = fila + "|"

    #Imprimir posicion 11
    fila = rellenar_posicion(fila, 11, pos1, pos2)
    fila = fila + "|"
    print(fila)

    #Fila 12
    print("|     |     |__________________|     |     |     |")

    #Fila 13
    fila = "|"
    #Imprimir posicion 27
    fila = rellenar_posicion(fila, 27, pos1, pos2)
    fila = fila + "|"

    #Imprimir posiciones 52-48
    for i in range(48,53):
        fila = rellenar_posicion(fila, i, pos1, pos2)
        if i == 52:
            fila = fila + " |"
        else:
            fila = fila + " "

    #Imprimir posicion 35
    fila = rellenar_posicion(fila, 35, pos1, pos2)
    fila = fila + "|"

    #Imprimir posicion 10
    fila = rellenar_posicion(fila, 10, pos1, pos2)
    fila = fila + "|"

    print(fila)

    #Fila 14
    print("|     |______________________________|     |     |")

    #Fila 15

    #Imprimir posiciones 28-34
    fila = "|"
    for i in range(28,35):
        fila = rellenar_posicion(fila, i, pos1, pos2)
        if i == 34:
            fila = fila + " |"
        else:
            fila = fila + " "

    #Imprimir posicion 9
    fila = rellenar_posicion(fila, 9, pos1, pos2)
    fila = fila + "|"

    print(fila)

    #Fila 16
    print("|__________________________________________|     |")

    #Fila 17
    fila = "|"
    for i in range(1,9):
        fila = rellenar_posicion(fila,i,pos1, pos2)
        fila = fila + " "
    fila = fila + "|"
    print(fila)

    #Fila 18
    print("|________________________________________________|")


#Funciones para controlar las casillas en las que has caido


#Función que comprueba si has caido en una oca
def pos_oca(pos):

    if pos in ocas:
        if (pos % 9) == 0:
            pos = pos + 5
        elif pos == 59:
            pos = 64
        else:
            pos = pos + 4

    return pos

#Funcion que comprueba si has caido en un puente
def pos_puente(pos):
    if pos == 6 or pos == 12:
        pos = 19
    return pos

#Funcion que comprueba si has caido en la posada
def pos_posada(pos,turno):
    if pos == 19:
        if turno < 0:
            turno = turno + 4
        else:
            turno = turno - 4
    return turno

#Funcion que comprueba si has caido en la carcel

def pos_carcel(pos, turno):
    if pos == 56:
        if turno < 0:
            turno = turno + 6
        else:
            turno = turno - 6
    return turno

#Funcion que comprueba si has caido en un laberinto
def pos_laberinto(pos):
    if pos == 42:
        pos = 30
    return pos

#Funcion que comprueba si has caido en la calavera
def pos_calavera(pos):
    if pos == 58:
        pos = 1
    return pos
