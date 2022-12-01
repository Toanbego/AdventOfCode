import numpy as np


def read_data(path="puzzle_input.txt"):
    """Reads puzzle input"""
    fin = open(path, "r")
    lines = [line.strip() for line in fin.readlines() if line.strip()]
    lines = np.array([[int(k) for k in i] for i in lines])
    lines = np.pad(lines,
           ((1, 1), (1, 1)),
           "constant", constant_values=(-100000, -100000))
    return lines


def get_adjacent_points(y, x):
    adjacent = []
    adjacent_idx_x, adjacent_idx_y = [-1, 1, 0, 0, -1, 1, 1, -1], [0, 0, -1, 1, -1, 1, -1, 1]
    for dx, dy in zip(adjacent_idx_x, adjacent_idx_y):
        adjacent.append([y + dy, x + dx])
    return adjacent


def increase_energy(array, y, x):
    """
    Recursively find each connected basin.
    Part of basin if point is 9 > point > connected point
    """
    array[y, x] = 0
    adjacent = get_adjacent_points(y, x)
    for dy, dx in adjacent:
        if 10 > array[dy, dx] > 0:
            array[dy, dx] += 1
            if array[dy, dx] > 9:
                array = increase_energy(array, dy, dx)
    return array


def task1(data, steps):
    """Write the code for task 1 here"""
    energies = data
    flashes = 0
    for i in range(steps):
        # Increase energy of all octo by 1
        energies = energies + np.ones(energies.shape)
        ready_to_flash = np.argwhere(energies > 9)
        for y, x in ready_to_flash:
            # Pad array to avoid out of bounds when checking adjacent elements
            energies = increase_energy(energies, y, x)
        flashes += len(np.argwhere(energies == 0))
    return flashes


def task2(data):
    """Write the code for task 2 here"""
    energies = data
    steps = 1
    while True:
        # Increase energy of all octo by 1
        energies = energies + np.ones(energies.shape)
        ready_to_flash = np.argwhere(energies > 9)
        for y, x in ready_to_flash:
            # Pad array to avoid out of bounds when checking adjacent elements
            energies = increase_energy(energies, y, x)
        if len(np.argwhere(energies == 0)) == (len(energies[0]) - 2) * (len(energies) - 2):
            return steps
        steps += 1


def main():
    puzzle_input = read_data()
    if task1(read_data("test_input.txt"), steps=100) == 1656:
        print(f"Solution to task 1: {task1(puzzle_input, steps=100)}")
    if task2(read_data("test_input.txt")) == 195:
        print(f"Solution to task 2: {task2(puzzle_input)}")


main()
