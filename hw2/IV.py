import numpy as np
import pandas as pd

conf = pd.read_csv('hw2/confusion.csv', index_col=0)
print(conf)

good = sum([conf.iat[x,x] for x in range(4)])
allg = sum([conf.iat[x,y] for x in range(4) for y in range(4)])
print('Classification accuracy: ', good/allg)
print('Missclassification error: ',1- good/allg)
