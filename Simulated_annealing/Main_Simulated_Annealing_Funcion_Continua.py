'''
Programa para optimizar la función en un intervalo dado:

Función objetivo:

    f(x_1,x_2 )=x_1^2+x_2^2, -5≤x_1,x_2≤5
'''
import random
import math
from Vector import Vector
from simulated_annealing import Simulated_Annealing

# Variables que definiremos de acuerdo al problema
T   = 350000
IT0 = 1
I   = 1000000
BETTA = 1/10
I0 = [0.0, 0.0] # Estado inicial

infimo_X = -5
infimo_Y = -10
supremo_X = 10
supremo_Y = 5

# Función para generar un valor inicial
def genera_estado_inicial(infimo_X, supremo_X, infimo_Y, supremo_Y):
    v = [random.uniform(infimo_X, supremo_X), random.uniform(infimo_Y, supremo_Y)]
    return Vector(v[0], v[1])

I0 = genera_estado_inicial(infimo_X, supremo_X, infimo_Y, supremo_Y) # Estado inicial

#print(I0.toString())
# Obtener un elemento alrededor de una vecindad
def FS(vector, V):
    radio_epsilon = 0.1
    '''
    vecindad para X         ->       (X - epsilon, X + epsilon )
    vecindad para Y         ->       (Y - epsilon, Y + epsilon )
    '''
    v = [random.uniform(vector.X - radio_epsilon, vector.X + radio_epsilon),
              random.uniform(vector.Y - radio_epsilon, vector.Y + radio_epsilon)]
    copia = vector.copia()
    estado_aceptacion = copia.actualiza(v[0], v[1])
    while(estado_aceptacion == False):
        v = [random.uniform(vector.X - radio_epsilon, vector.X + radio_epsilon),
                  random.uniform(vector.Y - radio_epsilon, vector.Y + radio_epsilon)]
        estado_aceptacion = copia.actualiza(v[0], v[1])

    return copia


def decrece_temperatura(T):
    return T - BETTA * T

def F(vector):
    '''
    Función objetivo:

        f(x_1,x_2 )=x_1^2+x_2^2, -5≤x_1,x_2≤5
    '''
    return vector.X**2 + vector.Y**2

MOptima, prom, objeto_maximo, objeto_minimo = Simulated_Annealing(T, {1}, F, FS, I0, IT0, decrece_temperatura, I, 1, "maximizar")
# Resultados
print("\n\n#### RESULTADOS ####")
print("Valor del vector inicial: ")
print(I0.toString())
print("Resultado del algoritmo SA: ")
print(MOptima.toString())
print("Objeto máximo en las iteraciones: ")
print(objeto_maximo.toString())
print("Objeto mínimo en las iteraciones: ")
print(objeto_minimo.toString())
