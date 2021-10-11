'''
Implementación de una mochila para el problema de la Mochila (optimización).

Materia de Cómputo Evolutivo, 5to semestre, Facultad de Ciencias, UNAM.

@author Diego Velázquez Trejo

'''
import random

class Mochila:

    # Constructor de la clase
    def __init__(self, conjunto_objetos, informacion, capacidad):
        self.informacion = informacion      # Contiene los valores y pesos de todo el conjunto de objetos
        self.conjunto = conjunto_objetos    # Conjunto de objetos para la mochila
        self.capacidad = capacidad
        self.peso = self.calcula_peso()          # Se tiene que calcular de manera directa
        self.valor = self.calcula_valor()        # Se tiene que calcular de manera directa

        self.promedio_pesos = self.calcula_promedio(1) # Calcular junto con todo el conjunto de información
        self.promedio_valores = self.calcula_promedio(0) # Calcular junto con todo el conjunto de información

    # Función para extraer un elemento de la mochila
    def obtiene_elemento(self):
        elemento = self.conjunto.pop()      # Ver si es necesario una función shuffle para el set
        # Tenemos que actualizar los pesos y valores de la mochila
        valor_elemento = self.informacion[elemento][0]
        peso_elemento = self.informacion[elemento][1]

        self.peso = self.peso - peso_elemento
        self.valor= self.valor - valor_elemento

        return elemento

    # Función para insertar un elemento en la mochila
    def agrega_elemento(self, elemento):
        # Tenemos que ver si el peso de la mochila es válido junto con el nuevo elemento
        valor_elemento = self.informacion[elemento][0]
        peso_elemento = self.informacion[elemento][1]

        if(self.peso + peso_elemento <= capacidad):
            self.conjunto.add(elemento)

            # Tenemos que actualizar los pesos y valores de la mochila
            self.valor += valor_elemento
            self.peso += peso_elemento

            return True
        else:
            return False

    # Función para mostrar los elementos de la mochila
    def toString(self):
        return str(self.conjunto)

    # Función para calcular el peso de la mochila
    def calcula_peso(self):
        peso = 0.0
        for elemento in self.conjunto:
            peso += self.informacion[elemento][1]
        return peso

    # Función para calcular el valor de la mochila
    def calcula_valor(self):
        valor = 0.0
        for elemento in self.conjunto:
            valor += self.informacion[elemento][0]
        return valor

    # Función para calcular el promedio de alguna de las variables del conjunto de información
    def calcula_promedio(self, numero):
        prom = 0.0
        for elemento in self.informacion:
            prom += self.informacion[elemento][numero]
        return prom/len(self.informacion)

    # Función objetivo a optimizar (utiliza los pesos y valores de la clase y no tiene que reelaborar cálculos)
