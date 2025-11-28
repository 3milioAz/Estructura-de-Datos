#---------Crear la matriz 4x4 que almacene las intensidades de luz medidas por sensores---------
intensidades = [
    [150, 700, 150, 150],
    [150, 650, 500, 150],
    [150, 500, 500, 300],
    [150, 150, 300, 300]
]

#----------Imprimir la matriz completa-----------
def imprimir_matriz(matriz):
    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            print(matriz[f][c], end=" ")
        print()

print("Matriz original:")
imprimir_matriz(intensidades)

#---------Consultar la intensidad de una zona especifica y modificar su valor---------
zona_consultada = [2, 3]
print(f"\nZona a consultar {zona_consultada}: {intensidades[zona_consultada[0]][zona_consultada[1]]} lux\n")

intensidades[zona_consultada[0]][zona_consultada[1]] = 4500
print("Matriz actualizada:")
imprimir_matriz(intensidades)

#---------Calcular el promedio general de iluminación en la cuadrícula-----------
suma_total = 0
for f in intensidades:
    suma_total += sum(f)

promedio = suma_total / (len(intensidades) * len(intensidades[0]))
print("\nPromedio general de iluminación en la cuadricula:", promedio)



