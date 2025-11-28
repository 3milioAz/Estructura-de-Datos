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


def swap(ind_n_izq, ind_n_der, array):
    temp = array[ind_n_izq]
    array[ind_n_izq] = array[ind_n_der]
    array[ind_n_der] = temp

def buble_sort_contado(tam, array):
    num_swaps = 0
    for i in range(tam):
        for j in range((tam - 1)):
        # Swap adjacent elements if they are in decreasing order
            if (array[j] > array[j + 1]):
                swap(j, j + 1, array)
                num_swaps += 1
    return num_swaps

# --------------- Generar la funcion que hace el calculo -----------------------

len_array = input_entero_positivo("Ingrese el tamaño del arreglo a ordenar: ")
array = input_enteros_cantidad(f"Ingrese los {len_array} elementos del arreglo: ", len_array)

swaps = buble_sort_contado(len_array, array)

print(f"Array is sorted in {swaps} swaps.")
print(f"First Element: {array[0]}")
print(f"Last Element: {array[-1]}" )