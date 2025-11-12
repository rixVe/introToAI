parents = [[3,6,5,1,2,4], [2,3,1,5,6,4]]

part = (1,3)

children = [[0 for k in range(6)] for _ in range(2)]

# part that is the same as in the parent
added = []
for i in range(2):
    added.append(parents[i][part[0]:part[1]+1])
    children[i] = children[i][:part[0]] + parents[i][part[0]:part[1]+1] + children[i][part[1]+1:]

for i in range(2):
    addList = []
    ChildIndex = part[1] + 1
    for j in range(6):
        k = (part[1] + 1 + j)%6
        ChildIndex %= 6
        if parents[(i+1)%2][k] not in added[i]:
            children[i][ChildIndex] = parents[(i+1)%2][k]
            ChildIndex += 1
print('Order 1 crossover: ')
print(children)