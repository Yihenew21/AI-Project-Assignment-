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
