neco = int(input("Zadej číslo:"))
neco2 = int(input("Zadej další číslo:"))
neco3 = str(input("Zvol operaci"))
 
if neco3 == "/":       #deleni
    print(neco/neco2)
elif neco3 == "+":     #scitani 
    print(neco+neco2)
elif neco3 == "-":     #odcitani
    print(neco-neco2)
elif neco3 == "*":     #nasobeni
    print(neco*neco2)
