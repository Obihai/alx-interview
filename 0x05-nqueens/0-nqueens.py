#!/usr/bin/python3
""" Nqueens """


import sys


def is_safe(board, row, col):
    """
    Check if a queen can be placed at the given row and col
    without attacking any other queens on the board.
    """
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_nqueens(board, row, N):
    """
    Solve the N Queens problem using backtracking.
    """
    if row == N:
        print([[i, board[i]] for i in range(N)])
        return

    # Try placing a queen in each column of the current row.
    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, N)
            board[row] = -1  # Backtrack to find other solutions.


def nqueens(N):
    """
    Solve the N Queens problem and print all possible solutions.
    """
    board = [-1] * N

    # Start the backtracking algorithm from the first row (row 0).
    solve_nqueens(board, 0, N)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(N)
