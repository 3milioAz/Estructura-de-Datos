#---------Crear el arreglo que almacene las calificaciones de los estudiantes------------
calificaciones = [8, 7, 10, 8, 9, 9, 7, 5, 7, 10]

#--------Consultar una calififacion especifica por indice y modificar su valor----------
indice = 5
print("Calificacion Antigua:", calificaciones[indice])
calificaciones[indice] = 8
print("Calificacion Modificada:", calificaciones[indice])

#---------Calcular el promedio general del grupo----------
promedio = sum(calificaciones) / len(calificaciones)
print("Promedio general del grupo:", promedio)