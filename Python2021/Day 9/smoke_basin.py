import numpy as np


def read_data(path="puzzle_input.txt"):
    """Reads puzzle input"""
    fin = open(path, "r")
    lines = [line.strip() for line in fin.readlines() if line.strip()]
    return lines


def get_adjacent_points(y, x):
    adjacent = []
    adjacent_idx_x, adjacent_idx_y = [-1, 1, 0, 0], [0, 0, -1, 1]
    for dx, dy in zip(adjacent_idx_x, adjacent_idx_y):
        adjacent.append([y + dy, x + dx])
    return adjacent


def get_low_points(height_map):
    """Find out if a point is its lowest compared to its adjacent points"""
    low_points = []
    for y in range(1, len(height_map) - 1):
        for x in range(1, len(height_map[0]) - 1):
            adjacent_heights = np.array([height_map[i[0], i[1]] for i in get_adjacent_points(y, x)])
            if len(adjacent_heights[adjacent_heights > height_map[y, x]]) == 4:
                low_points.append([y, x])
    return low_points


def get_basin(height_map, y, x, has_visited):
    """
    Recursively find each connected basin.
    Part of basin if point is 9 > point > connected point
    """
    adjacent = get_adjacent_points(y, x)
    for p in adjacent:
        if 9 > height_map[p[0], p[1]] > height_map[y, x] and [p[0], p[1]] not in has_visited:
            get_basin(height_map, p[0], p[1], has_visited)
            has_visited.append([p[0], p[1]])

    return has_visited


def task1(data):
    """Write the code for task 1 here"""
    height_map = np.pad(np.array([[int(k) for k in i] for i in data]),
                        ((1, 1), (1, 1)),
                        "constant", constant_values=(10, 10))
    low_points = get_low_points(height_map)
    return sum([1 + height_map[i[0], i[1]] for i in low_points])



def task2(data):
    """Write the code for task 2 here"""
    height_map = np.pad(np.array([[int(k) for k in i] for i in data]),
                        ((1, 1), (1, 1)),
                        "constant", constant_values=(10, 10))
    # Loop through each low point to find its basin
    low_points = get_low_points(height_map)
    basins = []
    for y, x in low_points:
        has_visited = [[y, x]]
        check = get_basin(height_map, y, x, has_visited)
        basins.append(check)
    # Find 3 largest basins and multiply them
    return np.prod(np.array(sorted([len(i) for i in basins])[-3:]))


def main():
    puzzle_input = read_data()
    if task1(read_data("test_input.txt")) == 15:
        print(f"Solution to task 1: {task1(puzzle_input)}")
    if task2(read_data("test_input.txt")) == 1134:
        print(f"Solution to task 2: {task2(puzzle_input)}")


main()
