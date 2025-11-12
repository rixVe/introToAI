import numpy as np

A = '101100'
B = '011001'
C = '001001'

items = [
    (2,10),
    (1,2),
    (3,20),
    (1,10),
    (2,15),
    (4,30)
]

valA = np.sum([items[i][1] if A[i] == '1' else 0 for i in range(len(A))])
weighA = np.sum([items[i][0] if A[i] == '1' else 0 for i in range(len(A))])

valB = np.sum([items[i][1] if B[i] == '1' else 0 for i in range(len(A))])
weighB = np.sum([items[i][0] if B[i] == '1' else 0 for i in range(len(A))])

valC = np.sum([items[i][1] if C[i] == '1' else 0 for i in range(len(A))])
weighC = np.sum([items[i][0] if C[i] == '1' else 0 for i in range(len(A))])

print('A:', valA if weighA <=7 else 0)
print('B:', valB if weighB <=7 else 0)
print('C:', valC if weighC <=7 else 0)

print('Best is max - C')