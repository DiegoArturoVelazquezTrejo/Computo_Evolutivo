import numpy as np
from CE.problems import *


def N(f, xk, ns, sigma):
    n = xk + np.random.normal(0, sigma, (ns, len(xk)))
    fn = []
    for i in range(ns):
        fn.append(f(n[i]))
    return n, fn

def hillclimbing(f, x0, N, ns, maxiter, sigma):
    xk = x0
    fxk= f(xk)
    # Generar los ns vecinos
    #Mientras condición de paro
    for k in range(maxiter):
        #Generar vecinos
        n, fn = N(f, xk, ns, sigma)
        #Encontrar el mejor vecino
        bn_idx = np.argmin(fn)                          #argmin_n f(n)
        #Movernos al mejor vecino si es mejor que el actual
        if fn[bn_idx] <= fxk:
            xk = n[bn_idx]
            fxk= fn[bn_idx]
        #sigma = 3/5*sigma
        print(k, xk, fxk)
    return xk, fxk

f = schwefel_f
x0= np.array([-247.42635437])
ns = 10
maxiter = 1000
sigma = 50

print('resultado:', hillclimbing(f, x0, N, ns, maxiter, sigma))
#resultado: (array([-280.1775097]), 178.70905850841373)