import pandas as pd
import jumpline as jl

df_books =pd.read_csv('./bestsellers-with-categories.csv')
print(df_books)
''' Print:
                                                  Name                    Author  User Rating  Reviews  Price  Year        Genre
0                        10-Day Green Smoothie Cleanse                  JJ Smith          4.7    17350      8  2016  Non Fiction    
1                                    11/22/63: A Novel              Stephen King          4.6     2052     22  2011      Fiction    
2              12 Rules for Life: An Antidote to Chaos        Jordan B. Peterson          4.7    18979     15  2018  Non Fiction    
3                               1984 (Signet Classics)             George Orwell          4.7    21424      6  2017      Fiction    
4    5,000 Awesome Facts (About Everything!) (Natio...  National Geographic Kids          4.8     7665     12  2019  Non Fiction    
..                                                 ...                       ...          ...      ...    ...   ...          ...    
545       Wrecking Ball (Diary of a Wimpy Kid Book 14)               Jeff Kinney          4.9     9413      8  2019      Fiction    
546  You Are a Badass: How to Stop Doubting Your Gr...               Jen Sincero          4.7    14331      8  2016  Non Fiction    
547  You Are a Badass: How to Stop Doubting Your Gr...               Jen Sincero          4.7    14331      8  2017  Non Fiction    
548  You Are a Badass: How to Stop Doubting Your Gr...               Jen Sincero          4.7    14331      8  2018  Non Fiction    
549  You Are a Badass: How to Stop Doubting Your Gr...               Jen Sincero          4.7    14331      8  2019  Non Fiction    

[550 rows x 7 columns]
'''

jl.run()

slice_df = df_books[0:4]
print(slice_df)
'''
                                      Name              Author  User Rating  Reviews  Price  Year        Genre
0            10-Day Green Smoothie Cleanse            JJ Smith          4.7    17350      8  2016  Non Fiction
1                        11/22/63: A Novel        Stephen King          4.6     2052     22  2011      Fiction
2  12 Rules for Life: An Antidote to Chaos  Jordan B. Peterson          4.7    18979     15  2018  Non Fiction
3                   1984 (Signet Classics)       George Orwell          4.7    21424      6  2017      Fiction
'''

jl.run()

'''
Para acceder a cierta columna, especificamos el header
'''
name_df = df_books['Name']
print(name_df)
'''
0                          10-Day Green Smoothie Cleanse
1                                      11/22/63: A Novel
2                12 Rules for Life: An Antidote to Chaos
3                                 1984 (Signet Classics)
4      5,000 Awesome Facts (About Everything!) (Natio...
                             ...
545         Wrecking Ball (Diary of a Wimpy Kid Book 14)
546    You Are a Badass: How to Stop Doubting Your Gr...
547    You Are a Badass: How to Stop Doubting Your Gr...
548    You Are a Badass: How to Stop Doubting Your Gr...
549    You Are a Badass: How to Stop Doubting Your Gr...
Name: Name, Length: 550, dtype: object
'''

jl.run()

'''
Igualmente podemos acceder a varias columnas, nombrando las columnas y poniendola entre otros []
'''
name_author_df = df_books[['Name','Author']]
print(name_author_df)
'''
                                                  Name                    Author
0                        10-Day Green Smoothie Cleanse                  JJ Smith
1                                    11/22/63: A Novel              Stephen King
2              12 Rules for Life: An Antidote to Chaos        Jordan B. Peterson
3                               1984 (Signet Classics)             George Orwell
4    5,000 Awesome Facts (About Everything!) (Natio...  National Geographic Kids
..                                                 ...                       ...
545       Wrecking Ball (Diary of a Wimpy Kid Book 14)               Jeff Kinney
546  You Are a Badass: How to Stop Doubting Your Gr...               Jen Sincero
547  You Are a Badass: How to Stop Doubting Your Gr...               Jen Sincero
548  You Are a Badass: How to Stop Doubting Your Gr...               Jen Sincero
549  You Are a Badass: How to Stop Doubting Your Gr...               Jen Sincero

[550 rows x 2 columns]
'''

jl.run()

'''
Si quisieramos solo ciertas filas usamos .loc[inicio:fin]

'''

df_4_9 = df_books.loc[4:9]
print(df_4_9)
'''
                                                Name                    Author  User Rating  Reviews  Price  Year        Genre      
4  5,000 Awesome Facts (About Everything!) (Natio...  National Geographic Kids          4.8     7665     12  2019  Non Fiction      
5      A Dance with Dragons (A Song of Ice and Fire)       George R. R. Martin          4.4    12643     11  2011      Fiction      
6  A Game of Thrones / A Clash of Kings / A Storm...       George R. R. Martin          4.7    19735     30  2014      Fiction      
7                     A Gentleman in Moscow: A Novel               Amor Towles          4.7    19699     15  2017      Fiction      
8      A Higher Loyalty: Truth, Lies, and Leadership               James Comey          4.7     5983      3  2018  Non Fiction      
9                          A Man Called Ove: A Novel           Fredrik Backman          4.6    23848      8  2016      Fiction
'''
jl.run()

