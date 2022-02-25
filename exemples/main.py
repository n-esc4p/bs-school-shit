"""
- Afficher verticalement et horizontalement les valeurs 123

- Afficher des traits

- Demander à l'utilisateur d'afficher votre nom et ensuit l'afficher

- Afficher des traits

- Entrer un nombre, convertir le nombre en float et calculer son carré en affichant "Le carré de x et y"

- Afficher des traits

- Afficher la séquence de nombres 123 verticalement et horizontalement à l'aide de la boucle for

- Afficher des traits

- Afficher 3 fois la phrase "Hello world" en utilisant dans la boucle for les instructions suivantes, les compléter si nécessaire :
        print("Hello", ...)
        print("world")
  À la sortie de la boucle, afficher le mot "End"

- Afficher des traits

- Demander à l'utilisateur d'entrer un nombre, si il est positif, afficher "Le nombre est positif".

- Afficher des traits

- Demander à l'utilisateur d'entrer un nombre, si il est positif, afficher "Le nombre est positif".
                                                 si il est égal à 0, afficher "Le nombre est egal a zero".
                                                 si il est négatif, afficher "Le nombre est negatif"

- Afficher des traits

- Afficher 10 fois "boucle Tant que" en utilisant la structure répétive while et afficher 10 fois "boucle for" en utilisant la structure répétive for.

- Afficher des traits

- Créer la liste Tab comprenant comme valeurs 5,4,2,0
  Afficher le deuxième élément du tableau
  Afficher le troisième élément du tableau
  Afficher la longueur du tableau
"""


def brline():
    print(" - - - - - - - - - - - - - - - - - - - - - ")


# - Afficher verticalement et horizontalement les valeurs 123

print("1 2 3 \n")
print("1\n2\n3")
brline()  # - - - - - - - - - - - - - - - - - - - - -


# - Demander à l'utilisateur d'afficher votre nom et ensuit l'afficher

nom = input("nom: ")
print(nom)
brline()  # - - - - - - - - - - - - - - - - - - - - -


# - Entrer un nombre, convertir le nombre en float et calculer son carré en affichant "Le carré de x et y"

x = float(input("x: "))
y = x**2
print(f"le carré de {x} est {y}")
brline()  # - - - - - - - - - - - - - - - - - - - - -


# - Afficher la séquence de nombres 123 verticalement et horizontalement à l'aide de la boucle for

for n in range(1, 4):
    print(f"{n} ", end="")
print("\n")
for n in range(1, 4):
    print(n)
brline()  # - - - - - - - - - - - - - - - - - - - - -


# - Afficher 3 fois la phrase "Hello world" en utilisant dans la boucle for les instructions suivantes, les compléter si nécessaire :
#         print("Hello", ...)
#         print("world")
#   À la sortie de la boucle, afficher le mot "End"

for n in range(3):
    print("Hellow, World!")
print("End")
brline()  # - - - - - - - - - - - - - - - - - - - - -


# - Demander à l'utilisateur d'entrer un nombre, si il est positif, afficher "Le nombre est positif".
x = int(input("x: "))
if x >= 0:
    print("positif")
else:
    print("négatif")
brline()  # - - - - - - - - - - - - - - - - - - - - -


# - Demander à l'utilisateur d'entrer un nombre, si il est positif, afficher "Le nombre est positif".
#                                                si il est égal à 0, afficher "Le nombre est egal a zero".
#                                                si il est négatif, afficher "Le nombre est negatif"

x = int(input("x: "))
if x > 0:
    print("Le nombre est positif")
elif x == 0:
    print("Le nombre est egal a zero")
else:
    print("Le nombre est negatif")
brline()  # - - - - - - - - - - - - - - - - - - - - -


# - Afficher 10 fois "boucle Tant que" en utilisant la structure répétive while et afficher 10 fois "boucle for" en utilisant la structure répétive for.

w = 0
while w < 10:
    print("boucle tant que")
    w += 1
for x in range(10):
    print("boucle for")
brline()  # - - - - - - - - - - - - - - - - - - - - -


# - Créer la liste Tab comprenant comme valeurs 5,4,2,0
Tab = [5, 4, 2, 0]
#   Afficher le deuxième élément du tableau
print(Tab[1])
#   Afficher le troisième élément du tableau
print(Tab[2])
#   Afficher la longueur du tableau
print(len(Tab))
brline()  # - - - - - - - - - - - - - - - - - - - - -


print("fin")
