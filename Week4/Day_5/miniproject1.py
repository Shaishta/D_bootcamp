print("Welcome to TIC TAC TOE!")
board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

def display_board(board):
    print("****************")
    print("*  " + board[7] + "  |" + board[8] + "  |" + board[9] + "   *")
    print("*  ---|---|--- *")
    print("*  " + board[4] + "  |" + board[5] + "  |" + board[6] + "   *")
    print("*  ---|---|--- *")
    print("*  " + board[1] + "  |" + board[2] + "  |" + board[3] + "   *")
    print("****************")
player1 = input("Player X: Enter your name: ")
player2 = input("Player 0: Enter your name: ")
print(player1 + ": X |" + player2 + ": O")

#main function is player_input()***** call at the end#

def player_input():
    turn = "X"
    count = 0
    player_turn = player1
    for i in range(10):
        display_board(board)
        print("It's your turn, " + player_turn + ". Select to which place?")
        move = eval(input())
        if board[move] == " ":
            board[move] = turn
            count += 1
        else:
            print("That place is already filled.\nSelect another place?")
            continue
#winning places: top, middle, bottom, left, middle, right, diagonal(x2),
        if count >= 5:
            # across the top
            if board[7] == board[8] == board[9] != " ":
                check_win(turn)
                break
            # across the middle
            elif board[4] == board[5] == board[6] != " ":
                check_win(turn)
                break
            # across the bottom
            elif board[1] == board[2] == board[3] != " ":
                check_win(turn)
                break
            # down the left side
            elif board[1] == board[4] == board[7] != " ":
                check_win(turn)
                break
            # down the middle
            elif board[2] == board[5] == board[8] != " ":
                check_win(turn)
                break
            # down the right side
            elif board[3] == board[6] == board[9] != " ":
                check_win(turn)
                break
            # diagonal
            elif board[7] == board[5] == board[3] != " ":
                check_win(turn)
                break
            # diagonal
            elif board[1] == board[5] == board[9] != " ":
                check_win(turn)
                break
 # If nobody wins and the board is full, it is a 'tie'.
        if count == 9:
            print("Game Over.\n")
            print("It's a Tie!!")
 # change of players.
        if turn == "X":
            turn = "O"
            player_turn = player2
        else:
            turn = "X"
            player_turn = player1

def check_win(turn):
    display_board(board)
    print("Game Over.")
    if turn == "X":
        print("Yeah!!! " + player1 + " won !!!!")
    else:
        print("Yeah!!! " + player2 + " won !!!!")

# #calling the functions with the param
if __name__ == "__main__":
    player_input()

