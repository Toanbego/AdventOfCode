import numpy as np


def read_data(path="puzzle_input.txt"):
    """Reads puzzle input"""
    fin = open(path, "r")
    lines = [line.strip() for line in fin.readlines() if line.strip()]
    return lines


def task1(data):
    """Write the code for task 1 here"""



def task2(data):
    """Write the code for task 2 here"""


def main():
    puzzle_input = read_data()
    print(f"Solution to task 1: {task1(puzzle_input)}")
    print(f"Solution to task 2: {task2(puzzle_input)}")


main()