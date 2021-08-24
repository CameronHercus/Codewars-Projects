import copy
import math

"""
3 kyu - Hard Sudoku Solver

This kata is a harder version of http://www.codewars.com/kata/sudoku-solver/python made by @pineappleclock

Write a function that will solve a 9x9 Sudoku puzzle. The function will take one argument consisting of the 2D puzzle 
array, with the value 0 representing an unknown square. 

The Sudokus tested against your function will be "insane" and can have multiple solutions. The solution only need to give one valid solution in the case of the multiple solution sodoku.

It might require some sort of brute force.

Consider applying algorithm with

Backtracking https://www.wikiwand.com/en/Sudoku_solving_algorithms#Backtracking
Brute Force
For Sudoku rules, see the Wikipedia : http://www.wikiwand.com/en/Sudoku

Used puzzle from : http://www.extremesudoku.info/sudoku.html

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

solve(puzzle)
"""


def solve(board):
    # init a blank sudoku
    sudoku = Sudoku()

    # set the input board to our sudoku
    sudoku.setboard(board)

    # if the input is invalid, raise an error
    if not sudoku.valid:
        raise ValueError

    # solve the sudoku, the results (if any) will be stored in sudoku.result_boards
    sudoku.solve()

    # if there are no solution, or there are more than 1 solution
    # return the only solution
    return sudoku.result_boards[0]


