import numpy as np


class Data:

    def __init__(self, inputs):
        """Reads puzzle input"""
        self.data = {"test_input": self.parse_data(inputs[1]), f"puzzle": self.parse_data(inputs[0])}

    def parse_data(self, path):
        """This parses data"""
        file = open(path, "r")
        data = [line.strip().split(",") for line in file.readlines()]

        # Use numpy.arange() to create a full list of numbers from the sections
        arrays = []
        for i in data:
            section1 = np.arange(int(i[0].split('-')[0]),
                                 int(i[0].split('-')[1])+1).tolist()
            section2 = np.arange(int(i[1].split('-')[0]),
                                 int(i[1].split('-')[1])+1).tolist()
            arrays.append([section1, section2])
        return arrays


def task1(data):
    """Write the code for task 1 here"""
    subsets = 0
    # Loop through data and look for subsets in each pair of sections
    for (s1, s2) in data:
        # Fetch the lowest and highest number of each section
        s1_low, s1_high = min(s1), max(s1)
        s2_low, s2_high = min(s2), max(s2)

        # Check if a sections low and high number is within another section
        if s2_low >= s1_low and s2_high <= s1_high:
            subsets += 1
        elif s1_low >= s2_low and s1_high <= s2_high:
            subsets += 1

    return subsets


def task2(data):
    """Write the code for task 2 here"""
    subsets = 0
    for (s1, s2) in data:
        # Check for matches in each section
        if len(list(set(s1) & set(s2))) > 0:
            subsets += 1

    return subsets


def main():
    puzzle_input = Data(["puzzle_input.txt", "test_input.txt"])

    assert task1(puzzle_input.data["test_input"]) == 2  # Set example answer here
    print(f"Solution to task 1: {task1(puzzle_input.data['puzzle'])}")

    assert task2(puzzle_input.data["test_input"]) == 4  # Set example answer here
    print(f"Solution to task 2: {task2(puzzle_input.data['puzzle'])}")


main()
