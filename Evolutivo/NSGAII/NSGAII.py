'''
Implementación del algoritmo NSGA-II para la optimización multiobjetivo
@author: Diego Arturo Velázquez
'''
import random
import numpy as np
import math
import sys

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


# Algoritmo Non-dominated sorting
'''
@params:
    P -> Elementos de la población (Array  ["Id_xi", f_1(x_i), ... , f_n(x_i)] )
@return:
    F -> Los frentes con los elementos de cada frentes (Dictionary)
'''
def non_dominated_sorting(P):
    S = {}
    Np = {}
    F = {}
    F[1] = []
    P_rank = {}
    for elemento in P:
        # Extraemos el identificador de cada elemento de la población
        identificador = elemento[0]
        # Extraemos los valores numéricos de las funciones aplicadas a cada elemento
        vector_valores = elemento[1:]
        # Conjunto de elementos que elemento dominará en la población
        S[identificador] = []     #Sp
        # Contador de los elementos que dominan a elemento
        Np[identificador] = 0     # np
        for q in P:
            # Tienen que ser distintos a elemento
            if(q != elemento):
                if(dominancia_pareto(elemento[1:], q[1:])):
                    S[identificador].append(q) # Elementos que domina p
                elif(dominancia_pareto(q[1:], elemento[1:])):
                    Np[identificador] += 1
        if(Np[identificador] == 0 ): # Esto implica que elemento pertenece al primer frente de dominancia pareto
            P_rank[identificador] = 1
            F[1].append(elemento)
    print(S)
    print(Np)

    # Ahora vamos a asignar los elementos a los distintos frentes
    i = 1
    while(len(F[i]) != 0):
        Q = []
        for p in F[i]:
            identificador = p[0]
            for q in S[identificador]:
                identificador_q = q[0]
                Np[identificador_q] -= 1    # Vamos disminuyendo el contador de elementos que dominan a q
                if(Np[identificador_q] == 0):
                    P_rank[identificador_q] = i + 1
                    Q.append(q) # Agregamos a q al siguiente frente
        i += 1
        F[i] = Q
    # Regresamos el diccionario con todos los frentes
    return F

# Función auxiliar para copiar un arreglo
def copy(arr):
    res = []
    for elem in arr:
        res.append(elem)
    return res

# Implementación de un algoritmo que ordena una matriz con base en un elemento jésimo de sus vectores
def partition(arr, low, high, E):
    i = (low-1)         # index of smaller element
    pivot = arr[high][E]     # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j][E] <= pivot:

            # increment index of smaller element
            i = i+1
            a = copy(arr[i])
            b = copy(arr[j])
            arr[i] = b
            arr[j] = a

    a = copy(arr[i+1])
    b = copy(arr[high])
    arr[i+1] = b
    arr[high] = a
    return (i+1)

# Función auxiliar de QuickSort
def quicksort(arr, low, high, E):
    if len(arr) == 1:
        return arr
    if low < high:

        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high, E)

        # Separately sort elements before
        # partition and after partition
        quicksort(arr, low, pi-1, E)
        quicksort(arr, pi+1, high, E)
# Función inicial de QuickSort
def quickSort(arr, E):
    return quicksort(arr, 0, len(arr)-1, E)

# Algoritmo de Crowding distance
'''
@params:
    F[i] -> El frente iésimo que son non-dominated solutions
    M -> Número de funciones objetivo
@return:
    P lista con los elementos ordenados por Crowding distance
'''
def crowding_distance(frente, M):
    p = len(frente)
    identificadores = np.array(frente)[:, 0]
    F_max = {}
    F_min = {}
    P = {}
    # Nos quedamos únicamente con la matriz que se genera de evaluar los elementos en cada f_j función objetivo
    frente_numerico = np.array(frente)[:,1:]
    # Extraemos los máximos y mínimos para cada función objetivo
    for i in range(0, M):
        F_max[i+1] = max(frente_numerico[:, i])
        F_min[i+1] = min(frente_numerico[:, i])
    for j in range(0, p):
        P[identificadores[j]] = 0 # Inicialización de la Crowding Distance de la jésima solución
    for i in range(0, M):
        # P ' = Se ordena P con base en el iésimo objetivo
        quickSort(frente_numerico, i)
        P_prima = frente_numerico # Tenemos P' que corresponde a la población ordenada con base en la función iésima
        P_prima_cwd = {}
        P_prima_cwd[1] = math.inf
        P_prima_cwd[p] = math.inf
        # Se calcula el semiperímetro entre las soluciones cercanas a la iésima
        for j in range(2, p-1):
            numerador = float(P_prima[j+1][i]) -  float(P_prima[j-1][i])
            denominador = float(F_max[i+1]) - float(F_min[i+1])
            P[identificadores[j-1]] += numerador/denominador

    return dict(sorted( P.items(), key=lambda item: item[1]))


'''

poblacion = [
    ["A", 0, 1.0],
    ["B", 1/3, 2/3],
    ["C", 2/3, 1/3],
    ["D", 1.0, 0],
    ["E", 1.0, 2.0],
    ["F", 4/3, 5/3],
    ["G", 5/3, 4/3],
    ["H", 2.0, 1.0],
    ["I", 2.0, 3.0],
    ["J", 7/3, 8/3],
    ["K", 8/3, 7/3],
    ["L", 3.0, 2.0]
]

from matplotlib import pyplot as plt

letras = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P"]

poblacion = []
for i in range(0, 200):
    reng = [str(i)]
    for j in range(0, 5):
        reng.append(random.randint(1, 20))
    poblacion.append(reng)

colores = ["black", "purple", "orange", "yellow", "brown","black", "purple", "orange", "yellow", "brown","black", "purple", "orange", "yellow", "brown"]
j = 0
frentes = non_dominated_sorting(poblacion)
fig, ax = plt.subplots()


for frente in frentes:
    print("Frente: {f} tiene a los elementos: {e} con color: {c}".format(f = frente, e = frentes[frente], c=colores[j]))
    X = []
    Y = []
    ids = []
    for elemento in frentes[frente]:
        ids.append(elemento[0])
        X.append(elemento[1])
        Y.append(elemento[2])
    ax.scatter(X, Y, c=colores[j])
    j += 1
    for i,txt in enumerate(ids):
        ax.annotate(txt, (X[i], Y[i]))
plt.show()

print(crowding_distance(frentes[2], 5))
'''
