"""
Écrire un programme qui permet de remplir un tableau de 10 entiers saisis par l'utilisateur,
Afficher le tableau.
Ensuite afficher explicitement tous les éléments impairs de ce tableau.
"""
tab = []
for x in range(10):
    n = tab.append(int(input(f"n{x} : ")))
print(*tab)  # afficher
for n in tab:
    if n%2 != 0:  # verifier si c'est pair
        print(n)
