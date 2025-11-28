edades = [25, 39, 48, 70, 16]

# Agregar uin elemento al final del arreglo
edades.append(50)
print(edades) # Salida: [25, 39, 48, 70, 16, 50]

# Eliminar un elemento por su valor
edades.remove(39) 
print(edades) # Salida: [25, 48, 70, 16, 50]

# Eliminar un elemento por su indice (pop)
edades.pop(2)
print(edades) # Salida: [25, 48, 16, 50]