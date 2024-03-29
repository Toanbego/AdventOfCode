import numpy as np
import requests as req

class Data:

    def __init__(self, inputs):
        """Reads puzzle input"""
        self.data = {"test_input": self.parse_data(inputs[1]), f"puzzle": self.parse_data(inputs[0])}

    def parse_data(self, path):
        """This parses data"""
        file = open(path, "r")
        return [line.strip() for line in file.readlines()]

def task1(data):
    """Write the code for task 1 here"""


def task2(data):
    """Write the code for task 2 here"""

def submit_answer(answer, level, day, year):
    cookies = {"session": open("../../credentials", "r").readlines()[0]}
    response = req.post(
        url=f'https://adventofcode.com/2018/day/4/answer',
        cookies=cookies,
        data={"level": {level}, "answer": {answer}},
    )


def main():
    puzzle_input = Data(["puzzle_input.txt", "test_input.txt"])

    assert task1(puzzle_input.data["test_input"]) == ""  # Set example answer here
    print(f"Solution to task 1: {task1(puzzle_input.data['puzzle'])}")

    assert task2(puzzle_input.data["test_input"]) == ""  # Set example answer here
    print(f"Solution to task 2: {task2(puzzle_input.data['puzzle'])}")


main()
