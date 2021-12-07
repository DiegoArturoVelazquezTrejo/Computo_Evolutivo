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
