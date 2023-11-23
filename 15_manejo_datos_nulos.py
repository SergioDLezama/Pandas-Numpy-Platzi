import pandas as pd
import numpy as np
import jumpline as jl

# Creamos un diccionario para nuestro DataFrame
dict = {'Col1':[1,2,3,np.nan],
        'Col2':[5,np.nan,7,8],
        'Col3':['a','b','c',None]}

# Pasamos el dict a un  DaraFrame
df = pd.DataFrame(dict)
print(df)
'''
   Col1  Col2  Col3
0   1.0   4.0     a
1   2.0   NaN     b
2   3.0   6.0     c
3   NaN   7.0  None
'''

jl.run()

# Para ver los elementos Nulos en bool .isnull()
print(df.isnull()) # Vemos que tenemos 3 elementos nulos
'''
    Col1   Col2   Col3
0  False  False  False
1  False   True  False
2  False  False  False
3   True  False   True
'''

jl.run()

#Podemos hacerlo mas visibles con 0 y 1. Es el metodo mas usado
print(df.isnull()*1)
'''
   Col1  Col2  Col3
0     0     0     0
1     0     1     0
2     0     0     0
3     1     0     1
'''

jl.run()

'''
Podemos llenar los valores nulos con .fillna()
Podriamos llenarlo con la media .mean()
O la moda o percentiles
'''
missing_df = df.fillna('Missing')
print(missing_df)

jl.run()

'''
Podemos rellenar los datos haciendo que python asuma que es una serie de numeros
Los string no son afectados
Usamos .interpolate()
'''
df_inter = df.interpolate()
print(df_inter)
'''
   Col1  Col2  Col3
0   1.0   5.0     a
1   2.0   6.0     b
2   3.0   7.0     c
3   3.0   8.0  None
'''

jl.run()

'''
Igualmente podriamos borrar los elementos nulos con .dropna()
'''

df_dropna = df.dropna()
print(df_dropna)



