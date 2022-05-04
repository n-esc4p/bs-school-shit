"""
Créer une fonction qui permet de calculer la multiplication de 5 valeurs d'une liste définie dans la fonction avec la boucle for.
L'affichage du résultat devra être explicite.
"""


def multip():
    numlist = []
    for n in range(5):
        numlist.append(int(input(f"numéro {n + 1} : ")))
    r = 1
    rtxt = ""
    for n in range(len(numlist)):
        if n < len(numlist)-1:
            rtxt += f"{str(numlist[n])} x "
        else:
            rtxt += str(numlist[n])
    for n in numlist:
        r *= n

    return f"{rtxt} = {r}"


print(multip())