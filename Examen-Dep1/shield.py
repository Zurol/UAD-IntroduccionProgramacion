from equipment import Equipment

class Shield(Equipment):

    def __init__(self, name="", defense="", durability=0):
        self.name = name
        self.durability = durability
        self.type = "Escudo"
        self.style = "Defensa"
        self.description = "Defensa de todas las fuentes"
