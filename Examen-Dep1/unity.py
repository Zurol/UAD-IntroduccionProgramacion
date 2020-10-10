import random

class Unity:
    name = ""
    type = ""
    armor = 0
    life = 0
    maxLife = 0
    sword = []
    bow = []
    shield = []

    def __init__(self, name, type, armor, life):
        self.name = name
        self.type = type
        self.armor = armor
        self.life = life

    def equip(self, weapon):
        weapon.details()
        if weapon.type == 'Espada':
            self.sword = weapon
            print("Espada equipada")

        elif weapon.type == 'Arco':
            self.bow = weapon
            print("Arco equipado")

        elif weapon.type == 'Shield':
            self.shield = weapon
            print("Escudo equipado")


    def attack(self, weapon, target):
        target.randomMove()

        damage = 0
        print("Ataque con {0}".format(weapon))
        if weapon == 'Espada':
            damage = random.randint(self.sword.minDamage, self.sword.maxDamage)

        if weapon == 'Arco':
            damage = random.randint(self.bow.minDamage, self.bow.maxDamage)

        print(damage)



    def defense(self, weapon, target):
        print("Defendiendo con {0}".format(weapon))

    def details(self):
        print("Nombre: {0} | Tipo: {1} | Armadura: {2} | Vida: {3}/{4} ".format(self.name, self.type, self.armor, self.life, self.maxLife))

    def equipment(self):
        #print("Mi espada es: {0} | Daño: {1}-{2} | Mi atributo especial: {3} ".format(espada))
        #print("Mi espada es: {0} ".format(espada))
        print(self.sword)