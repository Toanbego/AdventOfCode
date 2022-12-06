import numpy as np
import requests as req


def submit_answer(answer, level):
    cookies = {"session": open("../../credentials", "r").readlines()[0]}
    response = req.post(url=f'https://adventofcode.com/2022/day/5/answer',
                        cookies=cookies, data={"level": {level}, "answer": {answer}})
    if "That's not the right answer" in response.text:
        print(f"{answer} is not correct level {level}")
        exit()
    else:
        print(f"{answer} is the correct answer for level {level}")


class Data:

    def __init__(self, inputs):
        """Reads puzzle input"""
        self.data = {"test_input": self.parse_data(inputs[1]), f"puzzle": self.parse_data(inputs[0])}

    def parse_data(self, path):
        """This parses data"""
        file = open(path, "r")
        data = list(map(lambda x: [i for i in x.split("\n")], file.read().split("\n\n")))

        # Parse starting stack configuration as dictionary
        stacks = {}
        for idx, stack_number in enumerate(data[0][-1]):
            if stack_number != " ":
                stacks[int(stack_number)] = [crate[idx] for crate in data[0][:-1]]
                stacks[int(stack_number)] = "".join(stacks[int(stack_number)]).strip(" ")

        # Parse move instructions as list ["number of stacks", "from", "to"]
        moves = []
        for idx, move in enumerate(data[1]):
            moves.append([int(move.split(" ")[1]), int(move.split(" ")[3]), int(move.split(" ")[5])])
        return stacks, moves


def task1(data):
    """Write the code for task 1 here"""
    stack_conf, move_list = data[0], data[1]
    # Loop through move list
    for nr_of_stacks, from_stack, to_stack in move_list:
        # Move one stack at a time
        for i in range(nr_of_stacks):
            stack_conf[to_stack] = stack_conf[from_stack][0] + stack_conf[to_stack]
            stack_conf[from_stack] = stack_conf[from_stack][1:]

    return "".join([stack_conf[key][0] for key in stack_conf.keys()])


def task2(data):
    """Write the code for task 2 here"""
    stack_conf, move_list = data[0], data[1]
    # Loop through move list
    for nr_of_stacks, from_stack, to_stack in move_list:
        stack_conf[to_stack] = stack_conf[from_stack][:nr_of_stacks] + stack_conf[to_stack]
        stack_conf[from_stack] = stack_conf[from_stack][nr_of_stacks:]

    return "".join([stack_conf[key][0] for key in stack_conf.keys()])


def main():
    puzzle_input = Data(["puzzle_input.txt", "test_input.txt"])
    assert task1(puzzle_input.data["test_input"]) == "CMZ"  # Set example answer here
    submit_answer(task1(puzzle_input.data['puzzle']), 1)

    puzzle_input = Data(["puzzle_input.txt", "test_input.txt"])
    assert task2(puzzle_input.data["test_input"]) == "MCD"  # Set example answer here
    submit_answer(task2(puzzle_input.data['puzzle']), 2)


main()
