import pandas as pd
import jumpline as jl

df = pd.read_csv('./bestsellers-with-categories.csv',sep=',',header=0)
print(df)
'''
                                      Name              Author  User Rating  Reviews  Price  Year        Genre
0            10-Day Green Smoothie Cleanse            JJ Smith          4.7    17350      8  2016  Non Fiction
1                        11/22/63: A Novel        Stephen King          4.6     2052     22  2011      Fiction
2  12 Rules for Life: An Antidote to Chaos  Jordan B. Peterson          4.7    18979     15  2018  Non Fiction'''

jl.run()

'''
Funcion .groupby()
'''
df_authors = df.groupby('Author').count()
print(df_authors)
'''
Author
Abraham Verghese               2            2        2      2     2      2
Adam Gasiewski                 1            1        1      1     1      1
Adam Mansbach                  1            1        1      1     1      1
Adir Levy                      1            1        1      1     1      1
Admiral William H. McRaven     1            1        1      1     1      1
...                          ...          ...      ...    ...   ...    ...
Walter Isaacson                3            3        3      3     3      3
William Davis                  2            2        2      2     2      2
William P. Young               2            2        2      2     2      2
Wizards RPG Team               3            3        3      3     3      3
Zhi Gang Sha                   2            2        2      2     2      2
'''

jl.run()

'''
Podemos acceder a los autores porque ahora Authors no es una columna sino un indice
'''
df_authors = df.groupby('Author').sum().loc['Wizards RPG Team']
print(df_authors)
'''
Name           Player's Handbook (Dungeons & Dragons)Player's...
User Rating                                                 14.4
Reviews                                                    50970
Price                                                         81
Year                                                        6054
Genre                                      FictionFictionFiction
Name: Wizards RPG Team, dtype: object
'''

jl.run()

df_authors = df.groupby('Author').count().loc['Wizards RPG Team']
print(df_authors)

'''
Name           3
User Rating    3
Reviews        3
Price          3
Year           3
Genre          3
Name: Wizards RPG Team, dtype: int64
'''

jl.run()

'''
En caso que queramos que Author ya no sea el index usamos .reset_index()
'''
df_authors = df.groupby('Author').sum().reset_index()
print(df_authors)
'''
                         Author                                               Name  User Rating  ...  Price  Year                              Genre
0              Abraham Verghese                 Cutting for StoneCutting for Stone          9.2  ...     22  4021                     FictionFiction
1                Adam Gasiewski  Milk and Vine: Inspirational Quotes From Class...          4.4  ...      6  2017                        Non Fiction
2                 Adam Mansbach                               Go the F**k to Sleep          4.8  ...      9  2011                            Fiction
3                     Adir Levy  What Should Danny Do? (The Power to Choose Ser...          4.8  ...     13  2019                            Fiction
4    Admiral William H. McRaven  Make Your Bed: Little Things That Can Change Y...          4.7  ...     11  2017                        Non Fiction
..                          ...                                                ...          ...  ...    ...   ...                                ...
243             Walter Isaacson              Leonardo da VinciSteve JobsSteve Jobs         13.7  ...     61  6040  Non FictionNon FictionNon Fiction
244               William Davis  Wheat Belly: Lose the Wheat, Lose the Weight, ...          8.8  ...     12  4025             Non FictionNon Fiction
245            William P. Young  The Shack: Where Tragedy Confronts EternityThe...          9.2  ...     16  4026                     FictionFiction
246            Wizards RPG Team  Player's Handbook (Dungeons & Dragons)Player's...         14.4  ...     81  6054              FictionFictionFiction
247                Zhi Gang Sha  Divine Soul Mind Body Healing and Transmission...          9.2  ...     23  4022             Non FictionNon Fiction

[248 rows x 7 columns]
'''

jl.run()

'''
Agrupamiento por determinada funcion de agregacion
'''

# Elimine algunas columnas para ver el min y max en el codigo siguiente
df_2 = df.drop(['Reviews','Genre','Year','Price'],axis=1)

df_authors = df_2.groupby('Author').agg(['min','max'])
print(df_authors.sample())
'''
                                                                         Name                                                    Reviews       
                                                                          min                                                max     min    max     
Author
Abraham Verghese                                            Cutting for Stone                                  Cutting for Stone    4866   4866     
Adam Gasiewski              Milk and Vine: Inspirational Quotes From Class...  Milk and Vine: Inspirational Quotes From Class...    3113   3113     
Adam Mansbach                                            Go the F**k to Sleep                               Go the F**k to Sleep    9568   9568     
Adir Levy                   What Should Danny Do? (The Power to Choose Ser...  What Should Danny Do? (The Power to Choose Ser...    8170   8170     
Admiral William H. McRaven  Make Your Bed: Little Things That Can Change Y...  Make Your Bed: Little Things That Can Change Y...   10199  10199     
...                                                                       ...                                                ...     ...    ...     
Walter Isaacson                                             Leonardo da Vinci                                         Steve Jobs    3014   7827     
William Davis               Wheat Belly: Lose the Wheat, Lose the Weight, ...  Wheat Belly: Lose the Wheat, Lose the Weight, ...    7497   7497     
William P. Young                  The Shack: Where Tragedy Confronts Eternity        The Shack: Where Tragedy Confronts Eternity   19720  19720     
Wizards RPG Team                       Player's Handbook (Dungeons & Dragons)             Player's Handbook (Dungeons & Dragons)   16990  16990     
Zhi Gang Sha                Divine Soul Mind Body Healing and Transmission...  Soul Healing Miracles: Ancient and New Sacred ...      37    220     

[248 rows x 4 columns]
==========
'''

jl.run()

# Otro ejemplo

df_authors = df.groupby('Author').agg({'Reviews':['min','max'],'User Rating':'sum'})
print(df_authors)
'''
                           Reviews        User Rating
                               min    max         sum
Author
Abraham Verghese              4866   4866         9.2
Adam Gasiewski                3113   3113         4.4
Adam Mansbach                 9568   9568         4.8
Adir Levy                     8170   8170         4.8
Admiral William H. McRaven   10199  10199         4.7
...                            ...    ...         ...
Walter Isaacson               3014   7827        13.7
William Davis                 7497   7497         8.8
William P. Young             19720  19720         9.2
Wizards RPG Team             16990  16990        14.4
Zhi Gang Sha                    37    220         9.2

[248 rows x 3 columns]
'''

jl.run()

df_authors = df.groupby(['Author','Year']).count()
print(df_authors)
'''
                       Name  User Rating  Reviews  Price  Genre
Author           Year
Abraham Verghese 2010     1            1        1      1      1
                 2011     1            1        1      1      1
Adam Gasiewski   2017     1            1        1      1      1
Adam Mansbach    2011     1            1        1      1      1
Adir Levy        2019     1            1        1      1      1
...                     ...          ...      ...    ...    ...
Wizards RPG Team 2017     1            1        1      1      1
                 2018     1            1        1      1      1
                 2019     1            1        1      1      1
Zhi Gang Sha     2009     1            1        1      1      1
                 2013     1            1        1      1      1

[493 rows x 5 columns]
'''
