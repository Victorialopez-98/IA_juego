import random
# libreria para limpiar
import os
palabras = ["ORQUIDEA","DROMEDARIO","TECNOLOGIA","PARTITURA","ARCHIPIELAGO"]
# se obtiene una palabra aleatoria para jugar
palabra = random.choice(palabras)
fallo0 = '''
        !===|
            |
            |
            |
      ==========
'''
fallo1 = '''
        !===|
        O   |
            |
            |
      ==========
'''
fallo2 = '''
        !===|
       _O   |
            |
            |
      ==========
'''
fallo3 = '''
        !===|
       _O_  |
            |
            |
      ==========
'''
fallo4 = '''
        !===|
       _O_  |
        |   |
            |
      ==========
'''
fallo5 = '''
        !===|
       _O_  |
        |   |
       /    |
      ==========
'''
fallo6 = '''
        !===|
       _O_  |
        |   |
       / \  |
      ==========
'''
# definicion de variables
palabras_correctas = ""
palabras_seleccionadas = ""
fallos = 0
while True:
#     se limpia la pantalla
    os.system("cls")
    
    print("************************************************************************")
    print("********************** J U E G O  D E  A H O R C A D O *****************")
    print("************************************************************************")
    
# se imprimen los dibjos
    if fallos == 0:
        print (fallo0)
    elif fallos == 1:
        print (fallo1)
    elif fallos == 2:
        print (fallo2)
    elif fallos == 3:
        print (fallo3)
    elif fallos == 4:
        print (fallo4)
    elif fallos == 5:
        print (fallo5)
    elif fallos == 6:
        print (fallo6)
        
    print()


# resultado que se obtiene en cada iteracción
# se muestran las letras acertadas y las no acertadas como *
    resultado=""
    
    for letra in palabra :
        if letra in palabras_correctas:
            resultado += letra
        else:
            resultado += " _ "

    print("      {}".format(resultado))

    print()
    print()

    # se comprueba si gano o no

    if resultado == palabra:
        print("******** H A S  G A N A D O !!! (: ********")
        break

    if fallos > 5:
        print("la palabra era: ", palabra)
        print("******** H A S  P E R D I D O !!! ): ********")
        break

    while True:
    # letra que ingresa el usuario
        letra_sin_formato = input("Ingresa una letra: ")
        letra_usuario = letra_sin_formato.upper()
        if len(letra_usuario) < 1 or len(letra_usuario) > 1:
            print("Introduce una letra")
        elif letra_usuario in palabras_seleccionadas:
            print("Esa letra ya la has ingresado!")
        elif not letra_usuario.isalpha():
            print("Introduce una letra!")
        else:
            palabras_seleccionadas += letra_usuario
            break

    # comprobacion si la letra ya se ha ingresado
    if letra_usuario not in palabra:
        fallos +=1 
    else:
        palabras_correctas += letra_usuario
