'''
Clase que tiene los operadores genéticos (evolutivos) para los algoritmos
con soluciones/representación Real
@author: Diego Arturo Velázquez Trejo
'''
import random
import math
import numpy as np

# En números reales

# Operadores para selección

# Método de selección por ruleta
def seleccion_ruleta(aptitudes, n):
    p = aptitudes/sum(aptitudes)
    cp= np.cumsum(p)
    parents = np.zeros(n)
    for i in range(n):
        X = np.random.uniform()
        parents[i] = np.argwhere(cp > X)[0]
    return parents.astype(int)

# Método de selección por frente óptimo de pareto 
def seleccion_por_frente(frentes, n): 
    n = int(n/2)
    conjunto_indices = []
    frente = 1 
    while(len(conjunto_indices) < n): 
        while(len(frentes[frente]) != 0 and len(conjunto_indices) < n): 
            conjunto_indices.append(frentes[frente].pop(0)[0])
        frente += 1 
    return conjunto_indices

# Operadores para cruza

# Cruza intermedia
'''
Algoritmo que se ejecuta sobre dos elementos

@param P1 -> Arreglo de dimensión n
@param P2 -> Arrelgo de dimensión n
@return H1 -> Arreglo de dimensión n
@return H2 -> Arreglo de dimensión n
'''
def cruza_intermedia_s(P1, P2, posicion, alfa = random.random()):
    # Necesitamos que la longitud de ambos padres sea la misma
    if(len(P1) != len(P2)):
        return False
    h1 = np.zeros(len(P1))
    h2 = np.zeros(len(P2))
    for i in range(len(P1)):
        if(i < posicion):
            h1[i] = P1[i]
            h2[i] = P2[i]
        else:
            h1[i] = alfa * P2[i] + (1 - alfa)*P1[i]
            h2[i] = alfa * P1[i] + (1 - alfa)*P2[i]
    return h1, h2

# Extensión de cruza intermedia para un conjunto de elementos de población
def cruza_intermedia(indices, poblacion, posicion, alfa = random.random()):
    nueva_poblacion = []
    # Ejecutarlo sobre toda una matriz de elementos
    if(len(poblacion) % 2 == 1):
        cota = (len(poblacion) - 1)/2
    else:
        cota = len(poblacion)/2
    for i in range(0, int(cota)):
        id_h1 = int(random.choice(indices))
        id_h2 = int(random.choice(indices))
        padre1 = poblacion[id_h1]
        padre2 = poblacion[id_h2]
        h1, h2 = cruza_intermedia_s(padre1, padre2, posicion, alfa)
        nueva_poblacion.append(h1)
        nueva_poblacion.append(h2)
    return np.array(nueva_poblacion)

# Cruza Binaria Simulada
'''
@param P1 -> Arreglo de dimensión n
@param P2 -> Arrelgo de dimensión n
@return H1 -> Arreglo de dimensión n
@return H2 -> Arreglo de dimensión n
'''
def simulated_binary_crossover(P1, P2, nc):
    u = random.random()
    if(u <= 0.5):
        beta = math.pow(2*u, 1/(nc + 1))
    else:
        beta = math.pow(1/(2*(1 - u)), 1/(nc +1))
    # En caso de no tener los padres en arreglos de numpy para manipularlos
    P1 = np.array(P1)
    P2 = np.array(P2)

    h1 = 0.5 * (P1 + P2 - beta * abs(P2 - P1))
    h2 = 0.5 * (P1 + P2 + beta * abs(P2 - P1))
    return h1, h2


# Operadores para mutación

# Mutación no uniforme
'''
@param P1 -> Arreglo de dimensión p
@return P1 -> Arreglo de dimensión p
'''
def mutacion_no_uniforme(P, k, t, T, lbk, ubk, b=5):

    # Función auxiliar
    delta = lambda t, y: y * (1 - math.pow(random.random(),math.pow(1 - t/T, b) ))

    x = random.randint(0,1)
    if(x == 1):
        vk = P[k] + delta(t, ubk - P[k])
    else:
        vk = P[k] - delta(t, P[k] - lbk)
    h1 = []
    for i in range(0, len(P)):
        if(i == k):
            h1.append(vk)
        else:
            h1.append(P[i])
    return h1

# Mutación  uniforme
'''
@param P1 -> Arreglo de dimensión p
@return P1 -> Arreglo de dimensión p
'''
def mutacion_uniforme(P, k, lbk, ubk, nm, u=random.random()):
    delta = min(P[k]-lbk, ubk - P[k])/ubk - lbk
    delta = 1
    if(u <= 0.5):
        delta_q = math.pow(2*u + (1 - 2*u)*(1 - delta**(nm+1)), 1/(nm+1))- 1
    else:
        delta_q = 1- math.pow(2*(1-u)+ 2*(u - 0.5)*math.pow(1-delta, nm+1), 1/(nm+1))

    vk = P[k] + delta_q * (ubk - lbk)
    elemento = np.zeros(len(P))
    for i in range(len(P)):
        if(i != k):
            elemento[i] = P[i]
        else:
            elemento[i] = vk
    return elemento

# Extensión de la mutación uniforme a una matriz de elementos
def mutacion_uniforme_p(elementos, k, lbk, ubk, nm, u=random.random()):
    hijos = []
    for elemento in elementos:
        elemento = mutacion_uniforme(elemento, k, lbk, ubk, nm, u)
        hijos.append(elemento)
    return np.array(hijos)

# Mutación de límite
'''
@param P1 -> Arreglo de dimensión p
@return P1 -> Arreglo de dimensión p
'''
def mutacion_de_limite(P, k, lbk, ubk, x = random.random()):
    if(x <= 0.5):
        vk = lbk
    else:
        vk = ubk
    return P[:k]+[vk]+P[k+1:]
