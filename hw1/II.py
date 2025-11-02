import pandas as pd
import numpy as np

simmilarity = pd.read_csv("simmII.csv", index_col=0)
simmilarity2 = simmilarity.copy()
sim = simmilarity.copy()

#Ignore the main diagonal
np.fill_diagonal(simmilarity.values, -1)


maxsim = simmilarity.max().max()
row, col = (simmilarity == maxsim).stack().idxmax()
print("First cluster: ")
print(row,col)

clustern = row+col

simmilarity[clustern] = [np.max([simmilarity.at[row, x], simmilarity.at[col, x]]) for x in simmilarity.index.values.tolist()]
simmilarity.loc[clustern] = [np.max([simmilarity.at[row, x], simmilarity.at[col, x]]) for x in simmilarity]

simmilarity.drop(row, inplace=True)
simmilarity.drop(col, inplace=True)
simmilarity.drop(row, inplace=True,axis=1)
simmilarity.drop(col, inplace=True,axis=1)

simmilarity.at[clustern, clustern] = -1

print("Single link")
print(simmilarity)

simmilarity2[clustern] = [np.mean([simmilarity2.at[row, x], simmilarity2.at[col, x]]) for x in simmilarity2.index.values.tolist()]
simmilarity2.loc[clustern] = [np.mean([simmilarity2.at[row, x], simmilarity2.at[col, x]]) for x in simmilarity2]

simmilarity2.drop(row, inplace=True)
simmilarity2.drop(col, inplace=True)
simmilarity2.drop(row, inplace=True,axis=1)
simmilarity2.drop(col, inplace=True,axis=1)


print("Average link")
print(simmilarity2)

iter = 0

def complete():
    global sim

    tempsim = sim.copy()
    for x in tempsim:
        tempsim.at[x,x] = -1

    maxsim = tempsim.max().max()

    row, col = (tempsim == maxsim).stack().idxmax()

    clustern = row + col
    sim[clustern] = [np.min([sim.at[row, x], sim.at[col, x]]) for x in sim.index.values.tolist()]
    sim.loc[clustern] = [np.min([sim.at[row, x], sim.at[col, x]]) for x in sim]
    sim.at[clustern, clustern] = 1
    
    sim.drop(row, inplace=True)
    sim.drop(col, inplace=True)
    sim.drop(row, inplace=True,axis=1)
    sim.drop(col, inplace=True,axis=1)
    print("Complete-link iteration:", iter)    
    print("Simmilarity: ", maxsim)
    print(sim)
    
    
print(sim)
for i in range(3):
    iter +=1
    complete()
    