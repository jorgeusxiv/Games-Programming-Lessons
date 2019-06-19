import tablero
import math
import random
import time

#Variables globales

turno = 1
dado = 0
pos1 = 0
pos2 = 0

while(1):

    tablero.clear()
    if turno > 0:
        print("Turno: Jugador 1")
        print("Posicion: " + str(pos1))
    else:
        print("Turno: Jugador 2")
        print("Posicion: " + str(pos2))


    tablero.imprimir_tablero(pos1,pos2)
    a = input("Presione enter para lanzar los dados: ")
    dado = random.randint(1,6)
    print("Has sacado un " + str(dado) +"!")

    time.sleep(2)

    #Movemos al jugador que corresponde
    if turno > 0:

        pos1 = pos1 + dado

        if pos1 > 64:
            resto = pos1 - 64
            pos1 = 64 - resto

        print("Has caido en la posicion " + str(pos1) + "!")
        time.sleep(2)

        pos_oca = tablero.pos_oca(pos1) #Compruebo si he caido en una oca
        if pos_oca > pos1:
            print("De oca a oca y tiro porque me toca! Avanzas a la casilla " + str(pos_oca) + "!")
            time.sleep(2)
            pos1 = pos_oca
            if turno < 3:
                turno = turno + 2

        if pos1 == 64:
            break

        turno_posada = tablero.pos_posada(pos1,turno) #Ajustamos el turno si has caido en la posada
        print(turno_posada)
        if turno != turno_posada:
            turno = turno_posada
            print("Oh! Has caído en la posada. Estás un turno sin jugar")
            time.sleep(2)

        pos_puente = tablero.pos_puente(pos1) #Comprobamos si he caido en un puente
        if pos_puente > pos1:
            print("De puente a puente y tiro porque me lleva la corriente! Avanzas a la casilla " + str(pos_puente) + "!")
            time.sleep(2)
            pos1 = pos_puente
            if turno < 3:
                turno = turno + 2

        pos_laberinto = tablero.pos_laberinto(pos1) #Comprobamos si he caido en un laberinto
        if pos_laberinto < pos1:
            print("Has caído en el laberinto! Retrocedes a la casilla 30!")
            time.sleep(2)
            pos1 = pos_laberinto

        turno_carcel = tablero.pos_carcel(pos1,turno) #Ajustamos el turno si has caido en la carcel
        if turno != turno_carcel:
            turno = turno_carcel
            print("Oh! Has caído en la cárcel. Estás dos turnos sin jugar")
            time.sleep(2)

        pos_calavera = tablero.pos_calavera(pos1) #Ajustamos la posicion si hemos caido en la calavera
        if pos_calavera < pos1:
            print("Has caído en la calavera! Retrocedes a la casilla 1!")
            time.sleep(2)
            pos1 = pos_calavera

        turno = turno - 2

    else:

        pos2 = pos2 + dado

        if pos2 > 64:
            resto = pos2 - 64
            pos2 = 64 - resto

        print("Has caido en la posicion " + str(pos2) + "!")
        time.sleep(2)

        pos_oca = tablero.pos_oca(pos2) #Compruebo si he caido en una oca
        if pos_oca > pos2:
            print("De oca a oca y tiro porque me toca! Avanzas a la casilla " + str(pos_oca) + "!")
            time.sleep(2)
            pos2 = pos_oca
            if turno > -3:
                turno = turno - 2

        if pos2 == 64:
            break

        turno_posada = tablero.pos_posada(pos2,turno) #Ajustamos el turno si has caido en la posada
        if turno != turno_posada:
            turno = turno_posada
            print("Oh! Has caído en la posada. Estás un turno sin jugar")
            time.sleep(2)

        pos_puente = tablero.pos_puente(pos2) #Comprobamos si he caido en un puente
        if pos_puente > pos2:
            print("De puente a puente y tiro porque me lleva la corriente! Avanzas a la casilla " + str(pos_puente) + "!")
            time.sleep(2)
            pos2 = pos_puente
            if turno > -3:
                turno = turno - 2

        pos_laberinto = tablero.pos_laberinto(pos2) #Comprobamos si he caido en un laberinto
        if pos_laberinto < pos2:
            print("Has caído en el laberinto! Retrocedes a la casilla 30!")
            time.sleep(2)
            pos2 = pos_laberinto

        turno_carcel = tablero.pos_carcel(pos2,turno) #Ajustamos el turno si has caido en la carcel
        if turno != turno_carcel:
            turno = turno_carcel
            print("Oh! Has caído en la cárcel. Estás dos turnos sin jugar")
            time.sleep(2)

        pos_calavera = tablero.pos_calavera(pos2) #Ajustamos la posicion si hemos caido en la calavera
        if pos_calavera < pos2:
            print("Has caído en la calavera! Retrocedes a la casilla 1!")
            time.sleep(2)
            pos2 = pos_calavera

        turno = turno + 2

tablero.clear()
tablero.imprimir_tablero(pos1, pos2)
print("\n")

if turno > 0:
    print("ENHORABUENA JUGADOR 1, HAS GANADO!")
    print("\n")

if turno < 0:
    print("ENHORABUENA JUGADOR 2, HAS GANADO!")
    print("\n")
