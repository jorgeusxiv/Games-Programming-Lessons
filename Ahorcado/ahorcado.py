import posiciones as P

pantalla = P.posiciones()

palabra = input("Elige una palabra: ")
palabras = palabra.split(" ")
check = 0
lista_letras_leidas = set()
lista_letras_palabra = set()


for item in palabras:
    if item.isalpha():
        for j in range(len(item)):
            lista_letras_palabra.add(item[j])
    else:
        check = 1

if check == 1:
    print("La palabra o frase deben tener el formato adecuado ")
else:

    i = 0
    pantalla.clear()

    while(i < 6):

        pantalla.manejador(i)
        print("\n")
        pantalla.imprimir_palabra(palabra, lista_letras_leidas)
        print("")
        pantalla.guiones(palabra)
        print("\n")

        letra = input("Elige una letra: ")

        #Primero comprobamos que sea una letra

        if not (letra.isalpha() and len(letra)==1):
            continue

        else:
            if((letra in lista_letras_leidas) or (letra not in lista_letras_palabra)):
                i = i + 1
                pantalla.clear()
                print("ERROR!")
                print("Las letras leidas son:")
                print(lista_letras_leidas)
                print("\n")
                continue
            else:
                lista_letras_leidas.add(letra)
                pantalla.clear()
                print("CORRECTO!")
                print("Las letras leidas son:")
                print(lista_letras_leidas)
                print("\n")

        #comprobamos si hemos ganado el juego
        if (lista_letras_palabra == lista_letras_leidas):
            break

    pantalla.clear()
    pantalla.manejador(i)
    print("\n")
    pantalla.imprimir_palabra(palabra, lista_letras_leidas)
    print("")
    pantalla.guiones(palabra)
    print("\n")



    if(i < 6):
        print("ENHORABUENA HAS GANADO")
    else:
        print("LO SIENTO, HAS PERDIDO")
        print("La palabra era " + palabra.upper())
