import pandas as pd
import numpy as np


print('InformationGlain(D,C) = ', 1-1)
inf = pd.read_csv('hw3/information.csv', index_col=0)

infBE = inf[inf.B=='E']

infAX = infBE[infBE.A == 'X']
infAZ = infBE[infBE.A == 'Z']

DYinAX = len(infAX[infAX.D == 'Y'])
DNinAX = len(infAX[infAX.D == 'N'])

DYinAZ = len(infAZ[infAZ.D == 'Y'])
DNinAZ = len(infAZ[infAZ.D == 'N'])

entAX = 0
if DYinAX > 0:
    entAX -= DYinAX/len(infAX) * np.log2(DYinAX/len(infAX))
if DNinAX > 0:
    entAX -= DNinAX/len(infAX) * np.log2(DNinAX/len(infAX))

entAZ = 0
if DYinAZ > 0:
    entAZ -= DYinAZ/len(infAZ) * np.log2(DYinAZ/len(infAZ))
if DNinAZ > 0:
    entAZ -= DNinAZ/len(infAZ) * np.log2(DNinAZ/len(infAZ))
        
entDA = len(infAX)/(len(infBE))*entAX + len(infAZ)/(len(infBE))*entAZ

print('Ent(D,A) =',entDA)
print('InformationGain(D,A) =',1-entDA)

print("A" if 1-entDA > 0 else "C", " will be selected.")


# gain ratio = informationGain/splitinformation
# where splitinformation is defined as sum o
entD = 0.954
entA = 0.954
entB = 1.406

IGDA = 0.347
IGDB = 0.454
IGDC = 0.003

SIDA = 0
infAX = inf[inf.A == 'X']
infAZ = inf[inf.A == 'Z']

if len(infAX) > 0:
    SIDA -= len(infAX)/len(inf) * np.log2(len(infAX)/len(inf))
if len(infAZ) > 0:
    SIDA -= len(infAZ)/len(inf) * np.log2(len(infAZ)/len(inf))
    
print('GainRatio(D,A) =', IGDA/SIDA)
