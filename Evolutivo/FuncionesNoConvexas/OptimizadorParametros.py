'''
Programa que se encargará de ejecutar distintas veces un algoritmo genético, modificando sus parámetros
con base en eso, hará un torneo y escogerá los mejores parámetros

Parámetros para evaluar un algoritmo genético:

a) Desviación estándar del conjunto de óptimos
b) Media del conjunto de óptimos

Parámetros:

1) Tamaño de la población
2) Radio inicial de la población
3) Número total de generaciones de la población
4) Coeficiente de cruza de la población
5) Coeficiente de mutación de la población
6) Alfa
7) Posición
8) Disparos

Variables fijas:

1) Dimensión de la función
2) Función objetivo
3) Método: Minimizar o Maximizar

'''
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


# Variables que se mantendrán constantes durante la ejecución del algoritmo
# Función objetivo
F = f.ackley
n = 10   # Dimensión de la función objetivo
metodo = "minimizar"  # Método 
