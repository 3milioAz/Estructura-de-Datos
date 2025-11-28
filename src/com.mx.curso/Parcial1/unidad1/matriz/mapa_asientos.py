# Crear una matriz que represente el mapa de asientos

matriz = [  # 0: Asiento vacio, 1: Asiento ocupado
    [1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 0, 0],
]

# Imprimir el mapa de asientos

def imprimir_matriz(matriz):
    print("Sala 4: Superman\n  1 2 3 4 5")
    for f in range(len(matriz)):
        print(f"{f + 1}", end="")
        for c in range(len(matriz[f])):
            if matriz[f][c] == 0:
                print(" O", end="")
            else:
                print(" X", end="")
        print()
    print("O: Disponible | X: Ocupado")

imprimir_matriz(matriz)

# Pedir al usuario la fila y su asiento escogido

fila = 2
asiento = 2

# Marcar el asiento como ocupado

matriz[2-1][2-1] = 1

# Contar y mostrar el numero de asientos disponibles

asientos_dispo = 0
for f in range(len(matriz)):
    for c in range(len(matriz[f])):
        if matriz[f][c] == 0:
            asientos_dispo += 1
print(f"\nEl numero de asientos disponibles es: {asientos_dispo}\n")

imprimir_matriz(matriz)