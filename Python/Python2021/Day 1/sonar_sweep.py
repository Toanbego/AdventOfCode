import numpy as np


def read_data(path="puzzle_input.txt"):
    """Reads puzzle input"""
    fin = open(path, "r")
    lines = [line.strip() for line in fin.readlines() if line.strip()]
    return lines


def task1(data):
    """Write the code for task 1 here"""
    result = 0
    for i in range(1, len(data)):
        if int(data[i]) > int(data[i-1]):
            result += 1
    return result


def task2(data):
    """Write the code for task 2 here"""
    result = 0
    for i in range(3, len(data)):
        sumA = int(data[i - 1]) + int(data[i - 2]) + int(data[i - 3])
        sumB = int(data[i]) + int(data[i - 1]) + int(data[i - 2])
        if sumB > sumA:
            result += 1
    return result


def main():
    puzzle_input = read_data()
    print(f"Solution to task 1: {task1(puzzle_input)}")
    print(f"Solution to task 2: {task2(puzzle_input)}")


main()
