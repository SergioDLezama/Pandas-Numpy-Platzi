import pandas as pd
import jumpline as jl

'''
Para leer archivos csv .read_csv('path',sep=',',header=posicion,names=[nombre1,nombre2...])
Por default el separador es comma, en caso que sea uno diferente hay que especificarlo
Muchas veces el documento no viene con el header puesto, nosotros tenemos que especificar la posicion. 
    En caso que sea ninguno colocamos None
    Tambien podemos cargar los nombres que querramos de header en orden de las filas
'''

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

# Para solo ver las columnas
df_books_columns = df_books.columns
print(df_books_columns)
# Index(['Name', 'Author', 'User Rating', 'Reviews', 'Price', 'Year', 'Genre'], dtype='object')

jl.run()

'''
Para leer archivos json
'''

json = pd.read_json('./hpcharactersdataraw.json')
print(json)
''' Print
                      Name  ...                                     Profession
0              Mrs. Abbott  ...                                        Unknown
1            Hannah Abbott  ...                 Landlady of the Leaky Cauldron
2            Abel Treetops  ...                                        Unknown
3         Euan Abercrombie  ...                                        Unknown
4     Aberforth Dumbledore  ...                                         Barman
...                    ...  ...                                            ...
1935        Georgi Zdravko  ...                      Quidditch player (Seeker)
1936                Zograf  ...                      Quidditch player (Keeper)
1937                 Zonko  ...                                        Unknown
1938     Valentina Vázquez  ...  President of the Argentinian Council of Magic
1939         Zygmunt Budge  ...    Potions Master, Potioneer, Inventor, Author
'''

jl.run()

# Podemos especificar que tipo queremos que nos lea el json. En este caso Series de pandas

json_series = pd.read_json('./hpcharactersdataraw.json',typ='Series')
print(json_series)
