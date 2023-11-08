'''
Implementación de una heurística para la optimización de problemas: búsqueda Tabú.

Simulated Annealing (Recocido Simulado)
Materia de Complejidad Computacional, 8to semestre, Facultad de Ciencias, UNAM.

@author Diego Velázquez Trejo

'''

# Bibliotecas que usaremos
import random
import math

'''
@param: F función objetivo 
@param: Fs función para generar soluciones vecinas 
@param: I0 estado inicial
@param: MAXITER número de iteraciones
@param: tamaño_lista_tabu tamaño de la lista tabú

@return: Solución que minimiza o maximiza la función objetivo (según se especifique)
'''
def Busqueda_Tabu(I0, F, FS, MAXITER, tamaño_lista_tabu):
    mejor_solucion = I0
    mejor_valor = F(I0)
    lista_tabu = []
    iters = 0

    while iters < MAXITER:
        vecinos = [FS(mejor_solucion) for _ in range(tamaño_lista_tabu)]
        mejor_vecino = None
        mejor_vecino_valor = float('inf')
        
        for vecino in vecinos:
            if vecino not in lista_tabu:
                valor_vecino = F(vecino)
                
                if valor_vecino < mejor_vecino_valor:
                    mejor_vecino = vecino
                    mejor_vecino_valor = valor_vecino
        
        lista_tabu.append(mejor_vecino)
        if len(lista_tabu) > tamaño_lista_tabu:
            lista_tabu.pop(0)
        
        if mejor_vecino_valor < mejor_valor:
            mejor_solucion = mejor_vecino
            mejor_valor = mejor_vecino_valor

        iters += 1

    return mejor_solucion, mejor_valor
