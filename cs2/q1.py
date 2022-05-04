"""
Construire une fonction permettant de retourner le minimum d'une liste de 5 nombres entiers saisis par l'utilisateur.
Le minimum doit être trouvé à l'aide d'une boucle for.
L'affichage du minimum devra être explicite.
"""


def findmin():
    numlist = []
    for n in range(5):
        numlist.append(int(input(f"numéro {n+1} : ")))
        if n == 0:
            nmin = numlist[0]
        if numlist[n] < nmin:
            nmin = numlist[n]
    return f"minimum : {nmin}"


print(findmin())