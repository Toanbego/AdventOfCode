import numpy as np

class Data:

    def __init__(self, inputs):
        """Reads puzzle input"""
        self.data = {"test_input": self.parse_data(inputs[1])}
        self.data[f"puzzle"] = self.parse_data(inputs[0])

    def parse_data(self, path):
        """This parses data"""
        file = open(path, "r")
        return [line.strip() for line in file.readlines()]


def task1(data):
    """Write the code for task 1 here"""
    
    game_rules = {'A X': 3, 'B Y': 3, 'C Z': 3,
                  'A Y': 6, 'B Z': 6, 'C X': 6,
                  'A Z': 0, 'B X': 0, 'C Y': 0}
    play_score = {'X': 1, 'Y': 2, 'Z': 3}

    return sum([game_rules[play] + play_score[play[2]] for play in data])


def task2(data):
    """Write the code for task 2 here"""
    rule_table = {'A X': 'Z', 'B X': 'X', 'C X': 'Y',
                  'A Y': 'X', 'B Y': 'Y', 'C Y': 'Z',
                  'A Z': 'Y', 'B Z': 'Z', 'C Z': 'X'}
    play_score = {'X': 1, 'Y': 2, 'Z': 3}
    win_score = {'X': 0, 'Y': 3, 'Z': 6}

    return sum([win_score[play[2]] + play_score[rule_table[play]] for play in data])


def main():

    puzzle_input = Data(["puzzle_input.txt", "test_input.txt"])

    assert task1(puzzle_input.data["test_input"]) == 15
    print(f"Solution to task 1: {task1(puzzle_input.data['puzzle'])}")

    assert task2(puzzle_input.data["test_input"]) == 12
    print(f"Solution to task 2: {task2(puzzle_input.data['puzzle'])}")


main()
