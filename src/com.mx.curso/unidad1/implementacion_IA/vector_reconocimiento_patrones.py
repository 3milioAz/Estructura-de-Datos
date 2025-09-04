# Crear un arreglo unidimensional
flor = [3.5, 1.4, 0.2]

# Normalizar el vector de caracteristicas
suma = 0
for c in flor:
    suma += c

#flor_normalizada = []    
for i in range(len(flor)):
    #flor_normalizada[i] = flor_normalizada[i] / suma
    flor[i] = flor[i] / suma

print(suma)
#print(flor_normalizada)
print(flor)

#import numpy as np
#
#flor = np.array([3.5, 1.4, 0.2])
#
## Normalizar dividiendo entre la suma total
#flor_normalizada = flor / flor.sum()
#
#print(flor_normalizada)