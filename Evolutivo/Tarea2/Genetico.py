'''
Clase que modela un Algoritmo Genético
@author: Diego Arturo Velázquez Trejo
Materia de Cómputo Evolutivo, Facultad de Ciencias, UNAM.
Octubre 31/2021

Representación binaria
Selección de padres: ruleta
Cruza: intermedia
Escalamiento: sigma
Mutación: Inversión de un bit
Selección: coma

'''
import random
import numpy as np
import math
import pandas as pd

random.seed(10)

#np.set_printoptions(formatter={'float': '{0: 0.3f}'.format})

# Función objetivo   Df = [-500, 500] X [-500, 500]
def f(X):
    return  418.9829*2 - X[0]*math.sin(math.sqrt(abs(X[0]))) - X[1]*math.sin(math.sqrt(abs(X[1])))

# Función que toma f y la aplica a un arreglo
def F(fenotipos):
    evaluaciones = np.zeros(len(fenotipos))
    for i in range(0, len(evaluaciones)):
        evaluaciones[i] = f(fenotipos[i])
    return evaluaciones

'''
Representación de los elementos de la población será binaria:

[b1 b2 b3 b4 b5 b6 b7 b8 b9 b10]

Pregunta del millón: ¿Qué pasa cuando la función de decodificación del genotipo es una función determinista o no determinista?

'''
# Función que regresa el fenotipo. Observación: la longitud del cromosoma es de 9 bits
# Función de decodificación NO DETERMINISTA
'''
máx{fg} cuando cromosoma = [1,1,1,1,1,1,1,1,1], ui = 1 es 500 y mínimo cuando cromosoma = [0,0,0,0,0,0,0,0,0] y ui = 0 es -500
'''
def fg_ND(cromosoma, pinv=random.random()):
    #print(cromosoma)
    fen = 1
    i = 1
    for j in range(0,6):
        fen *= math.pow(i, cromosoma[j])
        i+=1
    u1 = 60 * random.random() * cromosoma[i-1]
    u2 = 100 * random.random() * cromosoma[i]
    u3 = 120 * random.random() * cromosoma[i+1]
    u4 = -1 if(random.random() < pinv) else 1
    return ((fen + u1 + u2 + u3) - 500) * u4

# Función que regresa el fenotipo. Observación: la longitud del cromosoma es de 9 bits
# Función de decodificación  DETERMINISTA
'''
Vamos a utilizar la siguiente sucesión de números:
                                        Parte entera            Parte decimal
        f(b1, b2, b3, ..., bn ) = 2 * sum_{i=0}^n 2**i * bi + 2/sum_{i=0}^n 2**i

'''
def fg_D(cromosoma):
    #print(cromosoma)
    fen = 0
    i = 0
    for bit in cromosoma:
        fen += (2**i) * bit
        i += 1
    decimal = 0 if(fen == 0) else 1/fen
    res = 2 * (fen + decimal)
    fx = 1000 if(res > 1000) else res
    return res - 500


# Función para obtener los genotipos
def calcula_fenotipos(poblacion):
    fenotipos_determinista = np.zeros((len(poblacion),2))
    fenotipos_No_determinista = np.zeros((len(poblacion),2))
    division = int(len(poblacion[1])/2)

    for i in range(0,len(poblacion)):

        x1 = poblacion[i,0:division]
        x2 = poblacion[i,division:]

        fenotipos_determinista[i][0] = fg_D(x1)
        fenotipos_determinista[i][1] = fg_D(x2)

        fenotipos_No_determinista[i][0] = fg_ND(x1)
        fenotipos_No_determinista[i][1] = fg_ND(x2)

    return fenotipos_No_determinista

'''
    Función para generar la población inicial: Va a ser una matriz de n * 18, en donde las primeras 9 columnas corresponden a X1 y las 9 columnas restantes a X2.
    n es el tamaño de la población inicial, tcrom el tamaño del cromosoma.

    Ejemplo:

    array([[1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0],
       [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0],
       [1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
       [0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0]])

'''
def genera_poblacion_inicial(n, tcrom=18):
    return np.random.randint(2, size=[n, tcrom])


'''
Función para inicializar todos los elementos del algoritmo genético
'''
def inicializar(F, n, tcrom):
    poblacion = genera_poblacion_inicial(n, tcrom)
    fenotipos_determinista = calcula_fenotipos(poblacion)
    aptitudes_determinista = F(fenotipos_determinista)
    #aptitudes_No_determinista = F(fenotipos_No_determinista)

    return poblacion, fenotipos_determinista, aptitudes_determinista

