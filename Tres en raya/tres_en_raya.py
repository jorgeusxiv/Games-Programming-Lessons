import numpy as np
# import only system from os
from os import system, name

# import sleep to show output for some time period
from time import sleep

def clear():
    _ = system('clear')

def comprobar_partida_ganada(matriz):

    if matriz[0][0]==matriz[0][1] and matriz[0][1]==matriz[0][2] and not(matriz[0][0] == " "):
        return True
    elif matriz[1][0]==matriz[1][1] and matriz[1][1]==matriz[1][2] and not(matriz[1][0] == " "):
        return True
    elif matriz[2][0]==matriz[2][1] and matriz[2][1]==matriz[2][2] and not(matriz[2][0] == " "):
        return True
    elif matriz[0][0]==matriz[1][0] and matriz[1][0]==matriz[2][0] and not(matriz[0][0] == " "):
        return True
    elif matriz[0][1]==matriz[1][1] and matriz[1][1]==matriz[2][1] and not(matriz[0][1] == " "):
        return True
    elif matriz[0][2]==matriz[1][2] and matriz[1][2]==matriz[2][2] and not(matriz[0][2] == " "):
        return True
    elif matriz[0][0]==matriz[1][1] and matriz[1][1]==matriz[2][2] and not(matriz[0][0] == " "):
        return True
    elif matriz[2][0]==matriz[1][1] and matriz[1][1]==matriz[0][2] and not(matriz[2][0] == " "):
        return True

    return False

def print_tablero(matriz):
    print("   1    2    3  ")
    print("")
    for i in range(0,3):
        fila = ""
        fila = fila + str(i+1) + "   " + matriz[i][0] + " | " + matriz[i][1] + " | " + matriz[i][2]
        print(fila)
        if(i<2):
            print("   -----------")
    print("")
    return True

def main():

    #FLAGS

    tablero = [[" "," "," "],[" "," "," "],[" "," "," "]]
    turno_jugador = 0
    error = 0
    errorMismaPosicion = 0
    contador = 0
    empate = 0

    while(1):
        clear()
        print_tablero(tablero)
        posicion = input("En que casilla quiere poner la ficha? \nPara ello debe indicar la fila y la columna separadas por un espacio: ")

        if (len(posicion) != 3 or posicion[1] != " "):
            error=1
            break
        try:
            fila = int(posicion[0]) - 1
            columna = int(posicion[2]) - 1
        except(ValueError):
            error=1
            break

        if(fila > 2 or fila < 0 or columna > 2 or columna < 0):
            error=1
            break

        if tablero[fila][columna] != " ":
            errorMismaPosicion=1
            break

        if turno_jugador == 0:
            tablero[fila][columna] = "O"
        else:
            tablero[fila][columna] = "X"

        if comprobar_partida_ganada(tablero):
            break

        if turno_jugador == 0:
            turno_jugador = 1
        else:
            turno_jugador = 0

        contador = contador + 1

        if contador == 9:
            empate = 1
            break

    if error == 1:
        clear()
        print("Error con el formato de la fila y la columna")
        print("Vuelva a intentarlo más tarde")
    elif empate == 1:
        clear()
        print_tablero(tablero)
        print("Ha habido un empate!")
    elif errorMismaPosicion == 1:
        clear()
        print("No puedes poner fichas en sitios ocupados!")
    else:
        clear()
        print_tablero(tablero)
        ganador = "Enhorabuena el jugador " + str(turno_jugador) + " ha ganado la partida"
        print(ganador)


if __name__ == "__main__":
    main()
