A=set(input('Mutimea A=').split( ))
B=set(input('Mutimea B=').split( ))
print('a) caracterele care se întâlnesc cel puţin în unul dintre şiruri: ',A.union(B)) 
print('b) caracterele care apar în ambele şiruri:', A.intersection(B))
print('c) caracterele care apar în primul şi nu apar în şirul al doilea: ', A.difference(B))