# Biblioteca para trabajar con multithreading
import threading

'''
Clase que va a generar hilos de trabajo para el cómputo paralelo
Clase que va a generar instancias de microservidores para procesar datos

'''
class Prueba:
    # Constructor de la clase hilo
    def __init__(self, id):
        self.id = id
        self.num = 0
    def set_num(self, num):
        self.num = num

def worker(num, obj):
    """thread worker function"""
    print('Worker: %s' % num)
    obj.set_num(num)
    # genetico.start()
    return num

# Supongamos que estos son genéticos
objs = []
for i in range(5):
    objs.append(Prueba(str(i)))

# Este será el bloque de código que se ejecute una vez que se segmentó la población inicial
threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,objs[i],))
    threads.append(t)
    t.start()

for i in range(5):
    print(objs[i].num)

'''
Vamos a tener un arreglo de algoritmos genéticos con las poblaciones distintas, pero mismos parámetros.
Vamos a ejecutar un método que mande a llamar su main junto con su población.
'''
