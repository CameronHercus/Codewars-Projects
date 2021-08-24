"""
3 kyu - Sudoku Solver

Write a function that will solve a 9x9 Sudoku puzzle. The function will take one argument consisting of the 2D puzzle array, with the value 0 representing an unknown square.

The Sudokus tested against your function will be "easy" (i.e. determinable; there will be no need to assume and test
possibilities on unknowns) and can be solved with a brute-force approach.

For Sudoku rules, see the Wikipedia article.

var puzzle = [
            [5,3,0,0,7,0,0,0,0],
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,7,9]];

sudoku(puzzle);
/* Should return
[[5,3,4,6,7,8,9,1,2],
[6,7,2,1,9,5,3,4,8],
[1,9,8,3,4,2,5,6,7],
[8,5,9,7,6,1,4,2,3],
[4,2,6,8,5,3,7,9,1],
[7,1,3,9,2,4,8,5,6],
[9,6,1,5,3,7,2,8,4],
[2,8,7,4,1,9,6,3,5],
[3,4,5,2,8,6,1,7,9]]
"""


def sudoku(puzzle):
    solve(puzzle)
    return puzzle


def solve(board):
    """ Attempts to place candidates 1-9 in unprocessed squares by
    recursively backtracking to fill the board and returning True once there
    no more unprocessed squares hence the Sudoku has been solved.

    Args:
        board (list):

    Returns:
        bool: Returns true if every square in the board is processed
    """
    square = find_unprocessed_square(board)
    if not square:  # Terminates if there are no more unprocessed squares
        return True
    else:
        row, col = square
    for candidate in range(1, 10, 1):
        if should_prune(board, candidate, (row, col)) is False:
            board[row][col] = candidate
            if solve(board):
                return True
            board[row][col] = 0
    return False


def should_prune(board, candidate, pos):
    """ Takes a candidate and returns true if it can be determined that they
    cannot lead to a solution.

    Args:
        board (list):
        candidate (int):
        pos (tuple):

    Returns:
        bool: Returns
    """
    row, col = pos[0], pos[1]  # pos is the tuple from find_empty_square
    # Check row
    for i in range(9):
        if board[row][i] == candidate and col != i:
            return True
    # Check column
    for i in range(9):
        if board[i][col] == candidate and row != i:
            return True
    # Check box
    box_x = col // 3
    box_y = row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == candidate and (i, j) != pos:
                return True
    return False


def find_unprocessed_square(board):
    """ Finds an unprocessed square on the board and returns the position as
    a tuple representing its row and column

    Args:
        board (list):

    Returns: object: Returns the position of an unprocessed square as a tuple if
        it can find one. Otherwise returns None
    """
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:  # 0 is denoted for unprocessed squares
                return i, j
    return None
