#!/usr/bin/python3
"""N queens"""

import sys


def is_valid(board, row, col):
    """Check if placing a queen in the given position is valid"""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def print_solution(board):
    """Print the current solution in the specified format"""
    print("[", end="")
    for i in range(len(board)):
        print("[{}, {}]".format(i, board[i]), end=" ")
    print("\b\b]]")


def solve_nqueens(board, row, n):
    """Recursively solve N-Queens"""
    if row == n:
        print_solution(board)
        return

    for col in range(n):
        if is_valid(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, n)


def nqueens(n):
    """Initialize the board with all queens in the first column"""
    board = [-1] * n
    solve_nqueens(board, 0, n)


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
