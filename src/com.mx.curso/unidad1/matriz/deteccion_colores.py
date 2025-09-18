# Crear la matriz de pixeles

matriz = [ 
    [[255, 0, 0],[0, 255, 0],[0, 0, 255]],
    [[0, 0, 255],[255, 0, 0],[0, 0, 255]],
    [[0, 0, 255],[0, 255, 0],[0, 255, 0]]
]

rojo = [255, 0, 0]
verde = [0, 255, 0]
azul = [0, 0, 255]

# Analizar cantidad de pixeles en la matriz
rojos = 0
verdes = 0
azules = 0
for f in range(len(matriz)):
    for c in range(len(matriz[f])):
        if matriz[f][c] == rojo:
            rojos += 1
        elif matriz[f][c] == verde:
            verdes += 1
        elif matriz[f][c] == azul:
            azules += 1
print(f"En la matriz de la imagen se encuentran:\n{rojos} pixeles rojos.\n{verdes} pixeles verdes.\n{azules} pixeles azules.")