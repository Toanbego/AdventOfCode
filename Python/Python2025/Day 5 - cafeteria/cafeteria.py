import numpy as np
import requests as req


def submit_answer(answer, level):
    cookies = {"session": open("../../credentials", "r").readlines()[0]}
    response = req.post(
        url=f'https://adventofcode.com/2025/day/5/answer',
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

    prods = [int(i) for i in data[data.index("")+1:]]
    rngs = [[int(i.split("-")[0]), int(i.split("-")[1])] for i in data[:data.index("")]]


    fresh_count = 0

    for i in prods:


        for r1, r2 in rngs:
            
            if r1 <= i <= r2:
                fresh_count += 1
                break
    
    return fresh_count



def task2(data):
    """Write the code for task 2 here"""
    rngs = [[int(i.split("-")[0]), int(i.split("-")[1])] for i in data[:data.index("")]]

    rngs.sort()

    fresh_ranges = []

    for r1, r2 in rngs:
        if not fresh_ranges or r1 > fresh_ranges[-1][1] + 1:
            fresh_ranges.append([r1, r2])
        else:
            fresh_ranges[-1][1] = max(fresh_ranges[-1][1], r2)

    
    diff = sum(end - start + 1 for start, end in fresh_ranges)
    return diff
  

def main():
    puzzle_input = Data(["puzzle_input.txt", "test_input.txt"])

    print(task1(puzzle_input.data["test_input"]))

    print(task1(puzzle_input.data['puzzle']))

    print(task2(puzzle_input.data["test_input"]))  # Set example answer here
    print(task2(puzzle_input.data['puzzle']))


main()
