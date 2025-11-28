# Limpieza de datos con numpy
import numpy as np
#import random

# Simular una matriz de datos de 10 * 3
#np.random.seed(42)
#datos = np.random.rand(10, 3) * 100
datos = np.array([
    [10.9,9.1,20.1,30.1],
    [5.9,9.1,20.1,3.1],
    [10.9,9.1,20.1,30.1],
    [10.9,9.1,20.1,30.1],
    [10.9,9.1,20.1,30.1],
    [10.9,9.1,20.1,30.1],
    [10.9,9.1,20.1,30.1],
    [7.9,100.1,20.1,30.1],
    [10.9,9.1,20.1,30.1],
    [10.9,9.1,20.1,30.1]
])
print("----- Datos Originales -----")
print(datos)

# Simular datos erroneos
datos[6] = [99.99, 99.99, 99.99, 99.99]

datos[1,1] = np.nan
datos[5,2] = np.nan
datos[9,3] = np.nan

print("----- Datos con Errores -----\n", datos)

# Simulación de una fila completa erronea
#datos[2] = [random.uniform(-100, 0) for _ in range(datos.shape[1])]
#print("Datos originales:\n", datos)

# Eliminar filas con valores nulos

datos_sin_errores = np.delete(datos, 5, axis=0)

print("----- Datos sin Errores -----\n", datos_sin_errores)

media_columna = np.nanmean(datos_sin_errores, axis=0)
print("----- Media de cada Columna  ----->", media_columna)

# Llenar los valores donde se encuentra nan por el promedio de cada columna
for f in range(datos.shape[0]): 
    for c in range(datos.shape[1]):
        if np.isnan(datos[f,c]):    # La funcion isnan evalua si es nan
            datos[f,c] = media_columna[c]   # Toma la media de la columna y la agrega en la posición del nan

print("----- Datos con nan Remplazados -----\n", datos)



#indices_erroneos = [0, 2]

#indices_erroneos = []
#for f in range(datos.shape[0]):
#    for c in range(datos.shape[1]):
#        if datos[f,c] < 0 or datos[f,c] > 100:
#            indices_erroneos.append(f)
#
#datos_limpios = np.delete(datos, indices_erroneos, axis=0)
#print("Datos limpios:\n", datos_limpios)