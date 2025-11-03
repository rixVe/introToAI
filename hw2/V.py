import numpy as np
import pandas as pd

cost = pd.read_csv('hw2/cost.csv', index_col=0)
conf = pd.read_csv('hw2/confusion.csv', index_col=0)

total = 0
for i in range(4):
    for j in range(4):
        total += cost.iat[i,j]*conf.iat[i,j]
        
print(total)