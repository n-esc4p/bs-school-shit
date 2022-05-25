"""
Écrire un programme qui permet de remplir à l'aide d'une boucle for un tableau de 7 entiers et ensuite afficher le tableau.
Vous devez par la suite saisir un entier z, puis chercher si cet entier appartient au tableau.
Au cas où l’entier z est égal à un entier du tableau, afficher explicitement le nombre et son indice.
Afficher explicitement le cas où l’entier z n’appartient pas au tableau.
"""
tab = []  # création du tableau
for x in range(7):
    n = tab.append(int(input(f"n{x+1} : ")))  # completer le tableau
print(*tab)  # afficher
z = int(input("z : "))
try:
    print(f"le nombre {z} est bien dans le tableau à l'indexe {tab.index(z)}")  # verifier si le nombre est present
except Exception as e:
    print(e)
    print(f"le nombre {z} n'est pas dans le tableau")
