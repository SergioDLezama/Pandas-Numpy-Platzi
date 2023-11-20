import numpy as np
import jumpline as jl

linea = '-' * 15

'''
Operaciones en numpy
'''

lista = [1,2]
print(lista) # [1, 2]

jl.run()

arr = np.arange(0,10)
print(arr) # [0 1 2 3 4 5 6 7 8 9]

arr_copy = arr.copy()

jl.run()

'''
Operaciones
'''

# Para multiplicar cada elemento por un numero
multipli = arr_copy * 2 
print(multipli)# [ 0  2  4  6  8 10 12 14 16 18]

jl.run()

# Para sumar cada elemento a un numero
suma = arr_copy + 5
print(suma) # [ 5  6  7  8  9 10 11 12 13 14]

jl.run()

# Para dividir
division = arr_copy / 2
print(division) # [0.  0.5 1.  1.5 2.  2.5 3.  3.5 4.  4.5]
''' 
Aunque dividir entre 0 da error. Python sigue corriendo el codigo dandonos un warning
o en este caso solo nos da 0 enves de cerrar todo el codigo
'''

jl.run()

# Para elevar a un numero los elemenetos
elevar = arr_copy ** 2
print(elevar) # [ 0  1  4  9 16 25 36 49 64 81]

jl.run()

# Tambien podemos hacer operaciones entre arrays
array_operaciones = suma + division
print(array_operaciones) # [ 5.   6.5  8.   9.5 11.  12.5 14.  15.5 17.  18.5]

# Podemos hacer cualquier operacion entre arrays
array_multi = suma * division
print(array_multi) # [ 0.  3.  7. 12. 18. 25. 33. 42. 52. 63.]

jl.run()

'''
Trabajando con matrices
'''
matriz = arr_copy.reshape(2,5)
print(matriz)
#[[0 1 2 3 4]
# [5 6 7 8 9]]

matriz_copy = matriz.copy()

jl.run()

# Podemos hacer operaciones entre matrices
suma_matriz = matriz + matriz_copy
print(suma_matriz)
# [[ 0  2  4  6  8]
# [10 12 14 16 18]]

print(linea)

# Multiplicacion entre matrices
multipli_matriz = matriz * matriz_copy
print(multipli_matriz)
#[[ 0  1  4  9 16]
# [25 36 49 64 81]]

print(linea)

# Resta entre matrices
resta_matrices = matriz - matriz_copy
print(resta_matrices)
#[[0 0 0 0 0]
# [0 0 0 0 0]]

print(linea)

# Division entre matrices
division_matrices = matriz / matriz_copy
print(division_matrices)
'''
Nos devuelve el primer elemento como nan. Debido al error que se produce
al dividir entre 0. De igual manera divide los demas elementos

[[nan  1.  1.  1.  1.]
 [ 1.  1.  1.  1.  1.]]
'''

jl.run()

'''
Operacion producto punto entre matrices
.matmul(matriz1,matriz2)

Debemos hacer una matriz Transpuesta con .T
'''

punto_punto = np.matmul(matriz,matriz_copy.T)
print(punto_punto) 
# [[ 30  80]
# [ 80 255]]

print(linea)

# Otra forma de hacer una operacion punto punto

punto_punto_2 = matriz @ matriz_copy.T
print(punto_punto_2)