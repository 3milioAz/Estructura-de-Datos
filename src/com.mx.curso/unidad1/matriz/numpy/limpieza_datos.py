# Limpieza de datos con numpy
import numpy as np

# Simular una matriz de datos de 5 * 5
np.random.seed(42)
datos = np.random.rand(5, 5) * 100

# Simular datos erroneos
datos[0, 0] = -90
datos[2, 3] = 1000

print("Datos originales:\n", datos)

indices_erroneos = [0, 2]

datos_limpios = np.delete(datos, indices_erroneos, axis=0)
print("Datos limpios:\n", datos_limpios)