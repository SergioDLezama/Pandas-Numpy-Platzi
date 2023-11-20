import numpy as np
import jumpline as jl

arr = np.array([[1,2],[3,4],[5,6]])
print(arr)
#[[ 1  2]
# [ 3  4]
# [ 5  6]]

jl.run()

# Con shape podemos ver la estructura y tamano de el array. Cuantas filas, columnas, dimensiones tengo
print(arr.shape) # (3,2)

jl.run()

# Reshape acomoda los datos iniciales de la forma indicada para que cumplan esta condicion
arr2 = arr.reshape(1,6)
print(arr2) # [[1 2 3 4 5 6]]

jl.run()

arr3 = arr.reshape(2,3)
print(arr3)
#[[1 2 3]
#[4 5 6]]

jl.run()

# Otra syntax de hacer el reshape
arr4 = np.reshape(arr,(1,6))
print(arr4) # [[ 1 2 3 4 5 6]]

jl.run()

'''
Podemos especificar la forma en que queremos que tome los datos para el reshape
'''

arr5 = np.reshape(arr,(2,3),'C')
print(arr5) # Estructura los datos por filas (De izquierda a derecha)
#[[1 2 3]
#[4 5 6]]

jl.run()

arr6 = np.reshape(arr,(2,3),'F')
print(arr6) # Estructura los datos por columna (De arriba a abajo). Con la syntax de Fortran
#[[1 5 4]
#[3 2 6]]

jl.run()

arr7 = np.reshape(arr,(2,3),'A')
print(arr6) # Estructura los datos de la forma que este mejor optimizado el sistema de la pc, sea la forma 'C' o 'F'
#[[1 5 4]
#[3 2 6]]

'''
Importante saber que no podemos cambiar la forma a un array si la estructura pedida no es compatible.
Es decir si tenemos un array (3,2) que tiene 6 elementos, podemos cambiarlo a (1,6) los mismos 6 elementos o (2,3)
los mismos 6 elementos estara bien. Pero si queremos cambiarlo a uno de (3,3) No podremos porque faltan elementos
'''
