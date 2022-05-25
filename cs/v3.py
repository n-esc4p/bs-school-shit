items = [
    ["Sandwich au poulet", 4.90],
    ["Chips paprika", 2.50],
    ["Barre de chocolat", 2.00],
    ["Bonbons", 3.30],
    ["Ice Tea", 2.20],
    ["Limonade", 1.90]
]
i = 0

print("Bienvenue ! Voici notre sélection de produit :\n")
print("--------------------------------------------------")

print("Menu: ")
for item in items:
    i += 1
    print(f"{i}. {item[0]} ${item[1]}")

def Taking_Order():

    def Order_Proccess():
        itemOrdered = items[order - 1][0]
        orderPrice = items[order - 1][1]
        print(f"Vous avez commander {itemOrdered}, cela coûte ${orderPrice}")

        money = float(input("Veuillez introduire votre monnaie: "))
        print(f"Vous avez introduit ${money}")

        if money >= orderPrice:
            if order == 5 or order == 6:
                print(f"{itemOrdered} servie! Sante ! \nMonnaie à rendre ${round(money - orderPrice, 2)}")
            else:
                print(f"{itemOrdered} servie! Bonne appetite ! \nMonnaie à rendre ${round(money - orderPrice, 2)}")
        else:
            print(f"Vous n'avais pas mis assez d'argent \n${money} rendu")
            answer = input("Voulez vous réessayer? y/n\n")
            if answer == "y":
                Taking_Order()
            else:
                exit()

    order = int(input("\nVeuillez sélectionner un produit: \n"))
    if order in range(1, 7):
        Order_Proccess()
    else:
        print("Cet article n'est pas valable")
        Taking_Order()

Taking_Order()

input("\n\nPress any key to exit...")
