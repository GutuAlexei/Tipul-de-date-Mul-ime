A=set(input('Mutimea A=').split( ))
B=set(input('Mutimea B=').split( ))
for i in A:
    for n in B:
        if ord (i) in range (65,90):
            if ord (n) in range (65,90):
                print('a) intersecţia mulţimilor A şi B;',A.intersection(B) )
                print('b) reuniunea mulţimilor A şi B;', A.union(B))
                print('c) diferenţa mulţimilor A şi B.', A.difference(B))
                print('d) diferenţa mulţimilor A şi B.', B.difference(A))
        else:
            print('Multimea nu este din numere intregi')
