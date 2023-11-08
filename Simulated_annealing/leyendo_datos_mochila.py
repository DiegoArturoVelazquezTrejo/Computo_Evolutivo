'''
Programa generado para leer los datos de los archivos que contienen
los pesos de los objetos junto con su valor
'''

# Le podemos pasar como parámetro de entrada el nombre del archivo
archivo = open("./Mochila_T1/ks_10000_0", "r")

# Vamos a iterar sobre cada línea y almacenar la información que contienen
lineas = archivo.read().split("\n")

datos_iniciales = lineas.pop(0).split(" ")

CAPACIDAD = int(datos_iniciales[1] )     # Variable que indica la capacidad de la mochila
OBJETOS_TOTALES = int(datos_iniciales[0])

conjunto_objetos = {}

# Identificador para cada objeto del conjunto que tenemos
identificador = 1

for linea in lineas:
    datos = linea.split(" ")
    if(len(datos) == 2):
        # tupla  valor       peso
        tupla = (int(datos[0]), int(datos[1]))
        conjunto_objetos[str(identificador)] = tupla
        identificador += 1

# Diccionario con identificadores para cada producto y su valor asociado es una tupla que contiene el valor del objeto y su peso
#print(conjunto_objetos)

CONJUNTO_OBJETOS = conjunto_objetos
