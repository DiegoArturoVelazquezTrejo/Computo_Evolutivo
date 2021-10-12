from simulated_annealing import Simulated_Annealing
from leyendo_datos_mochila import CONJUNTO_OBJETOS
from leyendo_datos_mochila import CAPACIDAD
from Mochila import Mochila

# Función que genera una copia del conjunto
def copia(conjunto):
    print(conjunto)
    n_conjunto = set()
    for el in conjunto:
        n_conjunto.add(el)
    return n_conjunto


# Variables que definiremos de acuerdo al problema
T   = 0
V   = 0
F   = 0
Fs  = 0
I0  = 0
IT0 = 0
E   = 0
I   = 0

# Necesito una estructura de datos para albergar los vecinos (YA)
CONJUNTO_OBJETOS # Contiene el identificador del objeto junto con su valor y peso

CONJUNTO_OBJETOS

conjunto_identificadores = set()
for i in range(1, len(CONJUNTO_OBJETOS)+1):
    conjunto_identificadores.add(str(i))

conjunto_identificadores    # Contiene los identificadores de los objetos

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
def obtiene_elemento_aleatorio():
    return conjunto_identificadores.pop()

# Necesito una función continua para ir decreciendo la temperatura
def decrece_temperatura(T, betta):
    return T - betta * T
'''
Observaciones:
Para ver qué mochila es más óptima, si M0 o M1, entonces M1 tiene que ser M0 con otro elemento

'''
