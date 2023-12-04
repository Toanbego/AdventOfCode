import numpy as np
import requests as req
import re

def submit_answer(answer, level):
    cookies = {"session": open("../../credentials", "r").readlines()[0]}
    response = req.post(
        url=f'https://adventofcode.com/2023/day/2/answer',
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
        data = []
        for line in file.readlines():
            line = line.strip()
            sets = line[8:].split(";")
            game = []
            for set in sets:
                cubes = re.findall("\d+ [a-z]+", set)
                check = {}
                for cube in cubes:
                    number = int(cube.split(" ")[0])
                    color = cube.split(" ")[1]
                    check[color] = number
                game.append(check)
            data.append(game)
        return data


def task1(data):
    """Write the code for task 1 here"""
    number_of_cubes = {"red": 12, "green": 13, "blue": 14}

    possible_games = 0

    for game_id, game in enumerate(data):
        is_impossible = False
        for set in game:
            for cube in set:
                if set[cube] > number_of_cubes[cube]:
                    is_impossible = True

        if not is_impossible:
            possible_games += game_id+1
    return possible_games


def task2(data):
    """Write the code for task 2 here"""
    powers = 0
    for game_id, game in enumerate(data):
        red, blue, green = [], [], []

        for set in game:
            for cube in set:
                if cube == "red":
                    red.append(set[cube])
                if cube == "blue":
                    blue.append(set[cube])
                if cube == "green":
                    green.append(set[cube])

        powers += max(red)*max(blue)*max(green)
    return powers


def main():
    puzzle_input = Data(["puzzle_input.txt", "test_input.txt"])

    print(task1(puzzle_input.data["test_input"]))
    print(task1(puzzle_input.data['puzzle']))

    print(task2(puzzle_input.data["test_input"]))
    print(task2(puzzle_input.data['puzzle']))


main()
