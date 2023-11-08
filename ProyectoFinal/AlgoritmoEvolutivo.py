# Biblioteca para trabajar con números aleatorios
import random
# Biblioteca para trabajar con matrices
import numpy as np
# Biblioteca para utilizar los operadores genéticos
import OperadoresGeneticos as og
# Biblioteca para utilizar el kmeans
import KMeans as km
# Biblioteca que contiene todas las funciones que se pretenden optimizar
import Funciones as f
# Biblioteca para graficar
from matplotlib import pyplot as plt
# Biblioteca para medir el tiempo de ejecición de un algoritmo
import time
# Biblioteca para crear la frontera pareto con non-dominated sorting 
from NSGAII import non_dominated_sorting

np.set_printoptions(formatter={'float': lambda x: "{0:0.2f}".format(x)})


'''
Algoritmo genético para codificaciones continuas
'''
class AlgoritmoGenetico:

    # Constructor de la clase
    def __init__(self, poblacion, gen, coef_mutacion, coef_cruza, F, alfa, posicion, color, identificador, metodo="minimizar"):
        self.poblacion = poblacion
        self.npop = len(self.poblacion)
        self.fenotipo  = []
        # Parámetros genéticos
        self.generaciones = gen
        self.coef_mutacion = coef_mutacion
        self.coef_cruza = coef_cruza
        # Parámetros de cruza
        self.posicion = posicion
        self.alfa = alfa
        # Parámetros de la mutación
        self.lbk = random.random()
        self.ubk =  -self.lbk
        self.nm  = random.randint(0, int(self.lbk))
        # Método indica si se desea maximizar o minimizar una función
        self.metodo = metodo
        # Función objetivo con la que se trabajará
        self.F = F
        # Óptimos por generación
        self.optimos = np.zeros((gen, len(poblacion[0])+1))
        # Color para la gráfica
        self.color = color
        self.identificador = identificador


    # Método para evaluar los elementos de la población
    # Es un diccionario con funciones 
    def evalua(self, poblacion):
        matriz_evaluaciones = []
        i = 0 
        for elemento in poblacion: 
            # El primer elemento hace referencia al índice del elemento en la población 
            evaluaciones = [i]
            for funcion in self.F: 
                f = self.F[funcion](elemento)
                evaluaciones.append(float(f))
            matriz_evaluaciones.append(evaluaciones)
            i += 1 
        return np.array(matriz_evaluaciones)

    # Método para desplegar el gráfico de convergencia de los óptimos
    def convergencia_optimos(self):
        plt.plot(self.optimos[:,-1], c=self.color, label=[self.identificador])
        plt.ylabel("Aptitud óptima")
        plt.xlabel("Número de generación")
        plt.title("Gráfico de convergencia")
        plt.grid()
        plt.legend()
        #plt.show()

    # Método para guardar los resultados en un csv file para estudiarlos después
    def to_csv(self, num, nom_func):
        string = "{f}-{i}".format(f = nom_func, i = num)
        np.savetxt("./Prueba_Validacion/"+string+".csv", self.optimos, delimiter=",")

    # Método para mostrar/imprimir los frentes óptimos 
    def muestra_frentes(self, frente): 
        np.set_printoptions(formatter={'float': lambda x: "{0:0.2f}".format(x)})
        for elemento in frente: 
            print(elemento[1:])

    # Método para obtener la nueva población
    def main(self):
        start_time_genetico = time.time()
        for i in range(self.generaciones):
            f_eval_1 = self.evalua(self.poblacion)
            start_time = time.time()
            
            poblacion_f = self.poblacion
            aptitudes = f_eval_1

            start_time = time.time()
            # Seleccionamos los elementos

            # Aplicamos el algoritmo del NSGA-II  non-dominated sorting 
            frentes = non_dominated_sorting(f_eval_1)
            optimo = frentes[1][0]
            # Con los frentes, realizamos la selección de elementos 
            idx_p = og.seleccion_por_frente(frentes, self.npop) # Regresa la lista de los índices de elementos
            #print("Selección Non-dominated-S : --- %s seconds ---" % (time.time() - start_time))
            

            # Cruzamos los elementos
            start_time = time.time()
            hijos = og.cruza_intermedia(idx_p, poblacion_f, self.posicion, self.alfa)
            #print("Cruza Intermedia : --- %s seconds ---" % (time.time() - start_time))
            # Mutamos los elementos
            start_time = time.time()
            hijos = og.mutacion_uniforme_p(hijos, k=random.randint(0, len(hijos[0])-1), lbk= self.lbk, ubk= self.ubk, nm=self.nm )
            #print("Mutación : --- %s seconds ---" % (time.time() - start_time))
            # Incorporación de los nuevos elementos
            self.poblacion = hijos
            # Vamos a agregar el elemento óptimo a la siguiente generación
            self.poblacion[0] = optimo[1:]   # Tomaremos el primer elemento del frente 
            self.optimos[i] = optimo

        # Tenemos que obtener el elemento del primer frente; ese será indice_minimo_global 

        frente_optimos = non_dominated_sorting(self.optimos)
        self.muestra_frentes(frente_optimos[1])
        print("Total : --- %s seconds ---" % (time.time() - start_time_genetico))