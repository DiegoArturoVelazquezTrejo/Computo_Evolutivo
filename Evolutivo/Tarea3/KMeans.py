'''
Clase para generar K-clusters utilizando el algoritmo de k-Means
'''
# Biblioteca con funciones para arreglos
import numpy as np
# Biblioteca con funciones matemáticas
import math
# Biblioteca con funciones reativas a procesos aleatorios
import random
# Biblioteca para trabajar con funciones del sistema
import sys
# Biblioteca para graficar
from matplotlib import pyplot as plt
'''
Clase para agrupación de elementos de una población con base en el algoritmo de k-KMeans
@author: Diego Arturo Velázquez Trejo
'''
class KMeans:
    '''
    @param: X población matriz de vectores
    @param: k (int), número de clusters que se desea generar
    '''
    def __init__(self, X, k, iter):
        # Elementos de la población
        self.X = X
        # Cantidad de clusters que se desea obtener
        self.k = k
        # Clusters
        self.clusters = {}
        self.centroides = {}
        self.cantidad_elementos = {}
        # Cantidad de iteraciones para el método
        self.iter = iter
        self.cond = False
        # Centroides iniciales
        if(k > len(X)):
            print("Ha ocurrido un error de tamaño de población con cantidad de clusters...")
            sys.exit()
        ie = 0
        indices_iniciales = np.random.choice(len(X), k, replace=False)

        for i in range(0, len(indices_iniciales)):
            self.centroides["centroide-{ies}".format(ies = i)] = X[i]
            self.clusters["centroide-{ies}".format(ies = i)] = np.zeros((len(X), len(X[i])))
            self.cantidad_elementos["centroide-{ies}".format(ies = i)] = 0

        # Ejecutaremos el algoritmo
        self.main()

    # Método para obtener los promedios de los nuevos centorides y actualizar sus coordenadas
    def actuliza_centroides(self):
        # Vamos a iterar sobre cada centroides
            # Extraer el promedio de para cada entrada
            # Actualizar las coordenadas del centroide
            # Inicializar las listas de elementos
        for centroide in self.centroides:
            # Extraemos la matriz que contiene los elementos agrupados bajo un mismo centroide
            elementos = self.clusters[centroide]
            nueva_coordenada = np.zeros(len(elementos[0]))
            # Vamos a iterar sobre cada coordenada para sacar el promedio
            for i in range(0, len(elementos[0])):
                nueva_coordenada[i] = self.promedio(elementos[:,i], centroide)
            # En caso de no haber concluido con las iteraciones, seguimos actualizando, en caso contrario ya nos quedaremos con la lista final
            if(not self.cond):
                self.centroides[centroide] = nueva_coordenada
                self.clusters[centroide] = np.zeros((len(self.X), len(self.X[0])))
                self.cantidad_elementos[centroide] = 0

    # Método para obtener el promedio
    def promedio(self, X, centroide):
        if(self.cantidad_elementos[centroide] == 0):
            return 0
        return sum(X)/self.cantidad_elementos[centroide]

    # Método para agregar un elemento a un cluster
    def agrega_cluster(self, centroide, elemento):
        indice = self.cantidad_elementos[centroide]
        self.clusters[centroide][indice] = elemento
        self.cantidad_elementos[centroide] += 1

    # Método para calcular la distancia entre dos puntos cualesquiera
    def distancia(self, p1, p2):
        if(len(p1) != len(p2)):
            print("Ha ocurrido un error en el tamaño de vectores :: (Distancia) ")
            sys.exit()
        dist = 0
        for i, j in zip(p1, p2):
            dist += math.pow(i - j, 2)
        return math.sqrt(dist)

    # Método que nos indica el centroide más cercano a un elemento dado (x)
    def centroide_mas_cercano(self, x):
        indice = 0
        distan = [ self.distancia(x, self.centroides[centroide]) for centroide in self.centroides]
        # Vamos a obtener el índice de la mínima distancia
        min = distan[0]
        for i in range(0, len(distan)):
            if(distan[i] < min):
                min = distan[i]
                indice = i
        return "centroide-{ies}".format(ies = indice)

    # Método principal de la clase :: Main
    def main(self):
        for i in range(0, self.iter):
            self.cond = True if i == self.iter -1 else False
            # Para cada elemento de la población vamos a iterar
            for x in self.X:
                '''
                1. Obtener el centroide más cercano
                2. Agregar el elemento x al centroide más cercano (agrega_cluster)
                '''
                centroide = self.centroide_mas_cercano(x)
                self.agrega_cluster(centroide, x)
            # Mandamos a llamar al método de actuliza_centroides
            self.actuliza_centroides()
        for cluster in self.clusters:
            print(self.clusters[cluster])
            print(self.cantidad_elementos)
        self.grafica()

    # Método para obtener los grupos para cada cluster
    # Regresa un arreglo de matrices
    def obtiene_agrupaciones(self):
        resultado = []
        for centroide in self.centroides:
            print("El cluster : {cl} , tiene {k} elementos".format(cl=centroide, k=self.cantidad_elementos[centroide]))
            matriz = self.clusters[centroide][:self.cantidad_elementos[centroide],:]
            resultado.append(matriz)
        return resultado

    # Método para graficar los elementos, suponiendo que son en R^2
    def grafica(self):
        #fig = plt.figure()
        #ax = fig.add_subplot(projection='3d')
        colores = ['green', 'pink', 'blue', 'red', 'yellow', 'black', 'purple','orange','pink','white']
        col = 0
        # Graficamos los elementos de cada cluster por color
        for cluster in self.clusters:
            matriz = self.clusters[cluster]
            x = matriz[:self.cantidad_elementos[cluster],0]
            y = matriz[:self.cantidad_elementos[cluster],1]
            #z = matriz[:self.cantidad_elementos[cluster],2]
            #plt.scatter(x,y,z,c=colores[col])
            plt.scatter(x, y, c = colores[col])
            col+=1
        plt.show()


# Ejemplo de ejecución

tam_pob = 1000
n_iter  = 100
k = 5
radio_inicial = 10
n_dim = 10

poblacion = np.random.uniform(-radio_inicial, radio_inicial, (tam_pob, n_dim))

#fig = plt.figure()
#ax = fig.add_subplot(projection='3d')

x = poblacion[:,0]
y = poblacion[:,1]
#z = poblacion[:,2]
#plt.scatter(x,y,z)
plt.scatter(x, y)
plt.show()
kmeans = KMeans(poblacion, k, n_iter)

# Imprimimos las agrupaciones del algoritmo
agrupaciones = kmeans.obtiene_agrupaciones()
for agrupacion in agrupaciones:
    print(agrupacion)
