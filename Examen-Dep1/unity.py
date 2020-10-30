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
    moveIndex = 0

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

        elif weapon.type == 'Escudo':
            self.shield = weapon
            print("Escudo equipado")


    def attack(self, weapon, target):

        damage = 0
        print("Ataque con {0}".format(weapon))
        if weapon == 'Espada':
            damage = random.randint(self.sword.minDamage, self.sword.maxDamage)
            self.moveIndex = 0

        if weapon == 'Arco':
            damage = random.randint(self.bow.minDamage, self.bow.maxDamage)
            self.moveIndex = 1

        print(damage)

        moveIndex = target.randomMove(self)

        if not (moveIndex == 2) :
            target.life -= damage

        else :
            self.moveIndex = 2
            if target.shield.durability > 0:
                print("El daño fue bloqueado")
                target.shield.durability -= 1
            else :
                print("No fue posible bloquear del daño")
                target.life -= damage


        return moveIndex




    def defense(self, weapon, target):
        print("Defendiendo con {0}".format(weapon))

        moveIndex = target.randomMove(self)
        print("[MoveIndex]>>>={0}".format(moveIndex))
        self.moveIndex = 2

        if self.shield.durability > 0 :
            print("El daño fue bloqueado")
            self.shield.durability -= 1

        else :
            print("Fue imposible bloquear el daño")
        print("[MoveIndex]={0}".format(moveIndex))
        print("[MoveIndex]={0}".format(target.moveIndex))
        return moveIndex

    def details(self):
        print("Nombre: {0} | Tipo: {1} | Armadura: {2} | Vida: {3}/{4} ".format(self.name, self.type, self.armor, self.life, self.maxLife))

    def equipment(self):
        #print("Mi espada es: {0} | Daño: {1}-{2} | Mi atributo especial: {3} ".format(espada))
        #print("Mi espada es: {0} ".format(espada))
        print(self.sword)