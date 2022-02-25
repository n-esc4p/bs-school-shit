print("salam alaikum ")
print("1 sandwitch au poulet 4.90€")
print("2 chips paprika 2.50€")
print("3 barre chocolat 2.00€")
print("4 bonbon 3.30€")
print("5 ice tea 2.20€")
print("6 limonade 1.90€")
argent = float(input("introduire le argent :"))
produit = int(input("selectione le produit :"))
if produit == 1:
    prix = 4.90
    print("sandwitch au poulet")
elif produit == 2:
    prix = 2.50
    print("chips paprika")
elif produit == 3:
    prix = 2.00
    print("barre chocolat")
elif produit == 4:
    prix = 3.30
    print("bonbons")
elif produit == 5:
    prix = 2.20
    print("ice tea")
elif produit == 6:
    prix = 1.90
    print("limonade")
if argent < prix:
    print("pas asser d'argent")
else:
    print("argent rendu :", argent-prix, "€")

