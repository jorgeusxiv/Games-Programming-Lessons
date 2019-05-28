def comprobar_partida_ganada(matriz):

    if matriz[0][0]==matriz[0][1] and matriz[0][1]==matriz[0][2] and not(matriz[0][0] == " "):
        return True
    elif matriz[1][0]==matriz[1][1] and matriz[1][1]==matriz[1][2] and not(matriz[1][0] == " "):
        return True
    elif matriz[2][0]==matriz[2][1] and matriz[2][1]==matriz[2][2] and not(matriz[2][0] == " "):
        return True
    elif matriz[0][0]==matriz[1][0] and matriz[1][0]==matriz[2][0] and not(matriz[0][0] == " "):
        return True
    elif matriz[0][1]==matriz[1][1] and matriz[1][1]==matriz[2][1] and not(matriz[1][0] == " "):
        return True
    elif matriz[0][2]==matriz[1][2] and matriz[1][2]==matriz[2][2] and not(matriz[2][0] == " "):
        erturn True
    elif matriz[0][0]==matriz[1][1] and matriz[1][1]==matriz[2][2] and not(matriz[0][0] == " "):
        return True
    elif matriz[2][0]==matriz[1][1] and matriz[1][1]==matriz[0][2] and not(matriz[2][0] == " "):
        return True

    return False
