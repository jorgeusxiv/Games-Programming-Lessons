import numpy as np


matriz = [[" ","X"," "],["1","X"," "],[" ","1"," "]]

def print_matriz(matriz):
    print("   1    2    3  ")
    print("")
    for i in range(0,3):
        fila = ""
        fila = fila + str(i+1) + "   " + matriz[i][0] + " | " + matriz[i][1] + " | " + matriz[i][2]
        print(fila)
        if(i<2):
            print("   -----------")
    return True

print_matriz(matriz)
