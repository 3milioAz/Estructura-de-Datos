# Crear el tablero (matriz 5x5)
tablero = [     # 0 = Nada, 1 = Obstaculo
    [0,1,0,1,0],
    [0,1,1,0,0],
    [0,0,1,1,0],
    [0,0,1,1,1],
    [0,1,0,0,0]
]

# Mostrar el tablero en forma de matriz.
for f in range(len(tablero)):
    for c in range(len(tablero[f])):
        print(tablero[f][c], end="")
    print()

# Contar cuántos obstáculos hay en total.
obstaculos = 0
for f in range(len(tablero)):
    for c in range(len(tablero[f])):
        if tablero[f][c] == 1:
            obstaculos += 1
print(f"Hay {obstaculos} obstaculos en total en el tablero.")

# Contar cuántos obstaculos hay en una fila específica elegida por el usuario.

obstaculos = 0
fila = 3
for c in range(len(tablero[fila - 1])):
    if tablero[fila - 1][c] == 1:
        obstaculos += 1
print(f"Hay {obstaculos} obstaculos en total en la fila {fila}.")