import numpy as np
from CE.problems import *


#Entradas: alpha en R+, tol en R+
def sd(f, j, x0, alpha, tol, maxiter):
    i = 0
    xk = x0
    #1) verificar optimalidad norm(j(xk))<=tol ~ j(xk)=0 o repetir
    while np.linalg.norm(xk) > tol and i < maxiter:
        #2) pk = negativo del gradiente -j(xk)
        pk = -j(xk)
        #3) x_{k+1} = x_k + alpha*pk
        xk = xk+alpha*pk
        #4) medir pérdida
        print(i, xk, f(xk), np.linalg.norm(j(xk)))
        i += 1

    return xk, f(xk)

f = schwefel_f
j = schwefel_j
x0= np.array([-247.42635437])
alpha = 0.05
tol = 1e-4
maxiter = 1000

print('resultado:', sd(f, j, x0, alpha, tol, maxiter))

