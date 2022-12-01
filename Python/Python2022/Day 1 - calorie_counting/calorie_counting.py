import numpy as np


class Data:

    def __init__(self, inputs):
        """Reads puzzle input"""
        self.inputs = inputs
        self.data = {}
        for i in range(len(inputs)):
            if "puzzle" not in list(self.data.keys()):
                self.data["puzzle"] = self.parse_data(inputs[i])
            else:
                self.data[f"test_input{i}"] = self.parse_data(inputs[i])

    def parse_data(self, path):
        """"""
        file = open(path, "r")
        lines = [line for line in file.readlines()]
        items, elves = [], []

        for idx, line in enumerate(lines):

            if line != "\n":
                items.append(int(line.strip()))

            if idx == len(lines)-1 or line == "\n":
                elves.append(items)
                items = []

        return elves


def task1(data):
    """Write the code for task 1 here"""
    return max([sum(item) for item in data])


def task2(data):
    """Write the code for task 2 here"""
    calories = [sum(i) for i in data]
    calories.sort()
    return sum(calories[-3:])


def main():
    puzzle_input = Data(["puzzle_input.txt", "test_input.txt"])

    assert task1(puzzle_input.data["test_input1"]) == 24000
    print(f"Solution to task 1: {task1(puzzle_input.data['puzzle'])}")

    assert task2(puzzle_input.data["test_input1"]) == 45000, "Failed test"
    print(f"Solution to task 2: {task2(puzzle_input.data['puzzle'])}")


main()
