import numpy as np
import jumpline as jl
jl.run()
lista = [1,2,3,4,5,6,7,8,9]

arr = np.array(lista)

print(arr)

jl.run()

matriz = [[1,2,3],[4,5,6],[7,8,9]]
matriz = np.array(matriz)
print(matriz)

jl.run()

'''
Indexing de array
'''
print(arr) # [1 2 3 4 5 6 7 8 9]
print(arr[0]) # 1
print(arr[1]) # 2

print(arr[0] + arr[5]) # 7

jl.run()

'''
Indexing de matrices
'''
print(matriz)
#[[1 2 3]
#[4 5 6]
#[7 8 9]]
jl.run()

# De esta forma vemos las filas por posicion
print(matriz[0]) # [1 2 3]
print(matriz[2]) # [7 8 9]

jl.run()

# Para acceder a las posicones dentro de las filas
print(matriz[0,1]) # [2]
print(matriz[2,0]) # [7]

jl.run()

# Si queremos acceder a mas de un objeto usamos el slicing

print(arr[0:3]) # [1 2 3]
jl.run()

print(matriz[0:2,1:])
# [[2 3]
# [5 6]]

jl.run()

