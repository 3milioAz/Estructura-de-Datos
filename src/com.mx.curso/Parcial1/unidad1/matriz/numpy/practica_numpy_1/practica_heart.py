# Practica con dataset heart+disease
import numpy as np

# 1.----------------------------Descargar y Cargar el Conjunto de Datos:------------------------------
# Cargar el dataset
link = 'src/com.mx.curso/unidad1/matriz/numpy/practica_numpy_1/heart+disease/processed.cleveland.data'
datos = np.genfromtxt(link, delimiter=',', dtype='object')

# Visualizar los datos
print("----- Datos -----\n", datos)
# Cargar solo las 5 primeras columnas
datos_numericos = np.genfromtxt(link, delimiter=',', usecols=(0,1,2,3,4))

# Visualizar los datos numericos
print("----- Datos Numericos -----\n", datos_numericos)

#2.---------------------------Introducir y Manejar Valores Faltantes:----------------------------------
# Simulación de datos incompletos
datos_numericos[0,0] = np.nan
datos_numericos[302,4] = np.nan

# Matriz con datos faltantes
print("----- Datos Faltantes -----\n", datos_numericos)

# Calcula la mediana de cada columna
median_columna = np.nanmedian(datos_numericos, axis=0) # El nanmedian calcula la media aunque hallan valores nan en los datos
print("----- Media de cada Columna  ----->", median_columna)

# Crea una copia de la matriz para guardar los datos limpios
datos_limpios = datos_numericos

# Toma la mediana de la columna y la coloca donde aparece un nan
for f in range(datos_numericos.shape[0]): 
    for c in range(datos_numericos.shape[1]):
        if np.isnan(datos_numericos[f,c]):    # La funcion isnan evalua si es nan
            datos_limpios[f,c] = median_columna[c]   # Toma la mediana de la columna y la agrega en la posición del nan

print("----- Matriz con nan Remplazados -----\n", datos_limpios)

#3.----------------------------------Análisis Descriptivo:-------------------------------------
# Imprime una comparación de la matriz antes y después de la limpieza.
print("----- Matriz pre Limpieza -----\n", datos_numericos)
print("----- Matriz post Limpieza -----\n", datos_limpios)

# Calcula y muestra en forma tabular para cada atributo
atributos = ["Edad                          ", "Sexo                          ", "Tipo de Dolor de Pecho        ", "Presion Arterial en Reposo    ", "Colesterol Serico en mg/dl    "]

media_columna = np.mean (datos_limpios, axis=0) 
print("-- Media de cada Columna  ----->", media_columna)

median_columna = np.median(datos_limpios, axis=0) 
print("-- Mediana de cada Columna  ----->", median_columna)

std_columna = np.std(datos_limpios, axis=0) 
print("-- Desviación Estandar de cada Columna  ----->", std_columna)

print("Dato ------------------------ Media --- Mediana --- Desviacion Estandar")
for a in range(len(atributos)):
    print(f"{atributos[a]}{round(media_columna[a],2)}      {round(median_columna[a],2)}            {round(std_columna[a],2)}")

# 4.--------------------------Análisis Específico de Salud Cardíaca:---------------------------

# Calcula el promedio de colesterol de todos los pacientes
media_col = np.mean(datos_limpios[:, 4]) # El : selecciona todas las filas, y el 4 significa mi columna elegida a calcularle su promedio
print("-- Media de Colesterol de Todos los Pacientes  ----->", media_col)

# Determina el porcentaje de pacientes con presión arterial mayor al promedio.
media_presion = np.mean(datos_limpios[:, 3])

cont = 0
for p in datos_limpios:
    if p[3] > media_presion:
        cont += 1
porcen_pacientes = round((cont / len(datos_limpios)),4) * 100
print(f"-- Porcentaje de Pacientes con Presion Arterial Mayor a la Media  -----> {porcen_pacientes}%")

# Encuentra la edad del paciente con la mayor frecuencia cardiaca alcanzada.
datos_numericos_thal = np.genfromtxt(link,
                      delimiter=',', usecols=(12)) # thal es el nombre que se le da a la columna de mayor presion cardiaca alcanzada por paciente

mayor = 0
for n in range(len(datos_numericos_thal)):
    if datos_numericos_thal[n] > datos_numericos_thal[mayor]:
        mayor = n

edad_may_thal = int(datos_limpios[mayor, 0])
print(f"-- Edad del Paciente con la Mayor Frecuencia Cardiaca Alcanzada  -----> {edad_may_thal} anos.")