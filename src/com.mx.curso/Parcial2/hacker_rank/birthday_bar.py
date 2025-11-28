def input_entero_positivo(input_text):
    valor = input(input_text)
    while not valor.isdigit():  # se repite hasta que sea un número entero positivo
        print("Error: Ingrese un entero positivo válido.")
        valor = input(input_text)
    return int(valor)

def input_enteros_cantidad(input_text, max_valores):
    while True:
        valores = input(input_text).split()
        try:
            numeros = [int(v) for v in valores]   # convierte a enteros
            if len(numeros) > max_valores:        # valida la cantidad
                print(f"Error: Solo puedes ingresar hasta {max_valores} valores.")
                continue
            else:
                 return numeros
        except ValueError:
            print("Error: Ingrese solo enteros válidos (positivos o negativos).")


# --------------- Generar la funcion que hace el calculo -----------------------

tam_arreglo = input_entero_positivo("Ingrese tamano del arreglo: ")
val_arreglo = input_enteros_cantidad(f"Ingrese los {tam_arreglo} valores del arreglo: ", tam_arreglo)
day_month = input_enteros_cantidad("Ingrese los valores de d y m: ", 2)

segmentos = 0
for i in range(0, tam_arreglo): # Aqui crea un for el cual marca desde que indice empezaremos a sumar y hacer los segmentos
    sumatoria = 0 # Guarda la suma total del segmento
    if (i + day_month[1]) <= tam_arreglo: # Evalua si el indice hasta el que vamos a sumar esta dentro del array
        for j in range(i, (i + day_month[1])): # Suma los valores del array que esten en el rango que se pidio en el input
            sumatoria += val_arreglo[j]
    if sumatoria == day_month[0]: # Evalua si la sumatoria del segmento creado es igual a el valor que buscamos que forme
        segmentos += 1

print(segmentos)