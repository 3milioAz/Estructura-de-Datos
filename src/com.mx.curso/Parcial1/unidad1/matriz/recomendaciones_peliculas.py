# Matriz de recomendacion de peliculas

matriz = [
    [5,	5,	4,	5,	5,	1,	5,	5,	3,	5,	3,	4,	4],
    [2,	5,	4,	5,	5,	3,	5,	4,	5,	5,	3,	5,	3],
    [2,	5,	5,	5,	4,	3,	5,	4,	4,	5,	2,	4,	3],
    [4,	5,	4,	5,	5,	4,	4,	5,	5,	5,	3,	4,	2],
    [5,	4,	4,	5,	5,	4,	5,	5,	3,	5,	1,	5,	1],
    [3,	5,	3,	5,	3,	5,	2,	1,	3,	5,	3,	1,	1],
    [2,	4,	5,	3,	5,	2,	5,	3,	3,	4,	1,	3,	2],
    [4,	5,	5,	2,	5,	1,	3,	5,	5,	4,	3,	1,	3],
    [3,	2,	5,	2,	5,	2,	3,	2,	5,	4,	5,	4,	2],
    [3,	5,	2,	5,	3,	1,	1,	5,	1,	5,	3,	1,	5],
    [5,	1,	5,	5,	5,	4,	4,	1,	4,	5,	4,	1,	5],
    [5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5],
    [5,	4,	3,	5,	5,	1,	4,	2,	3,	5,	2,	1,	5]
]

# Imprimir la matriz de calificaciones

for f in range(len(matriz)):
    for c in range(len(matriz[f])):
        print(matriz[f][c], end="")
    print()

# Promedio de una pelicula
suma = 0
pelicula = 10
for f in range(len(matriz)):
    suma += matriz[f][pelicula]

print("La suma de calificaciones de la pelicula 1 es:", suma)
promedio = suma / len(matriz)
print("El promedio de calificaciones de la pelicula 1 es:", promedio)

calificaciones_usuario = matriz[0]
print("Calificaciones del usuario 0:", calificaciones_usuario)