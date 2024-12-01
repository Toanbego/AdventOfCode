import numpy as np
import requests as req


def submit_answer(answer, level):
    cookies = {"session": open("../../credentials", "r").readlines()[0]}
    response = req.post(
        url=f'https://adventofcode.com/2023/day/6/answer',
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
    # g(x) = x*(t-x)
    # Find g(x) >= d and g(x) <= d


    race_time = [int(i) for i in data[0].split(" ") if str.isdigit(i)]
    race_distance = [int(i) for i in data[1].split(" ") if str.isdigit(i)]
    margins = []
    for t, d in zip(race_time, race_distance):
        t_rest = t
        t_hold = 0
        win_states = 0
        for i in range(t):
            t_hold += 1
            t_rest -= 1
            speed = t_hold * t_rest
            if speed > d:
                win_states += 1
        margins.append(win_states)

    return np.prod(margins)


def task2(data):
    """Write the code for task 2 here"""
    race_time = int("".join([i for i in data[0].split(" ") if str.isdigit(i)]))
    race_distance = int("".join([i for i in data[1].split(" ") if str.isdigit(i)]))
    t_rest = race_time
    t_hold = 0
    win_states = 0
    for i in range(race_time):
        t_hold += 1
        t_rest -= 1
        speed = t_hold * t_rest
        if speed > race_distance:
            win_states += 1
    return win_states


def main():
    puzzle_input = Data(["puzzle_input.txt", "test_input.txt"])

    print(task1(puzzle_input.data["test_input"]))
    print(task1(puzzle_input.data['puzzle']))

    print(task2(puzzle_input.data["test_input"]))  # Set example answer here
    print(task2(puzzle_input.data['puzzle']))


main()
