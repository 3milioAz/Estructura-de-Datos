# Analisis de complejidad de algoritmos

import time

def buscar_elemento(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return True
    return False
    
starTime = time.time()
mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

elemento = 15

encontrado = buscar_elemento(mi_lista, elemento)
endTime = time.time()
if encontrado:
    print(f"El elemento {elemento} fue encontrado en la lista.")
else:
    print(f"El elemento {elemento} no fue encontrado en la lista.")
print(f"Tiempo de ejecucion: {endTime - starTime} segundos.")