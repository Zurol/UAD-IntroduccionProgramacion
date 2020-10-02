class Persona:
    nombre = ""
    edad = 0
    puedeComprar = "NO"
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def comprarChatarra(self):

        if self.edad >= 18:
            self.puedeComprar = "SI"
        
        return self.puedeComprar

    def imprimirObjeto(self):
        print("Nombre: {0} - Edad: {1} - ¿Puede comprar?: {2}".format(self.nombre, self.edad, self.comprarChatarra()))




alumno1 = Persona("Alejandro", 13)
alumno2 = Persona("Javier", 18)
alumno3 = Persona("Rosa", 21)


print("Nombre: {0} - Edad: {1} - ¿Puede comprar?: {2}".format(alumno1.nombre, alumno1.edad, alumno1.comprarChatarra()))
print("Nombre: {0} - Edad: {1} - ¿Puede comprar?: {2}".format(alumno2.nombre, alumno2.edad, alumno2.comprarChatarra()))
print("Nombre: {0} - Edad: {1} - ¿Puede comprar?: {2}".format(alumno3.nombre, alumno3.edad, alumno3.comprarChatarra()))

print(" -------------------- ")

alumno1.imprimirObjeto()
alumno2.imprimirObjeto()
alumno3.imprimirObjeto()
