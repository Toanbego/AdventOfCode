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

    def parse_data(self):

        fin = open(path, "r")
        lines = [line.strip() for line in fin.readlines() if line.strip()]
        return "" # Add rest of parsing here

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
