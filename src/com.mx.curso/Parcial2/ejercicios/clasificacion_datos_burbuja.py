def burbuja(lista):
    n = len(lista)
    hubo_intercambio = True

    while hubo_intercambio:
        hubo_intercambio = False
        for i in range(n - 1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                hubo_intercambio = True


puntajes = [0.4, 0.9, 0.1, 0.7, 0.3]
burbuja(puntajes)

print("Lista ordenada:", puntajes)