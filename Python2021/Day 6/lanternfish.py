import numpy as np
from collections import Counter

def read_data(path="puzzle_input.txt"):
    """Reads puzzle input"""
    fin = open(path, "r")
    lines = [line.strip() for line in fin.readlines() if line.strip()]
    return lines


def task1(data):
    """Write the code for task 1 here"""
    # Create Model
    population_model = Counter(np.sort(np.array([int(i) for i in data[0].split(",")])))
    for key in range(10):
        if key not in population_model:
            population_model[key] = 0

    # Model over time
    for i in range(80):
        # Add new spawns and reset timer
        if population_model[0] > 0:
            population_model[7] += population_model[0]
            population_model[9] += population_model[0]

        # Decrement timer
        for k in range(len(population_model)-1):
            population_model[k] = population_model[k+1]
        population_model[9] = 0

    return sum(population_model.values())




def task2(data):
    """Write the code for task 2 here"""
    # Create Model
    population_model = Counter(np.sort(np.array([int(i) for i in data[0].split(",")])))
    for key in range(10):
        if key not in population_model:
            population_model[key] = 0

    # Model over time
    for i in range(256):
        # Add new spawns and reset timer
        if population_model[0] > 0:
            population_model[7] += population_model[0]
            population_model[9] += population_model[0]

        # Decrement timer
        for k in range(len(population_model) - 1):
            population_model[k] = population_model[k + 1]
        population_model[9] = 0

    return sum(population_model.values())

    return sum(population_model.values())


def main():
    puzzle_input = read_data()
    if task1(read_data("test_input.txt")) == 5934:
        print(f"Solution to task 1: {task1(puzzle_input)}")
    if task2(read_data("test_input.txt")) == 26984457539:
        print(f"Solution to task 2: {task2(puzzle_input)}")


main()
