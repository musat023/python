def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != "-":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "-":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "-":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "-":
        return True

    return False

def is_board_full(board):
    for row in board:
        if "-" in row:
            return False
    return True

def tic_tac_toe():
    board = [["-" for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)

        row = int(input(f"Hráč {current_player}, vyberte řádek (0, 1, 2): "))
        col = int(input(f"Hráč {current_player}, vyberte sloupec (0, 1, 2): "))
        
        if board[row][col] == "-":
            board[row][col] = current_player
        else:
            print("Tato pozice je již obsazena. Zkus to znovu.")
            continue

        if check_winner(board):
            print_board(board)
            print(f"Hráč {current_player} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

tic_tac_toe()
