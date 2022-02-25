"""
- Créer une fonction sans paramètre qui affiche la table de 7.


- Créer une deuxième fonction avec paramètre qui affiche n'importe quelle table de multiplication d'un nombre entier.
"""


def tbl7():
    for n in range(1, 11):
        print(n*7)


def tbl(t):
    for n in range(1, 11):
        print(n*t)


tbl7()
print("\n")
tbl(8)
