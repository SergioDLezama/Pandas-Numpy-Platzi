import numpy as np
import jumpline as jl

'''
Condiciones
'''

arr = np.linspace(1,10,10, dtype='int8')
print(arr) # [ 1  2  3  4  5  6  7  8  9 10]

jl.run()

# Nos devuelve en booleano los elementos que cumplen con la condicion
indices_cond  = arr > 5
print(indices_cond) # [False False False False False  True  True  True  True  True]

jl.run()

# Al imprimir arr con la condicion indices_cond solo nos devolvera los elementos que son True
print(arr[indices_cond]) # [ 6  7  8  9 10]

# Otra forma de obtener el mismo resultado
print(arr[arr > 5]) # [ 6  7  8  9 10]

jl.run()

# Podemos poner multiples condiciones usando &
arr_1 = arr[(arr > 5) & (arr < 9)]
print(arr_1) # [6 7 8]

jl.run()

# Podemos sobreescribir solo ciertos elementos dependiendo de la condicion
arr[arr > 5] = 10
print(arr) # [ 1  2  3  4  5 10 10 10 10 10]

print(arr[arr==10]) # [10 10 10 10 10]