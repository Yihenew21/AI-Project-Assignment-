# Tic-Tac-Toe Game Implementation in Python

def print_board(board):
    """Print the Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
def check_winner(board, player):
    """Check if the given player has won."""
    # Check rows, columns, and diagonals
    for row in board:
        if all([cell == player for cell in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False
def check_draw(board):
    """Check if the game is a draw."""
    return all([cell != " " for row in board for cell in row])
def tic_tac_toe():
    """Main function to run the Tic-Tac-Toe game."""
    # Initialize the board
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        
        # Get player input
        while True:
            try:
                row = int(input("Enter the row (0, 1, 2): "))
                col = int(input("Enter the column (0, 1, 2): "))
                if row in [0, 1, 2] and col in [0, 1, 2] and board[row][col] == " ":
                    board[row][col] = current_player
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 2.")
                # Check for a winner or draw
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()