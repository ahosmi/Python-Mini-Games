def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    turn = 0

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        player = players[turn % 2]
        row = int(input(f"Player {player}, enter row (1-3): ")) - 1
        col = int(input(f"Player {player}, enter column (1-3): ")) - 1

        if board[row][col] != " ":
            print("That cell is already taken. Try again.")
            continue

        board[row][col] = player
        print_board(board)

        if check_win(board, player):
            print(f"Player {player} wins!")
            break
        elif turn == 8:
            print("It's a tie!")
            break

        turn += 1

tic_tac_toe()
