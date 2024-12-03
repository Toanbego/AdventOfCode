import numpy as np
import requests as req
import re
from math import prod


def submit_answer(answer, level):
    cookies = {"session": open("../../credentials", "r").readlines()[0]}
    response = req.post(
        url=f'https://adventofcode.com/2024/day/3/answer',
        cookies=cookies,
        data={"level": {level}, "answer": {answer}},
    )
    if "That's not the right answer" in response.text:
        print(f"{answer} is not correct level {level}")
    else:
        print(f"{answer} is the correct answer for level {level}")


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

    data = "".join(data)
    matches = re.findall("mul\((\d+)\,(\d+)\)", data)
    mul_solution = [int(i[0]) * int(i[1]) for i in matches]
    return sum(mul_solution)



def task2(data):
    """Write the code for task 2 here"""
    total = 0
    data = "".join(data)
    enabled = re.findall("(.*?)(?<=do\(\))(.*?)(?=(?:don't\(\)|$))", data)
    for x in enabled:
        for t in x:
            if t.startswith("don't()"):
                continue
            mul_solution = [int(i[0]) * int(i[1]) for i in re.findall("mul\((\d+)\,(\d+)\)", t)]
            total += sum(mul_solution)
    return total



def main():
    puzzle_input = Data(["puzzle_input.txt", "test_input.txt"])

    print(task1(puzzle_input.data["test_input"]))
    print(task1(puzzle_input.data['puzzle']))

    print(task2(puzzle_input.data["test_input"]))  # Set example answer here
    print(task2(puzzle_input.data['puzzle']))


main()
