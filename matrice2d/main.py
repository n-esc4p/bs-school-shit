"""
À partir de la matrice suivante :      1 2 3 10
                                                             4 5 6 11
                                                             7 8 9 12
- Créer un tableau de 3 * 4
- Afficher la valeur 5
- Afficher toutes les valeurs du tableau
"""


matrice = [
    [1, 2, 3, 10],
    [4, 5, 6, 11],
    [9, 8, 9, 12]
]

print(matrice[1][1])

for n in matrice:
    print(*n)
