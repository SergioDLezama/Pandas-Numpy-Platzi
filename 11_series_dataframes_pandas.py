import pandas as pd
import jumpline as jl

'''
Para definir una serie pd.Series([elementos separados por coma], index=[indice separado por coma])
'''

psg_players = pd.Series(['Navas','Mbappe','Neymar','Messi'], 
          index=[1,7,10,30])
print(psg_players)
'''
1      Navas
7     Mbappe
10    Neymar
30     Messi
dtype: object
'''
jl.run()

# Si no definimos el indice. Se le asigna un indice iniciando en 0
psg_players_noindex = pd.Series(['Navas','Mbappe','Neymar','Messi'])
print(psg_players_noindex)
'''
0     Navas
1    Mbappe
2    Neymar
3     Messi
dtype: object
'''
jl.run()

# Tambien podemos definir Series mediante un diccionario de py
dict = {1:'Navas', 7:'Mbappe', 10:'Neymar', 30:'Messi'}
print('Diccionario:')
print(dict) # {1: 'Navas', 7: 'Mbappe', 10: 'Neymar', 30: 'Messi'}

print('\nSeries:')
psg_players_2 = pd.Series(dict)
print(psg_players_2)
'''
1      Navas
7     Mbappe
10    Neymar
30     Messi
dtype: object
'''

jl.run()

# Podemos acceder a ciertos elementos de el Series
player_1 = psg_players[1]
print(player_1) # 'Navas'

player_7 = psg_players[7]
print(player_7) # 'Mbappe'

jl.run()

# Podemos hacer slicing

slice_players = psg_players[0:3]
print(slice_players)
'''
1      Navas
7     Mbappe
10    Neymar
dtype: object
'''

jl.run()

'''
Para definir un DataFrame en pandas
'''

players_dict={'Jugador':['Navas','Mbappe','Neymar','Messi'],
              'Altura':[183.0,170.0,170.0,165.0],
              'Goles':[2,200,220,150]}

df_players = pd.DataFrame(players_dict,index=[1,7,10,30])
print(df_players)
'''
   Jugador  Altura  Goles
1    Navas   183.0      2
7   Mbappe   170.0    200
10  Neymar   170.0    220
30   Messi   165.0    150
'''

jl.run()

# Podemos acceder a las columnas
columnas_players = df_players.columns
print(columnas_players) # Index(['Jugador', 'Altura', 'Goles'], dtype='object')

# Podemos acceded a los indices
index_players = df_players.index
print(index_players)

