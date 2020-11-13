
#def <Nombre de la clase iniciando con mayúscula> :
class Jugadores():
    nombre = ""
    turnoActivo = False

    def __init__(self, nombre):
        self.nombre = nombre
    #Listado de atributos del objeto



#def <Nombre de la clase iniciando con mayúscula> :
class Tablero():

    #Listado de atributos del objeto
    casillas = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]
    jugadorEnTurno = ""



    #def <nombre del método>(parámetros) :
    def imprimeTablero(self):
        print(self.casillas)

    def tiradaTipo1(self, posicion):

        if posicion == 0 :
            posicionY = 0
            posicionX = 0
        elif posicion == 1:
            posicionY = 0
            posicionX = 1
        elif posicion == 2:
            posicionY = 0
            posicionX = 2

        #Revisar si la tirada es válida
        #Revisar si está vacia
        self.casillas[posicionY][posicionX] = "X"


    def tiradaTipo2(self, posicionY, posicionX):

        #Revisar si la tirada es válida
        #Revisar si está vacia
        self.casillas[posicionY][posicionX] = "O"


################## PROGRAMA ##################

miTablero = Tablero()
jugadorA = Jugadores("Paco")
jugadorB = Jugadores("Luisa")

print(jugadorA)
print(jugadorB)

victoria = False

while not (victoria==True) :
    if(miTablero.jugadorEnTurno=="A"): #jugador "X"
        print("Es el turno del jugador A")
        tiradaXY = int(input("Selecciona la casilla:"))

        # [0,1,2]
        # [3,4,5]
        # [6,7,8]
        # El jugador elige la posición #5 o #7 (por ejemplo)


        #Revisar si la tirada es válida
        #Revisar si está vacia
        #Asignar la tirada en el lugar
        miTablero.tiradaTipo1(tiradaXY)
        miTablero.imprimeTablero()

        #Evaluar si el jugar ganó
        #Actualizar el turno
        miTablero.jugadorEnTurno="B"

        jugadorA.turnoActivo = False
        jugadorB.turnoActivo = True


    else : #jugador "O"
        print("Es el turno del jugador B")
        tiradaY = int(input("Selecciona la fila:"))
        tiradaX = int(input("Selecciona la columna:"))

        # [0,1,2]
        # [3,4,5] <---- (1,2)
        # [6,7,8]
        # Preguntarle al jugador por la posición en X y Y
        # El jugador respondería a X con 2
        # El jugador respondería a Y con 1

        #Revisar si la tirada es válida
        #Revisar si está vacia
        #Asignar la tirada en el lugar
        miTablero.tiradaTipo2(tiradaY, tiradaX)
        miTablero.imprimeTablero()

        #Evaluar si el jugar ganó
        #Actualizar el turno
        miTablero.jugadorEnTurno="A"

        jugadorB.turnoActivo = False
        jugadorA.turnoActivo = True



miTablero.imprimeTablero()
