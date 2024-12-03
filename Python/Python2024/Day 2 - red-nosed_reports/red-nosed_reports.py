import numpy as np
import requests as req
import math



def submit_answer(answer, level):
    cookies = {"session": open("../../credentials", "r").readlines()[0]}
    response = req.post(
        url=f'https://adventofcode.com/2024/day/2/answer',
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
    safe_count = 0
    for line in data:
        report = [int(i) for i in line.split()]
        safe = True

        for i in range(1, len(report)-1):
            check1 = report[i] - report[i+1]
            check2 = report[i - 1] - report[i]

            if abs(check1) > 3 or abs(check1) < 1 or abs(check2) > 3 or abs(check2) < 1 or check1*check2 < 0:
                safe = False
                break

        if safe:
            safe_count += 1

    return safe_count


def prod(arr):
    product = 1
    for i in arr:
        product *= i
    return product


def find_bad_levels(report):
    diff = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    bad_levels = [i for i in range(len(report) - 1)
                  if abs(diff[i]) > 3
                  or abs(diff[i]) < 1
                  or diff[0] * diff[i] < 0]
    return bad_levels

def task2(data):
    """Write the code for task 2 here"""
    safe_count = 0
    for line in data:
        report = [int(i) for i in line.split()]
        bad_levels = find_bad_levels(report)

        if bad_levels:

            for l in bad_levels:
                report = [int(i) for i in line.split()]
                report.pop(l)
                is_unsafe = find_bad_levels(report)

                if not is_unsafe:
                    safe_count += 1
                    break
        else:
            safe_count += 1



    return safe_count





    return safe_count




def main():
    puzzle_input = Data(["puzzle_input.txt", "test_input.txt"])

    print(task1(puzzle_input.data["test_input"]))
    print(task1(puzzle_input.data['puzzle']))

    print(task2(puzzle_input.data["test_input"]))  # Set example answer here

    print(task2(puzzle_input.data['puzzle']))


main()
