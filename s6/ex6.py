"""
Tu joues à un jeu vidéo et lorsque tu termines la partie, l’ordinateur te donne le temps
(en secondes) qu’il t’a fallu pour jouer la partie. Le champion actuel a mis 265 sec pour
gagner la partie. Deviendras-tu le nouveau champion ? Tu dois écrire un algorithme qui
te permettra d’encoder le temps de jeu en secondes, qui calculera et affichera le temps
de jeu en minutes et secondes et qui te dira si tu es le nouveau champion ou si tu dois
continuer ton entrainement.
"""

s = int(input("sec : "))

if s <= 265:
    print("nouveau champion")
else:
    print("continue ton entrainement")