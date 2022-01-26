'''
Implementación del algoritmo SPEA-2
'''
import random
import math
import numpy as np
from matplotlib import pyplot as plt

'''
Input: N (population size)
       N' (archive size)
       T (maximum number of generations)

Output: A (nondominated set)
'''

# STEP 1: Inicialización de la población P0 y crear un archivo vacío P't
P_0 = set()
t = 0
# STEP 2: Fitness assignment: Se calcula los valores de los individuos que están en Pt y P't

# Función para determinar la dominancia pareto
''' NOTACIÓN ::
        TRUE    si X domina a Y, es decir, X <= Y
        FALSE   si X no domina a Y
'''
def dominancia_pareto(X, Y):
    if(X == Y):
        return False
    for x, y in zip(X, Y):
        if(x <= y):
            pass
        else:
            return False
    return True

# Función auxuliar para juntar los elementos de una lista
def concatena_listas(a, b):
    return a + b

# Función para obtener la cantidad de elementos que un elemento i domina en la población
'''
    Función que obtiene el número de elementos que elemento i domina
    INPUT:
        P población (set)
        A archivo (set)
        elemento
'''
def strenght_coefficient(P, A, i):
    union = concatena_listas(P, A)
    dominados = []
    for elemento in union:
        if(dominancia_pareto(i, elemento)):
                dominados.append(elemento)
    return len(dominados)

# Función que calcula the raw fitness R(i) of an individual i
'''
    Función que obtiene el raw fitness i
    INPUT:
        P población (set)
        A archivo (set)
        elemento
'''
def raw_fitness(P, A, i):
    union = concatena_listas(P, A)
    raw_fitness = 0
    for j in union:
        if(dominancia_pareto(j, i)):
            raw_fitness += strenght_coefficient(P, A, j)
    return raw_fitness

# Prueba para el examen
poblacion = [
    [0, 1.0],
    [1/3, 2/3],
    [2/3, 1/3],
    [1.0, 0],
    [1.0, 2.0],
    [4/3, 5/3],
    [5/3, 4/3],
    [2.0, 1.0],
    [2.0, 3.0],
    [7/3, 8/3],
    [8/3, 7/3],
    [3.0, 2.0]
]

markers = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]

# Vamos a calcular el raw fitness para cada elemento de la población
for i in range(len(poblacion)):
    medida_fit = raw_fitness(poblacion, [], poblacion[i])
    print("  {m}  ::  fitness ===> {f}    ::    #domina = {d}".format(m = markers[i], e = poblacion[i], f=medida_fit, d = strenght_coefficient(poblacion, [], poblacion[i])))

fig, ax = plt.subplots()
poblacion = np.array(poblacion)
x = poblacion[:,0]
y = poblacion[:,1]
ax.scatter(x, y)

for i, txt in enumerate(markers):
    ax.annotate(txt, (x[i], y[i]))

plt.ylabel("f1")
plt.xlabel("f2")
plt.title("Gráfica de las aptitudes")
plt.grid()
plt.legend()
plt.show()

# STEP 3:
'''
Vamos a copiar todos los elementos no dominados en Pt y en P't a P't+1. Si el tamaño de P't+1 excede al tamaño
máximo del archivo, hay que reducirlo. Si es menor, hay que meter elementos dominados de Pt y de P't.
'''

# STEP 4: Terminación
