board = [[" "," "," "],
         [" "," "," "],
         [" "," "," "]]

def game_board():
    print("-" * 5)
    for row in board:
        print("|".join(row))
        print("-" * 5)
        
def player_move():
    while True:
        try:
            row = int(input("Enter row number (0-2): "))
            column = int(input("Enter column number (0-2): "))
            if 0 <= row <= 2 and 0 <= column <= 2:
                return row, column
            else:
                print("Please only enter numbers between the range of 0 to 2.")
        except ValueError:
            print("Invalid input. Please only enter numbers in the range of 0 to 2.")
            
def update_board(row,column,player):
    if board[row][column] == " ":
        board[row][column] = player
        return True
    else:
        return False
    
def check_winner():
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    
def play_again():
    while True:
        answer = input("Do you want to play again? (yes/no): ").lower()
        if answer in ("yes", "no"):
            return answer == "yes"
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            
def reset_board():
    global board
    board = [[" "," "," "],
             [" "," "," "],
             [" "," "," "]]

def play_game():
    while True:
        current_player = "X"
        while True:
            game_board()
            print(f"Player {current_player}'s turn.")
            row, column = player_move()
            if update_board(row, column, current_player):
                winner = check_winner()
                if winner:
                    game_board()
                    print(f"Player {winner} wins!")
                    break
                elif all(board[i][j] != " " for i in range(3) for j in range(3)):
                    game_board()
                    print("It's a draw!")
                    break
                current_player = "O" if current_player == "X" else "X"
            else:
                print("That cell is already occupied. Please try again.")
        
        if not play_again():
            break
        else:
            reset_board()
            
print("lets play a TicTacToe game!!!")
play_game()
