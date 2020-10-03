class Animal:
    def __init__(self, name, age, type):
        self.Name = name
        self.Age = age
        self.Type = type

    def getName(self):
        return self.Name

    def setName(self, name):
        self.Name = name

class Bird(Animal):
    def __init__(self, Name="", Age=""):
        self.Name = Name
        self.Age = Age
        self.Type = "Bird"

    def fly(self, distance):
        if distance>=10:
            distance = 10

        for x in range(distance):
            print("Fly!")


class Fish(Animal):
    def __init__(self, Name="", Age=""):
        self.Name = Name
        self.Age = Age
        self.Type = "Fish"

    def swim(self, distance):
        if distance>=10:
            distance = 10

        for x in range(distance):
            print("Swim!")


Gallina = Bird("Camila", 2)
Salmon = Fish("Salomón", 0.5)

print(Gallina.getName())
Gallina.fly(5)

print(Salmon.getName())
Salmon.swim(2)