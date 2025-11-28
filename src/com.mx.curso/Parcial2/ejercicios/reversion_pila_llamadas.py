def invertir_cadena(s):
    if len(s) <= 1:  
        return s  # Caso base
    return invertir_cadena(s[1:]) + s[0]  # Caso recursivo


texto = "IA_es_genial"
resultado = invertir_cadena(texto)

print("Original:", texto)
print("Invertida:", resultado)