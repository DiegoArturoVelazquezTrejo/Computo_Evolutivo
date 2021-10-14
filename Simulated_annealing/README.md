# Aplicación del algoritmo Simulated Annealing en la optimización de un problema discreto y uno continuo
----
# Universidad Nacional Autónoma de México

## Facultad de Ciencias

### Ciencias de la Computación

----
Autor: Diego Arturo Velázquez Trejo (https://github.com/DiegoArturoVelazquezTrejo)

========================

#### Descripción de los problemas:
  - Problema de la mochila: Se cuenta con un conjunto de objetos de tamaño N. Cada objeto tiene asociado un peso y un valor. Por otra parte, se cuenta con una mochila con capacidad limitada C. Se pretende encontrar una mochila que contenga objetos que su suma de pesos no sobrepase la capacidad de la mochila y que su suma de valores maximice el valor de la mochila.

  - Problema de la función continua: Se tiene una función continua en dos dimensiones dada por: f(x_1,x_2 )=x_1^2+x_2^2, -5≤x_1,x_2≤5.
  Se pretende hallar un vector (x_1, x_2) que maximice la función.

### Requisitos para la ejecución correcta del programa:
  1) Versión Python2.7.0 en adelante.

### Para ejecutar el problema de la mochila:
En el archivo "leyendo_datos_mochila.py" escribir la ruta al arhivo que contenga la información de los pesos y valores por objeto.
```
$ python3 Main_Simulated_Annealing.py
```
### Para ejecutar el problema de la función continua:
```
$ python3 Main_Simulated_Annealing_Funcion_Continua.py
```

### Observaciones y análisis de complejidades:
Una vez que se utilizó el algoritmo de Simulated Annealing, vimos que este convergió de buena manera a una solución que optimizara el problema dado. Se le agregó una modificación al algoritmo con subiteraciones para tener más variedad al momento de seleccionar nuevos estados con una probabilidad que no cambiara con base en la temperatura. Además, la implementación va registrando los estados que minimizan el problema y aquellos que lo maximizan.

Su complejidad se define con base en el número de subiteraciones que se le definen. Además, el número de iteraciones tiene un máximo que se define en los parámetros de entrada y además, depende de la función que actualiza a la temperatura ya que este algoritmo trabajará mientras la temperatura sea mayor a 1, por lo que la función que actualiza la temperatura también influye en la cantidad de iteraciones.

El algoritmo es óptimo ya que empieza siendo un algoritmo que tiene una búsqueda muy amplia en el conujunto de posibles estados pero a medida que la temperatura cambia, esta probabilidad de aceptación cambia, por lo que se aceptan menos estados. 

### Resultados:


### Problema de optimización del problema de la Mochila

### RESULTADOS
Valor de la mochila inicial:
Peso: 4642.0, Valor:4574.0 : {'46', '28', '18', '22', '7', '27', '4', '3', '38', '10'}
Resultado del algoritmo SA:
Peso: 4401.0, Valor:4435.0 : {'16', '29', '38', '34', '41', '9', '2', '20', '48', '15'}
Promedio de las mochilas que se generaron en las iteraciones:
4650.163857
Objeto máximo en las iteraciones:
Peso: 5000.0, Valor:5327.0 : {'1', '4', '32', '21', '2', '39', '17', '19', '6', '48', '15'}

### RESULTADOS
Valor de la mochila inicial:
Peso: 4851.0, Valor:4845.0 : {'21', '5', '42', '34', '19', '16', '12', '20', '18', '48', '11'}
Resultado del algoritmo SA:
Peso: 4982.0, Valor:4834.0 : {'49', '22', '42', '34', '44', '6', '38', '20', '25'}
Promedio de las mochilas que se generaron en las iteraciones: 4649.621536
Objeto máximo en las iteraciones:
Peso: 4999.0, Valor:5287.0 : {'21', '17', '44', '6', '19', '32', '1', '14'}
Objeto mínimo en las iteraciones:
Peso: 2019.0, Valor:2017.0 : {'4', '40', '23', '39', '47', '7', '20', '18', '26', '48', '33', '3'}

### Problema de optimización de una función continua

### RESULTADOS
Valor del vector inicial:
(1.9793914887584103, 3.645698349138449), valor = 17.20910711868005
Resultado del algoritmo SA:
(137.95860600133008, -103.82513298893701), valor = 29812.235210000683
Objeto máximo en las iteraciones:
(155.05822499458577, -117.29272219391304), valor = 37800.635818130046
Objeto mínimo en las iteraciones:
(1.213196246017755, 3.65355035108032), valor = 14.820275299230703


### RESULTADOS
Valor del vector inicial:
(1.2048386000643179, 0.9500079014085809), valor = 2.3541510649436814
Resultado del algoritmo SA:
(170.5367605143699, -91.04202970015253), valor = 37371.437858659
Objeto máximo en las iteraciones:
(192.91053588167387, -117.64835507585379), valor = 51055.61030620875
Objeto mínimo en las iteraciones:
(0.9636898296462024, 0.7967066049401583), valor = 1.5634395021188001
