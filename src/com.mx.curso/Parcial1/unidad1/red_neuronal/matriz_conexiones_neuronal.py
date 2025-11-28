#Operación de producto punto (base de las redes neuronales)
 
import numpy as np

# Crear una matriz 3x2 para representar las conexiones entre neuronas

matriz = np.array([
    [1,2],
    [3,4],
    [5,6]
])

# Inicializar un vector de entrada y realizar producto punto

arreglo = np.array([1,2,3])

salida = np.dot(arreglo, matriz)
print(f"Vector de entrada: {arreglo}")
print(f"Matriz de pesos:\n{matriz}")
print(f"Los valores de salida son: {salida}")