import pandas as pd
import jumpline as jl

'''
Apply se usa para aplicar funciones a nuestro database
'''

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

# Definimos una funcion sencilla
def two_times(value):
    return value * 2

jl.run()

df_funct = df['User Rating'].apply(two_times)
print(df_funct.head(5))
'''
0    9.4
1    9.2
2    9.4
3    9.4
4    9.6
'''

jl.run()

'''Podemos agregar esta columna a nuestro df'''

df['Rating_2'] = df_funct
print(df.head(5))
'''
                                                Name                    Author  User Rating  Reviews  Price  Year        Genre  Rating_2
0                      10-Day Green Smoothie Cleanse                  JJ Smith          4.7    17350      8  2016  Non Fiction       9.4
1                                  11/22/63: A Novel              Stephen King          4.6     2052     22  2011      Fiction       9.2
2            12 Rules for Life: An Antidote to Chaos        Jordan B. Peterson          4.7    18979     15  2018  Non Fiction       9.4
3                             1984 (Signet Classics)             George Orwell          4.7    21424      6  2017      Fiction       9.4
4  5,000 Awesome Facts (About Everything!) (Natio...  National Geographic Kids          4.8     7665     12  2019  Non Fiction       9.6
'''
jl.run()

'''Igualmente podemos aplicar funciones lambda'''
df_funct = df['User Rating'].apply(lambda x : x * 3)
print(df_funct.head(5))
'''
0    14.1
1    13.8
2    14.1
3    14.1
4    14.4
'''

jl.run()

'''Podemos aplicar lambdas a varias partes de nuestro DF'''
df_funct = df.apply(lambda x : x['User Rating'] * 2 if x['Genre'] == 'Fiction'else x['User Rating'],axis=1)
print(df_funct.head())
'''
0    4.7
1    9.2
2    4.7
3    9.4
4    4.8
dtype: float64
'''

jl.run()

df['Rating_2'] = df.apply(lambda x : x['User Rating'] * 2 if x['Genre'] == 'Fiction'else x['User Rating'],axis=1)
print(df)
'''
                                                  Name                    Author  User Rating  Reviews  Price  Year        Genre  Rating_2
0                        10-Day Green Smoothie Cleanse                  JJ Smith          4.7    17350      8  2016  Non Fiction       4.7
1                                    11/22/63: A Novel              Stephen King          4.6     2052     22  2011      Fiction       9.2
2              12 Rules for Life: An Antidote to Chaos        Jordan B. Peterson          4.7    18979     15  2018  Non Fiction       4.7
3                               1984 (Signet Classics)             George Orwell          4.7    21424      6  2017      Fiction       9.4
4    5,000 Awesome Facts (About Everything!) (Natio...  National Geographic Kids          4.8     7665     12  2019  Non Fiction       4.8
..                                                 ...                       ...          ...      ...    ...   ...          ...       ...
545       Wrecking Ball (Diary of a Wimpy Kid Book 14)               Jeff Kinney          4.9     9413      8  2019      Fiction       9.8
546  You Are a Badass: How to Stop Doubting Your Gr...               Jen Sincero          4.7    14331      8  2016  Non Fiction       4.7
547  You Are a Badass: How to Stop Doubting Your Gr...               Jen Sincero          4.7    14331      8  2017  Non Fiction       4.7
548  You Are a Badass: How to Stop Doubting Your Gr...               Jen Sincero          4.7    14331      8  2018  Non Fiction       4.7
549  You Are a Badass: How to Stop Doubting Your Gr...               Jen Sincero          4.7    14331      8  2019  Non Fiction       4.7

[550 rows x 8 columns]
'''


