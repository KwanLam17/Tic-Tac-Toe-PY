def display_board(board):
    print(F" {board[1]} | {board[2]} | {board[3]}\n---|---|---\n {board[4]} | {board[5]} | {board[6]}\n---|---|---\n {board[7]} | {board[8]} | {board[9]}")

def player_input():
    marker = ''

    while (marker != 'X') and (marker != 'O'):
        marker = input("Please pick a marker 'X' or 'O': ")

def place_marker(board, marker, position):
    board[position] = marker

# -------- TESTS -----------

test_board = ['#','X','O','X','O','X','O','X','O','X']
#display_board(test_board)
#player1 = player_input()
place_marker(test_board, '$', 8)
display_board(test_board)


