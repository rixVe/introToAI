import numpy as np
import pandas as pd

base = pd.read_csv("hw2/template.csv", index_col=0)
binary = base.copy()
bow = base.copy()

D1 = "artificial intelligence artificial intelligence".split()
D2 = "artificial artificial introduction".split()
D3 = "artificial intelligence introduction artificial".split()

T = ["artificial","intelligence","introduction"]

Docs = [D1, D2, D3]

for i in range(len(Docs)):
    counter = 0
    for t in binary:
        j = i+1
        a = "D" + str(j)
        binary.at[a, t] = 1 if Docs[i].count(T[counter]) > 0 else 0
        counter +=1
print('Binary:')
print(binary)


bow[:] = 0.0
for i in range(len(Docs)):
    counter = 0
    for t in bow:
        j = i+1
        a = "D" + str(j)
        bow.at[a,t] += Docs[i].count(T[counter])
        counter +=1
print('BOW:')
print(bow)

tf = bow.copy()

for idx, row in tf.iterrows():
    mx = row.max()
    for t in tf:
        tf.at[idx, t] /= mx
        
print('TF:')
print(tf)

J1 = 'D1'
J2 = 'D2'
inter = sum([1 if (binary.at[J1, x] == 1 and binary.at[J2, x] == 1) else 0 for x in binary])
s = sum([1 if (binary.at[J1, x] == 1 or binary.at[J2, x] == 1) else 0 for x in binary])
print('Jac(D1,D2)')
print(inter/s)

J1 = 'D1'
J2 = 'D3'
inter = sum([1 if (binary.at[J1, x] == 1 and binary.at[J2, x] == 1) else 0 for x in binary])
s = sum([1 if (binary.at[J1, x] == 1 or binary.at[J2, x] == 1) else 0 for x in binary])
print('Jac(D1,D3)')
print(inter/s)

C1 = 'D1'
C2 = 'D3'
Cu = sum([tf.at[C1, x]*tf.at[C2, x] for x in tf])
Cl = np.sqrt(sum([tf.at[C1, x]**2 for x in tf]) + sum([tf.at[C2, x]**2 for x in tf]))
print('cos(D1,D3)')
print(Cu/Cl)