'''
Funciones objetivo para la tarea 3
'''
import math

# Rastrigin Function
def rast(X):
    d = len(X)
    sum = 0
    for i in range(0, d):
        sum += math.pow(X[i], 2) - 10 * math.cos(2 * math.pi * X[i])
    return 10 * d + sum

# Ackley Function
def ackley(X, a=5, b=2, c=1):
    d = len(X)
    xi_2 = 0
    cos = 0
    for i in range(0, d):
        xi_2 += X[i] * X[i]
        cos  += math.cos(c * X[i])
    return -a * math.exp(-b * math.sqrt(1/d * xi_2)) - math.exp(1/d * cos) + a + math.e

# Rosenbrock Function
def rosenbrock(X):
    d = len(X)
    sum = 0
    for i in range(0, d-1):
        sum += 100 * math.pow(X[i+1] - X[i]*X[i], 2) + math.pow(X[i]-1, 2)
    return sum

# Eggholder Function Está definida en R^2
def eggholder(X):
    return -(X[1] + 47) * math.sin(math.sqrt(abs(X[1] + X[0]/2 + 47))) - X[0] * math.sin(math.sqrt(abs(X[0] - X[1] - 47)))

# Easom Function Está definida en R^2
def eason(X):
    return  -math.cos(X[0])*math.cos(X[1])*math.exp(-math.pow(X[0]-math.pi, 2)-math.pow(X[1]-math.pi, 2))

# Diccionario que podemos exportar para que otros archivos hagan uso de las funciones
F = {"rast":rast, "ackley":ackley, "rosenbrock":rosenbrock, "eggholder":eggholder, "eason":eason}
