#cena_kebabu = [2, 3, 4]
#vzdalenost = [7, 3, 5]

#cena_jizdenky = 4
#pocet_podnik = len(cena_kebabu)

#vysledne_ceny = []

#for i in range(len(cena_kebabu)):
#    suma = cena_kebabu[i] + (cena_jizdenky*vzdalenost[i])
#    vysledne_ceny.append(suma)
#    print(min(vysledne_ceny))

#####################################################################################################################################################




#pole = [["a", "b", "c"]["d", "e", ["f", "g"]]
#print(pole[1][2][0])

#####################################################################################################################################################




#field = []

#for y in range(5):
#    row = []
#    for x in range(5):
#        row.append("o")
#    field.append(row)

#for x in field:
#    print(" ".join(x))

######################################################################################################################################################




    
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

######################################################################################################################################################




#import math

#points = [[1, 1]], [[2, 4]]

#x = (points[1][0] - points[0][0])**2
#y = (points[1][1] - points[0][1])**2

#print(math.sqrt(x+y))

######################################################################################################################################################

#                                                                      MINE GAME

######################################################################################################################################################
#import random
#w, h, mines = 16, 5, 10
 
## gene field
#field = [[0 for y in range(h)] for x in range(w)]
 
# put mine on random position
#for i in range(mines):
#    while True:
#        rx = random.randint(0, w - 1)
#        ry = random.randint(0, h - 1)
#        if field[rx][ry] != "m":
#           field[rx][ry] = "M"
#           break

#for y in range(h):
#    for x in range(w):
#        if field[x][y] == "M":
#           # print("Mina na[{}]".format(x, y))
#           for delta in deltas:
               
## print field
#     for y in range(h):
#      for x in range(w):
#        print(field[x][y], end="")
#    print()


######################################################################################################################################################


#arr = [[65, 98, 88, 54, 47],[35, 55, 98, 69],[35, 65, 62, 75, 99]]
#for i in range(len(arr)):
#    for y in range(len(arr[i])):
#        if arr[i][y] > 50:
#            # print("arr[", i,"][", y,"], " = ", arr[i][y])
#            print(f"arr[{i}][{y}] = {arr[i][y]}")

########################################################################################################################################################


#field = [["_" for _ in range(3)] for _ in range(3)]

#def print_field(field):
#     for x in field:
#          print(" ".join(x))

#current_player = 0

#while True:
#    print_field(field)

#    if current_player == 0:
#         print("hraje hráč X")
#    else:
#        print("hraje hráč O")

#    play_x = input("zadej x:")
#    if play_x == "q":
#          break
#    play_x = int(play_x)
#    play_y = int(input("zadej y:"))    

#    if current_player == 0:
#         field[play_y][play_x] = "x"
#         current_player = 1
#    else:
#        field[play_y][play_x] = "o"
#        current_player = 0


#######################################################################################################################################################

#arr = [5, 2, 8, 6, 1]

#arr[4], arr[0] = arr[0], arr[4]
#print(arr)




#def selection_sort(arr):
#    for i in range(len(arr)-1):
#        min_index = i
#        for j in range(i+1, len(arr)):
#            if arr[j] < arr[min_index]:
#                min_index = j
#        arr[i], arr[min_index] = arr[min_index], arr[i]
#    return arr

#print(selection_sort([5, 7, 3, 2, 6]))

##################################################################################################################################################################################

#                                                                                      XOX  

###################################################################################################################################################################################
#word = "valorant"
#g_letters = []
#lives = 8


#while True:
#    display = ""
#    for letter in word:
#        if letter in g_letters:
#            display += letter
#        else:
#            display += " "
#    print("\nslovo:", display)
#    print("životy:", lives)
    
#    guess = input("hádej písmeno: ")
    
#    if guess in g_letters:
#        print("tohle písmeno jsi už uhádl")
#        continue
    
#    g_letters.append(guess)
    
#    if guess not in word:
#        print("špatně")
#        lives -= 1
#        if lives == 0:
#            print("konec hry. Slovo bylo:", word)
#            break
#    else:
#        print("správně")
#        if all(letter in g_letters for letter in word):
#            print("vyhral jsi, slovo je:", word)
#            break

#######################################################################################################################################################################################

#                                                                                     CALCULATOR                                                  

#######################################################################################################################################################################################
#neco = int(input("Zadej číslo:"))
#neco2 = int(input("Zadej další číslo:"))
#neco3 = str(input("Zvol operaci"))
 
