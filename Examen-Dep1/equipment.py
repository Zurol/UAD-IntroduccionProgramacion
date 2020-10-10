class Equipment:
    name = ""
    type = ""
    style = ""
    durability = 0
    description = ""

    def __init__(self, name, type, style, durability):
        self.name = name
        self.type = type
        self.style = style
        self.durability = durability

    def details(self):
        print("Nombre: {0} | Tipo: {1} | Style: {2} | Durabilidad: {3} | Descripción: {4}".format(self.name, self.type, self.style, self.durability, self.description))