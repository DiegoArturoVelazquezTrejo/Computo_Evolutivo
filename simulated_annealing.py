'''
Implementación de una heurística para la optimización de problemas.

Simulated Annealing (Recocido Simulado)
Materia de Cómputo Evolutivo, 5to semestre, Facultad de Ciencias, UNAM.

@author Diego Velázquez Trejo

Sobre el algoritmo, consultar: https://www.sciencedirect.com/topics/engineering/simulated-annealing-algorithm

'''

# Bibliotecas que usaremos
import random
import math
'''
Método para obtener una variable aleatoria normal con media 0 y varianza 1
@return Número real aleatorio en el intervalo [0, 1]
'''
def Nom():
    return random.random()

'''
Método de recocido simulado
@param: T (temperatura) inicial
@param: v Estructura de datos con los vecinos
@param: F Función a (minimizar o maximizar) según se indique, es la función objetivo
@param: Fs Función que selecciona un elemento vecino a una solución del conjunto de posibles soluciones
@param: I0 Estado inicial del algoritmo
@param: IT0 la cota inferior para la temperatura, en caso de que la temperatura sea menor, el algoritmo termina
@param: E Regla con la que se actualizará la temperatura del sistema
@param: I Número de iteraciones máximo
@param: tec ("minimizar") en caso que se desee minimizar la función objetivo, ("maximizar") en caso contrario

@return: Solución que minimiza o maximiza la función objetivo (según se especifique)
'''
def Simulated_Annealing(T, V, F, Fs, I0, IT0, E, I, tec= "minimizar"):
    act = I0                    # Vamos a obtener un estado inicial
    iteracion = 0               # Variable que indicará el número de iteraciones que el algoritmo realiza
    infimo_temperaturas = IT0   # Máxima cota inferior de las temperaturas
    while (T > infimo_temperaturas or iteracion < I):
        est = act
        # Alteración (propuesta) al algoritmo (Vamos a ir iterando más veces conforme la temperatura sea mayor)
        for i in range(0, int(T)):

            sig = Fs(est, V)   # La función nos seleccionará un elemento del conjunto de vecinos dado un elemento que ya tengamos

            delta_E = F(sig) - F(est) # Obtenemos la diferencia numérica entre el elemento que tenemos y el vecino del mismo
            # Según se desee maximizar o minimizar le función objetivo
            if(tec == "minimizar"):         # Caso en donde se desea minimizar la función objetivo
                if(delta_E < 0):
                    est = sig               # sig minimiza a la función con respecto a act, por lo que cambiamos el valor que tenemos
                else:
                    # Vamos a aceptar el nuevo estado con base en una función de probabilidad
                    q = min(1, math.pow(math.e, -delta_E/T))
                    if(Nom() < q):
                        est = sig
            else:                           # Caso en donde se desea maximizar la función objetivo
                if(delta_E > 0):
                    est = sig               # sig maximiza a la función con respecto a act, por lo que cambiamos el valor que tenemos
                else:
                    # vmos a aceptar el nuevo estado con base en una función de probabilidad
                    q = min(1, math.pow(math.e, -delta_E/T))
                    if(Nom() < q):
                        est = sig
        iteracion += 1     #Aumentamos el número de iteraciones
        act = est
        T = E(T)           # Actualizamos la temperatura dada la regla que se le ingrese como parámetro, es una función decreciente ya que queremos T -> 0
    return act
