# Mapa de riesgo

# Crear una matriz de 8x8

matriz = [
    [0,1,2,1,2,0,1,1],
    [0,1,2,1,2,0,1,1],
    [0,1,2,1,2,0,1,1],
    [0,1,2,1,2,0,1,1],
    [0,1,2,1,2,0,1,1],
    [0,1,2,1,2,0,1,1],
    [0,1,2,1,2,0,1,1],
    [0,1,2,1,2,0,1,1]
]

for f in range(len(matriz)):
    for c in range(len(matriz[f])):
        print(matriz[f][c], end="")
    print()

area_riesgo = 0     #2
area_precaucion = 0 #1

for f in range(len(matriz)):
    for c in range(len(matriz[f])):
        if matriz[f][c] == 2:
            area_riesgo += 1
        elif matriz[f][c] == 1:
            area_precaucion += 1

print(f"\nArea de Riesgo (2): {area_riesgo}")
print(f"Area de Precaucion (1): {area_precaucion}")

# Analizar la matriz de navegacion
# Cambiar todos los 2 por 1

print("\nActualizacion de matriz de navegacion\n")

for f in range(len(matriz)):
    for c in range(len(matriz[f])):
        if matriz[f][c] == 2:
            matriz[f][c] = 1

area_riesgo_actualizada = 0     #2
area_precaucion_actualizada = 0 #1

for f in range(len(matriz)):
    for c in range(len(matriz[f])):
        print(matriz[f][c], end="")
        if matriz[f][c] == 2:
            area_riesgo_actualizada += 1
        elif matriz[f][c] == 1:
            area_precaucion_actualizada += 1
    print()

print(f"\nArea de Riesgo (2): {area_riesgo_actualizada}")
print(f"Area de Precaucion (1): {area_precaucion_actualizada}")