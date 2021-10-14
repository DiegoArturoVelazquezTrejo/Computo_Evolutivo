'''
Programa para optimizar la función en un intervalo dado:

Función objetivo:

    f(x_1,x_2 )=x_1^2+x_2^2, -5≤x_1,x_2≤5
'''
import random
import math

# Variables que definiremos de acuerdo al problema
T   = 350000
IT0 = 1
I   = 1000000
BETTA = 1/10

M0 = 0.0 # Estado inicial


def obtiene_elemento_aleatorio(identificadores):
    pass

def decrece_temperatura(T):
    return T - BETTA * T

def F(M):
    pass

def FS(est, V):
    pass

MOptima, prom, objeto_maximo = Simulated_Annealing(T, conjunto_identificadores, F, FS, M0, IT0, decrece_temperatura, I, 1, "maximizar")
