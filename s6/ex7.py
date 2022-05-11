"""
Ecrire un algorithme qui donne la durée de vol en heure minute connaissant l’heure de
départ ( à encoder) et l’heure d’arrivée (à encoder) ; on considère que le départ et
l’arrivée ont lieu le même jour.
"""


def asktime(msg):
    s = input(f"{msg}(HH:MM) : ")
    t = []
    try:
        t.append(int(s[0: 2]))
    except:
        t.append(0)
    try:
        t.append(int(s[3 : 5]))
    except :
        t.append(0)
    return t


dep = asktime("heure de départ")
arv = asktime("heure d'arrivée")
res = [arv[0]-dep[0], arv[1]-dep[1]]

if res[0] < 0 or 24 < res[0]:
    print("Erreur")
elif res[1] < 0 or 59 < res[1]:
    print("Erreur")
else:
    print(f"heure de vol : {'%02d' % (res[0],)}:{'%02d' % (res[1],)}")
