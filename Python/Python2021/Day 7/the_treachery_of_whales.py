import numpy as np



def read_data(path="puzzle_input.txt"):
    """Reads puzzle input"""
    fin = open(path, "r")

    lines = [line.strip() for line in fin.readlines() if line.strip()]
    return np.array(lines[0].split(",")).astype(int)


def task1(data):
    """Write the code for task 1 here"""
    crab_positions = data
    fuel_comparison = []
    for pos in range(int(np.min(crab_positions)), int(np.max(crab_positions))):
        fuel_comparison.append(sum([abs(pos-i) for i in crab_positions]))
    return min(fuel_comparison)


def task2(data):
    """Write the code for task 2 here"""
    crab_positions = data
    fuel_comparison = []
    for pos in range(int(np.min(crab_positions)), int(np.max(crab_positions))):
        fuel_comparison.append(sum([int((abs(pos-i)/2)*(1+(abs(pos-i)))) for i in crab_positions])) # (n/2)*(n1+n2)
    return min(fuel_comparison)


def main():
    puzzle_input = read_data()
    if task1(read_data("test_input.txt")) == 37:
        print(f"Solution to task 1: {task1(puzzle_input)}")
    if task2(read_data("test_input.txt")) == 168:
        print(f"Solution to task 2: {task2(puzzle_input)}")


main()
