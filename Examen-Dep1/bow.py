from weapon import Weapon

class Bow(Weapon):

    def __init__(self, name="", minDamage=0, maxDamage=0, durability=0):
        self.name = name
        self.minDamage = minDamage
        self.maxDamage = maxDamage
        self.durability = durability
        self.type = "Arco"
        self.style = "Ataque"
        self.description = "Ataque a distancia"
