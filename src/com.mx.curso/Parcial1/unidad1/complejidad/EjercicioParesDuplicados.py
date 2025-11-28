import time

def tiene_duplicados_lineal(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)): # Lo que esta antes de la coma en el range es de donde va a comenzar
            if arr[i] == arr[j]:
                return True
    return False

# Pruebas con diferentes tamaños de arreglos
sizes = [100, 1000, 10000]        

for n in sizes:
    arr = list(range(n)) # Arreglo sin duplicados para forzar el peor caso

    starTime = time.time()
    tiene_duplicados_lineal(arr)
    endTime = time.time()

    print(f"Busqueda de duplicados en un arreglo de {n} elementos: {endTime - starTime:.6f} segundos")