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

num_aves = input_entero_positivo("Ingrese el numero de aves avistadas a ingresar: ")
aves = input_enteros_cantidad(f"Ingrese los tipos de las {num_aves} aves avistadas. Tipos: 1 - 5. (Ejemplo: 1 5 4 2 ...): ", num_aves)

cont_tipos = [0] * 5  # En este array (de 5 ceros) vamos contando la frecuencia de cada tipo (el inidce 0 seria la frecuencia del 1)
for b in aves: # Con este for sumo 1 al respectivo indice del tipo de ave ingresada en aves
    cont_tipos[b - 1] += 1 

indx_max = 0
for n in range(len(cont_tipos)):  #Con este for leemos todo el arreglo cont_tipos para saber cual es el que se repitio mas, y si 2 o mas se repiten en la misma cantidad de veces el que se va a mostrar sera el de indice menor
    if cont_tipos[n] > cont_tipos[indx_max]:
        indx_max = n

print(indx_max + 1)