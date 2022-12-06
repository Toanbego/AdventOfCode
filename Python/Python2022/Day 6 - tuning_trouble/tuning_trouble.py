import numpy as np
import requests as req


def submit_answer(answer, level):
    cookies = {"session": open("../../credentials", "r").readlines()[0]}
    response = req.post(
        url=f'https://adventofcode.com/2022/day/6/answer',
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
        return [line.strip() for line in file.readlines()][0]


def process_signal(data, signal_len):
    for idx in range(signal_len-1, len(data)):
        if len(list(set(data[idx-signal_len+1:idx+1]))) == signal_len:
            return idx + 1


def task1(data):
    """Write the code for task 1 here"""
    return process_signal(data, 4)


def task2(data):
    """Write the code for task 2 here"""
    return process_signal(data, 14)


def main():
    puzzle_input = Data(["puzzle_input.txt", "test_input.txt"])

    assert task1(puzzle_input.data["test_input"]) == 7  # Set example answer here
    submit_answer(task1(puzzle_input.data['puzzle']), 1)

    assert task2(puzzle_input.data["test_input"]) == 19  # Set example answer here
    submit_answer(task2(puzzle_input.data['puzzle']), 2)


main()
