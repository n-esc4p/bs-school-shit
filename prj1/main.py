import keyboard

stock = [
    ["Article", "Pointure", "Prix"],
    ["Asics Gel 2000", 42, 119.00],
    ["Asics Gel 2000", 39, 119.00],
    ["Mizuno Wave Rider", 38, 129.00],
    ["Nike Air Zoom", 42, 125.00],
    ["Mizuno Wave plus", 39, 83.40],
    ["Mizuno Wave plus", 40, 83.40],
    ["Mizuno Wave plus", 41, 83.40],
    ["Merrel Poseidon", 39, 118.30]
]

run = True


while run == True:
    print("\n1 : Afficher les articles pour une pointure"
          "\n2 : Afficher les articles présents plusieurs fois"
          "\n3 : Afficher les articles pour chaque pointure"
          "\n4 : Afficher la pointure la plus présente"
          "\n5 : Afficher le nombre de fois la pointure la plus présente"
          "\n6 : Afficher l’article le plus cher"
          "\n0 : Quitter le programme")
    menu_input = keyboard.read_key()
    if menu_input == "0" or menu_input == "à":
        print("\nFin du programme")
        break
    elif menu_input == "2":
        for line in stock:
            print(line)
        print("yes")
