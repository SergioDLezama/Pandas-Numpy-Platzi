import numpy as np
import jumpline as jl

'''
Funcion .copy()
'''

arr = np.arange(0,11)
print(arr) # [ 0  1  2  3  4  5  6  7  8  9 10]

jl.run()

slice_arr = arr[0:6]
print(slice_arr) # [0 1 2 3 4 5]

jl.run()

slice_arr[:] = 0
print(slice_arr)
# [0 0 0 0 0 0]

print(arr)
# [ 0  0  0  0  0  0  6  7  8  9 10]

jl.run()

'''
Aunque nosotros seleccionamos una parte de arr y lo definimos en otra variable
al modificarlo se modifico tambien nuestro array padre.
Para evitar esto tenemos que hacer una copia
'''

arr = np.arange(0,11)
print(arr) # [ 0  1  2  3  4  5  6  7  8  9 10]

jl.run()

arr_copy = arr.copy()

slice_arr = arr_copy[0:6]
print(slice_arr) # [0 1 2 3 4 5]

jl.run()

slice_arr[:] = 0
print(slice_arr)
# [0 0 0 0 0 0]

print(arr)
# [ 0  0  0  0  0  0  6  7  8  9 10]

jl.run()

