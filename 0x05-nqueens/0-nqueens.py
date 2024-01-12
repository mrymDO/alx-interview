#!/usr/bin/python3
import sys


def check_two_queens(new_queen_position, other_queen_position):
    if new_queen_position[0] == other_queen_position[0] or\
            new_queen_position[1] == other_queen_position[1]:
        return False
    if new_queen_position[0] + new_queen_position[1] ==\
            other_queen_position[0] + other_queen_position[1]:
        return False
    if new_queen_position[0] - new_queen_position[1] ==\
            other_queen_position[0] - other_queen_position[1]:
        return False
    return True


def solve_nqueens(n):
    queens = []
    solutions = []

    def backtrack(row):
        if row == n:
            solutions.append(list(queens))
            return
        for col in range(n):
            if all(check_two_queens((row, col), queen) for queen in queens):
                queens.append([row, col])
                backtrack(row + 1)
                queens.pop()

    backtrack(0)

    for solution in solutions:
        print(solution)


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

    solve_nqueens(N)
