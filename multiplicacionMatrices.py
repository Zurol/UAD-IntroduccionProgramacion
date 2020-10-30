# Función que multiplica dos matrices de una sola dimensión y
# del mismo tamaño.
# int [N]     Matriz #1
# int [N]     Matriz #2
# Return int  Suma del producto de ambas matrices
def multiplicacionMatrizUnidimensional(a, b):
    sumatoria = 0
    for l in range(len(a)):
        sumatoria += a[l] * b[l]

    return sumatoria


# Función que multiplica dos matrices de NxM y MxO dimensiones
# int [N][M]     Matriz #1
# int [M][O]     Matriz #2
# Return int[N][O]  Suma del producto de ambas matrices
def multiplicacionMatrices(a, b):
    c = []
    if len(a[0]) == len(b):
        print("Es posible realizar la multiplicación de matrices...")
        print(("El resultado tendrá las dimensiones de {0}x{1}").format(len(a), len(b[0])))

        for y in range(len(a)):
            temporal = []
            for x in range(len(b[0])):
                resultadoOperacion = 0

                arregloHorizontal = a[y]
                arregloVertical = []

                for filas in range(len(b)):
                    arregloVertical.append(b[filas][x])

                resultadoOperacion = multiplicacionMatrizUnidimensional(arregloHorizontal, arregloVertical)

                temporal.append(resultadoOperacion)
            c.append(temporal)

    return(c)

a = [
    [5,  3, -4, -2],
    [8, -1,  0, -3],
    ]

b = [
    [ 1,  4,  0],
    [-5,  3,  7],
    [ 0, -9,  5],
    [ 5,  1,  4],
    ]

c = multiplicacionMatrices(a, b)
print(c)