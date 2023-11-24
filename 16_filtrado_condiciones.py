import pandas as pd
import numpy as np
import jumpline as jl

# Leemos nuestro csv
df_books = pd.read_csv('./bestsellers-with-categories.csv')
print(df_books.head(2))
'''
                            Name        Author  User Rating  Reviews  Price  Year        Genre
0  10-Day Green Smoothie Cleanse      JJ Smith          4.7    17350      8  2016  Non Fiction
1              11/22/63: A Novel  Stephen King          4.6     2052     22  2011      Fiction
'''

jl.run()

# Tenemos en bool los elementos que cumplen con nuestra condicion
mayor_2016 = df_books['Year'] > 2016
print(mayor_2016)
'''
0      False
1      False
2       True
3       True
4       True
       ...
545     True
546    False
547     True
548     True
549     True
'''

jl.run()

'''
Igualmente podemos aplicar la condicion sin definir una variable
df_books[df_books['Year'] > 2016]
'''


# De esta forma podemos ver solo los elementos que cumplen con nuestra condicon
print(df_books[mayor_2016]) 
'''
                                                  Name                    Author  User Rating  Reviews  Price  Year        Genre    
2              12 Rules for Life: An Antidote to Chaos        Jordan B. Peterson          4.7    18979     15  2018  Non Fiction    
3                               1984 (Signet Classics)             George Orwell          4.7    21424      6  2017      Fiction    
4    5,000 Awesome Facts (About Everything!) (Natio...  National Geographic Kids          4.8     7665     12  2019  Non Fiction    
7                       A Gentleman in Moscow: A Novel               Amor Towles          4.7    19699     15  2017      Fiction    
8        A Higher Loyalty: Truth, Lies, and Leadership               James Comey          4.7     5983      3  2018  Non Fiction    
..                                                 ...                       ...          ...      ...    ...   ...          ...    
544                                             Wonder             R. J. Palacio          4.8    21625      9  2017      Fiction    
545       Wrecking Ball (Diary of a Wimpy Kid Book 14)               Jeff Kinney          4.9     9413      8  2019      Fiction    
547  You Are a Badass: How to Stop Doubting Your Gr...               Jen Sincero          4.7    14331      8  2017  Non Fiction    
548  You Are a Badass: How to Stop Doubting Your Gr...               Jen Sincero          4.7    14331      8  2018  Non Fiction    
549  You Are a Badass: How to Stop Doubting Your Gr...               Jen Sincero          4.7    14331      8  2019  Non Fiction    

[150 rows x 7 columns]
'''

jl.run()

# Podemos usar cualquier tipo de condicion de python y varias el mismo tiempo
genre_diction = df_books['Genre'] == 'Fiction'

print(df_books[genre_diction & mayor_2016])
'''
                                                  Name             Author  User Rating  Reviews  Price  Year    Genre
3                               1984 (Signet Classics)      George Orwell          4.7    21424      6  2017  Fiction
7                       A Gentleman in Moscow: A Novel        Amor Towles          4.7    19699     15  2017  Fiction
10                           A Man Called Ove: A Novel    Fredrik Backman          4.6    23848      8  2017  Fiction
13                    A Wrinkle in Time (Time Quintet)  Madeleine L'Engle          4.5     5153      5  2018  Fiction
40            Brown Bear, Brown Bear, What Do You See?    Bill Martin Jr.          4.9    14344      5  2017  Fiction
..                                                 ...                ...          ...      ...    ...   ...      ...
509                              To Kill a Mockingbird         Harper Lee          4.8    26234      7  2019  Fiction
529  What Should Danny Do? (The Power to Choose Ser...          Adir Levy          4.8     8170     13  2019  Fiction
534                            Where the Crawdads Sing        Delia Owens          4.8    87841     15  2019  Fiction
544                                             Wonder      R. J. Palacio          4.8    21625      9  2017  Fiction
545       Wrecking Ball (Diary of a Wimpy Kid Book 14)        Jeff Kinney          4.9     9413      8  2019  Fiction

[65 rows x 7 columns]
'''

jl.run()

'''
En caso que querramos la condicion contraria, por ejemplo de mayor a 2016
a menor de 2016. Sin hacer otra condicion booleana con ~ pandas niega la condicion 
Hay que poner el ~ antes de la condicion
'''
print(df_books[~mayor_2016])
'''
                                                  Name               Author  User Rating  Reviews  Price  Year        Genre
0                        10-Day Green Smoothie Cleanse             JJ Smith          4.7    17350      8  2016  Non Fiction
1                                    11/22/63: A Novel         Stephen King          4.6     2052     22  2011      Fiction
5        A Dance with Dragons (A Song of Ice and Fire)  George R. R. Martin          4.4    12643     11  2011      Fiction
6    A Game of Thrones / A Clash of Kings / A Storm...  George R. R. Martin          4.7    19735     30  2014      Fiction
9                            A Man Called Ove: A Novel      Fredrik Backman          4.6    23848      8  2016      Fiction
..                                                 ...                  ...          ...      ...    ...   ...          ...
540                                             Wonder        R. J. Palacio          4.8    21625      9  2013      Fiction
541                                             Wonder        R. J. Palacio          4.8    21625      9  2014      Fiction
542                                             Wonder        R. J. Palacio          4.8    21625      9  2015      Fiction
543                                             Wonder        R. J. Palacio          4.8    21625      9  2016      Fiction
546  You Are a Badass: How to Stop Doubting Your Gr...          Jen Sincero          4.7    14331      8  2016  Non Fiction

[400 rows x 7 columns]
'''