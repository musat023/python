def vytvor_trojuhelnik(velikost_pole):
    pole = [['o' for _ in range(velikost_pole)] for _ in range(velikost_pole)]
 
    stred = velikost_pole // 2
 
    for i in range(stred + 1):
        pocet_o = 2 * i + 1
        zacatek_o = stred - i
        konec_o = zacatek_o + pocet_o
        pole[i][zacatek_o:konec_o] = ['x'] * pocet_o
 
    return pole
 
def vypis_trojuhelnik(trojuhelnik):
    for radek in trojuhelnik:
        print(' '.join(radek))
 
velikost_pole = 7
 
pole_s_trojuhelnikem = vytvor_trojuhelnik(velikost_pole)
vypis_trojuhelnik(pole_s_trojuhelnikem)