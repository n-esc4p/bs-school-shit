tab = [0, 0, 0, 0]


def afficher_tab():
    for n in tab:
        print(n)
    print("\n")


afficher_tab()
tab.append(100)
tab.append(250)
afficher_tab()
print(tab.index(250))
