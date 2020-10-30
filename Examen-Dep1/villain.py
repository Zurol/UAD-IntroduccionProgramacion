from unity import Unity
import random

class Villain(Unity):
    #velocidad=1.5

    def __init__(self, name="", armor=0, maxLife=0):
        self.name = name
        self.armor = armor
        self.life = maxLife
        self.maxLife = maxLife
        self.type = "Villano"

    def randomMove(self, target):
        moveIndex = random.randint(0, 2)
        print("-----------",moveIndex)
        print("[MoveIndex]>={0}".format(moveIndex))
        damage = 0

        if moveIndex == 0:
            print("Responde con espada")
            self.details()
            self.sword.details()
            damage = random.randint(self.sword.minDamage, self.sword.maxDamage)

        elif moveIndex == 1:
            print("Responde con arco")
            self.details()
            self.bow.details()
            damage = random.randint(self.bow.minDamage, self.bow.maxDamage)

        elif moveIndex == 2:
            print("Responde con escudo")
            self.details()
            self.shield.details()
            damage = 0
            self.shield.durability -= 1
            print("La durabilidad del escudo ha bajado a {0}".format(self.shield.durability))

        print("[Enemigo usando]={0}".format(moveIndex))

        print("[Caballero usando]={0}".format(target.moveIndex))

        #print(damage)
        if not (target.moveIndex == 2) :
            target.life -= damage

        #else:
        #    moveIndex = 2
        #target.moveIndex = moveIndex

        return moveIndex
