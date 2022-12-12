import math

import numpy as np
import requests as req
import re



def submit_answer(answer, level):
    cookies = {"session": open("../../credentials", "r").readlines()[0]}
    response = req.post(
        url=f'https://adventofcode.com/2022/day/11/answer',
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
        monkeys = {}
        for monkey in file.read().split("\n\n"):
            ID = int(monkey.split("\n")[0][-2])
            items = [int(i) for i in monkey.split("\n")[1][18:].split(",")]
            operation = monkey.split("\n")[2].split("=")[1].split(" ")[1:]

            tests = [int(i) for i in re.findall(r'\d+', " ".join(monkey.split("\n")[3:]))]
            monkeys[ID] = Monkey(ID, items, operation, tests)
        return monkeys


class Monkey:
    def __init__(self, ID, items, operation, tests):
        self.monkeyID = ID
        self.items = items
        self.operation = operation
        self.tests = tests
        self.inspection_counter = 0


    def play(self, data, worry_management):
        if len(self.items) > 0:
            for item_num, item in reversed(list(enumerate(self.items))):
                self.inspection_counter += 1
                self.inspect_item(item_num, worry_management)
                data[self.find_target(self.items[item_num])].items.append(self.items[item_num])
                del self.items[item_num]

    def inspect_item(self, item, worry_management):
        operation = lambda old, op="".join(self.operation): eval(op)
        self.items[item] = math.floor(operation(item) / worry_management)

    def find_target(self, item):
        if item % self.tests[0] == 0:
            return self.tests[1]
        else:
            return self.tests[2]


def task1(data):
    """Write the code for task 1 here"""
    for _ in range(20):
        for idx, _ in enumerate(data):
            data[idx].play(data, 3)

    monkey_business = [data[i].inspection_counter for i in data]
    return sorted(monkey_business)[-1] * sorted(monkey_business)[-2]


def task2(data):
    """Write the code for task 2 here"""
    lcm = 1
    for x in data:
        lcm = (lcm * data[x].tests[0])

    for _ in range(10000):
        for idx, _ in enumerate(data):
            if len(data[idx].items) > 0:
                for item_num, item in reversed(list(enumerate(data[idx].items))):
                    data[idx].inspection_counter += 1
                    item = data[idx].inspect_item(item, 1)
                    data[data[idx].find_target(item)].items.append(item % lcm)
                    del data[idx].items[item_num]

    monkey_business = [data[i].inspection_counter for i in data]
    return sorted(monkey_business)[-1] * sorted(monkey_business)[-2]


def main():
    puzzle_input = Data(["puzzle_input.txt", "test_input.txt"])

    assert task1(puzzle_input.data["test_input"]) == 10605  # Set example answer here
    submit_answer(task1(puzzle_input.data['puzzle']), 1)

    # puzzle_input = Data(["puzzle_input.txt", "test_input.txt"])
    #
    # assert task2(puzzle_input.data["test_input"]) == 2713310158  # Set example answer here
    # submit_answer(task2(puzzle_input.data['puzzle']), 2)


main()
