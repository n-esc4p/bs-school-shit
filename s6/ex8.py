"""
Ecrire un algorithme permettant la saisie d’une note entre 0 et 20 et affichant les
mentions suivantes en fonction de la valeur de la note. Appelons la note n. Voici les
mentions :
n≥16 : TB,
n≥14 : B,
n≥12 : AB,
n≥10 : Passable,
n<10 : Mauvais
"""
n = int(input("note(/20) : "))
if n>=16 :
    print("TB")
elif n>=14 :
    print("B")
elif n>=12 :
    print("AB")
elif n>=10 :
    print("Passable")
else :
    print("Mauvais")

