m = int(input("m:"))
s = 0
if m > 0:
    for p in range(1, m+1):
        s += p**5
        print(f"{p}^5 = {p ** 5}")
    print(f"somme = {s}")
else:
    print("erreur : m doit être un entier naturel non nul ")
