import numpy as np
from collections import Counter

def read_data(path="puzzle_input.txt"):
    """Reads puzzle input"""
    fin = open(path, "r")
    lines = [line.strip() for line in fin.readlines() if line.strip()]
    return lines


def task1(data):
    """Write the code for task 1 here"""
    grid = np.full((1000, 1000), 0)
    for vent in data:
        x1, y1, x2, y2 = np.array(vent.replace(" -> ", ",").split(",")).astype(int)
        x_coordinates = np.linspace(x1, x2, num=abs(x1 - x2) + 1)
        y_coordinates = np.linspace(y1, y2, num=abs(y1 - y2) + 1)
        if x1 == x2 or y1 == y2:
            for x in x_coordinates:
                for y in y_coordinates:
                    grid[int(y), int(x)] += 1
    return len(grid[grid > 1])


def task2(data):
    """Write the code for task 2 here"""
    grid = np.full((1000, 1000), 0)
    for vent in data:
        x1, y1, x2, y2 = np.array(vent.replace(" -> ", ",").split(",")).astype(int)
        x_coordinates = np.linspace(x1, x2, num=abs(x1 - x2) + 1)
        y_coordinates = np.linspace(y1, y2, num=abs(y1 - y2) + 1)
        if x1 == x2 or y1 == y2:
            for x in x_coordinates:
                for y in y_coordinates:
                    grid[int(y), int(x)] += 1

        elif len(x_coordinates) == len(y_coordinates):
            for y, x in zip(y_coordinates, x_coordinates):
                grid[int(y), int(x)] += 1
    return len(grid[grid > 1])


def main():
    puzzle_input = read_data()

    if task1(read_data("test_input.txt")) == 5:
        print(f"Solution to task 1: {task1(puzzle_input)}")
    if task2(read_data("test_input.txt")) == 12:
        print(f"Solution to task 2: {task2(puzzle_input)}")


main()
