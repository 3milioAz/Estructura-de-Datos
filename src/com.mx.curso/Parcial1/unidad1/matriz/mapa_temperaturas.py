#----------Crear la matriz que represente un mapa de temperaturas de 3x3 zonas de una ciudad----------
temperaturas = [
    [20.1, 21.3, 21.4],
    [20.4, 19.0, 22.7],
    [24.1, 20.8, 23.3]
]

#----------Imprimir toda la matriz---------
def imprimir_matriz(matriz):
    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            print(matriz[f][c], end=" ")
        print()

print("Matriz original:")
imprimir_matriz(temperaturas)

#--------Acceder a una celda especifica y modificar su valor
celda = [1, 1]
print(f"\nCelda seleccionada {celda}: {temperaturas[celda[0]][celda[1]]} grados C\n")

temperaturas[celda[0]][celda[1]] = 33.3
print("Matriz actualizada:")
imprimir_matriz(temperaturas)