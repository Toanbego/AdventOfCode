import numpy as np
from collections import *
from copy import deepcopy


def read_data(path="puzzle_input.txt"):
    fin = open(path, "r")
    lines = [line.strip() for line in fin.readlines() if line.strip()]
    return lines


def check_seating(empty, occupied, mode='normal'):
    if list(occupied):
        if list(empty) and mode == 'normal':

            if min(empty[0]) < min(occupied[0]):
                return 0
            else:
                return 1
        elif list(empty) and mode == 'reverse':
            if min(empty[0]) > min(occupied[0]):
                return 0
            else:
                return 1
        else:
            return 1
    else:
        return 0



def getDiagonals(matrix, pos):
    row, col = pos
    nrows = len(matrix)
    ncols = len(matrix[0]) if nrows > 0 else 0
    # First diagonal
    d1_i, d1_j = nrows - 1 - max(row - col, 0), max(col - row, 0)
    d1_len = min(d1_i + 1, ncols - d1_j)
    diag1 = [matrix[d1_i - k][d1_j + k] for k in range(d1_len)]
    # Second diagonal
    t = min(row, ncols - col - 1)
    d2_i, d2_j = nrows - 1 - row + t, col + t
    d2_len = min(d2_i, d2_j) + 1
    diag2 = [matrix[d2_i - k][d2_j - k] for k in range(d2_len)]
    return np.array(diag2), np.array(diag1)


def find_word(board, index):
    """ Finds visible occupied seats in matrix """
    # Get index
    idx_y, idx_x = index[0], index[1]
    occupied_counter = 0

    # Check east
    empty_seats = np.argwhere(board[idx_y, idx_x+1:] == 'L')
    occupied_seats = np.argwhere(board[idx_y, idx_x+1:] == '#')
    occupied_counter += check_seating(empty_seats, occupied_seats)

    # Check west
    empty_seats = np.argwhere(board[idx_y, :idx_x] == 'L')
    occupied_seats = np.argwhere(board[idx_y, :idx_x] == '#')
    occupied_counter += check_seating(empty_seats, occupied_seats, "reverse")

    # Check south
    empty_seats = np.argwhere(board[idx_y + 1:, idx_x] == 'L')
    occupied_seats = np.argwhere(board[idx_y + 1:, idx_x] == '#')
    occupied_counter += check_seating(empty_seats, occupied_seats)

    # Check North
    empty_seats = np.argwhere(np.flip(board[:idx_y, idx_x], 0) == 'L')
    occupied_seats = np.argwhere(np.flip(board[:idx_y, idx_x], 0) == '#')
    occupied_counter += check_seating(empty_seats, occupied_seats, "reverse")

    # Check South-East
    diag1, diag2 = getDiagonals(board, (idx_y, idx_x))
    diag = np.flip(diag1, 0)
    empty_seats = np.argwhere(diag[idx_x+1:] == 'L')
    occupied_seats = np.argwhere(diag[idx_x+1:] == '#')
    occupied_counter += check_seating(empty_seats, occupied_seats, "normal")

    # Check north west
    empty_seats = np.argwhere(diag1[:idx_x] == 'L')
    occupied_seats = np.argwhere(diag1[:idx_x] == '#')
    occupied_counter += check_seating(empty_seats, occupied_seats, "reverse")

    # Check North-East
    empty_seats = np.argwhere(diag2[idx_x + 1:] == 'L')
    occupied_seats = np.argwhere(diag2[idx_x + 1:] == '#')
    occupied_counter += check_seating(empty_seats, occupied_seats, "normal")

    # Check North-East
    empty_seats = np.argwhere(diag2[:idx_x] == 'L')
    occupied_seats = np.argwhere(diag2[:idx_x] == '#')
    occupied_counter += check_seating(empty_seats, occupied_seats, "normal")
    return occupied_counter


def find_adjacent_neighbors(array, index=None):
    """
    Find vertical, horizontal and diagonal neighbors of a given element
    :param board_shape:
    :return:
    """
    neighbors = defaultdict(list)
    i, j = index[0], index[1]
    neighbors[array[i - 1][j - 1]].append([i - 1, j - 1])
    neighbors[array[i - 1][j]].append([i - 1, j])
    neighbors[array[i - 1][j + 1]].append([i - 1, j + 1])
    neighbors[array[i][j - 1]].append([i, j - 1])
    neighbors[array[i][j + 1]].append([i, j + 1])
    neighbors[array[i + 1][j - 1]].append([i + 1, j - 1])
    neighbors[array[i + 1][j]].append([i + 1, j])
    neighbors[array[i + 1][j + 1]].append([i + 1, j + 1])
    return neighbors


def arrays_equal(a, b):
    if a.shape != b.shape:
        return False
    for ai, bi in zip(a.flat, b.flat):
        if ai != bi:
            return False
    return True


def first_task(board):
    current_board = [list(row) for row in board]
    current_board = np.array(list(current_board))
    current_board = np.pad(current_board, (1, 1), mode='constant')

    while True:
        state_check = deepcopy(current_board)
        for idx1, row in enumerate(state_check[1:-1], 1):
            for idx2, seat_space in enumerate(row[1:-1], 1):
                neighbors = find_adjacent_neighbors(state_check, index=[idx1, idx2])
                if seat_space == 'L' and '#' not in list(neighbors.keys()):
                    current_board[idx1, idx2] = '#'
                elif seat_space == '#' and len(neighbors['#']) >= 4:
                    current_board[idx1, idx2] = 'L'
        if arrays_equal(state_check, current_board):
            occupied_seats = np.argwhere(current_board == '#')
            number_of_occupied = len(occupied_seats)
            break
    print("Solution to task 1: " + str(number_of_occupied))


def second_task(board):
    current_board = [list(row) for row in board]
    current_board = np.array(list(current_board))
    current_board = np.pad(current_board, (1, 1), mode='constant')

    while True:
        state_check = deepcopy(current_board)
        for idx1, row in enumerate(state_check[1:-1], 1):
            for idx2, seat_space in enumerate(row[1:-1], 1):
                neighbors = find_word(state_check, index=[idx1, idx2])
                if seat_space == 'L' and neighbors == 0:
                    current_board[idx1, idx2] = '#'
                elif seat_space == '#' and neighbors > 5:
                    current_board[idx1, idx2] = 'L'
        if arrays_equal(state_check, current_board):
            occupied_seats = np.argwhere(current_board == '#')
            number_of_occupied = len(occupied_seats)
            break
    print("Solution to task 2: " + str(number_of_occupied))



if __name__ == '__main__':
    puzzle_input = read_data("puzzle_input.txt")

    first_task(puzzle_input)

    second_task(puzzle_input)

