import numpy as np
import requests as req
import re
from collections import defaultdict

def submit_answer(answer, level):
    cookies = {"session": open("../../credentials", "r").readlines()[0]}
    response = req.post(
        url=f'https://adventofcode.com/2023/day/3/answer',
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

    part_sum = 0

    for idx, i in enumerate(data):


        i = "." + i + "."
        if idx == 0:
            above_line = "." + "".join(["." for x in i]) + "."
        else:
            above_line = "." + data[idx-1] + "."

        if idx+1 == len(data):
            below_line = "." + "".join(["." for x in i]) + "."
        else:
            below_line = "." + data[idx+1] + "."

        for match in re.finditer("\d+", i):

            isPart = False

            start, end = match.start(), match.end()
            if len(re.findall("\.+", i[start-1:end+1])) < 2 \
                    or len(re.findall("[.0-9]+", below_line[start-1:end+1])[0]) < end-start+2 \
                    or len(re.findall("[.0-9]+", above_line[start-1:end+1])[0]) < end-start+2:
                isPart = True


            if isPart:
                part_sum += int(match.group())

    return part_sum



def task2(data):
    """Write the code for task 2 here"""
    part_sum = 0
    groups = []
    for idx, i in enumerate(data):

        i = "." + i + "."
        if idx == 0:
            above_line = "." + "".join(["." for x in i]) + "."
        else:
            above_line = "." + data[idx - 1] + "."

        if idx + 1 == len(data):
            below_line = "." + "".join(["." for x in i]) + "."
        else:
            below_line = "." + data[idx + 1] + "."

        for match in re.finditer("\d+", i):
            isGearPart = []

            start, end = match.start(), match.end()

            right = re.findall("\*", i[end])
            left = re.findall("\*", i[start-1])


            if len(right) > 0:
                isGearPart.append(int(right[0]))
            if len(left) > 0:
                isGearPart.append(int(left[0]))

            for sub_match in re.finditer("(\d+)", above_line):
                check_start = above_line.index(sub_match.group())
                check_end = check_start + len(sub_match.group())


                if start-1< check_start < end+1:
                    isGearPart.append(int(sub_match.group()))
                    break
                elif start-1 < check_end < end+1:
                    isGearPart.append(int(sub_match.group()))
                    break
                elif start - 1 == check_start and end + 1 == check_end:
                    isGearPart.append(int(sub_match.group()))
                    break

            for sub_match in re.finditer("(\d+)", below_line):
                check_start = below_line.index(sub_match.group())
                check_end = check_start + len(sub_match.group())


                if start-1< check_start < end+1:
                    isGearPart.append(int(sub_match.group()))
                    break
                elif start-1 < check_end < end+1:
                    isGearPart.append(int(sub_match.group()))
                    break
                elif start - 1 == check_start and end + 1 == check_end:
                    isGearPart.append(int(sub_match.group()))
                    break

            if len(isGearPart) == 2:
                part_sum += isGearPart[0] * isGearPart[1]

    return part_sum



def main():
    puzzle_input = Data(["puzzle_input.txt", "test_input.txt"])

    print(task1(puzzle_input.data["test_input"]))  # Set example answer here
    print(task1(puzzle_input.data['puzzle']))

    print(task2(puzzle_input.data["test_input"]))  # Set example answer here
    print(task2(puzzle_input.data['puzzle']))



main()
