import numpy as np
from collections import  *

def read_data(path="puzzle_input.txt"):
    """Reads puzzle input"""
    fin = open(path, "r")
    lines = [line.strip() for line in fin.readlines() if line.strip()]
    return lines

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

def task1(data):
    """Write the code for task 1 here"""
    initial_state = np.array([list(row) for row in data])
    initial_state = np.pad(initial_state, (1, 1), mode='constant')
    initial_state = initial_state.reshape((1, len(initial_state), len(initial_state)))

    print(initial_state[0])


    cycles = 6
    for i in range(cycles):

        for dim in initial_state:
            for row_idx, row in enumerate(dim, 1):
                for col_idx, col in enumerate(row, 1):
                    neighbor = find_adjacent_neighbors(dim, [row_idx, col_idx])
                    print(neighbor)

            exit()


        initial_state = np.pad(initial_state, (1, 1), mode='constant', constant_values='.')




def task2(data):
    """Write the code for task 2 here"""


def main():
    puzzle_input = read_data()

    print(f"Solution to task 1: {task1(puzzle_input)}")
    print(f"Solution to task 2: {task2(puzzle_input)}")


main()