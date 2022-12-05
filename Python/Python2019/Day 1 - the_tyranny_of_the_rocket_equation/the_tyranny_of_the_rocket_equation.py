import numpy as np


class Data:
    class Data:

        def __init__(self, inputs):
            """Reads puzzle input"""
            self.data = {"test_input": self.parse_data(inputs[1])}
            self.data[f"puzzle"] = self.parse_data(inputs[0])

        def parse_data(self, path):
            """This parses data"""
            file = open("puzzle_input.txt", "r")
            return list(map(lambda x: [int(i) for i in x.split("\n")], file.read().split("\n\n")))


def task1(data):
    """Write the code for task 1 here"""


def task2(data):
    """Write the code for task 2 here"""


def main():
    puzzle_input = Data(["puzzle_input.txt", "test_input.txt"])

    assert task1(puzzle_input.data["test_input1"]) == ""
    print(f"Solution to task 1: {task1(puzzle_input.data['puzzle'])}")

    # assert task2(puzzle_input.data["test_input1"]) == "", "Failed test"
    print(f"Solution to task 2: {task2(puzzle_input.data['puzzle'])}")


main()
