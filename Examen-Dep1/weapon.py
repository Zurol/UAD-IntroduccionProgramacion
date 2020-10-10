from equipment import Equipment

class Weapon(Equipment):
    minDamage = 0
    maxDamage = 0

    def __init__(self, name, type, minDamage, maxDamage, durability):
        self.name = name
        self.type = type
        self.minDamage = minDamage
        self.maxDamage = maxDamage
        self.durability = durability

    def details(self):
        print("Nombre: {0} | Tipo: {1} | Estilo: {2} | Daño: {3}-{4} | Durabilidad: {5} | {6}".format(self.name, self.type, self.style, self.minDamage, self.maxDamage, self.durability, self.description))