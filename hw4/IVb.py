import numpy as np

parents = [[3,6,5,1,2,4], [2,3,1,5,6,4]]
cycles = []

idx = 0
used = [0 for x in range(len(parents[0]))]
while True:
    cycle = []
    while(True):
        if idx in cycle:
            break
    
        cycle.append(idx)
        used[idx] = 1
        second = (1+1)%2
        nextItem = parents[second][idx]
        idx = parents[1].index(nextItem)
    cycles.append(cycle)
    if np.sum(used) >= 6:
        break
    for i in range(6):
        if(used[i] == 0):
            idx = i
            break

children = [[0 for i in range(6)] for _ in range(2)]

for i in range(len(cycles)):
    for x in cycles[i]:
        children[0][x] = parents[i%2][x]
        children[1][x] = parents[(i+1)%2][x]
print('Cycle crossover:')
print(children)