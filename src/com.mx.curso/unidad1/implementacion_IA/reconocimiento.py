# Crear un arreglo unidimensional
flor = [3.5, 1.4, 0.2]

# Normalizar el vector de caracteristicas
suma = 0
for c in flor:
    suma += c

for i in range(len(flor)):
    flor[i] = flor[i] / suma

print(suma)
print(flor)