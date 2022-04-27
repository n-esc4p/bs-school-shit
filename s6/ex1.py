"""
Permuter le contenu de deux variables contenant les valeurs 7 et 10, afficher les
nouvelles valeurs des variables.
"""

x = 7
y = 10

x = x + y
y = x - y
x = x - y

print(f"x : {x}")
print(f"y : {y}")
