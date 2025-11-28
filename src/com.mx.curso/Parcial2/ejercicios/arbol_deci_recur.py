def es_manzana(pregunta_num=1):
    if pregunta_num == 1:
        respuesta = input("¿La fruta es roja? (si/no): ").lower()
        if respuesta == "si":
            return es_manzana(2)  # Llamada recursiva a la siguiente pregunta
        else:
            return "No es una manzana."

    elif pregunta_num == 2:
        respuesta = input("¿La fruta es redonda? (si/no): ").lower()
        if respuesta == "si":
            return "Sí es una manzana."
        else:
            return "No es una manzana."
