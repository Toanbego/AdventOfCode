import numpy as np


def read_data(path="puzzle_input.txt"):
    """Reads puzzle input"""
    fin = open(path, "r")
    lines = [line.strip() for line in fin.readlines() if line.strip()]
    return lines


def task1(data):
    """Write the code for task 1 here"""
    final_depth, final_horizontal = 0, 0
    for i in data:
        if "forward" in i:
            final_horizontal += int(i[-1])
        elif "down" in i:
            final_depth += int(i[-1])
        elif "up" in i:
            final_depth -= int(i[-1])

    return final_horizontal * final_depth


def task2(data):
    """Write the code for task 2 here"""
    final_depth, final_horizontal, aim = 0, 0, 0
    for i in data:
        if "forward" in i:
            final_depth += aim * int(i[-1])
            final_horizontal += int(i[-1])
        elif "down" in i:
            aim += int(i[-1])
        elif "up" in i:
            aim -= int(i[-1])

    return final_horizontal * final_depth


def main():
    puzzle_input = read_data()
    print(f"Solution to task 1: {task1(puzzle_input)}")
    print(f"Solution to task 2: {task2(puzzle_input)}")


main()
