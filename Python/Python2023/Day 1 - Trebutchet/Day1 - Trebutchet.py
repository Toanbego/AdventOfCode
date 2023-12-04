import numpy as np
import requests as req
import re
import time

def submit_answer(answer, level):
    cookies = {"session": open("../../credentials", "r").readlines()[0]}
    response = req.post(
        url=f'https://adventofcode.com/{year}/day/{day}/answer',
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
    calibration_list = []
    for i in data:
        digits = re.findall("\d{1}", i)
        f, l = digits[0], digits[-1]
        calibration_list.append(int(f"{f}{l}"))
    return sum(calibration_list)


def task1_python(data):
    """Write the code for task 1 here"""
    total = 0

    for i in data:
        n = "".join(filter(str.isdigit, i))
        fc = n[0]
        lc = n[-1]
        total += int(fc+lc)

    return total



def task2(data):
    """Write the code for task 2 here"""
    calibration_list = []
    spelled_digits = {
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }


    checks = list(spelled_digits.keys())
    checks += spelled_digits.values()

    for i in data:
        digits = re.findall("(?=(one|two|three|four|five|six|seven|eight|nine|\d))", i)


        f, l = spelled_digits[digits[0]], spelled_digits[digits[-1]]


        calibration_list.append(int(f"{f}{l}"))
    return sum(calibration_list)


def main():
    puzzle_input = Data(["puzzle_input.txt", "test_input.txt"])

    t1 = time.time()
    # print(task1(puzzle_input.data["test_input"]))
    print(task1(puzzle_input.data['puzzle']))
    t2 = time.time()
    print(t2-t1)

    t1 = time.time()
    # print(task1(puzzle_input.data["test_input"]))
    print(task1(puzzle_input.data['puzzle']))
    t2 = time.time()
    print(t2-t1)
    exit()
    print(task2(puzzle_input.data["test_input"]))
    print(task2(puzzle_input.data['puzzle']))


main()
