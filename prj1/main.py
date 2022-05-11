import keyboard
from terminaltables import AsciiTable

stock = [
    ["Article", "Pointure(EUR)", "Prix(€)"],
    ["Asics Gel 2000", 42, 119.00],
    ["Asics Gel 2000", 39, 119.00],
    ["Mizuno Wave Rider", 38, 129.00],
    ["Nike Air Zoom", 42, 125.00],
    ["Mizuno Wave plus", 39, 83.40],
    ["Mizuno Wave plus", 40, 83.40],
    ["Mizuno Wave plus", 41, 83.40],
    ["Merrel Poseidon", 39, 118.30]
]


def wait_for_input():
    global inp_val, inp
    inp = False
    while inp == False:
        inp_val = keyboard.read_key()
        if inp_val == "à" or inp_val == "&" or inp_val == "é" or inp_val == '"' or inp_val == "'" or inp_val == "(" or inp_val == "-" or inp_val == "0" or inp_val == "1" or inp_val == "2" or inp_val == "3" or inp_val == "4" or inp_val == "5" or inp_val == "6":
            inp = True
            break


def reset():
    global inp_val
    inp_val = ""



run = True
while run:

    print("\n1 : Afficher les articles pour une pointure"
          "\n2 : Afficher les articles présents plusieurs fois"
          "\n3 : Afficher les articles pour chaque pointure"
          "\n4 : Afficher la pointure la plus présente"
          "\n5 : Afficher le nombre de fois la pointure la plus présente"
          "\n6 : Afficher l’article le plus cher"
          "\n0 : Quitter le programme")

    wait_for_input()

    if inp_val == "0" or inp_val == "à":
        print("\nFin du programme ...")
        break

    elif inp_val == "1" or inp_val == "&":
        print("\n1")
        reset()

    elif inp_val == "2" or inp_val == "é":
        print("\n")
        table = AsciiTable(stock)
        print(table.table)
        reset()

    elif inp_val == "3" or inp_val == '"':
        print("\n3")
        reset()
    elif inp_val == "4" or inp_val == "'":
        print("\n4")
        reset()
    elif inp_val == "5" or inp_val == "(":
        print("\n5")
        reset()
    elif inp_val == "6" or inp_val == "-":
        print("\n6")
        reset()
