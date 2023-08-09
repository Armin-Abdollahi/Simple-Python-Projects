#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Function to draw the game screen
def draw_board(board):
    print("-------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i][j], "|", end=" ")
        print("\n-------------")

# Function to check game status
def check_win(board, player):
    
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player or board[0][i] == board[1][i] == board[2][i] == player:
            return True

    # Checking diameters
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

# The main function of the game
def play_game():
    
    # First, we clear the game screen
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    # Start the game with the turn of the first player (X)
    current_player = "X"

    while True:
        draw_board(board)
        
        # Get the position of the current player
        row = int(input("Row selection (0-2): "))
        col = int(input("Column selection (0-2): "))
        
        # Checking the accuracy of the position and placing the player's token on the game board
        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("This house has already been selected. Please try another position.")
            continue
        
        # Checking the current player's win
        if check_win(board, current_player):
            draw_board(board)
            print("player", current_player, "you won!")
            break
            
        # Change the player's turn    
        current_player = "O" if current_player == "X" else "X"

# Start the game
play_game()