'''
Para filtrar filas y columnas
'''

df = df_books.loc[4:9, ['Name', 'Author']]
print(df)
'''
                                                Name                    Author
4  5,000 Awesome Facts (About Everything!) (Natio...  National Geographic Kids
5      A Dance with Dragons (A Song of Ice and Fire)       George R. R. Martin
6  A Game of Thrones / A Clash of Kings / A Storm...       George R. R. Martin
7                     A Gentleman in Moscow: A Novel               Amor Towles
8      A Higher Loyalty: Truth, Lies, and Leadership               James Comey
9                          A Man Called Ove: A Novel           Fredrik Backman
'''

jl.run()

'''
Podemos aplicar operaciones matematicas a los datos numericos
'''

df = df_books.loc[:,['Reviews']] * -1
print(df)
'''
     Reviews
0     -17350
1      -2052
2     -18979
3     -21424
4      -7665
..       ...
545    -9413
546   -14331
547   -14331
548   -14331
549   -14331

[550 rows x 1 columns]
'''

jl.run()

'''
Igualmente podemos poner condicionales
'''
df = df_books.loc[:,['Author']] == 'JJ Smith'
print(df)
'''
     Author
0      True
1     False
2     False
3     False
4     False
..      ...
545   False
546   False
547   False
548   False
549   False

[550 rows x 1 columns]
'''

jl.run()

'''
Funcion .iloc
Trabaja similar a .loc pero aqui filtramos por indice
'''

df = df_books.iloc[:]
print(df)
'''
                                                  Name                    Author  User Rating  Reviews  Price  Year        Genre
0                        10-Day Green Smoothie Cleanse                  JJ Smith          4.7    17350      8  2016  Non Fiction    
1                                    11/22/63: A Novel              Stephen King          4.6     2052     22  2011      Fiction    
2              12 Rules for Life: An Antidote to Chaos        Jordan B. Peterson          4.7    18979     15  2018  Non Fiction    
3                               1984 (Signet Classics)             George Orwell          4.7    21424      6  2017      Fiction    
4    5,000 Awesome Facts (About Everything!) (Natio...  National Geographic Kids          4.8     7665     12  2019  Non Fiction    
..                                                 ...                       ...          ...      ...    ...   ...          ...    
545       Wrecking Ball (Diary of a Wimpy Kid Book 14)               Jeff Kinney          4.9     9413      8  2019      Fiction    
546  You Are a Badass: How to Stop Doubting Your Gr...               Jen Sincero          4.7    14331      8  2016  Non Fiction    
547  You Are a Badass: How to Stop Doubting Your Gr...               Jen Sincero          4.7    14331      8  2017  Non Fiction    
548  You Are a Badass: How to Stop Doubting Your Gr...               Jen Sincero          4.7    14331      8  2018  Non Fiction    
549  You Are a Badass: How to Stop Doubting Your Gr...               Jen Sincero          4.7    14331      8  2019  Non Fiction    

[550 rows x 7 columns]
'''

jl.run()

'''
Con iloc podemos acceder a las columnas con su indice
'''
df = df_books.iloc[:,0:3]
print(df)
'''
                                                  Name                    Author  User Rating
0                        10-Day Green Smoothie Cleanse                  JJ Smith          4.7
1                                    11/22/63: A Novel              Stephen King          4.6
2              12 Rules for Life: An Antidote to Chaos        Jordan B. Peterson          4.7
3                               1984 (Signet Classics)             George Orwell          4.7
4    5,000 Awesome Facts (About Everything!) (Natio...  National Geographic Kids          4.8
..                                                 ...                       ...          ...
545       Wrecking Ball (Diary of a Wimpy Kid Book 14)               Jeff Kinney          4.9
546  You Are a Badass: How to Stop Doubting Your Gr...               Jen Sincero          4.7
547  You Are a Badass: How to Stop Doubting Your Gr...               Jen Sincero          4.7
548  You Are a Badass: How to Stop Doubting Your Gr...               Jen Sincero          4.7
549  You Are a Badass: How to Stop Doubting Your Gr...               Jen Sincero          4.7

[550 rows x 3 columns]
'''

jl.run()

# Podemos acceder a elementos por su indice

df = df_books.iloc[1,3]
print(df) # 2052

df = df_books.iloc[50,1]
print(df) # Francis Chan

jl.run()

df = df_books.iloc[:2,2:]
print(df)
