import itertools
a={'A','B','C','D'}
for i in range(len(a)):
    sub=itertools.combinations(a , i+1)
    print(set(sub))