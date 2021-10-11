'''
Vamos a estudiar la frecuencia con la que se extraen ciertos elementos de un conjunto
'''
import random

elementos = random.randint(0, 100)

conj = set()

for i in range(0, elementos):
    conj.add(str(i))

while(len(conj) > 0):
    print(conj.pop())
