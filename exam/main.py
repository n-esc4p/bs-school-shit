# examen programation 2022 zouine


def printex(ex):
    print(f"-------------------- ex{ex} --------------------")

# ex1
printex(1)
m = 7
a = 9.81
F = m * a
print(f"Force = {F}")



# ex2
printex(2)
def mutliplication(n):
    resultat = 1
    x = 1
    while x<n:
        x += 1
        resultat *= x
    return resultat

print(mutliplication(3))


# ex3
printex(3)
billes = [4, 8, 9, 6, 8, 1]
print(len(billes))
print(billes.index(6))
print(sum(billes))
billes.append(3)
print(billes[4])
print(*billes)



# ex4
printex(4)
M = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12],
    [13,14,15],
    [16,17,18]
]
print("liste :")
for x in range(len(M)):
    for y in M[x]:
        print(y)
print("les nombres paires sont :")
for x in range(len(M)):
    for y in M[x]:
        if y%2==0:
            print(y)
print("les nombres impaires sont :")
for x in range(len(M)):
    for y in M[x]:
        if y%2!=0:
            print(y)
