import numpy as np
import requests as req
from math import gcd


def lcm(xs):
    ans = 1
    for x in xs:
        ans = (x*ans)//gcd(x,ans)
    return ans

def submit_answer(answer, level):
    cookies = {"session": open("../../credentials", "r").readlines()[0]}
    response = req.post(
        url=f'https://adventofcode.com/2023/day/8/answer',
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
    sequence = data[0]
    current_location = 'AAA'
    desert_map = {x.split(" ")[0]: (x.split(" ")[2][1:-1], x.split(" ")[3][:-1]) for x in data[2:] }
    steps = 0
    move = {'L': 0, 'R': 1}
    while current_location != 'ZZZ':

        for direction in sequence:
            current_location = desert_map[current_location][move[direction]]
            steps += 1

            if current_location == 'ZZZ':
                break

    return steps


def task2(data):
    """Write the code for task 2 here"""
    sequence = data[0]
    desert_map = {x.split(" ")[0]: (x.split(" ")[2][1:-1], x.split(" ")[3][:-1]) for x in data[2:]}
    current_locations = [x for x in desert_map.keys() if x[-1] == 'A']
    move = {'L': 0, 'R': 1}

    check = {}
    t = 0

    while True:
        new_position = []
        for i, pos in enumerate(current_locations):

            p = desert_map[pos][move[sequence[t%len(sequence)]]]

            if p.endswith('Z'):
                check[i] = t + 1

                if len(check) == len(current_locations):
                    return lcm(check.values())

            new_position.append(p)

        current_locations = new_position

        t += 1



def main():
    puzzle_input = Data(["puzzle_input.txt", "test_input.txt"])

    # print(task1(puzzle_input.data["test_input"]))

    # print(task1(puzzle_input.data['puzzle']))
    # print(task2(puzzle_input.data["test_input"]))  # Set example answer here
    print(task2(puzzle_input.data['puzzle']))
    exit()


main()
