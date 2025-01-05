import numpy as np
rows = 6
cols = 7
game_over = False
player_turn = 1

def create_board():
    board = np.zeros((rows, cols))
    return board

board = create_board()
print(board)

def valid_column(board, col):
    if int(board[0][col]) == 0:
        return True
    else:
        return False

def move_piece(board, col, player):
    if valid_column(board, col):
        for r in range(len(board)-1, -1, -1):
            if board[r][col] == 0:
                board[r][col] = player
                return True
            
        else: 
            print("Column is full")
            return False

def player_input(board, player):
    player_input = 0 
    while player_input >= 8 or player_input <= 0:

        player_input = int(input("Player " + str(player) + " Choose a column (1-7): "))
        if player_input > 0 and player_input < 8:
            player_input -= 1
            if move_piece(board, player_input, player):
                print(board)
                return True
            else:
                return False
        else:
            print("Invalid input")
    

def play(game_over, player_turn, board):
    print(board)
    while not game_over:
        if player_turn == 1:
            if player_input(board, 1):
                player_turn = 2
                if check_win(board):
                    break
            else:
                player_turn = 1
        if player_turn == 2:
            if player_input(board, 2):
                player_turn = 1
                if check_win(board):
                    break
            else:
                player_turn = 2

def check_win(board):
    for r in range(len(board)):
        for c in range(len(board[r])-3):
            if board[r][c] == 1 or board[r][c] == 2:
                if board[r][c] == board[r][c+1] == board[r][c+2] == board[r][c+3]:
                    print("Player " + str(board[r][c])[0]," wins!")
                    return True
                
    for r in range(len(board)-3):
        for c in range(len(board[r])):
            if board[r][c] == 1 or board[r][c] == 2:
                if board[r][c] == board[r+1][c] == board[r+2][c] == board[r+3][c]:
                    print("Player " + str(board[r][c])[0]," wins!")
                    return True
                
    for r in range(len(board)-3):
        for c in range(0, len(board[r])):
            if board[r][c] == 1 or board[r][c] == 2:
                if board[r][c] == board[r+1][c+1] == board[r+2][c+2] == board[r+3][c+3]:
                    print("Player " + str(board[r][c])[0]," wins!")
                    return True
                
    for r in range(3, len(board)-3):
        for c in range(len(board[r])-3):
            if board[r][c] == 1 or board[r][c] == 2:
                if board[r][c] == board[r+1][c-1] == board[r+2][c-2] == board[r+3][c-3]:
                    print("Player " + str(board[r][c])[0]," wins!")
                    return True
                

play(game_over, player_turn, board)

