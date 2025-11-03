import pandas as pd
import numpy as np

simm = pd.read_csv('hw2/simmilarities.csv', index_col=0)

simm.sort_values(by=['sY'], axis=1, inplace=True,ascending=False)
classes = dict()
classes['A'] = 0
classes['B'] = 0
classes['C'] = 0
for i in range(4):

    classes[simm.iat[0,i].lstrip()] += 1
    
mx = max(classes, key=classes.get)
print("Majority")
print("Scores")
print(classes)
print("Recommended")
print(mx)

classes['A'] = 0
classes['B'] = 0
classes['C'] = 0
for i in range(4):

    classes[simm.iat[0,i].lstrip()] += float(simm.iat[1,i])
    
mx = max(classes, key=classes.get)
print("Weighted")
print("Scores")
print(classes)
print("Recommended")
print(mx)

classes['A'] = 0
classes['B'] = 0
classes['C'] = 0
for i in range(7):

    classes[simm.iat[0,i].lstrip()] += 1 
    
mx = max(classes, key=classes.get)
print("Majority 7")
print("Scores")
print(classes)
print("Recommended")
print(mx)


print("Minimal k:")
def majority(n):
    global classes
    global simm
    classes['A'] = 0
    classes['B'] = 0
    classes['C'] = 0
    for i in range(n):
    
        classes[simm.iat[0,i].lstrip()] += 1 
        
    mx = max(classes, key=classes.get)
    return mx 
for i in range(1, 11):
    if(majority(i) == 'A'):
        print(i)
        break
    