# Función para realizar la selección por medio del método de la ruleta
def seleccion_ruleta(aptitudes, n):
    p = aptitudes/sum(aptitudes)
    cp= np.cumsum(p)
    print(p)
    print(cp)
    padres = np.zeros(n)
    for i in range(n):
        X = np.random.uniform()
        padres[i] = np.argwhere(cp > X)[0]
    return padres.astype(int)

# Función cruza intermedia para la representación binaria
def cruza_un_punto(genotipo, idx, pc):
    hijos_genotipo = np.zeros(np.shape(genotipo))
    k = 0
    for i, j in zip(idx[::2], idx[1::2]):
        flip = np.random.uniform()<=pc
        if flip:
            punto_cruza = np.random.randint(0, len(genotipo[0]))
            hijos_genotipo[k] = np.concatenate((genotipo[i,0:punto_cruza], genotipo[j,punto_cruza:]))
            hijos_genotipo[k+1] = np.concatenate((genotipo[j, 0:punto_cruza], genotipo[i, punto_cruza:]))
        else:
            hijos_genotipo[k] = np.copy(genotipo[i])
            hijos_genotipo[k + 1] = np.copy(genotipo[j])
        k += 2
    return hijos_genotipo

# Función de cruza en el punto medio
def cruza_medio_punto(genotipo, idx):
    hijos_genotipo = np.zeros(np.shape(genotipo))
    k = 0
    punto_cruza = int(len(genotipo[0])/2)
    for i, j in zip(idx[::2], idx[1::2]):

        hijos_genotipo[k] = np.concatenate((genotipo[i,0:punto_cruza], genotipo[j,punto_cruza:]))
        hijos_genotipo[k+1] = np.concatenate((genotipo[j, 0:punto_cruza], genotipo[i, punto_cruza:]))

        k += 2

    #print(hijos_genotipo)
    return hijos_genotipo

# Función de mutación: se encarga de modificar la estructura de un elemento de la población para agregar variabilidad
def mutacion_inversion_bit(genotipo, pm):
    cantidad_mutaciones = 0
    for i in range(len(genotipo)):
        for j in range(len(genotipo[i])):
            prob = np.random.uniform()<= pm
            if prob:
                genotipo[i,j] = 0 if(genotipo[i, j] == 1) else 1
                cantidad_mutaciones += 1
    return genotipo, cantidad_mutaciones

# Función para realizar la selección de la nueva población
def seleccion_coma(genotipos, fenotipos, aptitudes, hijos_genotipo, hijos_fenotipo, hijos_aptitudes):
    return hijos_genotipo, hijos_fenotipo, hijos_aptitudes


def estadisticas(generacion, genotipos, fenotipos, aptitudes, hijos_genotipo, hijos_fenotipo, hijos_aptitudes, padres, cantidad_mutaciones):
    stri = ""
    stri += '---------------------------------------------------------\n'
    stri += 'Generación:' + str(generacion)+"\n"
    stri += 'Población:\n'+str(np.concatenate((np.arange(len(aptitudes)).reshape(-1,1), genotipos, fenotipos, aptitudes.reshape(-1, 1), aptitudes.reshape(-1, 1)/np.sum(aptitudes)), 1))+"\n"
    stri += 'Padres:'+ str(padres)+"\n"
    stri +='frecuencia de padres:'+ str(np.bincount(padres))+"\n"
    stri += 'Cantidad de mutaciones efectuadas: '+str(cantidad_mutaciones)+"\n"
    stri += 'Hijos:\n'+ str(np.concatenate((np.arange(len(aptitudes)).reshape(-1, 1), hijos_genotipo, hijos_fenotipo, hijos_aptitudes.reshape(-1, 1), hijos_aptitudes.reshape(-1, 1)/np.sum(hijos_aptitudes)), 1))+"\n"
    stri += 'Desempeño en línea para t=1: '+ str(np.mean(aptitudes))+"\n"
    stri += 'Desempeño fuera de línea para t=1: '+ str(np.max(aptitudes))+"\n"
    stri += 'Mejor individuo en la generación: '+ str(np.argmax(aptitudes))+"\n"
    stri += 'Mejor hijo en la generación: '+ str(np.argmax(hijos_aptitudes))+"\n"
    stri += 'Cadena del mejor hijo: '+str(hijos_genotipo[np.argmax(hijos_aptitudes)])+"\n"
    stri += 'Fenotipo del mejor hijo: '+str(hijos_fenotipo[np.argmax(hijos_aptitudes)]) +"\n"
    stri += 'Evaluación del mejor hijo: '+str(hijos_aptitudes[np.argmax(hijos_aptitudes)]) + "\n"
    print(stri)
    return stri


