import numpy as np


def read_data(path="puzzle_input.txt"):
    """Reads puzzle input"""
    fin = open(path, "r")
    lines = [line.strip() for line in fin.readlines() if line.strip()]
    return lines


def find_adjacent_points(array, x, y):
    adjacent = []
    adjacent_idx_x, adjacent_idx_y = [-1, 1, 0, 0], [0, 0, -1, 1]
    for dx, dy in zip(adjacent_idx_x, adjacent_idx_y):
        adjacent.append(array[y + dy, x + dx])
    return np.array(adjacent)


def task1(data):
    """Write the code for task 1 here"""
    height_map = np.pad(np.array([[int(k) for k in i] for i in data]),
                        ((1, 1), (1, 1)),
                        "constant", constant_values=(10, 10))
    low_points = []
    for y in range(1, len(height_map)-1):
        for x in range(1, len(height_map[0])-1):
            adjacent = find_adjacent_points(height_map, x, y)
            if len(adjacent[adjacent > height_map[y, x]]) == 4:
                low_points.append(1+height_map[y, x])
    return sum(low_points)



def task2(data):
    """Write the code for task 2 here"""


def main():
    puzzle_input = read_data()
    if task1(read_data("test_input.txt")) == 15:
        print(f"Solution to task 1: {task1(puzzle_input)}")
    if task2(read_data("test_input.txt")) == 12:
        print(f"Solution to task 2: {task2(puzzle_input)}")


main()