#if neco3 == "/":       #deleni
#    print(neco/neco2)
#elif neco3 == "+":     #scitani 
#    print(neco+neco2)
#elif neco3 == "-":     #odcitani
#    print(neco-neco2)
#elif neco3 == "*":     #nasobeni
#    print(neco*neco2)


#######################################################################################################################################################################################

#                                                                                   CESTA 

#####################################################################################################################################################################################
#kopce = [12, 9, 11, 8, 14, 13, 12, 13]
#cesta_pěšky = 0
 
#for i in range(1,len(kopce)):
#    rozdíl_výšky = kopce[i] - kopce [i - 1]
#    if rozdíl_výšky > 0:
#        cesta_pěšky += rozdíl_výšky
 
#print (cesta_pěšky)
    
######################################################################################################################################################################################

#                                                                                    CESTA

######################################################################################################################################################################################
#hills = [12, 9, 11, 8, 14, 13, 12, 13] ##total 8
#speed = 0
#walk = 0

#for i in range(len(hills)):##lenght 8 <0, 8)
#    if i == len(hills)-1:
#        break
#    this_hills = hills[i]
#    next_hill = hills[i+1]
#    if speed + this_hill > next_hill:                                     ##[i] = aktualni
#        speed += this_hill - next_hill
#    else:
#        walk += next_hill - this_hill
#        speed = 0

#print(walk)        

##########################################################################################################################################################################################


############################################################################################################################################################################################

 #                                                                                 DICTIONARIES

######################################################################################################################################################################################

#person = {
#    "name": "Jakub",
#    "age" : 22,
#    "pets" : ["Nani", "Ten"]
#    }

#person["name"] = "Jakub Hájek"
#person["hair"] = "brown"

#for key in person.keys():
#    print(key)

#for values in person.values():
#    print(values)

#for key, value in person.items():
#    print(key, value)

#######################################################################################################################################################################################

#from readline import append_history_file


#dictionary = {
#    "dog" : "pes",
#    "cat" : "kočka",
#    "bird" : "pták"
#}

#while True:
#    user_input = input("zadej anglické slovo nebo 'q' pro končení")
#    if user_input == "q":
#        break
#    elif user_input in dictionary:
#        print(dictionary[user_input])
#    else:
#        print("slovo není ve slovníku")
#        add_word_prompt = input("Chceš přidat překlad y/n")
#        if add_word_prompt == "y":
#            add_word


########################################################################################################################################################


        ########################################################################################################################################################
#dict = {'A':'0',
#         'B':'1',
#         'C':'00',
#         'D':'01',
#         'E':'10',
#         'F':'11',
#         'G':'000',
#         'H':'001',
#         'I':'010',
#         'J':'011',
#         'K':'100',
#         'L':'101',
#         'M':'110',
#         'N':'111',
#         'O':'0000',
#         'P':'0001',
#         'Q':'0010',
#         'R':'0011',
#         'S':'0100',
#         'T':'0101',
#         'U':'0110',
#         'V':'0111',
#         'W':'1000',
#         'X':'1001',
#         'Y':'1010',
#         'Z':'1011',
#         '.':'1100',
#         ',':'1101',
#         ':':'1110',
#         ' ':'1111',        
#         }
         
#print(dict["X"])
#print(dict.values())
#vysledek = ""
 
#user_input = input("")
 
#for x in range(1):
#    for y in user_input.upper():
#        vysledek += f"{dict[y]}/"
#    print(vysledek)

#####################################################################################################################################################################################


def caesar_cipher(text, shift, mode='encrypt'):
    # Anglická abeceda
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
   
    for char in text:
        if char.lower() in alphabet:
            is_lower = char.islower()
            index = alphabet.find(char.lower())
           
            if mode == 'encrypt':
                new_index = (index + shift) % len(alphabet)
            elif mode == 'decrypt':
                new_index = (index - shift) % len(alphabet)
            else:
                raise ValueError("Invalid mode! Use 'encrypt' or 'decrypt'.")
               
            if is_lower:
                result += alphabet[new_index]
            else:
                result += alphabet[new_index].upper()
        else:
            result += char
 
    return result
 
# Testovací příklady
text = "axk gb eljlpburái"
shift = 3
 
# Šifrování
encrypted_text = caesar_cipher(text, shift, mode='encrypt')
print(f'Šifrovaný text: {encrypted_text}')
 
# Dešifrování
decrypted_text = caesar_cipher(encrypted_text, shift, mode='decrypt')
print(f'Dešifrovaný text: {decrypted_text}')




    

    


























































































































































        
       


