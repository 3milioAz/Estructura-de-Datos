# -------Generar el arreglo de ventas semanales---------
dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
ventas_semanales = []

# --------Ingresar las ventas de cada dia-----------
#ventas = [1030, 2300, 1450, 1000, 780, 659, 2780]
#for i in ventas:
#    ventas_semanales.append(i)
#print(ventas_semanales)

for dia in dias:
    venta = input(f"Ingrese la venta del dia {dia}: ")
    while not venta.isdigit():  # se repite hasta que sea un número entero 
        print("Error: Ingrese un número de ventas válido.")
        venta = input(f"Ingrese la venta del día {dia}: ")
    ventas_semanales.append(int(venta))

# --------Mostrar el total de ventas a la semana-------------
print("Total de ventas semanales: ",sum(ventas_semanales))

# --------Calcular y mostrar el dia con mas y menos ventas----------
#print("Dia con mas ventas:", max(ventas_semanales))
#print("Dia con menos ventas:", min(ventas_semanales))
mayor_venta = 0
menor_venta = 0
for v in range(len(ventas_semanales)):
    if ventas_semanales[v] > ventas_semanales[mayor_venta]:
        mayor_venta = v
    elif ventas_semanales[v] < ventas_semanales[menor_venta]:
        menor_venta = v
print(f"El dia con mas ventas fue el {dias[mayor_venta]} con: {ventas_semanales[mayor_venta]}")
print(f"El dia con menos ventas fue el {dias[menor_venta]} con: {ventas_semanales[menor_venta]}")