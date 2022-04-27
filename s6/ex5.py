"""
Ecrire un algorithme qui permet d’encoder le nombre de cigarettes que l’utilisateur fume
par jour, qui calcule ses dépenses mensuelles et annuelles en cigarettes. (on suppose
qu’une cigarette coûte 0,23 € et qu’un mois est composé de 30 jours). L’algorithme écrira
ensuite les dépenses mensuelles, les dépenses annuelles et le message « si tu ne fumais
pas, tu pourrais te payer une tablette ACER A500 32GB WIFI à 499 € » si les dépenses
annuelles sont égales ou dépassent 499 €. Si ce n’est pas le cas, l’algorithme écrira le
message « si tu ne fumais pas, tu pourrais te payer une mini-tablette de 8 pouces
MPMAN à 199 € » si les dépenses annuelles sont égales ou dépassent 199 €.
"""
cpj = int(input("cigarette par jour : "))
dm = 30*0.23*cpj
print(f"dépenses mensuelles : {dm}")
da = 12*dm
print(f"dépenses annuelles : {da}")
if da >= 499:
    print("si tu ne fumais pas, tu pourrais te payer une tablette ACER A500 32GB WIFI à 499 €")
elif da >= 199:
    print("si tu ne fumais pas, tu pourrais te payer une mini-tablette de 8 pouces MPMAN à 199 €")
else:
    print("continue de fumer")
