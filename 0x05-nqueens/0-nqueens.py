#!/usr/bin/python3
"""
A script for cheers
"""
import sys

def show_usage_and_exit():
    """
    A method to show how to use the script
    """
    print("Usage: nqueens N")
    sys.exit(1)

def show_not_a_number_error_and_exit():
    """
    A method to show error with number.
    """
    print("N must be a number")
    sys.exit(1)

def show_too_small_number_error_and_exit():
    """
    A method to handle errors with small numbers
    """
    print("N must be at least 4")
    sys.exit(1)

def find_nqueens_solutions(size):
    """
    A method used to search for solutions
    """
    def is_position_valid(board_state, current_row, current_col):
        """
        A method to look for valid positions.
        """
        for row in range(current_row):
            if board_state[row][1] == current_col or \
               board_state[row][1] - row == current_col - current_row or \
               board_state[row][1] + row == current_col + current_row:
                return False
        return True

    def place_queens(row):
        """
        A method used to look for places.
        """
        if row == size:
            all_solutions.append([list(state) for state in board_state])
            return
        for col in range(size):
            if is_position_valid(board_state, row, col):
                board_state[row][1] = col
                place_queens(row + 1)
                board_state[row][1] = -1

    all_solutions = []
    board_state = [[i, -1] for i in range(size)]
    place_queens(0)
    return all_solutions

def main():
    if len(sys.argv) != 2:
        show_usage_and_exit()

    try:
        n = int(sys.argv[1])
    except ValueError:
        show_not_a_number_error_and_exit()

    if n < 4:
        show_too_small_number_error_and_exit()

    solutions = find_nqueens_solutions(n)
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()
