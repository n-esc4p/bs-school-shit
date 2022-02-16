HT = int(input("prix HT:"))
n = int(input("nombre d'articles:"))
TVA = int(input("taux de TVA (%):"))
TTC = (HT*n)+(HT*n)*(TVA/100)

print(f"prix total: {TTC}")
