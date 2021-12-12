# Biblioteca con funciones matemáticas
import math
# Biblioteca con funciones relativas a procesos aleatorios
import random
# Biblioteca con funciones para arreglos
import numpy as np

# Método para generar una serie de disparos aleatorios
'''
@param: Vector mínimo/máximo de un cluster K-ésimo (Ki), es una lista de orden n
@param: F función objetivo
@param: Radio de disparo
@param: Cantidad de disparos a realizar
@param: Bandera para indicar si se desea maximizar o minimizar
@return: tupla (Vector ganador del método, Vector de diferencias)
'''
def shooting_method(v_critico, F, radio, N, bandera="minimizar"):
    #print(radio)
    v_critico = np.array(v_critico)
    disparos = np.random.uniform(-radio, radio, (N, len(v_critico)))
    trayectos = np.array([v_critico for i in range(0, N)])
    nuevos_vectores = disparos + trayectos
    evaluaciones = np.array([F(nuevos_vectores[i]) for i in range(0, N)])
    optimos = np.argwhere(evaluaciones >= F(v_critico)) if(bandera == "maximizar") else np.argwhere(evaluaciones <= F(v_critico))
    #print(optimos)
    # Vamos a seleccionar un elemento de los que optimizan al punto minimo o máximo
    if(len(optimos) != 0):
        #print("EXITO :: OBTENIENDO NUEVA TRAYECTORIA")
        index = random.choice(optimos)[0]
        #print(len(disparos[index]))
        #print(disparos[index])
        return nuevos_vectores[index], disparos[index]
    else:
        #print("FAIL :: OBTENIENDO NUEVA TRAYECTORIA")
        return v_critico, np.zeros(len(v_critico))

# Método para actualizar todos los elementos de una población de un cluster K-ésimo
'''
@param: Elementos de la población de un cluster
@param: Vector de diferencias
@return: Vectores trasladados
'''
def trasladar_vectores(P, v_dif):
    vectores_diferencias = []
    for i in range(len(P)):
        vectores_diferencias.append(v_dif)
    vectores_diferencias = np.array(vectores_diferencias)
    #print(vectores_diferencias)
    return P + vectores_diferencias

'''
Para el genético:

Generamos una población de 1000 individuos, por ejemplo,
Aplicaremos el K-Means para hallar cierta cantidad de centroides
Ejecutaremos hilo sobre cada centroide para ejecutar el siguiente algoritmo:


Repetir las generaciones que se desee:

    Implementación del algoritmo Memético para elementos de una población continua.
    Propuesta de algoritmo de mejoramiento: Shooting Method Uniforme-Beta

    Observación: Cada cluster de elementos va a tener un Archivo que tenga registro del mejor elemento para cada cluster.

    1. Para cada cluester, hallar el elemento máximo o mínimo, según se desee. Supongamos, spg, que nos tomamos en mínimo
    ya que deseamos minimizar.
    2. Tomar el mínimo y vamos a empezar el método del disparo:

        Para el cluster Ki, sea x_min el mínimo dentro del cluster:

        beta -> radio de disparo, este disparo vamos a considerarlo como

        # Sea x* el centro del cluster y sea x_min el elemento que mininiza la función:

        # Tres opciones para beta ->   VAMOS A PROBAR CON CADA BETA Y ESTUDIAR LA CONVERGENCIA HACIA LAS SOLUCIONES ÓPTIMAS

            beta_1 = Norma [ abs(  x*  - x_min     ) ]

            beta_2 = abs( f(x*  - x_min)  )

            beta_3 = max{ beta_1, beta_2  }

        For i = 0 : cantidad_disparos

            // Generamos el disparo
            di = np.random.uniform(-beta, beta, n)

            if(  F(x_min + di) < F(x_min))

                x_min = x_min + di

        end

        # Después de generar una cierta cantidad de disparos, pudimos hallar, o no, una trayectoria a un nuevo punto
        que minimiza aún más a los elementos dentro del cluster

        # Trasladaremos el cluster hacia el nuevo x_min
        Sea d_n la distancia que se desplazó el x_min inicial hacia su valor final, entonces:

        For i = 0 : cantidad_de_elementos_en_cluster

            # Trasladaremos cada vector

            K[i] = K[i] + d_n

        end

        # Volvemos a evaluar los nuevos elementos de la población y aquellos que tendieron a mejorar de mejor manera, son aquellos que se reproducirán:

        Diferencias = abs(  F(K elementos antes del traslado) - F(K elementos después del traslado )  )

        Aquellos que tengan una mayor distancia, son los que se van a reproducir con el mejor elemento del cluster.
        Es decir, obtenemos los indice_max(Diferencias) y serán esos los elementos que vamos a reproducir

        # Después de reproducir, vamos a mutar los elementos

    '''
