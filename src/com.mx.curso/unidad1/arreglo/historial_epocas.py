# Generar la lista dinamica

lista = [
    0.75,    # Precision de la epoca 1
    0.89,    # Precision de la epoca 2
    0.21,    # Precision de la epoca 3
    0.34,    # Precision de la epoca 4
    0.67,    # Precision de la epoca 5
    0.77,    # Precision de la epoca 6
    0.78,    # Precision de la epoca 7
    0.54,    # Precision de la epoca 8
    0.62     # Precision de la epoca 9
]

print(lista)

# Agregar precision a la lista

lista.append(0.43)
print(lista)


lista_nuevas_precisiones = [0.61, 0.88, 0.94, 0.42, 0.37]

for i in lista_nuevas_precisiones:
    lista.append(i)
print(lista)

# Imprimir la precision final
print(lista[-1])

# Imprimir la precision mas alta
print(max(lista))