import numpy as np
import jumpline as jl
jl.run()

scalar = np.array(42)
print(scalar) # 42

# Para ver cuantas dimesiones tiene un array usamos .ndim
print(scalar.ndim) # 0

jl.run()

vector = np.array([1,2,3])
print(vector) # [1 2 3]
print(vector.ndim) # 1

jl.run()

matriz = np.array([[1,2,3],[4,5,6]])
print(matriz)
# [1 2 3]
# [4 5 6]
print(matriz.ndim) # 2

jl.run()

tensor = np.array([[[1,2,3], [4,5,8], [8,7,9], [9,7,8]], [[1,2,3], [4,5,8], [8,7,9], [9,7,8]]])
print(tensor)
print(tensor.ndim) # 3

jl.run()

'''
Para agregar o eliminar dimensiones
'''
vector = np.array([1,2,3], ndmin=10)
print(vector) # [[[[[[[[[[1 2 3]]]]]]]]]]
print(vector.ndim) # 10

jl.run()

# Expandir dimensiones

expand = np.expand_dims(np.array([1,2,3]) ,axis=0) 
# axis=0 Implica expandir una dimension a nivel de filas. En py 0 es filas. 1 es columnas
print(expand) # [[1,2,3]]
print(expand.ndim) # 2

jl.run()

# Eliminar dimensiones

print(vector, vector.ndim) # [[[[[[[[[[1 2 3]]]]]]]]]] 10

vector_2 = np.squeeze(vector) # squeeze va a llevar las dimensiones a el punto que crea correcto

print(vector_2, vector_2.ndim) # [1 2 3] 1



