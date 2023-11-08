import numpy as np


def f(x):
    return -np.sum((x-50)**2, axis=1)+50*len(x)


def inicializar(f, npop, nvars):
    # Generar población inicial
    genotipos = lb + (ub - lb) * np.random.uniform(low=0.0, high=1.0, size=[npop, nvars])
    # Fenotipos
    fenotipos = genotipos
    # Evaluar población
    aptitudes = f(fenotipos)
    return genotipos,fenotipos,aptitudes


def seleccion_ruleta(aptitudes, n):
    p = aptitudes/sum(aptitudes)
    cp= np.cumsum(p)
    parents = np.zeros(n)
    for i in range(n):
        X = np.random.uniform()
        parents[i] = np.argwhere(cp > X)[0]
    return parents.astype(int)


def seleccion_coma(genotipos, fenotipos, aptitudes, hijos_genotipo, hijos_fenotipo, hijos_aptitudes):
    return hijos_genotipo, hijos_fenotipo, hijos_aptitudes


def cruza_un_punto(genotipo, idx, pc):
    hijos_genotipo = np.zeros(np.shape(genotipo))
    k = 0
    for i, j in zip(idx[::2], idx[1::2]):
        flip = np.random.uniform()<=pc

        if flip:
            punto_cruza = np.random.randint(0, len(genotipo[0]))
            hijos_genotipo[k] = np.concatenate((genotipo[i,0:punto_cruza], genotipo[j,punto_cruza:]))
            hijos_genotipo[k+1] = np.concatenate((genotipo[j, 0:punto_cruza], genotipo[i, punto_cruza:]))
        else:
            hijos_genotipo[k] = np.copy(genotipo[i])
            hijos_genotipo[k + 1] = np.copy(genotipo[j])
        k += 2
    return hijos_genotipo


def mutacion_uniforme(genotipos, lb, ub, pm):
    for i in range(len(genotipos)):
        for j in range(len(genotipos[i])):
            flip = np.random.uniform() <= pm
            if flip:
                genotipos[i, j] = np.random.uniform(lb[j], ub[j])
    return genotipos


def estadisticas(generacion, genotipos, fenotipos, aptitudes, hijos_genotipo, hijos_fenotipo, hijos_aptitudes, padres):
    print('---------------------------------------------------------')
    print('Generación:', generacion)
    print('Población:\n', np.concatenate((np.arange(len(aptitudes)).reshape(-1,1), genotipos, fenotipos, aptitudes.reshape(-1, 1), aptitudes.reshape(-1, 1)/np.sum(aptitudes)), 1))
    print('Padres:', padres)
    print('frecuencia de padres:', np.bincount(padres))
    print('Hijos:\n', np.concatenate((np.arange(len(aptitudes)).reshape(-1, 1), hijos_genotipo, hijos_fenotipo, hijos_aptitudes.reshape(-1, 1), hijos_aptitudes.reshape(-1, 1)/np.sum(hijos_aptitudes)), 1))
    print('Desempeño en línea para t=1: ', np.mean(aptitudes))
    print('Desempeño fuera de línea para t=1: ', np.max(aptitudes))
    print('Mejor individuo en la generación: ', np.argmax(aptitudes))


def EA(f, lb, ub, pc, pm, nvars, npop, ngen):
    #Inicializar
    bg = np.zeros((ngen, nvars))
    bf = np.zeros((ngen, nvars))
    ba = np.zeros((ngen, 1))
    genotipos, fenotipos, aptitudes = inicializar(f, npop, nvars)
    #Hasta condición de paro
    for i in range(ngen):
        #Selección de padres
        idx = seleccion_ruleta(aptitudes, npop)
        #Cruza
        hijos_genotipo = cruza_un_punto(genotipos, idx, pc)
        #Mutación
        hijos_genotipo = mutacion_uniforme(hijos_genotipo, lb, ub, pm)
        hijos_fenotipo = hijos_genotipo
        hijos_aptitudes= f(hijos_genotipo)

        # Estadisticas
        estadisticas(i, genotipos, fenotipos, aptitudes, hijos_genotipo, hijos_fenotipo, hijos_aptitudes, idx)

        #Mejor individuo
        idx_best = np.argmax(aptitudes)
        b_gen = np.copy(genotipos[idx_best])
        b_fen = np.copy(fenotipos[idx_best])
        b_apt = np.copy(aptitudes[idx_best])
        ba[i] = np.copy(aptitudes[idx_best])

        #Selección de siguiente generación
        genotipos, fenotipos, aptitudes = seleccion_coma(genotipos, fenotipos, aptitudes, hijos_genotipo, hijos_fenotipo, hijos_aptitudes)

        #Elitismo
        idx = np.random.randint(npop)
        genotipos[idx] = b_gen
        fenotipos[idx] = b_fen
        aptitudes[idx] = b_apt
    #Fin ciclo

    print('Tabla de mejores:\n', ba)
    #Regresar mejor solución
    idx = np.argmax(aptitudes)
    return genotipos[idx], fenotipos[idx], aptitudes[idx]

nvars= 10
lb = 0*np.ones(nvars)
ub = 100*np.ones(nvars)
pc = 0.9
pm = 0.01
npop = 200
ngen = 500

np.set_printoptions(formatter={'float': '{0: 0.3f}'.format})
print(EA(f, lb, ub, pc, pm, nvars, npop, ngen))
