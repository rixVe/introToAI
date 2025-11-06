import pandas as pd
import numpy as np

inf = pd.read_csv('hw3/informationIII.csv', index_col=0)

infE = inf[inf.B == 'E']
infG = inf[inf.B == 'G']

countE = len(infE[infE.D == 'Y'])
countG = len(infG[infG.D == 'Y'])

if countE/len(infE) > 2/3 or countE/len(infE) < 1/3:
    print("Leftmost expanded") 
else:
    print('Leftmost not expanded')
if countG/len(infG) > 2/3 or countG/len(infG) < 1/3:
    print("Rightmost expanded") 
else:
    print('Rightmost not expanded')