# Biblioteca para trabajar con números aleatorios
import random
# Biblioteca para trabajar con matrices
import numpy as np
# Biblioteca para utilizar los operadores genéticos
import OperadoresGeneticos as og
# Biblioteca para utilizar el kmeans
import KMeans as km
# Biblioteca para utilizar el algoritmo memético
import AlgoritmoMemetico as am
# Biblioteca que contiene todas las funciones que se pretenden optimizar
import Funciones as f
# Biblioteca para graficar
from matplotlib import pyplot as plt
# Biblioteca para trabajar con algoritmos genéticos
import AlgoritmoEvolutivo as ag
'''
Procedimiento para el algoritmo genético:
1. Inicializar la población.
2. Aplicar el algoritmo k-menas para generar grupos en la población.
3. Mandar a llamar la clase de hilos y por cada hilo hacer:

Repetir:

    a) Se evalúa la población del késimo cluster.
    b) Se aplican los algoritmos meméticos.
    c) Se seleccionan los elementos de la población una vez que mejoraron.
    d) Se cruzan los elementos seleccionados.
    e) Se mutan los elementos obtenidos de la cruza.
    f) Incorporación de los elementos a la población.

'''

# Inicialización de la población:
tam_pob = 1000
radio_inicial = 100

# Función objetivo a optimizar
n_dim = 10    # es 2 únicamente para la función 2 de la tarea, es 10 para las demás funciones
F = f.rast

# Parámetros del algoritmo K-means
k = 6
n_iter = 100

poblacion = np.random.uniform(-radio_inicial, radio_inicial, (tam_pob, n_dim))

# Parámetros del genético
gen = 500
coef_mutacion = random.random()
coef_cruza  = random.random()
alfa = random.random()
posicion = 5
disparos = 10
metodo = "minimizar"

# Aplicación del algoritmo K-Means a la población:
kmeans = km.KMeans(poblacion, k, n_iter)

# Obtenemos las agrupaciones del algoritmo y las mandamos a un distinto algoritmo genético
agrupaciones = kmeans.obtiene_agrupaciones()
algoritmos_geneticos = []
# Colores al momento de mostrar gráficas
colores = ['green', 'pink', 'blue', 'red', 'yellow', 'black', 'purple','orange','pink','white']
j = 0

for agrupacion in agrupaciones:
    if(len(agrupacion) != 0):
        agen = ag.AlgoritmoGenetico(agrupacion, gen, coef_mutacion, coef_cruza, F, alfa, posicion, disparos, colores[j], "AG-"+str(j) ,metodo)
        algoritmos_geneticos.append(agen)
        j += 1

# PARALELISMO ::: multithreading
# Se manda a ejecutar cada algoritmo sobre un hilo:
# Biblioteca para trabajar con multithreading
import threading

def worker(num, agenetico):
    """thread worker function"""
    print('Número de hilo de ejecución: %s' % num)
    agenetico.main()
    agenetico.convergencia_optimos()
    agenetico.to_csv()
    return

# Este será el bloque de código que se ejecute una vez que se segmentó la población inicial
threads = []

for i in range(k):
    t = threading.Thread(target=worker, args=(i,algoritmos_geneticos[i],))
    threads.append(t)
    t.start()

for th in threads:
    th.join()
plt.show()
