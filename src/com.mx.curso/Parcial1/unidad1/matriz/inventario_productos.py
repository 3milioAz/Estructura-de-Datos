# Crear una matriz para almacenar los datos de 3 productos

matriz = [
    [19, 400, 50],
    [31, 150, 200],
    [33, 950, 22]
]

# Imprimir los datos del inventario
print("Inventario total:\n ID Stock Precio")
for f in range(len(matriz)):
    for c in range(len(matriz[f])):
        print(f" {matriz[f][c]} ", end="")
    print()

# Calcular valor de un producto especifico

product_id = 31

for f in range(len(matriz)):
    if matriz[f][0] == product_id:
        valor_total = matriz[f][1] * matriz[f][2]
        print(f"Valor total del producto {product_id}: ${valor_total}")

# Vender 10 unidades del producto y actualizarlo

for f in range(len(matriz)):
    if matriz[f][0] == product_id:
        matriz[f][1] -= 10
        valor_total = matriz[f][1] * matriz[f][2]
        print(f"Valor total del producto {product_id} (Actualizado): ${valor_total}")
