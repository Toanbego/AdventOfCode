import numpy as np
import requests as req
from collections import defaultdict
from pathlib import Path


def submit_answer(answer, level):
    cookies = {"session": open("../../credentials", "r").readlines()[0]}
    response = req.post(
        url=f'https://adventofcode.com/2022/day/7/answer',
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
        return file.read().split("\n")



def get_size(data, dir_path, dir_list, file_list, directory_size, idx):

    for cmd in data:
        if '$ cd' in cmd and '$ cd ..' not in cmd:
            dir_path += cmd.split(" ")[-1]
        elif cmd[0].isnumeric():
            directory_size[dir_path] = [int(cmd.split(" ")[0])]
        elif "dir" in cmd:
            directory_size[dir_path].append(get_size(data, dir_path, dir_list, file_list, directory_size))



def task1(data):
    """Write the code for task 1 here"""

    dir_path = "/"
    directory_size = {"/": 0}
    for idx, line in enumerate(data):
        if line == "$ cd /": continue
        if line.startswith("$ cd") and "$ cd .." not in line:
            dir_path += " " + line.split(" ")[-1]
            if line.split(" ")[-1] not in directory_size.keys():
                directory_size[line.split(" ")[-1]] = 0
        elif line == "$ cd ..":
            dir_path = dir_path.rsplit(" ", 1)[0]
        elif line.startswith("$ ls"): continue
        elif line.startswith("dir"): continue
        else:
            size = int(line.split(" ")[0])
            dir = dir_path.split(" ")[-1]
            directory_size[dir] += size
            parents = dir_path.split(" ")[:-1]
            for parent in parents:
                directory_size[parent] += size

    return sum(v for v in directory_size.values() if v <= 100000)



def task2(data):
    """Write the code for task 2 here"""
    dir_path = "/"
    directory_size = {"/": 0}
    for idx, line in enumerate(data):
        if line == "$ cd /": continue
        if line.startswith("$ cd") and "$ cd .." not in line:
            dir_path += " " + line.split(" ")[-1]
            if line.split(" ")[-1] not in directory_size.keys():
                directory_size[line.split(" ")[-1]] = 0
        elif line == "$ cd ..":
            dir_path = dir_path.rsplit(" ", 1)[0]
        elif line.startswith("$ ls"): continue
        elif line.startswith("dir"): continue
        else:
            size = int(line.split(" ")[0])
            dir = dir_path.split(" ")[-1]
            directory_size[dir] += size
            parents = dir_path.split(" ")[:-1]
            for parent in parents:

                directory_size[parent] += size

    return max(v for v in directory_size.values() if v <= 30000000)


def main():
    puzzle_input = Data(["puzzle_input.txt", "test_input.txt"])

    print(task1(puzzle_input.data['test_input']))
    print(task1(puzzle_input.data['puzzle']))
    print(task2(puzzle_input.data['test_input']))
    print(task2(puzzle_input.data['puzzle']))


main()
