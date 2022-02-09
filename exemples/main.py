def br():
    print(" - - - - - - - - - - - - - - - - - - - - - ")


print("1 2 3 \n")
print("1\n2\n3")
br()

nom = input("nom: ")
print(nom)
br()

x = float(input("x: "))
y = x**2
print(f"le carré de {x} est {y}")
br()

for n in range(1, 4):
    print(f"{n} ", end="")
print("\n")
for n in range(1, 4):
    print(n)
br()

for n in range(3):
    print("Hellow, World!")
print("End")
br()

x = int(input("x: "))
if x >= 0:
    print("positif")
else:
    print("négatif")
br()

x = int(input("x: "))
if x > 0:
    print("Le nombre est positif")
elif x == 0:
    print("Le nombre est egal a zero")
else:
    print("Le nombre est negatif")
br()

w = 0
while w < 10:
    print("boucle tant que")
    w += 1
for x in range(10):
    print("boucle for")
br()

Tab = [5, 4, 2, 0]
print(Tab[1])
print(Tab[2])
print(len(Tab))
br()

print("fin")