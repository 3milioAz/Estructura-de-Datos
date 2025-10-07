def input_enteros_cantidad(input_text, max_valores):
    while True:
        valores = input(input_text).split()
        try:
            numeros = [int(v) for v in valores]   # convierte a enteros
            if len(numeros) > max_valores:        # valida la cantidad
                print(f"Error: Solo puedes ingresar hasta {max_valores} valores.")
            else:
                 return numeros
        except ValueError:
            print("Error: Ingrese solo enteros válidos (positivos o negativos).")

def distacias_calculadas(ubicacion_arbol, cantidades, rango_casa):
    valores = []
    for v in cantidades:
        valores.append(ubicacion_arbol + v)

    cont = 0
    for v in valores:
        if v >= rango_casa[0] and v <= rango_casa[1]:
            cont += 1
    print(cont)

# Crear funcion para calcular manzanas y naranjas
casa_range = input_enteros_cantidad("Ingrese los valores de s y t: ", 2)
arboles = input_enteros_cantidad("Ingrese los valores de a y b: ", 2)
cantidad_frutos = input_enteros_cantidad("Ingrese los valores de m y n: ", 2)
distancias_frutos1 = input_enteros_cantidad(f"Ingrese la distancias de caida de los m({cantidad_frutos[0]}) frutos: ", cantidad_frutos[0])
distancias_frutos2 = input_enteros_cantidad(f"Ingrese la distancias de caida de los n({cantidad_frutos[1]}) frutos: ", cantidad_frutos[1])

distacias_calculadas(arboles[0], distancias_frutos1, casa_range)

distacias_calculadas(arboles[1], distancias_frutos2, casa_range)