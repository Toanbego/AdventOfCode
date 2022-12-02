import numpy as np

class Data:

    def __init__(self, inputs):
        """Reads puzzle input"""
        self.data = {"test_input": self.parse_data(inputs[1])}
        self.data[f"puzzle"] = self.parse_data(inputs[0])

    def parse_data(self, path):
        """This parses data"""
        file = open("puzzle_input.txt", "r")

        # Splitte opp i alver
        data = file.read().split("\n\n")

        # Splitte opp listene i items
        data = [element.split("\n") for element in data]

        # Konverter strings til integer
        for idx1 in range(len(data)):
            for idx2 in range(len(data[idx1])):
                data[idx1][idx2] = int(data[idx1][idx2])

        # Summer hvert element
        for idx1 in range(len(data)):
            data[idx1] = sum(data[idx1])

        # Get highest calorie count
        print(max(data))

        # Sort data
        data.sort()

        # Fetch last three elements and sum them up
        print(sum(data[-3:]))



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

    puzzle_input = Data(["puzzle_input.txt", "test_input.txt"])

    assert task1(puzzle_input.data["test_input"]) == 24000
    print(f"Solution to task 1: {task1(puzzle_input.data['puzzle'])}")

    assert task2(puzzle_input.data["test_input"]) == 45000
    print(f"Solution to task 2: {task2(puzzle_input.data['puzzle'])}")


main()
