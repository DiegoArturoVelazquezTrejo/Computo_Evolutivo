#Comparativa entre dos algoritmos evolutivos

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)
nsamp = 10000

#Los evolutivos en eggholder
s1 = np.random.normal(20, 100, (nsamp, 1)) #Salida de algoritmo de Tarea 2
s2 = np.random.normal(0, 1, (nsamp, 1)) #Salida de algoritmo de Tarea 3

print(np.mean(s1))
print(np.mean(s2))

fig1, ax1 = plt.subplots()
ax1.hist(np.concatenate((s1, s2), 1), bins = 50)
plt.show()

fig2, ax2 = plt.subplots()
ax2.boxplot(np.concatenate((s1, s2), 1))
plt.show()

print(stats.ranksums(s1, s2, alternative='two-sided'))
print(stats.ranksums(s1, s2, alternative='less'))
print(stats.ranksums(s1, s2, alternative='greater'))


x = stats.ranksums(s1, s2, alternative='less')
if stats.ranksums(s1, s2, alternative='less').pvalue <= 0.05:
    print('Gana s1')
elif stats.ranksums(s2, s1, alternative='less').pvalue <= 0.05:
    print('Gana s2')
else:
    print('Empate')
