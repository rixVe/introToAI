orig = [3,6,5,1,2,4]
chrom = orig.copy()
indeces = [1,3]
t = chrom[indeces[0]]
chrom[indeces[0]] = chrom[indeces[1]]
chrom[indeces[1]] = t
print('Swap:')
print(chrom)

chrom = orig.copy()
chrom = chrom[:indeces[0]+1] + [chrom[indeces[1]]] + chrom[indeces[0]+1:]
chrom.pop(indeces[1] + 1)
print(chrom)