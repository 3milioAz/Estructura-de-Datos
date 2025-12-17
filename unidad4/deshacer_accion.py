pila_cambios = []

for i in range(1, 6):
    pila_cambios.append(f"Cambio {i}")

ultimo = pila_cambios.pop()
print("Deshaciendo:", ultimo)