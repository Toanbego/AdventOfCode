import numpy as np
import requests as req


def submit_answer(answer, level):
    cookies = {"session": open("../../credentials", "r").readlines()[0]}
    response = req.post(
        url=f'https://adventofcode.com/2018/day/1/answer',
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
        return file.read().split('\n')

def task1(data):
    """Write the code for task 1 here"""

    changes = np.array([int(delta) for delta in data])
    progress = np.cumsum(changes)
    return progress[-1]


def task2(data):
    """Write the code for task 2 here"""
    changes = np.array([int(delta) for delta in data])
    progress = np.cumsum(changes)

    firstround = len(np.unique(progress)) != len(progress)
    unique = set([])
    found = False
    current = progress
    currentset = set(progress)

    while not found:
        if unique.intersection(currentset) != set() or firstround:
            for num in current:
                numset = set([num])
                if unique.intersection(numset) != set():
                    result = num
                    found = True
                    break
                unique = unique.union(numset)
        unique = unique.union(currentset)
        current = progress + current[-1]
        currentset = set(current)
    return result


def main():
    puzzle_input = Data(["puzzle_input.txt", "test_input.txt"])

    assert task1(puzzle_input.data["test_input"]) == 3  # Set example answer here
    submit_answer(task1(puzzle_input.data['puzzle']), 1)

    assert task2(puzzle_input.data["test_input"]) == 2  # Set example answer here
    submit_answer(task2(puzzle_input.data["puzzle"]), 2)


main()
