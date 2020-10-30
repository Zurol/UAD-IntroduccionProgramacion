import tkinter as tk

class Tamagotchi:
    name = ""
    state = 0 #ESTADO DEL TAMAGOTCHI

def startGame():
    print("Iniciando el juego")
    tamagotchi.state = 0
    etiquetaEstado.configure(text=("Estado: {0}".format(estados[tamagotchi.state])))
    actualizarCuadricula(15,10)

def accion(numeroAccion):
    print("Acción {0}".format(numeroAccion))
    tamagotchi.state = maquina[tamagotchi.state][numeroAccion]
    etiquetaEstado.configure(text=("Estado: {0}".format(estados[tamagotchi.state])))
    actualizarCuadricula(15,10)
    #cuadricula = nuevaCuadricula(15, 10, 170, 70)

def actualizarCuadricula(numeroX, numeroY):
    #print(cuadricula)
    for y in range(numeroY):
        for x in range(numeroX):
            if personaje[y][x] != 9:
                    colorTemporal = tamagotchi.state
            else :
                colorTemporal = 9
            cuadricula[y][x].configure(bg=colores[colorTemporal])



def nuevaCuadricula(numeroX, numeroY, posX, posY):

    posX = posX
    posY = posY

    cuadricula = []

    for y in range(numeroY):
        fila = []
        for x in range(numeroX):
            if personaje[y][x] != 9:
                colorTemporal = tamagotchi.state
            else :
                colorTemporal = 9
            temporal = tk.Label(root, text="", width=2, heigh=1, bg=colores[colorTemporal])
            temporal.place(x=(posX + x*25), y=(posY + y*25))
            fila.append(temporal)
        cuadricula.append(fila)


    return cuadricula



heigh = 500
width = 700

colores = ["#ffffff", "#f5b5c8", "#c92d39", "#ef8d22", "#ffdf71", "#5abaa7", "#3aa6dd", "#834187", "#999","#000", ]
estados = ["Recién Nacido", "Cariñoso", "Enojado", "Nervioso", "Asustado", "Feliz", "Tranquilo", "Enfermo", "Triste","Muerto", ]

#[0] - ALIMENTAR
#[1] - ACARICIAR
#[2] - GOLPEAR
#[3] - JUGAR
#[4] - CASTIGAR
#[5] - ASUSTAR
#[6] - PASEAR
#[7] - BAÑAR
#[8] - INYECTAR
#[9] - MATAR

maquina = [
        [5, 1, 4, 5, 8, 4, 5, 5, 7, 9], #[0]RECIEN NACIDO
        [5, 1, 4, 1, 8, 3, 5, 6, 7, 9], #[1]CARIÑOSO
        [7, 6, 7, 3, 7, 7, 6, 6, 7, 9], #[2]ENOJADO
        [2, 6, 2, 6, 4, 4, 6, 6, 7, 9], #[3]NERVIOSO
        [7, 6, 8, 6, 4, 4, 6, 6, 7, 9], #[4]ASUSTADO
        [5, 1, 8, 5, 3, 3, 5, 6, 7, 9], #[5]FELIZ
        [5, 1, 3, 5, 8, 4, 5, 6, 7, 9], #[6]TRANQUILO
        [7, 7, 9, 7, 9, 9, 7, 3, 6, 9], #[7]ENFERMO
        [6, 5, 9, 6, 9, 3, 5, 6, 7, 9], #[8]TRISTE
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9], #[9]MUERTO
    ]

personaje = [
        [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
        [9,9,9,9,0,9,9,9,9,9,0,9,9,9,9],
        [9,9,9,9,9,0,9,9,9,0,9,9,9,9,9],
        [9,9,9,9,0,0,0,0,0,0,0,9,9,9,9],
        [9,9,9,0,0,9,0,0,0,9,0,0,9,9,9],
        [9,9,0,0,0,0,0,0,0,0,0,0,0,9,9],
        [9,9,0,9,0,0,0,0,0,0,0,9,0,9,9],
        [9,0,9,9,0,9,9,9,9,9,0,9,9,0,9],
        [9,9,9,9,0,0,9,9,9,0,0,9,9,9,9],
        [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
        [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    ]


root = tk.Tk()
root.config(width=width, height=heigh, bg='white')

startButton = tk.Button(root, text="Reiniciar el juego",
    command=lambda: startGame())
startButton.place(x=(width/2-45), y=25)

#Nace el tamagochi
print("Nacimiento de tamagochi")
tamagotchi = Tamagotchi()
tamagotchi.name = "Jamón"
tamagotchi.state = 0        #Estado [0] = Recién nacido


cuadricula = nuevaCuadricula(15, 10, 170, 70)

#Botones de acciones

etiquetaEstado = tk.Label(root, text=("Estado: {0}".format(estados[tamagotchi.state])), width=20, heigh=1, bg=colores[tamagotchi.state], fg='#000')
etiquetaEstado.place(x=100, y=50)


accion1 = tk.Button(root, bg='#000', fg='white', height = 2, width = 10, text="ALIMENTAR",
    command=lambda: accion(0))
accion1.place(x=135, y=350)

accion2 = tk.Button(root, bg='#000', fg='white', height = 2, width = 10, text="ACARICIAR",
    command=lambda: accion(1))
accion2.place(x=225, y=350)

accion3 = tk.Button(root, bg='#000', fg='white', height = 2, width = 10, text="GOLPEAR",
    command=lambda: accion(2))
accion3.place(x=315, y=350)

accion4 = tk.Button(root, bg='#000', fg='white', height = 2, width = 10, text="JUGAR",
    command=lambda: accion(3))
accion4.place(x=405, y=350)

accion5 = tk.Button(root, bg='#000', fg='white', height = 2, width = 10, text="CASTIGAR",
    command=lambda: accion(4))
accion5.place(x=495, y=350)

accion6 = tk.Button(root, bg='#000', fg='white', height = 2, width = 10, text="ASUSTAR",
    command=lambda: accion(5))
accion6.place(x=135, y=400)

accion7 = tk.Button(root, bg='#000', fg='white', height = 2, width = 10, text="PASEAR",
    command=lambda: accion(6))
accion7.place(x=225, y=400)

accion8 = tk.Button(root, bg='#000', fg='white', height = 2, width = 10, text="BAÑAR",
    command=lambda: accion(7))
accion8.place(x=315, y=400)

accion9 = tk.Button(root, bg='#000', fg='white', height = 2, width = 10, text="INYECTAR",
    command=lambda: accion(8))
accion9.place(x=405, y=400)

accion10 = tk.Button(root, bg='#000', fg='white', height = 2, width = 10, text="MATAR",
    command=lambda: accion(9))
accion10.place(x=495, y=400)


root.mainloop()
print(tamagotchi.name)
