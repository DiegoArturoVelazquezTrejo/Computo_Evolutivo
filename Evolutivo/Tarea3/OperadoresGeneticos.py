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

# Operadores para cruza

# Cruza intermedia
'''
@param P1 -> Arreglo de dimensión n
@param P2 -> Arrelgo de dimensión n
@return H1 -> Arreglo de dimensión n
@return H2 -> Arreglo de dimensión n
'''
def cruza_intermedia(P1, P2, posicion, alfa = random.random()):
    # Necesitamos que la longitud de ambos padres sea la misma
    if(len(P1) != len(P2)):
        return False
    h1 = P1[:posicion]+[  alfa * P2[i] + (1 - alfa)*P1[i] for i in range(posicion, len(P2)) ]
    h2 = P2[:posicion]+[  alfa * P1[i] + (1 - alfa)*P2[i] for i in range(posicion, len(P1)) ]
    return h1, h2

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
    if(u <= 0.5):
        delta_q = math.pow(2*u + (1 - 2*u)*(1 - delta**(nm+1)), 1/(nm+1))- 1
    else:
        delta_q = 1- math.pow(2*(1-u)+ 2*(u - 0.5)*math.pow(1-delta, nm+1), 1/(nm+1))

    vk = P[k] + delta_q * (ubk - lbk)
    return P[:k]+[vk]+P[k+1:]

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
