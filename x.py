class Strom:
    def __init__(self, druh, vyska):
        self.druh = druh 
        self.vyska = vyska

    def __str__(self):
        return f"{self.vyska} metru vysoký {self.druh}"
    
class Ozdoba:
    def __init__(self, nazev, barva):
        self.barva = barva
        self.nazev = nazev

    def __str__(self):
        return f"{self.barva} {self.nazev}"
    
class VanocniStrom:
    def __init__(self, druh, vyska):
        self.druh = druh
        self.vyska = vyska 
        self.ozdoby = [] 

    def pridat_ozdobu(self, ozdoba):
        self.ozdoby.append(ozdoba)

    def zobrazit(self):
        print(f"Vánoční stromek ({self.druh}, {self.vyska}m):")
        for ozdoba in self.ozdoby:
            print(f"- {ozdoba}")


stromek = VanocniStrom("Jedle", 2.5)

stromek.pridat_ozdobu("červená koule")
stromek.pridat_ozdobu("zlatý řetěž")
stromek.pridat_ozdobu("stříbrná hvězda")

stromek.zobrazit()

















