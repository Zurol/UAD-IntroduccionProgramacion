import tkinter as tk

from knight import Knight
from villain import Villain
from sword import Sword
from bow import Bow
from shield import Shield


def startGame():
    #Desplegar imagen
    print("Iniciando el juego")


def makeMove(Seleccion):
    if Seleccion=="Escudo":
        response = hero.defense(Seleccion, villain)

    else :
        response = hero.attack(Seleccion, villain)

    balance = "{0}/{1}".format(hero.life, hero.maxLife)
    firstCharacterContainer.configure(text = balance)
    print(response)



#Iniciar el juego
#Se crea una ventana
#Inicias el juego
#Despliegas las imágenes del caballero y el enemigo
#

heigh = 500
width = 700

root = tk.Tk()
root.config(width=width, height=heigh, bg='white')

startButton = tk.Button(root, text="Iniciar el juego",
    command=lambda: startGame())
startButton.place(x=(width/2-45), y=25)

#espada = Espada()

print("--------------------")
print("Creando Caballero")
hero = Knight("Rhys", 50, 100)
hero.details()
#hero.equipment()

print("--------------------")

print("\nCreando Espada")
heroSword = Sword("Storm Song", 1, 11, 100)

print("Equipando espada ...")
hero.equip(heroSword)


print("\nCreando Arco")
heroBow = Bow("Armatus", 4, 7, 70)
print("Equipando arco ...")
hero.equip(heroBow)


print("\nCreando Escudo")
heroShield = Shield("Aegis", 10, 100)
print("Equipando escudo ...")
hero.equip(heroShield)


print("--------------------")

#ENEMIGO
print("Creando Enemigo")
villain = Villain("Rixton", 45, 100)
villain.details()
#villain.equipment()

print("--------------------")

print("\nCreando Espada")
villainSword = Sword("Dark Sword", 5, 11, 100)

print("Equipando espada ...")
villain.equip(villainSword)


print("\nCreando Arco")
villainBow = Bow("Dark Bow", 2, 9, 70)
print("Equipando arco ...")
villain.equip(villainBow)


print("\nCreando Escudo")
villainShield = Shield("Dark Shield", 10, 100)
print("Equipando escudo ...")
villain.equip(villainShield)


print("--------------------")





#hero.equipment()

#hero.attack("Arco")


################################

playerName = "CABALLERO ( {0} )".format(hero.name.upper())
firstCharacterName = tk.Label(root, text=playerName, width=20, heigh=1, bg='#424251', fg='white')
firstCharacterName.place(x=100, y=70)

firstCharacterContainer = tk.Label(root, text=("{0}/{1}".format(hero.life, hero.maxLife)), width=20, heigh=10, bg='orange')
firstCharacterContainer.place(x=100, y=100)

firstCharacterLife = tk.Label(root, text="", width=20, heigh=1, bg='#424251', fg='white')
firstCharacterLife.place(x=100, y=270)

firstCharacterCurrentLife = tk.Label(root, text="", width=10, heigh=1, bg='#00B22D', fg='white')
firstCharacterCurrentLife.place(x=100, y=270)

fcSwordAttackButton = tk.Button(root, bg='#000', fg='white', height = 2, width = 10, text="ESPADA",
    command=lambda: makeMove("Espada"))
fcSwordAttackButton.place(x=200, y=120)

fcBowAttackButton = tk.Button(root, bg='#000', fg='white', height = 2, width = 10, text="ARCO",
    command=lambda: makeMove("Arco"))
fcBowAttackButton.place(x=200, y=170)

fcShieldAttackButton = tk.Button(root, bg='#000', fg='white', height = 2, width = 10, text="ESCUDO",
    command=lambda: makeMove("Escudo"))
fcShieldAttackButton.place(x=200, y=220)


playerName = "ENEMIGO ( {0} )".format(villain.name.upper())
secondCharacterName = tk.Label(root, text=playerName, width=20, heigh=1, bg='#424251', fg='white')
secondCharacterName.place(x=455, y= 70)

secondCharacterContainer = tk.Label(root, text=("{0}/{1}".format(villain.life, villain.maxLife)), width=20, heigh=10, bg='#FF5C26')
secondCharacterContainer.place(x=455, y=100)

secondCharacterLife = tk.Label(root, text="", width=20, heigh=1, bg='#424251', fg='white')
secondCharacterLife.place(x=455, y=270)

secondCharacterCurrentLife = tk.Label(root, text="", width=10, heigh=1, bg='#00B22D', fg='white')
secondCharacterCurrentLife.place(x=455, y=270)

scSwordAttackButton = tk.Label(root, bg='#000', fg='white', height = 2, width = 10, text="ESPADA")
scSwordAttackButton.place(x=420, y=120)


scBowAttackButton = tk.Label(root, bg='#000', fg='white', height = 2, width = 10, text="ARCO")
scBowAttackButton.place(x=420, y=170)


scShieldAttackButton = tk.Label(root, bg='#000', fg='white', height = 2, width = 10, text="ESCUDO")
scShieldAttackButton.place(x=420, y=220)


root.mainloop()