# Generar la unión e intersección de 2 colecciones.

animalesTerrestres = ["Perro", "Gato", "Tortuga", "Liebre", "Pingüino"]
animalesMarinos    = ["Tortuga", "Ballena", "Calamar", "Pingüino"]




# A Unión B
animales = []

for animalMarino in animalesMarinos :
    for animalTerrestre in animalesTerrestres :
        #print("A: {0} X B: {1} \n".format(animalMarino, animalTerrestre))
        animales.append(animalTerrestre)


        #if len(animales) > 0 :
        #    for animal in animales:
        #        print(animales)
        #        print(">", animal)
        #        #print("Ciclo interno")
        #        if animal != animalMarino :
        #            animales.append(animalMarino)

        #else : 
        #    animales.append(animalMarino)


print(animales)




# A Intersección B
animalesTerrestresMarinos = []

for animalMarino in animalesMarinos :
    for animalTerrestre in animalesTerrestres :
        if animalMarino == animalTerrestre :
            animalesTerrestresMarinos.append(animalMarino)



print(animalesTerrestresMarinos)
