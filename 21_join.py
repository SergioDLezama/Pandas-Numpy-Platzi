import numpy as np
import pandas as pd
import jumpline as jl

'''Join, tambien usada para una combinacion
a diferencia de merge, join ira directamente a los indices'''

left = pd.DataFrame(
    {'A':['A0','A1','A2'],
     'B':['B0','B1','B2']},
     index=['k0','k1','k2'])

right = pd.DataFrame(
    {'C':['C0','C1','C2'],
     'D':['D0','D1','D2']},
     index=['k0','k2','k3'])

print('Left:\n',left)
print('-'*15)
print('Right:\n',right)

jl.run()

left_right = left.join(right) # Se hace un left join
print(left_right)
'''
     A   B    C    D
k0  A0  B0   C0   D0
k1  A1  B1  NaN  NaN
k2  A2  B2   C1   D1
'''

jl.run()

'''Si quisieramos hacer un inner join'''
inner = left.join(right,how='inner') # Se hace un inner join
print(inner)
'''
     A   B   C   D
k0  A0  B0  C0  D0
k2  A2  B2  C1  D1
'''
jl.run()

'''Si quisieramos hacer un right join'''
right_left = left.join(right,how='right') # Se hace un right join
print(right_left)
'''
      A    B   C   D
k0   A0   B0  C0  D0
k2   A2   B2  C1  D1
k3  NaN  NaN  C2  D2
''' 

jl.run()

'''Si quisieramos hacer un outer join'''
outer = left.join(right,how='outer') # Se hace un outer join
print(outer)
'''
      A    B    C    D
k0   A0   B0   C0   D0
k1   A1   B1  NaN  NaN
k2   A2   B2   C1   D1
k3  NaN  NaN   C2   D2
''' 

