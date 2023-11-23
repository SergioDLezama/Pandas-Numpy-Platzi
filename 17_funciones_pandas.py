import pandas as pd
import jumpline as jl

df_books = pd.read_csv('./bestsellers-with-categories.csv')
print(df_books.head(2))

jl.run()

'''
Podemos ver un resumen de nuestros datos con .info()
Podremos ver las columnas, sus indices, cuantos valores no son nulos
Tipos de datos que teiene cada columna, cuantos registros tenenmos
'''
print(df_books.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 550 entries, 0 to 549
Data columns (total 7 columns):
 #   Column       Non-Null Count  Dtype
---  ------       --------------  -----
 0   Name         550 non-null    object
 1   Author       550 non-null    object
 2   User Rating  550 non-null    float64
 3   Reviews      550 non-null    int64
 4   Price        550 non-null    int64
 5   Year         550 non-null    int64
 6   Genre        550 non-null    object
dtypes: float64(1), int64(3), object(3)
memory usage: 30.2+ KB
'''

jl.run()

'''
Podemos ver un resumen estadistico de los columnas numericas con .describe()
Como la media, std, minimo, maximo y los percentiles
'''
print(df_books.describe())
'''
       User Rating       Reviews       Price         Year
count   550.000000    550.000000  550.000000   550.000000
mean      4.618364  11953.281818   13.100000  2014.000000
std       0.226980  11731.132017   10.842262     3.165156
min       3.300000     37.000000    0.000000  2009.000000
25%       4.500000   4058.000000    7.000000  2011.000000
50%       4.700000   8580.000000   11.000000  2014.000000
75%       4.800000  17253.250000   16.000000  2017.000000
max       4.900000  87841.000000  105.000000  2019.000000
'''

jl.run()

'''
Podemos ver las ultimas lineas con .tail() viceversa de .head()
'''
print(df_books.tail(3))
'''
                                                  Name       Author  User Rating  Reviews  Price  Year        Genre
547  You Are a Badass: How to Stop Doubting Your Gr...  Jen Sincero          4.7    14331      8  2017  Non Fiction
548  You Are a Badass: How to Stop Doubting Your Gr...  Jen Sincero          4.7    14331      8  2018  Non Fiction
549  You Are a Badass: How to Stop Doubting Your Gr...  Jen Sincero          4.7    14331      8  2019  Non Fiction
'''

jl.run()

'''
Podemos ver el uso de memoria con .memory_usage(deep=True)
'''
print(df_books.memory_usage(deep=True))
'''
Index            132
Name           59737
Author         39078
User Rating     4400
Reviews         4400
Price           4400
Year            4400
Genre          36440
dtype: int64
'''

jl.run()

'''
Podemos ver cuantos valores tenemos en una fila con .value_count()
'''
print(df_books['Author'].value_counts())
'''
Author
Jeff Kinney                           12
Gary Chapman                          11
Rick Riordan                          11
Suzanne Collins                       11
American Psychological Association    10
                                      ..
Keith Richards                         1
Chris Cleave                           1
Alice Schertle                         1
Celeste Ng                             1
Adam Gasiewski                         1
Name: count, Length: 248, dtype: int64
'''

jl.run()

'''
Para limpiar dupicados usamos .drop_duplicates()
'''

# Duplicamos una linea
df = df_books._append(df_books.iloc[0])
print(df.head(2),df.tail(2))
'''
                            Name        Author  User Rating  Reviews  Price  Year        Genre
0  10-Day Green Smoothie Cleanse      JJ Smith          4.7    17350      8  2016  Non Fiction
1              11/22/63: A Novel  Stephen King          4.6     2052     22  2011      Fiction                                      
             Name       Author  User Rating  Reviews  Price  Year        Genre
549  You Are a Badass: How to Stop Doubting Your Gr...  Jen Sincero          4.7    14331      8  2019  Non Fiction
0                        10-Day Green Smoothie Cleanse     JJ Smith          4.7    17350      8  2016  Non Fiction
'''

jl.run()

'''
Eliminamos los duplicados
Si quisieramos mantener el ultimo usamos .drop_duplicates(keep='last)
'''

df = df.drop_duplicates()
print(df.head(2),df.tail(2))
'''
                            Name        Author  User Rating  Reviews  Price  Year        Genre
0  10-Day Green Smoothie Cleanse      JJ Smith          4.7    17350      8  2016  Non Fiction
1              11/22/63: A Novel  Stephen King          4.6     2052     22  2011      Fiction                                      
             Name       Author  User Rating  Reviews  Price  Year        Genre
548  You Are a Badass: How to Stop Doubting Your Gr...  Jen Sincero          4.7    14331      8  2018  Non Fiction
549  You Are a Badass: How to Stop Doubting Your Gr...  Jen Sincero          4.7    14331      8  2019  Non Fiction
'''

jl.run()

'''
Podemos ordenar los valores por columna con .sort_values()
Por default sera de menor a mayor, para hacerlo al reves usamos
.sort_values('Columna',ascending='False')
'''
print(df_books.sort_values('Year').head(3))
print('-'*15)
print(df_books.sort_values('Year',ascending=False).head(3))




