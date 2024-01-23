#cena_kebabu = [2, 3, 4]
#vzdalenost = [7, 3, 5]

#cena_jizdenky = 4
#pocet_podnik = len(cena_kebabu)

#vysledne_ceny = []

#for i in range(len(cena_kebabu)):
#    suma = cena_kebabu[i] + (cena_jizdenky*vzdalenost[i])
#    vysledne_ceny.append(suma)
#    print(min(vysledne_ceny))





#pole = [["a", "b", "c"]["d", "e", ["f", "g"]]
#print(pole[1][2][0])





#field = []

#for y in range(5):
#    row = []
#    for x in range(5):
#        row.append("o")
#    field.append(row)

#for x in field:
#    print(" ".join(x))





    
#field = []
#i = 1
#for y in range(8):
#    row = []
#    j = 0
#    for x in range(8):
#        if i > 0:
#            if j%2 == 0:
#                row.append("o")
#            else:
#                row.append("x")
#            j+=1
#        else: 
#            if j%2 == 0:
#                row.append("x")
#            else:
#               row.append("o")
#            j+=1
#        i*=1
#        field.append(row)
#        for x in field:
#            print(" ".join(x))





#import math

#points = [[1, 1]], [[2, 4]]

#x = (points[1][0] - points[0][0])**2
#y = (points[1][1] - points[0][1])**2

#print(math.sqrt(x+y))






field = []
i = 1
for y in range(8):
    row = []
    j = 0
    for x in range(8):
        if i > 0:
            if j%2 == 0:
                row.append("o")
            else:
                row.append("x")
            j+=1
        else: 
            if j%2 == 0:
                row.append("x")
            else:
               row.append("o")
            j+=1
        i*=1
        field.append(row)
        for x in field:
            print(" ".join(x))
            




        
       


