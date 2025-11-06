import numpy as np
import pandas as pd

collection = pd.read_csv('hw2/document.csv', index_col=1)

binary = pd.read_csv('hw2/binaryrep.csv', index_col=0)

for i in range(3):
    binary.iat[4,i] = 1 if collection.at[str('D5'), 'Content'].count(str('T' + str(i+1))) > 0 else 0
print(binary)

a = sum([1 if binary.at['D' + str(x), 'Class']=='A' else 0 for x in range(1,6)])
print('P(A)')
print(a/5)
a1 = sum([1 if (binary.at['D' + str(x), 'Class']=='A' and  binary.at['D' + str(x), 'T3']==1 )else 0 for x in range(1,6)])
print('P(T3=1|A)')
print(a1/a)

print('P(A|D6)')
print(a/5 * 2/3 * 2/3 * a1/a)

print("Assigned to ", 'A' if a/5 * 2/3 * 2/3 * a1/a > 0.02 else 'B')
print("Because ", a/5 * 2/3 * 2/3 * a1/a, " is bigger than 0.02")

bow = binary.copy()
for i in range(3):
    for j in range(6):
        bow.iat[j, i] = collection.iat[j, 1].count("T"+str(i+1))
print(bow)

dicts = 3
print("Dictionary size: ", dicts)

print('P(B) = ', 1 - 3/5)

print('P(T3|B) = ', end='')

bt3 = sum([bow.at['D' + str(x), 'T3'] if bow.at['D' + str(x), 'Class']=='B' else 0 for x in range(1,6)])
pool = sum([bow.iat[x, y] if bow.at['D' + str(x+1), 'Class'] == 'B' else 0 for x in range(5) for y in range(3)])
print((bt3+1)/(pool + dicts))

print('P(B|D6) = ', (1-3/5) * 3/7 * ((bt3+1)/(pool + dicts)) ** bow.at['D6', 'T3'])

print('Assigned to ', end='')
print('A' if 0.039 > (1-3/5) * 3/7 * ((bt3+1)/(pool + dicts)) ** bow.at['D6', 'T3'] else 'B')
print('because 0.039 > ', (1-3/5) * 3/7 * ((bt3+1)/(pool + dicts)) ** bow.at['D6', 'T3'])