class Sudoku:
    ### Notes:
    # cells will be indexed from 0 to 80

    ### init static constants:

    # list of the digits that will be filled in the sudoku
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # List of block/units that each cell stays in.
    # For example, cell[9] (row 1, col 0) has 3 units:
    # units[9][0] == [9, 10, 11, 12, 13, 14, 15, 16, 17] (all cells in the same row)
    # units[9][1] == [0,  9, 18, 27, 36, 45, 54, 63, 72] (all cells in the same column)
    # units[9][2] == [0,  1,  2,  9, 10, 11, 18, 19, 20] (all cells in the same box)
    units = []

    # list of all peers of each cell, which are all the unique cells in the same row, column and box.
    # For example, cell[9] (row 1, col 0) has the following peers:
    # peers[9] == [9, 10, 11, 12, 13, 14, 15, 16, 17, 0, 18, 27, 36, 45, 54, 63, 72, 0, 1, 2, 19, 20]
    peers = []

    # init units and peers table
    for i in range(81):
        units.append([])
        # add cells in same row
        units[i].append([])
        r = int(i / 9)
        for c in range(9):
            units[i][0].append(r * 9 + c)
        # add cells in same col
        units[i].append([])
        c = int(i % 9)
        for r in range(9):
            units[i][1].append(r * 9 + c)
        # add cells in same box
        units[i].append([])
        br = int(int(i / 9) / 3)
        cr = int(int(i % 9) / 3)
        for r in range(br * 3, br * 3 + 3):
            for c in range(cr * 3, cr * 3 + 3):
                units[i][2].append(r * 9 + c)
        # collect all neighbor cells of each cell
        peers.append([])
        for unit in units[i]:
            for cell in unit:
                if cell not in peers[i]:
                    peers[i].append(cell)
        peers[i].remove(i)

    # init a blank sudoku
    def __init__(self):
        self.mask = []
        self.valid = True
        self.solutions = []
        self.result_boards = []

    # set the input board to our sudoku
    def setboard(self, board):
        # the mask array of the 80 cells
        self.mask = []

        # whether the sudoku is valid
        self.valid = True

        # the list of solutions (if any) in mask format
        self.solutions = []

        # the list of solutions (if any) in human readable array format
        self.result_boards = []

        # check the input board dimensions
        if not self.validate(board):
            self.valid = False

        # init mask matrix with all cells set to 0x1ff, indicating that all 9 digits are still allowed in that cell
        self.mask = [0x1ff] * 81

        # set the input board to this sudoku matrix, and also update the peers' masks for each cell along the way
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c]:
                    # if the digit cannot be set at a cell, we mark that the input board is invalid (unsolvable)
                    if not self.set(r * 9 + c, board[r][c]):
                        self.valid = False
                        return

    # validate board dimensions
    def validate(self, board):
        if len(board) != 9:
            return False
        for r in range(len(board)):
            if len(board[r]) != 9:
                return False
        return True

    # convert mask to human readable two-dimensional array
    def mask_to_board(self, mask):
        board = []
        for r in range(9):
            board.append([0] * 9)
        for r in range(9):
            for c in range(9):
                if self.is_single_bit(mask[r * 9 + c]):
                    for d in self.digits:
                        if mask[r * 9 + c] & (1 << (d - 1)):
                            board[r][c] = d
        return board

    # clone the current status of the sudoku
    def clone(self):
        sudoku = Sudoku()
        sudoku.mask = copy.copy(self.mask)
        sudoku.valid = self.valid
        return sudoku

    # the main function to solve the sudoku
    def solve(self):
        # call the recursive function solve_helper to solve
        self.solve_helper()

        # convert the solution masks into human readable two-dimensional array and stored in result_boards
        for result in self.solutions:
            self.result_boards.append(self.mask_to_board(result))

    # recursive function to solve the board
    def solve_helper(self):
        # choose the vacant cell with the fewest possibilities
        cell = self.find_vacant_with_min_possibilities()

        # if all cells have been filled (no vacant cell), we have found a solution!
        if cell is None:
            self.add_solution(self.mask)
            return

        # try the remaining possible value in this cell
        for d in self.digits:
            # skip if d is not allowed in this cell
            if not (self.mask[cell] & (1 << (d - 1))):
                continue

            # clone the sudoku status...
            sudoku = self.clone()

            # ... and try digit d in the cloned one to start searching for a solution
            # if setting d in this cell leads to an unsolvable sudoku: stop further processing
            if not sudoku.set(cell, d):
                continue

            # solve the cloned sudoku with the newly filled value
            sudoku.solve_helper()

            # if we found any solutions for the cloned sudoku:
            if len(sudoku.solutions) > 0:
                # collect those solutions for our current sudoku
                for solution in sudoku.solutions:
                    self.add_solution(solution)

            # the problem requires us raise error if there are more than one solution,
            # so we can skip further processing if 2 solutions have been found
            if len(self.solutions) >= 2:
                return

    # a mask is considered as set if there's only one bit turned on.
    # m has exactly one bit turned on if (m & (m - 1)) == 0
    def is_single_bit(self, m):
        return (m & (m - 1)) == 0

    # count number of turned on bits in a mask
    def count_bits(self, m):
        count = 0
        while m:
            m &= (m - 1)
            count += 1
        return count

    # add a solution to our collection, skip if that solution already exists
    def add_solution(self, mask):
        for result in self.solutions:
            if result == mask:
                return
        self.solutions.append(copy.deepcopy(mask))

    # find the vacant cell with fewest allowed value
    def find_vacant_with_min_possibilities(self):
        vacant_cnt = 0
        best_vacant_possibilities = 10
        best_vacant_i = 0
        for i in range(81):
            if best_vacant_possibilities == 2:
                break;
            if not self.is_single_bit(self.mask[i]):
                vacant_cnt += 1
                choices = self.count_bits(self.mask[i])

                if choices < best_vacant_possibilities:
                    best_vacant_possibilities = choices
                    best_vacant_i = i

        if (vacant_cnt == 0):
            # no more vacant cell:
            return None

        return best_vacant_i

    # set digit d at cell by clearing all the other bits (except for dth bit) in mask[cell]
    # return False if a contradiction is detected.
    # return True otherwise
    def set(self, cell, d):
        other_values = [d2 for d2 in self.digits if d2 != d and self.mask[cell] & (1 << (d2 - 1))]
        for d2 in other_values:
            if not self.clear(cell, d2):
                return False
        return True

    # removing a digit d from being allowed at cell by clearing the dth bit
    def clear(self, cell, d):
        # if already cleared
        if not (self.mask[cell] & (1 << (d - 1))):
            return True

        # turn off bit at d to mark d is no longer allowed at this cell
        self.mask[cell] &= ~(1 << (d - 1))

        # Rule 1: If this cell has only one allowed value d2,
        # then make d2 the value at cell and eliminate d2 from the peers.
        if self.mask[cell] == 0:
            return False  # error: no value is allowed at this cell (Rule 3)
        elif self.is_single_bit(self.mask[cell]):
            val = int(math.log2(self.mask[cell])) + 1
            for cell2 in self.peers[cell]:
                if not self.clear(cell2, val):
                    return False

        ## Rule 2: If all cells in the unit cannot be filled with d except for one cell2,
        # we can fill d in that cell2.
        for u in self.units[cell]:
            dplaces = [cell2 for cell2 in u if self.mask[cell2] & (1 << (d - 1))]
            if len(dplaces) == 0:
                return False  # error: no place for this value (Rule 4)
            elif len(dplaces) == 1:
                # d can only be in one place in unit; assign it there
                if not self.set(dplaces[0], d):
                    return False
        return True
