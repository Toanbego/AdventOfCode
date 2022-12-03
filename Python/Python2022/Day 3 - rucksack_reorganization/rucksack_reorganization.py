import numpy as np
import string

class Data:

    def __init__(self, inputs):
        """Reads puzzle input"""
        self.data = {"test_input": self.parse_data(inputs[1]), f"puzzle": self.parse_data(inputs[0])}

    def parse_data(self, path):
        """This parses data"""
        file = open(path, "r")
        return [line.strip() for line in file.readlines()]


def find_matches(data):
    """Loop through each rucksack and add matching items to priority list"""
    priority_list = []
    for items in data:

        # Split the items into two compartments using // operator
        c1, c2 = items[:(len(items) // 2)], items[(len(items) // 2):]

        # Find common chars with set() and & operator
        matches = list(set(c1) & set(c2))

        # Append to list
        priority_list.append(matches)

    return priority_list

def find_badges(data):
    """Finds the common item for each group of three
    return list(map(lambda x: [int(i) for i in x.split("\n")], file.read().split("\n\n")))
    """
    priority_list = []

    # Loop through every 3 lines
    for i in data[2:len(data):3]:

        # Fetch group
        c1, c2, c3 = data[data.index(i)-2:data.index(i)+1]

        # Find match and append to list
        matches = list(set(c1) & set(c2) & set(c3))
        priority_list.append(matches)

    return priority_list


def task1(data):
    """Write the code for task 1 here"""
    priority_list = find_matches(data)
    alphabet = string.ascii_lowercase + string.ascii_uppercase

    # Convert alphabet to priority
    priority_score = []
    for matches in priority_list:
        # The index element of alphabet + 1 would be the correct priority score
        for match in matches:
            priority_score.append(alphabet.index(match)+1)

    return sum(priority_score)


def task2(data):
    """Write the code for task 2 here"""
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    priority_list = find_badges(data)
    return sum([[alphabet.index(match) + 1 for match in matches][0] for matches in priority_list])


def task1_oneliner(data):
    """
    Task 1 as a sexy oneliners.
    :param data:
    :return:
    """
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    return sum([[alphabet.index(match) + 1 for match in matches][0]
                for matches in [list(set(items[:(len(items) // 2)]) &
                                     set(items[(len(items) // 2):]))[0] for items in data]])


def task2_oneliner(data):
    """
    Task 2 as a sexy oneliners.
    :param data:
    :return:
    """
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    return sum([[alphabet.index(match) + 1 for match in matches][0]
                for matches in [list(set(data[data.index(i)-2:data.index(i)+1][0]) &
                                     set(data[data.index(i)-2:data.index(i)+1][1]) &
                                     set(data[data.index(i)-2:data.index(i)+1][2])) for i in data[2:len(data):3]]])




def main():
    puzzle_input = Data(["puzzle_input.txt", "test_input.txt"])

    assert task1(puzzle_input.data["test_input"]) == 157
    print(f"Solution to task 1: {task1(puzzle_input.data['puzzle'])}")

    assert task2(puzzle_input.data["test_input"]) == 70
    print(f"Solution to task 2: {task2(puzzle_input.data['puzzle'])}")


main()
