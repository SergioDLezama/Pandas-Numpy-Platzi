import pandas as pd
import numpy as np
import jumpline as jl

'''Crearemos nuestros DF desde cero'''

df_1 = pd.DataFrame(
    {'A':['A0','A1','A2','A3'],
    'B':['B0','B1','B2','B3'],
    'C':['C0','C1','C2','C3'],
    'D':['D0','D1','D2','D3']})

df_2 = pd.DataFrame(
    {'A':['A4','A5','A6','A7'],
    'B':['B4','B5','B6','B7'],
    'C':['C4','C5','C6','C7'],
    'D':['D4','D5','D6','D7']})

'''Concat'''

'''Por default el concat es por el axis 0, por las filas'''


df_3 = pd.concat([df_1,df_2])
print(df_3)
'''
0  A0  B0  C0  D0
1  A1  B1  C1  D1
2  A2  B2  C2  D2
3  A3  B3  C3  D3
0  A4  B4  C4  D4
1  A5  B5  C5  D5
2  A6  B6  C6  D6
3  A7  B7  C7  D7
'''

jl.run()

'''Para evitar que los indices se repitan agregamos la condicion ignore_index=True'''

df_4 = pd.concat([df_1,df_2],ignore_index=True)
print(df_4)
'''
    A   B   C   D
0  A0  B0  C0  D0
1  A1  B1  C1  D1
2  A2  B2  C2  D2
3  A3  B3  C3  D3
4  A4  B4  C4  D4
5  A5  B5  C5  D5
6  A6  B6  C6  D6
7  A7  B7  C7  D7
'''


jl.run()


'''Tambien podemos reiniciar los index con reset_index()'''

df_5 = df_3.reset_index()
print(df_5)
'''
   index   A   B   C   D
0      0  A0  B0  C0  D0
1      1  A1  B1  C1  D1
2      2  A2  B2  C2  D2
3      3  A3  B3  C3  D3
4      0  A4  B4  C4  D4
5      1  A5  B5  C5  D5
6      2  A6  B6  C6  D6
7      3  A7  B7  C7  D7
'''

jl.run()

'''Concat por axis 1'''

df_3 = pd.concat([df_1,df_2],axis=1)
print(df_3)
'''
    A   B   C   D   A   B   C   D
0  A0  B0  C0  D0  A4  B4  C4  D4
1  A1  B1  C1  D1  A5  B5  C5  D5
2  A2  B2  C2  D2  A6  B6  C6  D6
3  A3  B3  C3  D3  A7  B7  C7  D7
'''

jl.run()

'''Merge'''

# Creamos DF
left = pd.DataFrame(
    {'key':['k0','k1','k2','k3'],
    'A':['A0','A1','A2','A3'],
    'B':['B0','B1','B2','B3']})

right = pd.DataFrame(
    {'key':['k0','k1','k2','k3'],
    'C':['C0','C1','C2','C3'],
    'D':['D0','D1','D2','D3']})

print(left)
print('-'*15)
print(right)

jl.run()

'''
Para hacer un merge de inner, que es el default
Pandas hace el merge con la columna que esta en comun, pero es buena practica
especificar en que columna queremos hacer el merge
'''

left_right = left.merge(right,on='key')
print(left_right)
'''
  key   A   B   C   D
0  k0  A0  B0  C0  D0
1  k1  A1  B1  C1  D1
2  k2  A2  B2  C2  D2
3  k3  A3  B3  C3  D3
'''

jl.run()

# Modificamos el DF 2 nombramos la columna 'key' a 'key_2
left = pd.DataFrame(
    {'key':['k0','k1','k2','k3'],
    'A':['A0','A1','A2','A3'],
    'B':['B0','B1','B2','B3']})

right = pd.DataFrame(
    {'key_2':['k0','k1','k2','k3'],
    'C':['C0','C1','C2','C3'],
    'D':['D0','D1','D2','D3']})

print(left)
print('-'*15)
print(right)

jl.run()

'''
El merge nos dara error porque ambos DF no tienen 'key'
Tenemos que espcificar en donde queremos iniciar el merge de cada DF
con left_on='columna', right_on='columna_2'
'''

left_right = left.merge(right,left_on='key',right_on='key_2')
print(left_right)
'''
  key   A   B key_2   C   D
0  k0  A0  B0    k0  C0  D0
1  k1  A1  B1    k1  C1  D1
2  k2  A2  B2    k2  C2  D2
3  k3  A3  B3    k3  C3  D3
'''

jl.run()

# Modificamos el DF right donde ponemos uno de los elementos como NaN

left = pd.DataFrame(
    {'key':['k0','k1','k2','k3'],
    'A':['A0','A1','A2','A3'],
    'B':['B0','B1','B2','B3']})

right = pd.DataFrame(
    {'key_2':['k0','k1','k2',np.nan],
    'C':['C0','C1','C2','C3'],
    'D':['D0','D1','D2','D3']})

print(left)
print('-'*15)
print(right)

jl.run()

'''Al haber un elemento NaN el merge se hara sin la fila 3, donde se ubica el Nan'''
left_right = left.merge(right,left_on='key',right_on='key_2')
print(left_right)
'''
  key   A   B key_2   C   D
0  k0  A0  B0    k0  C0  D0
1  k1  A1  B1    k1  C1  D1
2  k2  A2  B2    k2  C2  D2
'''

jl.run()

'''
Si quisieramos traer los elementos de la izquierda,
sin importar que uno de los datos de la derecha este NaN
usamos how='left' '''
left_right = left.merge(right,left_on='key',right_on='key_2',how='left')
print(left_right)
'''
  key   A   B key_2    C    D
0  k0  A0  B0    k0   C0   D0
1  k1  A1  B1    k1   C1   D1
2  k2  A2  B2    k2   C2   D2
3  k3  A3  B3   NaN  NaN  NaN
'''

jl.run()

'''Para hacer merge con los datos de la derecha'''
left_right = left.merge(right,left_on='key',right_on='key_2',how='inner')
print(left_right)
'''
   key    A    B key_2   C   D
0   k0   A0   B0    k0  C0  D0
1   k1   A1   B1    k1  C1  D1
2   k2   A2   B2    k2  C2  D2
3  NaN  NaN  NaN   NaN  C3  D3
'''

