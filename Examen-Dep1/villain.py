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

    def randomMove()