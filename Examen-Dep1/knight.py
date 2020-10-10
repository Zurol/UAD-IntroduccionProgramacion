from unity import Unity

class Knight(Unity):
    #velocidad=1.5

    def __init__(self, name="", armor=0, maxLife=0):
        self.name = name
        self.armor = armor
        self.life = maxLife
        self.maxLife = maxLife
        self.type = "Caballero"
