import pandas as pd
#'Numero':[9, 23, 10, 6, 5, 1]
dict = {
        'Jugador':['Luis Suarez','Jorge Molina', 'Antonio Puertas', 'German Sanchez', 'Luis Milla', 'Luis Manuel Arantes Maximiano'],
        'Posicion':['Delantero', 'Delantero', 'Centrocampista', 'Defensa', 'Centrocampista', 'Portero'],
        'Altura':[185.0, 187.0, 185.0, 187.0, 175.0, 190.0],
        'Goles':[7, 7, 5, 2, 2, 0],
        }

df = pd.DataFrame(dict,index=[9,23,10,6,5,1])
print(df)