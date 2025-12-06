import numpy as np
import requests as req
import re


def submit_answer(answer, level):
    cookies = {"session": open("../../credentials", "r").readlines()[0]}
    response = req.post(
        url=f'https://adventofcode.com/2025/day/6/answer',
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
        return [line for line in file.readlines()]

def task1(data):
    """Write the code for task 1 here"""

    operators =[i.strip() for i in data[-1].split()]
    nums = [[int(x.strip()) for x in i.split()]for i in data[:-1]]
    
    # Convert to numpy array
    nums = np.array(nums).transpose()

    answers = []
    for num, ops in zip(nums, operators):
        if ops == "+":
            answers.append(np.sum(num))
        elif ops == "*":
            answers.append(np.prod(num))

    
    return sum(answers)


def task2(data):
    """Write the code for task 2 here"""
    data = [i.strip("\n") for i in data]
    lines = ["".join(reversed(i)) for i in data]
  
    columns = []
    current_col = []

    answers = []

    for idx in range(len(lines[0])):

        num = [lines[x][idx] for x in range(len(lines[:-1]))]
        current_col.append(int("".join(num).strip())) if len("".join(num).strip()) > 0 else None
        
        if lines[-1][idx] == "*" or lines[-1][idx] == "+":
                if lines[-1][idx] == "*":
                    answers.append(np.prod(current_col))

                elif lines[-1][idx] == "+":
                    answers.append(np.sum(current_col))

                columns.append(current_col)
                current_col = []

    return sum(answers)



def main():
    puzzle_input = Data(["puzzle_input.txt", "test_input.txt"])

    print(task1(puzzle_input.data["test_input"]))
    print(task1(puzzle_input.data['puzzle']))

    print(task2(puzzle_input.data["test_input"]))
    print(task2(puzzle_input.data['puzzle']))

main()
