import numpy as np
import requests as req


def submit_answer(answer, level):
    cookies = {"session": open("../../credentials", "r").readlines()[0]}
    response = req.post(
        url=f'https://adventofcode.com/2024/day/1/answer',
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
    # Create two lists, sort them in ascending order, find diff then sum answer
    l1, l2 = [], []
    for i in data:
        l1.append(int(i.split()[0])), l2.append(int(i.split()[1]))
    l1.sort(), l2.sort()
    answer = sum([abs(x-y) for x, y in zip(l1, l2)])
    return answer


def task2(data):
    """Write the code for task 2 here"""
    l1, l2 = [], []
    for i in data:
        l1.append(int(i.split()[0])), l2.append(int(i.split()[1]))
    l1.sort(), l2.sort()

    similarity = sum([x*l2.count(x) for x in l1])
    return similarity



def main():
    puzzle_input = Data(["puzzle_input.txt", "test_input.txt"])


    print(task1(puzzle_input.data["test_input"]))
    print(task1(puzzle_input.data['puzzle']))

    print(task2(puzzle_input.data["test_input"]))  # Set example answer here
    print(task2(puzzle_input.data['puzzle']))


main()
