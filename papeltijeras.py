#
# Programa básico para un juego de piedra, papel y tijeras.
#
# [0] - Selección del modo de juego "0" o "1".
# [1] - Limpieza de la entrada.
# [2] - Entrada del primer jugador.
# [3] - Entrada del segundo jugador o computadora según sea el caso.
# [4] - Comparación entre ambas opciones.
# [5] - Impresión del resultado.
#

import getpass, random, os

modo = input("Selecciona el modo de juego:\n[0]Jugador vs Jugador\n[1]Jugador vs Máquina\n")

modo = modo.replace(" ","")
modo = modo.replace("[","")
modo = modo.replace("]","")
modo = int(modo)

tiradas = ["Piedra", "Papel", "Tijeras"]

if modo == 0:

    primerOpcionValida = False

    while primerOpcionValida == False:
        #os.system('cls')
        print("Has elegido el modo de Jugador vs Jugador\n\n\t\tPRIMER JUGADOR")
        primerPersonaje = getpass.getpass(prompt="Selecciona tu tirada:\n[0]Piedra\n[1]Papel\n[2]Tijeras\n?")
        primerPersonaje = primerPersonaje.replace(" ", "")
        primerPersonaje = primerPersonaje.lower()

        if primerPersonaje == "0" or primerPersonaje == "1" or primerPersonaje == "2" :
            primerOpcionValida = True
            primerPersonaje = int(primerPersonaje)

    segundaOpcionValida = False

    while segundaOpcionValida == False:
        #os.system('cls')
        print("\n\n\t\tSEGUNDO JUGADOR")
        segundoPersonaje = getpass.getpass(prompt="Selecciona tu tirada:\n[0]Piedra\n[1]Papel\n[2]Tijeras\n?")
        segundoPersonaje = segundoPersonaje.replace(" ", "")
        segundoPersonaje = segundoPersonaje.lower()

        if segundoPersonaje == "0" or segundoPersonaje == "1" or segundoPersonaje == "2" :
            segundaOpcionValida = True
            segundoPersonaje = int(segundoPersonaje)

    print("J1: {0}  |  J2: {1}".format(tiradas[primerPersonaje], tiradas[segundoPersonaje]))

    if primerPersonaje == segundoPersonaje :
        print("Empate\n")

    elif primerPersonaje == 0 and segundoPersonaje == 2 or primerPersonaje == 1 and segundoPersonaje == 0 or primerPersonaje == 2 and segundoPersonaje == 1 :
        print("Victoria del primer jugador\n")
    else :
        print("Victoria del segundo jugador\n")


elif modo == 1:
    #os.system('cls')
    print("Has elegido el modo de Jugador vs Máquina\n")

    primerOpcionValida = False

    while primerOpcionValida == False:
        #os.system('cls')
        print("Has elegido el modo de Jugador vs Jugador\n\n\t\tPRIMER JUGADOR")
        primerPersonaje = getpass.getpass(prompt="Selecciona tu tirada:\n[0]Piedra\n[1]Papel\n[2]Tijeras\n?")
        primerPersonaje = primerPersonaje.replace(" ", "")
        primerPersonaje = primerPersonaje.lower()

        if primerPersonaje == "0" or primerPersonaje == "1" or primerPersonaje == "2" :
            primerOpcionValida = True
            primerPersonaje = int(primerPersonaje)

    segundoPersonaje = random.randint(0, 2)

    print("J1: {0}  |  J2: {1}".format(tiradas[primerPersonaje], tiradas[segundoPersonaje]))

    if primerPersonaje == segundoPersonaje :
        print("Empate\n")

    elif primerPersonaje == 0 and segundoPersonaje == 2 or primerPersonaje == 1 and segundoPersonaje == 0 or primerPersonaje == 2 and segundoPersonaje == 1 :
        print("Victoria del primer jugador\n")
    else :
        print("Victoria del segundo jugador\n")


else :
    print("\nHas elegido un modo no válido.\n")
