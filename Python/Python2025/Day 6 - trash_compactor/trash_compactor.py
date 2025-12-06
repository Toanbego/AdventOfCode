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

    with open(data, "r") as f:
        text = f.read()
    
    lines = text.splitlines()

    positions = sorted({m.start() for line in lines for m in re.finditer(r"\S", line)})

    columns = []
    for i in range(len(positions)):
        start = positions[i]
        end = positions[i+1] if i < len(positions) - 1 else None
        col = [line[start:end].rstrip() for line in lines]
        columns.append(col)
    
    answers = []
    nums = []
    for i in reversed(columns):

        

        nums.append(int("".join(i[:-1]).strip()))

        # End of problem
        if i[-1] == "*" or i[-1] == "+":
            current_problem = np.array([i for i in nums])
            if i[-1] == "*":
                answers.append(np.prod(current_problem))

            elif i[-1] == "+":
                answers.append(np.sum(current_problem))

            nums = []
        

    return sum(answers)



def main():
    puzzle_input = Data(["puzzle_input.txt", "test_input.txt"])

    print(task1(puzzle_input.data["test_input"]))
    print(task1(puzzle_input.data['puzzle']))

    print(task2("test_input.txt"))  # Set example answer here
    print(task2('puzzle_input.txt'))


main()
