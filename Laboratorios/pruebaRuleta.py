import numpy as np

def seleccion_ruleta(aptitudes, n):
    p = aptitudes/sum(aptitudes)
    print(p)
    cp= np.cumsum(p)
    print(cp)
    parents = np.zeros(n)
    for i in range(n):
        X = np.random.uniform()
        print("Aleatorio: {y}".format(y=X))
        parents[i] = np.argwhere(cp > X)[0]
    print(parents.astype(int))
    return parents.astype(int)


aptitudes = np.array([-3313837.5, 192641.7, -130317.3, -840300])
n = 4

print(seleccion_ruleta(aptitudes, n))
