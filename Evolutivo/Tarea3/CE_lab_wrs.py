#Comparativa entre dos algoritmos evolutivos

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
from scipy.stats import wilcoxon
from scipy.stats import ranksums

# Vamos a leer los resultados de la ejecución de un algoritmo que se ejecutó (intermedio) de los 4 hilos y los resultados de la tarea1:
t2 = pd.read_csv("./ResultadosOptimos/resultados-tarea2.csv")['Z'].tolist()
a0 = pd.read_csv("./ResultadosOptimos/funcion_tarea2-0.csv")['Z'].tolist()

s1 = []
s2 = []

for i in range(0,len(t2)):
    s1.append([t2[i]])
    s2.append([a0[i]])

s1 = np.array(s1)
s2 = np.array(s2)

print(np.mean(s1))
print(np.mean(s2))

fig1, ax1 = plt.subplots()
ax1.hist(np.concatenate((s1, s2), 1), bins = 50)
plt.show()

fig2, ax2 = plt.subplots()
ax2.boxplot(np.concatenate((s1, s2), 1))
plt.show()

print(ranksums(s1, s2, alternative='two-sided'))
print(ranksums(s1, s2, alternative='less'))
print(ranksums(s1, s2, alternative='greater'))


x = stats.ranksums(s1, s2, alternative='less')
if stats.ranksums(s1, s2, alternative='less').pvalue <= 0.05:
    print('Gana el algoritmo de la tarea 2')
elif stats.ranksums(s2, s1, alternative='less').pvalue <= 0.05:
    print('Gana el algoritmo de la tarea 3')
else:
    print('Empate')
