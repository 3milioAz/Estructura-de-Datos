# Practica con dataset iris
import numpy as np

# Cargar el dataset
datos = np.genfromtxt('src/com.mx.curso/unidad1/matriz/numpy/practica_numpy_1/iris/iris.data',
                      delimiter=',', dtype='object')

# Visualizar los datos
print("----- Datos -----\n", datos)
# Cargar solo las 4 primeras columnas
datos_numericos = np.genfromtxt('src/com.mx.curso/unidad1/matriz/numpy/practica_numpy_1/iris/iris.data',
                      delimiter=',', usecols=(0,1,2,3))

# Visualizar los datos numericos
print("----- Datos Numericos -----\n", datos_numericos)

# Listado de indices a eliminar
indices_eliminar = [0,1,2,50]

# Eliminar las filas con losindies detectados con error
datos_limpios = np.delete(datos_numericos, indices_eliminar, axis=0)

# Visualizar datos limpios
print("----- Datos Limpios -----\n", datos_limpios)

datos_limpios[0,0] = np.nan
datos_limpios[4,0] = np.nan
datos_limpios[12,1] = np.nan
datos_limpios[10,2] = np.nan
datos_limpios[10,0] = np.nan
datos_limpios[110,1] = np.nan
datos_limpios[10,2] = np.nan
datos_limpios[4,1] = np.nan
datos_limpios[5,0] = np.nan
datos_limpios[145,1] = np.nan

ultima_fila = datos_limpios.shape[0] - 1
print("Ultima fila: ", ultima_fila)

# Matriz con datos faltantes
print("----- Datos Faltantes -----\n", datos_limpios)


media_columna = np.nanmean(datos_limpios, axis=0)
print("----- Media de cada Columna  ----->", media_columna)

for f in range(datos_limpios.shape[0]): 
    for c in range(datos_limpios.shape[1]):
        if np.isnan(datos_limpios[f,c]):    # La funcion isnan evalua si es nan
            datos_limpios[f,c] = media_columna[c]   # Toma la media de la columna y la agrega en la posición del nan

print("----- Matriz con nan Remplazados -----\n", datos_limpios)