def EA(F, pc, pm, nvars, npop, ngen):
    estad = ""
    #Inicialización de los arreglos:
    bg = np.zeros((ngen, nvars))
    bf = np.zeros((ngen, 2))
    ba = np.zeros((ngen, 1))
    genotipos, fenotipos, aptitudes = inicializar(F, npop, nvars)
    # Ejecutamos tantas veces como generaciones tengamos
    for i in range(ngen):
        #Selección de padres
        idx = seleccion_ruleta(aptitudes, npop)
        #Cruza
        hijos_genotipo = cruza_medio_punto(genotipos, idx)
        #Mutación
        hijos_genotipo, cantidad_mutaciones = mutacion_inversion_bit(hijos_genotipo, pm)
        hijos_fenotipo = calcula_fenotipos(hijos_genotipo)
        hijos_aptitudes= F(hijos_genotipo)

        # Estadisticas
        estad += estadisticas(i, genotipos, fenotipos, aptitudes, hijos_genotipo, hijos_fenotipo, hijos_aptitudes, idx, cantidad_mutaciones)

        #Mejor individuo
        idx_best = np.argmax(aptitudes)
        b_gen = np.copy(genotipos[idx_best])
        b_fen = np.copy(fenotipos[idx_best])
        b_apt = np.copy(aptitudes[idx_best])
        ba[i] = np.copy(aptitudes[idx_best])
        bg[i] = np.copy(genotipos[idx_best])
        bf[i] = np.copy(fenotipos[idx_best])

        #Selección de siguiente generación
        genotipos, fenotipos, aptitudes = seleccion_coma(genotipos, fenotipos, aptitudes, hijos_genotipo, hijos_fenotipo, hijos_aptitudes)

        #Elitismo
        idx = np.argmax(aptitudes)
        genotipos[idx] = b_gen
        fenotipos[idx] = b_fen
        aptitudes[idx] = b_apt

    #Fin ciclo

    mejores_aptitudes = []
    for aptitud in ba:
        mejores_aptitudes.append(aptitud[0])

    mejores_genotipos_tabla = []
    for bgenotipo in bg:
        cad = ""
        for j in range(0, len(bgenotipo)):
            cad += str(int(bgenotipo[j]))
        mejores_genotipos_tabla.append(cad)

    mejores_fenotipos_tabla = []
    for bfenotipo in bf:
        cad = " {x1}, {x2} ".format(x1 = bfenotipo[0], x2 = bfenotipo[1])
        mejores_fenotipos_tabla.append(cad)

    df = {"Mejores aptitudes":mejores_aptitudes, "Mejores genotipos":mejores_genotipos_tabla, "Mejores fenotipos":mejores_fenotipos_tabla}
    df = pd.DataFrame(df)
    print(df.head())
    print(df.describe())
    estad += str(df.head()) +"\n"
    estad += str(df.describe())

    #print('Tabla de mejores aptitudes:\n', ba)
    #print('Tabla de mejores genotipos:\n', bg)
    #print('Tabla de mejores fenotipos:\n', bf)
    #Regresar mejor solución
    idx = np.argmax(aptitudes)
    return genotipos[idx], fenotipos[idx], aptitudes[idx], estad, ba


nvars= 18
pm = 0.01
pc = 0.7
npop = 50
ngen = 500

mejores_aptitudes = []

#np.set_printoptions(formatter={'float': '{0: 0.3f}'.format})
for i in range(1, 21):
    genotipos, fenotipos, aptitudes, estad, ba = EA(F,pc, pm, nvars, npop, ngen)
    mejores_aptitudes.append(ba[np.argmax(ba)])

    #Guardamos en un .txt toda la ejecución a mano
    #arch = open("Estadisticas_No_Determinista/estadisticas{j}.txt".format(j = i), "a")
    #arch.write(estad)
    #arch.close()

# Generaremos el gráfico de convergencia
from matplotlib import pyplot as plt
plt.plot(mejores_aptitudes)
plt.show()

'''
Parámetros:

nvars= 18  # Por la codificación que se diseñó
pm = 0.01
pc = 0.7
npop = 50
ngen = 500

'''
