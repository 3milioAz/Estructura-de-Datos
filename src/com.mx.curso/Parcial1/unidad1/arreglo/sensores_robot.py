# Crear un arreglo para almacenar las lecturas de los sensores

arreglo = [120, 85, 210, 150]

# Crear una funcion que lea los valores y verifique si cumplen cierta condicion

for i in range(len(arreglo)):
    if arreglo[i] < 100:
        print(f"Lectura del sensor No. {i + 1}: {arreglo[i]} !!! Advertencia: La lectura esta por debajo del umbral crítico (100).")
    else:
        print(f"Lectura del sensor No. {i + 1}: {arreglo[i]}")