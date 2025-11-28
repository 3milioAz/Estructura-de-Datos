def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        mitad = (inicio + fin) // 2
        if lista[mitad] == objetivo:
            return mitad
        elif lista[mitad] > objetivo:
            fin = mitad - 1
        else:
            inicio = mitad + 1

    return -1


hiperparametros = [0.001, 0.01, 0.05, 0.1, 0.2, 0.5, 1.0]
objetivo = 0.1

resultado = busqueda_binaria(hiperparametros, objetivo)
print("Encontrado en índice:", resultado)