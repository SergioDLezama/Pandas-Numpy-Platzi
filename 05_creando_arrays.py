import numpy as np
import jumpline as jl

# Normalmente hacemos rangos con range
print(list(range(0,10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

jl.run()

'''
Podemos hacer rangos directamente con numpy creando arrays
'''

array = np.arange(0,10)
print(array) # [0 1 2 3 4 5 6 7 8 9]

array = np.arange(0,20,2)
print(array) # [ 0  2  4  6  8 10 12 14 16 18]

jl.run()

'''
Podemos crear un array compuesto por ceros nosotros indicando la cantidad de elementos o ceros en este caso
'''

ceros = np.zeros(4)
print(ceros) # [0. 0. 0. 0.]

# Tambien podemos crear una matriz usando una tupla
matriz = np.zeros((3,3))
print(matriz)
'''
[[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]
'''

# De la mismoa forma que funciona zeros funciona ones con unos
unos = np.ones(4)
print(unos) # [1. 1. 1. 1.]

matriz = np.ones((3,3))
print(matriz)
'''
[[1. 1. 1.]
 [1. 1. 1.]
 [1. 1. 1.]]
'''

jl.run()

'''
Linspace syntax
linspace(donde quiero que inicie, donde quiero que termine, cuantos datos quiero generar)
'''

lin = np.linspace(0,10,10)
print(lin)
'''
[ 0.          1.11111111  2.22222222  3.33333333  4.44444444  5.55555556
  6.66666667  7.77777778  8.88888889 10.        ]
'''
jl.run()

lin = np.linspace(0,15,5)
print(lin) # [ 0.    3.75  7.5  11.25 15.  ]
jl.run()

# Uso de eye
eye = np.eye(4)
print(eye)
'''
[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]
'''
jl.run()

'''
Podemos generar datos aleatorios con numpy random
'''

numero = np.random.rand()
print(numero) # Cada ver que corramos el codigo nos dara un numero aleatorio

# Podemos crear arrays con numeros aleatorios indicando el numero de elementos
random_array = np.random.rand(4)
print(random_array) # [0.17332765 0.46408631 0.73726062 0.95395714]

'''
Cada vez que corra el codigo los valores cambiaran pero la cantidad de elementos no
'''

# Al igual podemos crear matrices

random_matriz = np.random.rand(4,4)
print(random_matriz)
'''
[[0.51163632 0.82431065 0.49844643 0.7232133 ]
 [0.54367505 0.18634469 0.07051778 0.21861019]
 [0.35151179 0.32917756 0.14595751 0.16867071]
 [0.67248498 0.25831723 0.82702941 0.27377015]]
'''
jl.run()

# Para recibir numeros enteros aleatorios
random_integer = np.random.randint(1,15)
print(random_integer) # Nos dara in integer entre 1 a 15


# Para recibir una matriz de numeros enteros aleatorios
matriz_int = np.random.randint(1,100,(5,5))
print(matriz_int)
'''
[[58 30  6  1 18]
 [ 4  2 25 40 21]
 [21 45 77 31 67]
 [99 14 61 20 91]
 [ 6 68 87 69 27]]
'''
jl.run()

# Para recibir un array de numeros enteros aleatorios
array_int = np.random.randint(1,100,(5))
print(array_int)
'''
[[58 30  6  1 18]
 [ 4  2 25 40 21]
 [21 45 77 31 67]
 [99 14 61 20 91]
 [ 6 68 87 69 27]]
'''

