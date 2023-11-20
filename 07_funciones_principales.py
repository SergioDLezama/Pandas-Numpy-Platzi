import numpy as np
import jumpline as jl

# Definimos un array
arr = np.array([17, 11,  2, 17, 11,  9, 11, 12,  7, 12])
print(arr) # [17, 11,  2, 17, 11,  9, 11, 12,  7, 12]

jl.run()

# Modificamos el array a una matriz
matriz_arr = arr.reshape(2,5)
print(matriz_arr)
#[[17 11  2 17 11]
#[ 9 11 12  7 12]]

jl.run()

'''
Funcion .max() Traeremos el numero mas grande dentro de nuestro array
'''

max_arr = arr.max()
print(max_arr) # 17

jl.run()

# Igualmente funciona para una matriz
max_matriz = matriz_arr.max()
print(max_matriz) # 17

jl.run()

'''
Igualmente a la funcion podemos pedirle los maximos de una matriz de eje 0 (Vertical) o 1 (Horizontal)
'''

# Compara cada columna y nos da el numero mayor
max_matriz_0 = matriz_arr.max(0)
print(max_matriz_0) 
# [17 11 12 17 12] 

jl.run()

# Compara cada fila y nos da el numero mayor
max_matriz_1 = matriz_arr.max(1)
print(max_matriz_1) 
# [17 12] 

jl.run()

'''
Funcion .argmax() nos da el indice de donde esta ubicado nuestro valor mas grande de nuestro array
'''

argmax_arr = arr.argmax()
print(argmax_arr) # 0

jl.run()

# De igual forma podemos hacer con una matriz
argmax_matriz = matriz_arr.argmax()
print(argmax_matriz) # 0

jl.run()

# De igual forma podemos hacer con una matriz en eje 0
argmax_matriz_0 = matriz_arr.argmax(0)
print(argmax_matriz_0) # [0 0 1 0 1]

jl.run()

# De igual forma podemos hacer con una matriz en eje 1
argmax_matriz_1 = matriz_arr.argmax(1)
print(argmax_matriz_1) # [0 2]

jl.run()

'''
Funcion .min() nos da el numero mas pequeno que tiene el array
'''

min_arr = arr.min()
print(min_arr) # 2

jl.run()

# Igualmente con matriz

min_matriz = matriz_arr.min()
print(min_matriz) # 2

jl.run()

# Con eje 0

min_matriz_0 = matriz_arr.min(0)
print(min_matriz_0) # [ 9 11  2  7 11]

jl.run()

# Con eje 1

min_matriz_1 = matriz_arr.min(1)
print(min_matriz_1) # [2 7]

jl.run()

'''
Funcion .armin() nos da el indice de donde esta ubicado nuestro valor mas pequeno de nuestro array
'''

argmin_arr = arr.argmin()
print(argmin_arr) # 2

jl.run()

# De igual forma podemos hacer con una matriz
argmin_matriz = matriz_arr.argmin()
print(argmin_matriz) # 2

jl.run()

# De igual forma podemos hacer con una matriz en eje 0
argmin_matriz_0 = matriz_arr.argmin(0)
print(argmin_matriz_0) # [1 0 0 1 0]

jl.run()

# De igual forma podemos hacer con una matriz en eje 1
argmin_matriz_1 = matriz_arr.argmin(1)
print(argmin_matriz_1) # [2 3]

jl.run()

'''
Funcion .ptp() de un pico a otro pico. Podemos ver la diferencia del valor mas grande al mas pequeno
'''
# arr = [17 11  2 17 11  9 11 12  7 12] de 2 a 17 hay 15 de diferencia

ptp_arr = arr.ptp()
print(ptp_arr) # 15

jl.run()

'''
Igualmente con las matrices
'''

#[[17 11  2 17 11]
#[ 9 11 12  7 12]]

ptp_matriz = matriz_arr.ptp()
print(ptp_matriz) # 15

jl.run()

# Con eje 0

ptp_matriz_0 = matriz_arr.ptp(0)
print(ptp_matriz_0) # [ 8  0 10 10  1]

jl.run()

# Con eje 1

ptp_matriz_1 = matriz_arr.ptp(1)
print(ptp_matriz_1) # [15 0]

jl.run()

'''
Funcion np.percentile()
'''

# Percentile 50 o mediana
per_50 = np.percentile(arr,50)
print(per_50) # 11

jl.run()

# Numero mas altp
per_100 = np.percentile(arr,100)
print(per_100) # 17

jl.run()

# Numero mas bajo
per_0 = np.percentile(arr,0)
print(per_0) # 2

jl.run()

'''
Funcion .sort() acomoda los datos de menor a mayor los numeros del arreglo
'''
# Copio arr a arr2 para no modificar el array original
arr2 = arr

arr2.sort()
print(arr2) # [ 2  7  9 11 11 11 12 12 17 17]

jl.run()

'''
Funcion .median() nos devuelve la mediana de un array
'''

arr_median = np.median(arr)
print(arr_median) # 11

jl.run()

# Igualmente con una matriz

matriz_median = np.median(matriz_arr)
print(matriz_median) # 11

jl.run()

# Matriz en eje 0

matriz_median_0 = np.median(matriz_arr,0)
print(matriz_median_0) # [ 6.5  9.5 10.5 14.  14. ]

jl.run()

# Matriz en eje 1

matriz_median_1 = np.median(matriz_arr,1)
print(matriz_median_1) # [9 10]

jl.run()

'''
Funcion .std() Para conocer la desviacion estandart de un array o matriz
'''

std_arr = np.std(arr)
print(std_arr) # 4.182104733265296

jl.run()

'''
Funcion .var() Para conocer la varianza de un array o matriz
'''

var_arr = np.var(arr)
print(var_arr) # 17.49

jl.run()

'''
Funcion .mean() Obtenemos la media de un array o matriz
Es la suma de todos los valores dividos por la cantidad de valores que tengo
'''

mean_arr = np.mean(arr)
print(mean_arr) # 10.9

jl.run()

'''
Funcion .concatenate() Podemos unir arrays. 
Siempre y cuando tengan la misma cantidad de dimensiones
'''

a = np.array([[1, 2],  [3, 4]])
print(a)
print(f'a tiene {a.ndim} dimensiones')

jl.run()

b = np.array([[5, 6]])
print(b)
print(f'b tiene {b.ndim} dimensiones')

jl.run()

# Tenemos que especificar por cual axis queremos que la concatenacion

# Axis 0
a_b_0 = np.concatenate((a,b),axis=0)
print(a_b_0)
#[[1 2 5]
# [3 4 6]]

jl.run()

# Axis 1 No podemos concatenar por Axis 1 porque b no tiene elementos en Axis 1
#a_b_1 = np.concatenate((a,b),axis=1)#
#print(a_b_1)

'''
Para poder concatenar b por el axis 1 podemos usar la funcion .T (Transpuesta)
Que incierte los axis del array 
'''

print(b)
#[[5 6]]

print('-----')

print(b.T)
#[[5]
# [6]]

jl.run()

a_b_1 = np.concatenate((a,b.T),axis=1)#
print(a_b_1) 
#[[1 2 5]
#[3 4 6]]
