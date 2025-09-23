# Operaciones con matrices utilizando numpy

import numpy as np

matriz_A = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matriz_B = [
    [3,4,5],
    [7,8,9],
    [1,2,6]
]

# Suma de matrices
suma = np.add(matriz_A, matriz_B)
print("Suma de matrices:\n", suma)

# Multiplicación de matrices
multiplicacion = np.multiply(matriz_A, matriz_B)
print("Multiplicacion de matrices:\n", multiplicacion)

# Producto punto (elemento a elemento)
vector_E = np.array([1,2,3])
resultado = np.dot(matriz_A, vector_E)
print("Producto punto:\n", resultado)