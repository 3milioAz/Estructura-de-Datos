import time

# Entrenamiento de una red neuronal

entrada = [1,2]

# Matriz Pesos 3x2
pesos = [
    [4,1,5,6],
    [4,1,5,6]
]

salida = [0,0,0,0]



start_time = time.time()
# Realizar el producto punto
for j in range(len(pesos[0])):
    for i in range(len(entrada)):
        salida[j] += entrada[i] * pesos[i][j]

end_time = time.time()

print("Inicio :", start_time)
print("Tiempos:",end_time)
print("Vector de entrada:", entrada)
print("Matriz de pesos:\n", pesos)
print("\nSalida de la capa de neuronas (producto punto):", salida)