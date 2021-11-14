import itertools
a={1,2,3,4}
for i in range(len(a)):
    sub=itertools.combinations(a , i+1)
    print(set(sub))