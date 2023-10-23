import numpy as np
import jumpline as jl
jl.run()

arr = np.array([1,2,3,4])
print(arr) # [1 2 3 4]
print(arr.dtype) # int32

jl.run()

# Cambiamos el dtype con la siguiente linea, sobreescribiendo el array
arr = np.array([1,2,3,4], dtype='float64')
print(arr) # [1. 2. 3. 4.]
print(arr.dtype) # float64

jl.run()

'''
Para corregir el tipo de dato una vez el array esta definido
'''
arr = np.array([1,2,3,4])
print(arr) # [1 2 3 4]
print(arr.dtype) # int32

arr = arr.astype(np.float64) 
print(arr) # [1. 2. 3. 4.]

jl.run()

# Podemos hacerlo con diferentes tipos de dato, ejemplo bool
arr = np.array([0, 1,2,3,4])
print(arr) # [0, 1, 2, 3, 4]
print(arr.dtype) # int32

arr = arr.astype(np.bool_) 
print(arr) # [False, True, True, True, True]

jl.run()

# Ejemplo String
arr = np.array([0, 1,2,3,4])
print(arr) # [0, 1, 2, 3, 4]
print(arr.dtype) # int32

arr = arr.astype(np.string_) 
print(arr) # [b'0' b'1' b'2' b'3' b'4'] 
jl.run()

# Ejemplo Int
arr = np.array(['0', '1','2','3','4'])
print(arr) # ['0', '1', '2', '3', '4']

arr = arr.astype(np.int8) 
print(arr) # [0 1 2 3 4]  
