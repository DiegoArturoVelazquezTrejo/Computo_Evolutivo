'''
Funciones objetivo parciales correspondientes al problema Multiobjetivo 
'''
import math

# Constante presupuestal 
K = 1500

# Funciones parciales de la ecuación resultante de los multiplicadores de Lagrange 

# vector = (  x , y , z, u, l )

def parcial_x(vector): 
    x = vector[0]
    l = vector[4]
    try: 
        a =  (-8/5)*math.pow(x, -3)+2 * x - (14/9)*math.pow(x, -2) - l
        return abs(a) 
    except: 
        return None

def parcial_y(vector): 
    y = vector[1]
    l = vector[4]
    return abs((2/5)*y + (1/10) - l)

def parcial_z(vector):
    z = vector[2]
    l = vector[4]
    try:  
        a =  (-4/5) * math.pow(z, -2) - l  
        return abs(a)
    except: 
        return None

def parcial_u(vector):
    u = vector[3]
    l = vector[4]
    try:  
        a=  (2/9) * ((3*math.pow(u, 3)-3-3*math.pow(u, 2)*(3*u+1))/(math.pow(math.pow(u, 3)-1, 2))) - l
        return abs(a)
    except: 
        return None 

# Función que incorpora el lambda de la ecuación de Lagrange 
def parcial_l(vector):
    x = vector[0]
    y = vector[1]
    z = vector[2]
    u = vector[3]
    return abs(-(x+y+z+u - K))

# Diccionario que podemos exportar para que otros archivos hagan uso de las funciones
F = {"dx":parcial_x, "dy":parcial_y, "dz":parcial_z, "du":parcial_u, "dl":parcial_l}

