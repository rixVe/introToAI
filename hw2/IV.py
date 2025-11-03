import numpy as np
import pandas as pd

conf = pd.read_csv('hw2/confusion.csv', index_col=0)
print(conf)

good = sum([conf.iat[x,x] for x in range(4)])
allg = sum([conf.iat[x,y] for x in range(4) for y in range(4)])
print('Classification accuracy: ', good/allg)
print('Missclassification error: ',1- good/allg)
conf['s'] = conf.sum(axis=1)
conf.loc['s'] = conf.sum()

print('Recall for C1 = ', conf.at['Actual C1', 'Predicted C1']/conf.at['Actual C1', 's'])
print('Recall for C4 = ', conf.at['Actual C4', 'Predicted C4']/conf.at['Actual C4', 's'])

print('Precision for C2 = ', conf.at['Actual C2', 'Predicted C2']/conf.at['s', 'Predicted C2'])
print('Precision for C3 = ', conf.at['Actual C3', 'Predicted C3']/conf.at['s', 'Predicted C3'])

