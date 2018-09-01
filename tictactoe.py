# ---- START OF IMPORTS ----

import random

# ---- END OF IMPORTS/START OF CONSTANTS ------

WIN_POSITIONS = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))

# ---- END OF CONSTANTS/START OF FUNCTIONS ------

def display_board(board):
    print(F" {board[1]} | {board[2]} | {board[3]}\n---|---|---\n {board[4]} | {board[5]} | {board[6]}\n---|---|---\n {board[7]} | {board[8]} | {board[9]}")

def player_input():
    marker = ''
    while (marker != 'X') and (marker != 'O'):
        marker = input("Player 1, please pick a marker 'X' or 'O': ")
    return marker

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    for win_cond in WIN_POSITIONS:
        count = 0
        for pos in win_cond:
            if board[pos] == mark:
                count += 1
        if count == 3:
            return True
    return False

def choose_first():
    return random.randint(1,2)

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for pos in board[1:]:
        if pos == ' ':
            return False
    return True

def player_choice(board):
    position = 0   # always not empty
    while(not space_check(board, position)):
        position = int(input("Please enter a position 1-9: "))
    return position

def replay():
    again = input("Would you like to play again? (YES/NO): ")
    if again.lower() == "yes":
        return True
    return False

# ---- END OF FUNCTIONS/START OF TESTS ------

# test_board = ['#','X','O','X','O','X','O','X','O','X']
# blank_board = ['#',' ','O','X','O','X','O','X','O','X']
# display_board(test_board)
# player1 = player_input()
# place_marker(test_board, '$', 8)
# display_board(test_board)
# print(win_check(test_board,'X'))
# print(str(choose_first())
# print(space_check(blank_board, 1))
# print(full_board_check(test_board))
# print(full_board_check(blank_board))
# player_choice(blank_board)
# print(replay())

# ---- END OF TESTS/START OF MAIN ------

print("Welcome to Tic-Tac-Toe!")

while(True):
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    markers = []

    markers.append(player_input())

    if markers[0] == 'X':
        markers.append('O')
    else:
        markers.append('X')

    cur_player = choose_first()

    display_board(board)

    while(full_board_check):
        print(f"PlAYER {cur_player}'S TURN")
        position = player_choice(board)
        place_marker(board, markers[cur_player - 1], position)
        display_board(board)
        if win_check(board, markers[cur_player - 1]):
            print(f"Player {cur_player} wins!")
            break
        else:
            cur_player = int(not cur_player)
        
    if(not replay()):
        break
    

