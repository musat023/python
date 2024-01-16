#(1)
#liche nebo sude cislo

#cislo = input('cislo : ')
#if(int(cislo)%16==0):
#    print("cislo je sude")
#else:
#    print("cislo je liche")





#(2)
#kladna, zaporna

#numbers = [ 12, 33, -43, -22, 19]

#for x in numbers:
#    kladna = 0
#    zaporna = 0

#    if x > 0:
#        kladna += 1
#    elif x < 0:
#        zaporna += 1
    
#    print (x)





#(3)
#total students in class

#student_in_classes = [43, 87, 12, 43, 65]

#total_students = 0
#for x in student_in_classes:
#    total_students += x
#    print(total_students)





#(4)
#animals legs

#animals = [32, 4, 6] #chickens, pigs, cows
#legs = 0
#for i in range(len(animals)):
#    if i == 0 :
#        legs += animals[i]*2
#    else:
#        legs += animals[i]*4

#print(legs)





#(5)
#true or false last char 

#def is_last_char_h(name):
#    if name[len(name)-1] == "h":
#        return True
#    else:
#        return False
    
#print(is_last_char_h("jakub"))




#(6)
#BMI calculator
#def calculate_bmi():
#    weight = float(input('enter your weight (in kg)'))
#    height = float(input('enter your height(in meters)'))

#    bmi = weight / (height ** 2)
#    bmi = round(bmi, 2)

#    print('your body mass index (BMI):', bmi)

#    if bmi < 18.5:
#        print('Under weight')
#    elif bmi >= 18.5 and bmi < 25:
#        print('Normal weight')
#    elif bmi >= 25 and bmi < 30:
#        print('Over weight')
#    else:
#        print('Obesity')

#calculate_bmi()      





#(7)xox game
#def print_board(board):
#    for row in board:
#        print(" | ".join(row))
#        print("-" * 9)

#def check_winner(board):
#    for row in board:
#        if row.count(row[0]) == len(row) and row[0] != ' ':
#            return True

#    for col in range(3):
#        if board[0][col] == board[1][col] == board[2][col] != ' ':
#            return True

#    if board[0][0] == board[1][1] == board[2][2] != ' ' or board[0][2] == board[1][1] == board[2][0] != ' ':
#        return True

#    return False

#def is_board_full(board):
#    return all(all(cell != ' ' for cell in row) for row in board)

#def tic_tactoe():
#    board = [[' ' for  in range(3)] for _ in range(3)]
#    current_player = 'X'

#    while True:
#        print_board(board)

#        row = int(input(f"Player {current_player}, enter row (0, 1, or 2): "))
#        col = int(input("Enter column (0, 1, or 2): "))

#        if board[row][col] == ' ':
#            board[row][col] = current_player
#            if check_winner(board):
#                print_board(board)
#                print(f"Player {current_player} wins!")
#                break
#            elif is_board_full(board):
#                print_board(board)
#                print("It's a tie!")
#                break
#            else:
#                current_player = 'O' if current_player == 'X' else 'X'
#        else:
#            print("Cell already occupied. Try again.")

#if name == "main":
#    tic_tac_toe()





#(8)Clock
#from tkinter import *
#from tkinter.ttk import *

#from time import strftime

#root = Tk()
#root.title('Ceas')

#def time():
#    string = strftime('%D ''' '%H:%M:%S %p')
#    lbl.config(text=string)
#    lbl.after(1000, time)

#lbl = Label(root, font=('calibri', 109, 'bold'),
#            background='purple',
#            foreground='white')

#lbl.pack(anchor='center')
#time()
#mainloop()





#(9)Password Strength Checker
#import string
#import getpass


#def check_password_strength():
#   password = getpass.getpass('Enter the password: ')
#   strength = 0
#   remarks = ''
#   lower_count = upper_count = num_count = wspace_count = special_count = 0

#   for char in list(password):
#       if char in string.ascii_lowercase:
#           lower_count += 1
#       elif char in string.ascii_uppercase:
#           upper_count += 1
#       elif char in string.digits:
#           num_count += 1
#       elif char == ' ':
#           wspace_count += 1
#       else:
#           special_count += 1

#   if lower_count >= 1:
#       strength += 1
#   if upper_count >= 1:
#       strength += 1
#   if num_count >= 1:
#       strength += 1
#   if wspace_count >= 1:
#       strength += 1
#   if special_count >= 1:
#       strength += 1

#   if strength == 1:
#       remarks = ('That\'s a very bad password.'
#           ' Change it as soon as possible.')
#   elif strength == 2:
#       remarks = ('That\'s a weak password.'
#           ' You should consider using a tougher password.')
#   elif strength == 3:
#       remarks = 'Your password is okay, but it can be improved.'
#   elif strength == 4:
#       remarks = ('Your password is hard to guess.'
#           ' But you could make it even more secure.')
#   elif strength == 5:
#       remarks = ('Now that\'s one hell of a strong password!!!'
#           ' Hackers don\'t have a chance guessing that password!')

#   print('Your password has:-')
#   print(f'{lower_count} lowercase letters')
#   print(f'{upper_count} uppercase letters')
#   print(f'{num_count} digits')
#   print(f'{wspace_count} whitespaces')
#   print(f'{special_count} special characters')
#   print(f'Password Score: {strength / 5}')
#   print(f'Remarks: {remarks}')


#def check_pwd(another_pw=False):
#   valid = False
#   if another_pw:
#       choice = input(
#           'Do you want to check another password\'s strength (y/n) : ')
#   else:
#       choice = input(
#           'Do you want to check your password\'s strength (y/n) : ')

#   while not valid:
#       if choice.lower() == 'y':
#           return True
#       elif choice.lower() == 'n':
#           print('Exiting...')
#           return False
#       else:
#           print('Invalid input...please try again. \n')


#if __name__ == '__main__':
#   print('===== Welcome to Password Strength Checker =====')
#   check_pw = check_pwd()
#   while check_pw:
#       check_password_strength()
#       check_pw = check_pwd(True)





#(10) Password Generator
#import secrets
#import string


#def create_pw(pw_length=12):
#   letters = string.ascii_letters
#   digits = string.digits
#   special_chars = string.punctuation

#   alphabet = letters + digits + special_chars
#   pwd = ''
#   pw_strong = False

#   while not pw_strong:
#       pwd = ''
#       for i in range(pw_length):
#           pwd += ''.join(secrets.choice(alphabet))

#      if (any(char in special_chars for char in pwd) and
#               sum(char in digits for char in pwd) >= 2):
#           pw_strong = True

#   return pwd


#if __name__ == '__main__':
#   print(create_pw())