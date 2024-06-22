# Tic-Tac-Toe Game Implementation in Python

def print_board(board):
    """Print the Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
