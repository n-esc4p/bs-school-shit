"""
L’entrée pour un adulte dans un parc d’attraction est de 32 €. Cependant, le ticket
acheté par internet ne coûte que 26 €. Ecrire un algorithme qui permet d’afficher le prix
d’entrée en fonction du mode de paiement choisi.
"""
website = input("payer sur le site? (o/n)")
if website == "o":
    print("prix : 26€")
else:
    print("prix : 32€")

