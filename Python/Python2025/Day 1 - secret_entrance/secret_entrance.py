import numpy as np
import requests as req
import os
from math import floor, ceil



def submit_answer(answer, level):
    cookies = {"session": open("../../credentials", "r").readlines()[0]}
    response = req.post(
        url=f'https://adventofcode.com/2025/day/1/answer',
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
      
        file = open(f"Python2025/Day 1 - secret_entrance/{path}", "r")
        return [line.strip() for line in file.readlines()]

def task1(data):
    """Write the code for task 1 here"""
    dial_position = 50
    counter = 0
    for i in data:        
        # Rotate dial
        dial_position += int(i[1:]) * -1 if i[0] == "L" else int(i[1:]) * 1

        # Adjust for overflow
        dial_position = dial_position % 100

        if dial_position == 0:
            counter += 1
      
    return counter
        
            
        


def task2(data):
    """Write the code for task 2 here"""
    dial_position = 50
    clicks = 0

    for i in data:
        counter = dial_position
        # Get operator
        rotation = int(i[1:]) * -1 if i[0] == "L" else int(i[1:]) * 1
        
        dial_position += rotation

        if dial_position == 0:
            clicks += 1

        else:
            for i in range(abs(rotation)):
                if rotation < 0:
                    counter -= 1
                    if counter == 0:
                        clicks += 1
                    if counter < 0:
                        counter = 99

                else:
                    counter += 1
                    if counter == 100:
                        clicks += 1
                        counter = 0

        dial_position = dial_position % 100
      
    return clicks



def main():
    puzzle_input = Data(["puzzle_input.txt", "test_input.txt"])

    print(task1(puzzle_input.data["test_input"]))
    print(task1(puzzle_input.data['puzzle']))

    print(task2(puzzle_input.data["test_input"]))  # Set example answer here
    print(task2(puzzle_input.data['puzzle']))


main()
