#!/usr/bin/python3
'''N-Queens Challenge'''

import sys


def is_safe(placed_queens, row, col):
    for cord in placed_queens:
        if (
            cord[1] == col
            or cord[1] + (row - cord[0]) == col
            or cord[1] - (row - cord[0]) == col
        ):
            return False
    return True


def print_solution(placed_queens):
    """Print the current solution in the specified format"""
    print("[", end="")
    for cord in placed_queens:
        print("[{}, {}]".format(cord[0], cord[1]), end=" ")
    print("\b\b]]")


def solve_nqueens(n, row, placed_queens, solutions):
    """Recursively solve N-Queens"""
    if row == n:
        print_solution(placed_queens)
        return

    for col in range(n):
        if is_safe(placed_queens, row, col):
            placed_queens.append([row, col])
            solve_nqueens(n, row + 1, placed_queens, solutions)
            placed_queens.pop()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)

    if n < 4:
        print('N must be at least 4')
        exit(1)

    solutions = []
    solve_nqueens(n, 0, [], solutions)
