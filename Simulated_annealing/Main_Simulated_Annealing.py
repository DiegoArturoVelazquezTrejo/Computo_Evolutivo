'''
Programa Main para la optimización del problema de la mochila
Materia de Cómputo Evolutivo, 5to semestre, Facultad de Ciencias, UNAM.
@author Diego Velázquez Trejo
'''
from simulated_annealing import Simulated_Annealing
from leyendo_datos_mochila import CONJUNTO_OBJETOS
from leyendo_datos_mochila import CAPACIDAD
from leyendo_datos_mochila import OBJETOS_TOTALES
from Mochila import Mochila
import random

# Función que genera una copia del conjunto
def copia(conjunto):
    print(conjunto)
    n_conjunto = set()
    for el in conjunto:
        n_conjunto.add(el)
    return n_conjunto


# Variables que definiremos de acuerdo al problema
T   = 350000
IT0 = 1
I   = 1000
BETTA = 1/10

# Necesito una estructura de datos para albergar los vecinos (YA)
CONJUNTO_OBJETOS # Contiene el identificador del objeto junto con su valor y peso

CONJUNTO_OBJETOS

conjunto_identificadores = set()
for i in range(1, len(CONJUNTO_OBJETOS)+1):
    conjunto_identificadores.add(str(i))

conjunto_identificadores    # Contiene los identificadores de los objetos

#MT = Mochila(conjunto_identificadores, CONJUNTO_OBJETOS, CAPACIDAD)

#print(MT.toString())

# Necesito una función para generar una mochila inicial VÁLIDA
def genera_mochila_valida(informacion, capacidad):
    # Copia del conjunto
    M0 = Mochila(set(), informacion, capacidad)
    #copia_informacion = copia(informacion)
    el = conjunto_identificadores.pop()
    while(M0.agrega_elemento(el) and len(conjunto_identificadores) > 0):
        el = conjunto_identificadores.pop()
    conjunto_identificadores.add(el)
    return M0

CONJUNTO_OBJETOS

conjunto_identificadores # Va a tener todos los objetos que no se encuentran en la mochila, mientras que la mochila tendrá los otros

M0 = genera_mochila_valida(CONJUNTO_OBJETOS, CAPACIDAD)

# Función para obtener un elemento de la población de manera aleatoria
def obtiene_elemento_aleatorio(identificadores):
    lista = list(identificadores)
    random.shuffle(lista)
    elemento = lista.pop()
    identificadores.remove(elemento)
    return elemento

# Necesito una función continua para ir decreciendo la temperatura
def decrece_temperatura(T):
    return T - BETTA * T


# Función objetivo a optimizar (utiliza los pesos y valores de la clase y no tiene que reelaborar cálculos)
'''
Necesitamos que la función que regrese un número positivo en caso en que la propuesta a nueva mochila sea mejor, un número negativo en caso opuesto.
Observaciones:
Para ver qué mochila es más óptima, si M0 o M1, entonces M1 tiene que ser M0 con otro elemento
'''
# Función objetivo
def F(M):
    # Podemos usar el hecho de que el peso no haya aumentado más que el peso que tenía mas el promedio de pesos
    return M.valor

# Función que ontenga los valores (valor, peso) para una nueva mochila

# Vamos a extraer dos elementos de la mochila e insertar dos elementos

def FS(est, V):
    i = 0
    M0 = est # Mochila actual (estado en la iésima iteración)
    # Utilizaremos la función de obtiene_elemento_aleatorio y agregarlo a la mochila
    copia = M0.copia()

    elemento_eliminado_1 = copia.obtiene_elemento()
    elemento_eliminado_2 = copia.obtiene_elemento()

    for i in range(0, 3):
        elemento_nuevo = str(random.randint(1, OBJETOS_TOTALES))
        while(copia.verifica_elemento(elemento_nuevo) == True):
            elemento_nuevo = str(random.randint(1, OBJETOS_TOTALES))
        copia.agrega_elemento(elemento_nuevo)

    return copia

MOptima, prom, objeto_maximo, objeto_minimo = Simulated_Annealing(T, conjunto_identificadores, F, FS, M0, IT0, decrece_temperatura, I, 1, "maximizar")

# Resultados
print("\n\n#### RESULTADOS ####")
print("Valor de la mochila inicial: ")
print(M0.toString())
print("Resultado del algoritmo SA: ")
print(MOptima.toString())
print("Promedio de las mochilas que se generaron en las iteraciones: ", end="")
print(prom)
print("Objeto máximo en las iteraciones: ")
print(objeto_maximo.toString())
print("Objeto mínimo en las iteraciones: ")
print(objeto_minimo.toString())