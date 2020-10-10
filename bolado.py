import tkinter as tk
import random

# 
# Función que haga un 'bolado'
# Se elige un botón de iniciar
# Se despliegan 2 opciones para elegir
# Se da click a jugar
# Se despliega una imagen y un mensaje
#


#
# return    bool
#
def inciarJuego():
    # Habilitar los botones

    buttonCara.place(x=60, y=80)
    buttonCruz.place(x=160, y=80)
    return True

def limpiarTablero():
    label.configure(text = "", bg='white')
    return True

def tirarMoneda(tirada):
    temp = random.randrange(0, 2)
    print(temp)
    print(tirada)
    
    buttonJugarDeNuevo.place(x=(ancho/2-45), y=245)

    if tirada=="CARA" and temp==0:
        print("VERDADERO")
        label.configure(text = "GANASTE", fg='green')
        #labelDetalle.configure(text = ("Numero de Ganadas: X   Pedidas:"))
        return True
    elif tirada=="CRUZ" and temp==1:
        print("VERDADERO")
        label.configure(text = "GANASTE", fg='green')
        #labelDetalle.configure(text = ("Numero de Ganadas: X   Pedidas:"))
        return True
    else :
        print("FALSO")
        label.configure(text = "PERDISTE", fg='red')
        return False



alto = 300
ancho = 300
anchoInput = 20 #Aprox 100px

root = tk.Tk()
root.config(width=ancho, height=alto, bg='white')



# Botón para realizar el llamado al input
button = tk.Button(root, text="Iniciar el juego",
    command=lambda: inciarJuego())

button.place(x=(ancho/2-45), y=25)




buttonCara = tk.Button(root, bg='blue', fg='white', height = 5, width = 10, text="CARA",
    command=lambda: tirarMoneda("CARA"))
#buttonCara.place(x=60, y=80)

buttonCruz = tk.Button(root, bg='orange', fg='white', height = 5, width = 10,  text="CRUZ",
    command=lambda: tirarMoneda("CRUZ"))
#buttonCruz.place(x=160, y=80)



# Botón para realizar el llamado al input
buttonJugarDeNuevo = tk.Button(root, text="Jugar de nuevo",
    command=lambda: limpiarTablero())

#buttonJugarDeNuevo.place(x=(ancho/2-45), y=245)





# Label para la entra del resultado
label = tk.Label(root, text="", width=anchoInput, bg='white')
label.place(x=(ancho/2-70), y=190)


labelDetalle = tk.Label(root, text="",  width=20, bg='white')
#labelDetalle.place(x=(ancho/2-100), y=225)

root.mainloop()
