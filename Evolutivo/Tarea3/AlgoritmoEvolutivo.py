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
# Biblioteca para medir el tiempo de ejecición de un algoritmo
import time

'''
Algoritmo genético para codificaciones continuas
'''
class AlgoritmoGenetico:

    # Constructor de la clase
    def __init__(self, poblacion, gen, coef_mutacion, coef_cruza, F, alfa, posicion, disparos, color, identificador, metodo="minimizar"):
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
        # Parámetros internos (para el algoritmo Memético)
        self.ejecuciones_efectivas_memetico = 0
        # Método indica si se desea maximizar o minimizar una función
        self.metodo = metodo
        # Función objetivo con la que se trabajará
        self.F = F
        # Parámetros del algoritmo memético
        self.cantidad_disparos = disparos
        # Óptimos por generación
        self.optimos = np.zeros((gen, len(poblacion[0])+1))
        # Color para la gráfica
        self.color = color
        self.identificador = identificador


    # Método para evaluar los elementos de la población
    def evalua(self, poblacion):
        return np.array([self.F(elemento) for elemento in poblacion])

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
        np.savetxt("./ResultadosOptimos/"+string+".csv", self.optimos, delimiter=",")

    # Método para obtener la nueva población
    def main(self):
        start_time_genetico = time.time()
        for i in range(self.generaciones):
            f_eval_1 = self.evalua(self.poblacion)
            min    = np.argmin(f_eval_1)
            max    = np.argmax(f_eval_1)

            # Calculamos el radio (STAND BY)
            radio_disparo = f_eval_1[max] - f_eval_1[min]
            radio = 10

            start_time = time.time()
            # Llamamos al algoritmo memético
            minimo = self.poblacion[min]
            maximo = self.poblacion[max]
            punto_critico = minimo if(self.metodo == "minimizar") else maximo
            memetico = am.shooting_method(punto_critico, self.F, radio, self.cantidad_disparos, self.metodo)
            poblacion_iesima = am.trasladar_vectores(self.poblacion, memetico[1])
            #print("Memético : --- %s seconds ---" % (time.time() - start_time))

            start_time = time.time()
            f_eval_2 = self.evalua(poblacion_iesima)
            # vamos a ver en promeido, qué población tendió a mejorar: si la que pasó por el memético o la que no, nos quedamos con la mejor.
            # Dependiendo del método, vamos a ver si el promedio de las evaluaciones fue mayor o menor

            promedio_diferencias_1 = np.mean(f_eval_1)
            promedio_diferencias_2 = np.mean(f_eval_2)
            #print("Evaluando medias : --- %s seconds ---" % (time.time() - start_time))

            # Imrpimimos los promedios de las dos poblaciones existentes
            #print("Promedios :: Sin-Memético := {ini}, Con-Memético := {fin}".format(ini = promedio_diferencias_1, fin = promedio_diferencias_2))

            if(self.metodo == "maximizar" and promedio_diferencias_2 > promedio_diferencias_1):
                poblacion_f =  poblacion_iesima
                aptitudes   = f_eval_2
                self.ejecuciones_efectivas_memetico += 1
                optimo = memetico[0]
                #print("SUCEDO ....... 1")
            elif(self.metodo == "maximizar" and promedio_diferencias_1 > promedio_diferencias_2):
                poblacion_f = self.poblacion
                aptitudes   = f_eval_1
                optimo = punto_critico
                #print("SUCEDO ....... 2")
            elif(self.metodo == "minimizar" and promedio_diferencias_2 < promedio_diferencias_1):
                poblacion_f = poblacion_iesima
                aptitudes   = f_eval_2
                optimo = memetico[0]
                self.ejecuciones_efectivas_memetico += 1
                #print("SUCEDO ....... 3")
            elif(self.metodo == "minimizar" and promedio_diferencias_1 < promedio_diferencias_2):
                poblacion_f = self.poblacion
                aptitudes   = f_eval_1
                optimo = punto_critico
                #print("SUCEDO ....... 4")
            else:
                #print("SUCEDO ....... 5")
                optimo = punto_critico
                poblacion_f = self.poblacion
                aptitudes = f_eval_1

            #Vamos a guardar el óptimo por generación
            self.optimos[i] = np.append(optimo, self.F(optimo))

            start_time = time.time()
            # Seleccionamos los elementos
            idx_p = og.seleccion_ruleta(aptitudes, self.npop) #Este método me egresa los índices de los elementos seleccionados
            #print("Ruleta : --- %s seconds ---" % (time.time() - start_time))
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
            self.poblacion[0] = optimo

        print("\n"+self.identificador)
        print("Aplicación del Algoritmo Memético :: {mem}".format(mem = self.ejecuciones_efectivas_memetico))
        #print("Óptimos por generación: ", end="")
        #print(self.optimos[:,-1])

        indice_minimo_global = np.argmin(self.optimos[:,-1]) if(self.metodo == "minimizar") else np.argmax(self.optimos[:,-1])
        fenotipo = self.optimos[indice_minimo_global][-1]
        genotipo = self.optimos[indice_minimo_global][:-1]
        print("Evaluación óptima del algoritmo :: {min}, genotipo :: {gen}, generacion :: {generacion}".format(min = fenotipo, gen = genotipo, generacion = indice_minimo_global), end="\n\n")
        #self.convergencia_optimos()
        print("Total : --- %s seconds ---" % (time.time() - start_time_genetico))


# Ejemplo del algoritmo genético
tam_pob = 750
radio_inicial = 20
n_dim = 2

poblacion = np.random.uniform(-radio_inicial, radio_inicial, (tam_pob, n_dim))
# Parámetros del genético
gen = 1000
coef_mutacion = random.random()
coef_cruza  = random.random()
F = f.rast
alfa = random.random()
posicion = 5
disparos = 10
metodo = "minimizar"

ag = AlgoritmoGenetico(poblacion, gen, coef_mutacion, coef_cruza, F, alfa, posicion, disparos, "red", "AG-0", metodo)
ag.main()
ag.convergencia_optimos()
