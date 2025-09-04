# Generacion de matriz de calificaciones
calificaciones = [ # Cada fila es un usuario y cada columna es una pelicula
    [5,3,4,1],
    [4,4,5,2],
    [5,2,3,2],
    [5,4,4,1]
          ]
def imprimir_matriz(matriz):
    print("Matriz de calificaciones:")
    for f in range(len(matriz)):
        print(matriz[f])

def calif_promedio(matriz, pelicula):
    suma = 0
    for f in range(len(matriz)):
        #for c in range(len(matriz[f])):
        suma += matriz[f][pelicula - 1]
    media = suma / len(matriz)
    print(f"\nLa calificacion promedio de la pelicula No. {pelicula} es de: {media}/5")

def calif_usuario(matriz, usuario):
    print(f"\nCalificaciones del usuario No. {usuario}:")
    print(matriz[usuario - 1])  
        
imprimir_matriz(calificaciones)
calif_promedio(calificaciones, 1)
calif_usuario(calificaciones, 2)