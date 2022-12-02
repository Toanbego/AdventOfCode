import numpy as np

class Data:

    def __init__(self, inputs):
        """Reads puzzle input"""
        self.data = {"test_input": self.parse_data(inputs[1])}
        self.data[f"puzzle"] = self.parse_data(inputs[0])

    def parse_data(self, path):
        """This parses data"""
        file = open(path, "r")
        return list(map(lambda x: [int(i) for i in x.split("\n")], file.read().split("\n\n")))


def task1(data):
    """Write the code for task 1 here"""
    return max([sum(item) for item in data])


def task2(data):
    """Write the code for task 2 here"""
    calories = [sum(i) for i in data]
    calories.sort()
    return sum(calories[-3:])

def oneliner(path):
    with open(path, 'r') as file:
        return sum(list(sorted([sum(int(x) for x in line.split('\n') if x != '') for line in file.read().split('\n\n')], reverse=True))[0:3])

def main():
    print(oneliner("puzzle_input.txt"))
    exit()
    puzzle_input = Data(["puzzle_input.txt", "test_input.txt"])

    assert task1(puzzle_input.data["test_input"]) == 24000
    print(f"Solution to task 1: {task1(puzzle_input.data['puzzle'])}")

    assert task2(puzzle_input.data["test_input"]) == 45000
    print(f"Solution to task 2: {task2(puzzle_input.data['puzzle'])}")


main()
