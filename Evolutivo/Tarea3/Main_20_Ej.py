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
from Funciones import F
# Biblioteca para graficar
from matplotlib import pyplot as plt
# Biblioteca para trabajar con algoritmos genéticos
import AlgoritmoEvolutivo as ag
# Biblioteca para crear directorios
import os
# Biblioteca para trabajar con datos
import pandas as pd

'''
Script que se dedica a ejecutar 20 veces los algoritmos para obtener las medidas estadísticas por ejecución

'''

# Inicialización de la población:
tam_pob = 800
radio_inicial = 20

# Parámetros del algoritmo K-means
k = 4
n_iter = 70

# Parámetros del genético
gen = 400
coef_mutacion = random.random()
coef_cruza  = random.random()
alfa = random.random()
posicion = 6
disparos = 10
metodo = "minimizar"

# Colores al momento de mostrar gráficas
colores = ['green', 'pink', 'blue', 'red', 'yellow', 'black', 'purple','orange','pink','white']
# Número de iteraciones
iteracion = 0
dimensiones = {"rast":2,"ackley":2, "rosenbrock":2, "eggholder":2, "eason":2, "funcion_tarea2":2}

FUNCIONES = [f.rast, f.ackley, f.rosenbrock, f.eggholder, f.eason, f.funcion_tarea2]
nombres = ["rast", "ackley", "rosenbrock", "eggholder", "eason", "funcion_tarea2"]
indice = 0


informacion = {"funcion":[],"X_min":[], "Y_min":[], "Z_min":[],"X_max":[], "Y_max":[], "Z_max":[], "cantidad_disparos":[], "mean":[], "std":[]}

for funcion in FUNCIONES:
    # Vamos a crear un directorio por función
    #directorio = "Directorio-"+funcion.upper()
    #os.mkdir(directorio)
    # Abriremos el archivo dond escribiremos las estadísticas para la función asociada
    #f= open("./"+directorio+"/informe.txt","w+")
    informe = ""

    # Vamos a iterar 20 veces por función para obtener estadísticas
    F = funcion
    nom_func = nombres[indice]
    indice +=1

    # Tenemos que obtener la dimensión:
    n_dim = dimensiones[nom_func]

    for j in range(0, 20):

        # Generamos la población
        poblacion = np.random.uniform(-radio_inicial, radio_inicial, (tam_pob, n_dim))
        j = 0
        # Aplicación del algoritmo K-Means a la población:
        kmeans = km.KMeans(poblacion, k, n_iter)

        # Obtenemos las agrupaciones del algoritmo y las mandamos a un distinto algoritmo genético
        agrupaciones = kmeans.obtiene_agrupaciones()
        algoritmos_geneticos = []

        for agrupacion in agrupaciones:
            if(len(agrupacion) != 0):
                agen = ag.AlgoritmoGenetico(agrupacion, gen, coef_mutacion, coef_cruza, F, alfa, posicion, disparos, colores[j], "AG-"+str(j) ,metodo)
                algoritmos_geneticos.append(agen)
                j += 1

        # PARALELISMO ::: multithreading
        # Se manda a ejecutar cada algoritmo sobre un hilo:
        # Biblioteca para trabajar con multithreading
        import threading

        def worker(num, agenetico):
            """thread worker function"""
            print('Número de hilo de ejecución: %s' % num)
            agenetico.main()
            agenetico.convergencia_optimos()
            #agenetico.to_csv(num, nom_func)
            return

        # Este será el bloque de código que se ejecute una vez que se segmentó la población inicial
        threads = []

        for i in range(k):
            t = threading.Thread(target=worker, args=(i,algoritmos_geneticos[i],))
            threads.append(t)
            t.start()

        for th in threads:
            th.join()

        #plt.savefig("./"+directorio+"/Gráfica_en_la_iteración_{k}".format(k = iteracion))
        plt.clf()
        iteracion += 1
        cadena = ""
        # Tengo que recuperar el informe para cada algoritmo genético
        for alg_genetico in algoritmos_geneticos:
            # Vamos a extraer la solución final mínima, la máxima, la media, desviación estándar, promedio
            poblacion = alg_genetico.poblacion
            optimos = alg_genetico.optimos
            # Obtenemos mínimo de la población
            indice_minimo_global = np.argmin(optimos[:,-1])
            indice_maximo_global = np.argmax(optimos[:,-1])

            fenotipo_min = optimos[indice_minimo_global][-1]
            genotipo_min = optimos[indice_minimo_global][:-1]

            fenotipo_max = optimos[indice_maximo_global][-1]
            genotipo_max = optimos[indice_maximo_global][:-1]

            cantidad_disparos = alg_genetico.cantidad_disparos

            # Obtenemos media de los óptimos
            media = np.mean(optimos)
            # Obtenemos desviación estándar de los óptimos
            dve   = np.std(optimos)
            # Lo agregamos a un string
            informacion["funcion"].append(nom_func)
            informacion["X_min"].append(genotipo_min[0])
            informacion["Y_min"].append(genotipo_min[1])
            informacion["Z_min"].append(fenotipo_min)
            informacion["X_max"].append(genotipo_max[0])
            informacion["Y_max"].append(genotipo_max[1])
            informacion["Z_max"].append(fenotipo_max)
            informacion["cantidad_disparos"].append(cantidad_disparos)
            informacion["mean"].append(media)
            informacion["std"].append(dve)

            cadena += "Algoritmo: {id} \nGenotipo Máximo: {gmax}, Fenotipo Máximo: {fmax}\nGenotipo Mínimo: {gmin}, Fenotipo Mínimo:{fmin}\nMean:{m}, Desviación Estándar:{sd}\n".format(id=alg_genetico.identificador, gmax = genotipo_max, fmax = fenotipo_max, gmin = genotipo_min, fmin = fenotipo_min, m = media, sd = dve)
            print(cadena)
        informe += cadena+"\n\n"

    # Escribimos el informe en el archivo
    #f.write(informe)

informacion = pd.DataFrame(informacion)
informacion.to_csv("resultados_ejecucion_n2.csv", header = True, index = False)
