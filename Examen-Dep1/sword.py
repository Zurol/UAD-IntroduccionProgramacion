from weapon import Weapon

class Sword(Weapon):

    def __init__(self, name="", minDamage=0, maxDamage=0, durability=0):
        self.name = name
        self.minDamage = minDamage
        self.maxDamage = maxDamage
        self.durability = durability
        self.type = "Espada"
        self.style = "Ataque"
        self.description = "Cuerpo a cuerpo"
