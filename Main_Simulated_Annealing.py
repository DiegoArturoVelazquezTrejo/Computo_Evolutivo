from simulated_annealing import Simulated_Annealing
from leyendo_datos_mochila import CONJUNTO_OBJETOS
from Mochila import Mochila
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

print(CONJUNTO_OBJETOS)

conjunto_identificadores = set()
for i in range(1, len(CONJUNTO_OBJETOS)+1):
    conjunto_identificadores.add(str(i))

print(conjunto_identificadores)    # Contiene los identificadores de los objetos

MT = Mochila(conjunto_identificadores, CONJUNTO_OBJETOS, 5000) # Mochila Total, no es válida, es para una prueba

# Necesito una función para generar una mochila inicial VÁLIDA
def genera_mochila_valida():
    pass

'''
Observaciones:
Para ver qué mochila es más óptima, si M0 o M1, entonces M1 tiene que ser M0 con otro elemento

'''
