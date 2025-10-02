# -------Generar el arreglo de ventas semanales---------
ventas_semanales = []

# --------Ingresar las ventas de cada dia-----------
ventas = [1030, 2300, 1450, 1000, 780, 659, 2780]

for i in ventas:
    ventas_semanales.append(i)
print(ventas_semanales)

# --------Mostrar el total de ventas a la semana-------------
print("Total de ventas semanales: ",sum(ventas_semanales))

# --------Calcular y mostrar el dia con mas y menos ventas----------
print("Dia con mas ventas:", max(ventas_semanales))

print("Dia con menos ventas:", min(ventas_semanales))