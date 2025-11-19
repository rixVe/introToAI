import pandas as pd
import numpy as np

alternatives = pd.read_csv('hw5/alterII.csv', index_col=0)
criteria = pd.read_csv('hw5/criteriaII.csv', index_col=0)

cuttingLevel = 0.6

# (a,c)
# g1 up (gain type) g2 down (cost type)

print('(a,c)')
print('   C1(x,y)',end=' ')
diff1 = alternatives.at['a', 'g1'] - alternatives.at['c','g1']
c1ac = 0
if diff1 >= -criteria.at['q', 'g1']:
    c1ac = 1
elif diff1 <= -criteria.at['p', 'g1']:
    c1ac = 0
else:
    c1ac = (criteria.at['p', 'g1']+ diff1)/(criteria.at['p','g1'] - criteria.at['q','g1'])
print(c1ac)

print('   C2(x,y)',end=' ')
diff2 = alternatives.at['a', 'g2'] - alternatives.at['c','g2']
c2ac = 0
if -diff2 >= -criteria.at['q', 'g2']:
    c2ac = 1
elif -diff2 <= -criteria.at['p', 'g2']:
    c2ac = 0
else:
    c2ac = (criteria.at['p', 'g2'] - diff2)/(criteria.at['p','g2'] - criteria.at['q','g2'])
print(c2ac)
print('   C(x,y) ', end='')
C1 = (c1ac*criteria.at['w','g1']+c2ac*criteria.at['w','g2'])/(criteria.at['w','g2'] + criteria.at['w','g1'])
print(C1)
print('   conc? ', end='')
print('1 (yes)' if C1>=cuttingLevel else '0 (no)')
print('   d1(x,y) ',end='')
print('1' if -diff1 >= criteria.at['w', 'g1'] else '0')
print('   d2(x,y) ',end='')
print('1' if diff2 >= criteria.at['w', 'g2'] else '0')

print('   D(x,y) ',end='')
print('1 (yes)' if (-diff1 >= criteria.at['w', 'g1'] or diff2 >= criteria.at['w', 'g2']) else '0 (no)')
print('   xSy? ', end='')
print('YES (1)' if (C1 >= cuttingLevel and not(-diff1 >= criteria.at['w', 'g1'] or diff2 >= criteria.at['w', 'g2'])) else 'NO (0)')


print('(b,c)')
print('   C1(x,y)',end=' ')
diff1 = alternatives.at['b', 'g1'] - alternatives.at['c','g1']
c1ac = 0
if diff1 >= -criteria.at['q', 'g1']:
    c1ac = 1
elif diff1 <= -criteria.at['p', 'g1']:
    c1ac = 0
else:
    c1ac = (criteria.at['p', 'g1']+ diff1)/(criteria.at['p','g1'] - criteria.at['q','g1'])
print(c1ac)

print('   C2(x,y)',end=' ')
diff2 = alternatives.at['b', 'g2'] - alternatives.at['c','g2']
c2ac = 0
if -diff2 >= -criteria.at['q', 'g2']:
    c2ac = 1
elif -diff2 <= -criteria.at['p', 'g2']:
    c2ac = 0
else:
    c2ac = (criteria.at['p', 'g2'] - diff2)/(criteria.at['p','g2'] - criteria.at['q','g2'])
print(c2ac)
print('   C(x,y) ', end='')
C1 = (c1ac*criteria.at['w','g1']+c2ac*criteria.at['w','g2'])/(criteria.at['w','g2'] + criteria.at['w','g1'])
print(C1)
print('   conc? ', end='')
print('1 (yes)' if C1>=cuttingLevel else '0 (no)')
print('   d1(x,y) ',end='')
print('1' if -diff1 >= criteria.at['w', 'g1'] else '0')
print('   d2(x,y) ',end='')
print('1' if diff2 >= criteria.at['w', 'g2'] else '0')

print('   D(x,y) ',end='')
print('1 (yes)' if (-diff1 >= criteria.at['w', 'g1'] or diff2 >= criteria.at['w', 'g2']) else '0 (no)')
print('   xSy? ', end='')
print('YES (1)' if (C1 >= cuttingLevel and not(-diff1 >= criteria.at['w', 'g1'] or diff2 >= criteria.at['w', 'g2'])) else 'NO (0)')