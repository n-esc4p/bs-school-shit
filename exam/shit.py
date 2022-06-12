#ex1
print("----ex1")
r = 5
i = 5
u = r * i
print("U=", u)
#ex2
print("---------ex2")
def somme(n):
    resultat = 0
    x = 0
    while x<n:
        x = x+1
        resultat = resultat+x
    return resultat
print(somme(2))
#ex3
print("-----ex3")
gateau = [11,5,6,3,8]
print(len(gateau))
print(gateau.index(5))
print(sum(gateau))
gateau.append(2)
print(gateau[4])
for x in gateau:
    print(x)
#ex4
print("-------ex4")
M = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
for x in range(len(M)):
    for y in M[x]:
        print(y)
print("les entier paire sont:")
for x in range(len(M)):
    for y in M[x]:
        if y%2==0:
            print(y)
print("les entier impaire sont:")
for x in range(len(M)):
    for y in M[x]:
        if y%2!=0:
            print(y)