A = {1, 3, 5, 7, 9}
B = {3, 6, 9}
C = {2, 4, 6, 8}

print("\nConjunto A: {0}".format(A))
print("Conjunto B: {0}".format(B))
print("Conjunto C: {0}".format(C))

print("-- Operaciones --\n")

# Ejercicio a
resultado = A.union(B)
print("A ∪ B: {0}".format(resultado))

# Ejercicio b
resultado = A.intersection(B)
print("A ∩ B: {0}".format(resultado))

# Ejercicio c
resultado = A.union(C)
print("A ∪ C: {0}".format(resultado))

# Ejercicio d
resultado = A.intersection(C)
print("A ∩ C: {0}".format(resultado))

# Ejercicio e
resultado = A.difference(B)
print("A - B: {0}".format(resultado))

# Ejercicio f
resultado = B.difference(A)
print("B - A: {0}".format(resultado))

# Ejercicio g
resultado = B.union(C)
print("B ∪ C: {0}".format(resultado))

# Ejercicio h
resultado = B.intersection(C)
print("B ∩ C: {0}".format(resultado))
