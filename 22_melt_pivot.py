import pandas as pd
import jumpline as jl

df = pd.read_csv('./bestsellers-with-categories.csv')
print(df.head(5))
'''
                                                Name                    Author  ...  Year        Genre
0                      10-Day Green Smoothie Cleanse                  JJ Smith  ...  2016  Non Fiction
1                                  11/22/63: A Novel              Stephen King  ...  2011      Fiction
2            12 Rules for Life: An Antidote to Chaos        Jordan B. Peterson  ...  2018  Non Fiction
3                             1984 (Signet Classics)             George Orwell  ...  2017      Fiction
4  5,000 Awesome Facts (About Everything!) (Natio...  National Geographic Kids  ...  2019  Non Fiction

[5 rows x 7 columns]
'''

jl.run()

'''
pivot_table
Pivot, básicamente, transforma los valores de determinadas columnas o filas en los índices de un nuevo 
DataFrame, y la intersección de estos es el valor resultante.

Como resultado, los valores de Author pasan a formar el índice por fila y los valores de Genre pasan 
a formar parte de los índices por columna, y el User Rating se mantiene como valor.
'''
df_pivot =df.pivot_table(index='Author',columns='Genre',values='User Rating')
print(df_pivot.head(5))
'''
Genre                       Fiction  Non Fiction
Author
Abraham Verghese                4.6          NaN
Adam Gasiewski                  NaN          4.4
Adam Mansbach                   4.8          NaN
Adir Levy                       4.8          NaN
Admiral William H. McRaven      NaN          4.7
'''

jl.run()

'''
Otra variacion
En este caso tenemos por cada género, la suma a lo largo de los años. Esto es mucho 
más interesante, ¿verdad? La mejor noticia es que no solo podemos obtener la suma, 
también podemos obtener la media, la desviación estándar, el conteo, la varianza, etc. 
Únicamente con cambiar el parámetro aggfunc que traduce función de agrupamiento.
'''
df_pivot = df.pivot_table(index='Genre' ,columns='Year', values='User Rating',aggfunc='sum')
print(df_pivot)
'''
Year          2009   2010   2011   2012   2013   2014   2015   2016   2017   2018   2019
Genre
Fiction      110.2   92.3   97.0   94.4  109.1  134.3   79.1   89.6  113.7   99.5   96.4
Non Fiction  119.0  135.6  130.9  132.2  118.6   96.8  153.3  144.3  119.3  133.9  140.6
'''

jl.run()

'''
melt
El método melt toma las columnas del DataFrame y las pasa a filas, con dos nuevas columnas 
para especificar la antigua columna y el valor que traía.
'''

print(df[['Name','Genre']].head(5))
'''
                                                Name        Genre
0                      10-Day Green Smoothie Cleanse  Non Fiction
1                                  11/22/63: A Novel      Fiction
2            12 Rules for Life: An Antidote to Chaos  Non Fiction
3                             1984 (Signet Classics)      Fiction
4  5,000 Awesome Facts (About Everything!) (Natio...  Non Fiction
'''

jl.run()

'''
Aplicamos Melt
Ahora cada resultado de las dos columnas pasa a una fila de
este modo a tipo llave:valor.
'''
df_melt = df[['Name','Genre']].head(5).melt()
print(df_melt)
'''
  variable                                              value
0     Name                      10-Day Green Smoothie Cleanse
1     Name                                  11/22/63: A Novel
2     Name            12 Rules for Life: An Antidote to Chaos
3     Name                             1984 (Signet Classics)
4     Name  5,000 Awesome Facts (About Everything!) (Natio...
5    Genre                                        Non Fiction
6    Genre                                            Fiction
7    Genre                                        Non Fiction
8    Genre                                            Fiction
9    Genre                                        Non Fiction
'''

jl.run()

'''
Otra variacion
Simplemente, podemos seleccionar las columnas que no quiero hacer 
melt usando el parámetro id_vars. Para este caso Year y también la
única columna que quiero aplicar el melt, para este caso Genre con 
la propiedad value_vars.
'''
df_melt = df.melt(id_vars='Year',value_vars='Genre')
