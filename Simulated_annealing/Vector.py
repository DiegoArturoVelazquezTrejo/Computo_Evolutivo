'''
Implementación de un vector para el problema de la función (optimización).

Materia de Cómputo Evolutivo, 5to semestre, Facultad de Ciencias, UNAM.

@author Diego Velázquez Trejo

'''
import random
import math

class Vector:

    # Constructor de la clase
    def __init__(self, X, Y):

        intervalo_X = [-5, math.inf]
        intervalo_Y = [-math.inf, 5]
        self.radio_epsilon = 0.1

        self.X = X # Valor en X
        self.Y = Y # Valor Y = F(x)

        # Información sobre el intervalo en el que se encuentran nuestras variables
        self.infimo_Y = intervalo_Y[0]
        self.supremo_Y = intervalo_Y[1]

        self.infimo_X = intervalo_X[0]
        self.supremo_X = intervalo_X[1]

        self.valor = math.pow(self.X, 2) + math.pow(self.Y, 2)

    # Función para actualizar los elementos del vector
    def actualiza(self, X, Y):
        if((self.infimo_X <= X and X <= self.supremo_X) and (self.infimo_Y <= Y and Y <= self.supremo_Y)):
            self.X = X
            self.Y = Y
            self.F()
            return True
        else:
            return False

    # Función para generar una copia del vector
    def copia(self):
        return Vector(self.X, self.Y)

    # Función para desplegar el vector
    def toString(self):
        return "({x}, {y}), valor = {v}".format(x = self.X, y = self.Y, v = self.valor)

    # Función para determinar el valor de un vector
    def F(self):
        '''
        Función objetivo:

            f(x_1,x_2 )=x_1^2+x_2^2, -5≤x_1,x_2≤5
        '''
        self.valor =  math.pow(self.X, 2) + math.pow(self.Y, 2)
