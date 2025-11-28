# Operaciones de limpieza de matrices
import numpy as np

datos = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print("Datos originales:\n", datos)

datos_limpios = np.delete(datos, 1, axis=0) # Elimina la segunda fila
print("Datos despues de eliminar la segunda fila:\n", datos_limpios)

# Introducir datos erroneos
datos[0] = [10,-2,10]
datos[1] = [20,-2,20]
datos[2] = [30,30,30]
print("Datos con errores introducidos:\n", datos)

# Eliminar filas con valores negativos
valores_negativos = []
for f in range(datos.shape[0]):
    for c in range(datos.shape[1]):
        if datos[f,c] < 0:
            valores_negativos.append((f,c))

datos_limpios = np.delete(datos, valores_negativos, axis=0) # Eliminar datos negativos usando los indices del axis=0 (filas), las cuales fueron la fila: 0 y 1 (contenian valores negativos)
print("Datos limpios despues de eliminar valores negativos:\n", datos_limpios)


