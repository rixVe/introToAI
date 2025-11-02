import pandas as pd
import numpy as np

# wanted to try doing it by hand
rep = pd.DataFrame(
    {
        'Document': [
            "D1",
            "D2",
        ],
        "U1": [
            0.2,
            0.7
        ],
        "U2": [
            0.5,
            0.2
        ],
        "U3": [
            0.7,
            0.6
        ],
        "U4": [
            0.7,
            0.3
        ],
        "U5": [
            0.8,
            0.6
        ],
    }
)


simmilarity = pd.read_csv("simmI.csv", index_col=0)


rep.set_index('Document', inplace=True)
minsim = simmilarity.min().min()
row, col = (simmilarity == minsim).stack().idxmax()
print(row, col)

centr1 = row
centr2 = col

cluster1 = list()
cluster2 = list()


for series in simmilarity:
    s1 = simmilarity.at[centr1, series]
    s2 = simmilarity.at[centr2, series]
    if s1 >= s2:
        cluster1.append(series)
    else:
        cluster2.append(series)
        
print("C1: ", cluster1)
print("C2: ", cluster2)

centr3 = 'U3'
centr4 = 'U4'

cluster3 = list()
cluster4 = list()


for series in simmilarity:
    s1 = simmilarity.at[centr3, series]
    s2 = simmilarity.at[centr4, series]
    if s1 >= s2:
        cluster3.append(series)
    else:
        cluster4.append(series)
        
print("C3: ", cluster3)
print("C4: ", cluster4)


J = 0

for item in cluster1:
    J += simmilarity.at[centr1, item]    
for item in cluster2:
    J += simmilarity.at[centr2, item]        
    
print(J)

nCentr1 = np.mean([rep.at['D1', x] for x in cluster2])
nCentr2 = np.mean([rep.at['D2', x] for x in cluster2])
print(nCentr1, nCentr2)
