def busqueda_secuencial(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return 1
        return -1

if __name__ == "__main__":
    datos = [2, 4, 5, 3, 6, 8, 12]
    elemento = 9

    indice = busqueda_secuencial(datos, elemento)
    if indice != -1:
        print(f"Elemento {elemento} encontrado en el indice {indice}")
    else:
        print(f"Elemento {elemento} no encontrado en el indice {indice}")
