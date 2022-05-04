def findmin():
    numlist = []
    for n in range(5):
        numlist.append(int(input(f"numéro {n+1} : ")))
        if n == 0:
            nmin = numlist[0]
        if numlist[n] < nmin:
            nmin = numlist[n]
    return f"minimum : {nmin}"


print(findmin())