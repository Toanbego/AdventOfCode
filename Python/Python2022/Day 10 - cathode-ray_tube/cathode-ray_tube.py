import numpy as np
import requests as req


def submit_answer(answer, level):
    cookies = {"session": open("../../credentials", "r").readlines()[0]}
    response = req.post(
        url=f'https://adventofcode.com/2022/day/10/answer',
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


class CathComp():
    def __init__(self, data):
        self.operations = data
        self.cycle = 0
        self.X = 1
        self.signal_strength = {}
        self.crt_pos = 0
        self.grid = np.full((6, 40), ['.'], dtype=str)
        self.crt_row = 0

    def increment_cycle(self, instruction):
        if "addx" in instruction:
            self.render_image(instruction)
        if "noop" in instruction:
            self.render_image(instruction)


    def addx(self, value):
        self.X += value

    def process_cpu(self):
        for ops in self.operations:
            self.increment_cycle(ops)
            if self.cycle - self.cycle % 20 not in self.signal_strength.keys():
                if (self.cycle - self.cycle % 20) % 40 != 0:
                    self.signal_strength[self.cycle - self.cycle % 20] = self.X * (self.cycle - self.cycle % 20)
            if "addx" in ops:
                self.addx(int(ops.split(" ")[1]))

    def render_image(self, ops):
        draw_count = 2 if 'addx' in ops else 1
        for c in range(draw_count):
            if self.cycle % 40 == 0 and self.cycle != 0:
                self.crt_row += 1
                self.crt_pos = 0
            if self.crt_pos in [self.X - 1, self.X, self.X + 1]:
                self.grid[self.crt_row, self.crt_pos] = "#"
            self.crt_pos += 1
            self.cycle += 1


def task1(data):
    """Write the code for task 1 here"""
    cathcomp = CathComp(data)
    cathcomp.process_cpu()
    return sum(cathcomp.signal_strength.values())


def task2(data):
    """Write the code for task 2 here"""
    cathcomp = CathComp(data)
    cathcomp.process_cpu()
    for row in cathcomp.grid:
        print(*row)


def main():
    puzzle_input = Data(["puzzle_input.txt", "test_input.txt"])

    assert task1(puzzle_input.data["test_input"]) == 13140  # Set example answer here
    submit_answer(task1(puzzle_input.data['puzzle']), 1)

    task2(puzzle_input.data["test_input"])
    task2(puzzle_input.data["puzzle"])



main()
