import numpy as np
import requests as req




exit()

def submit_answer(answer, level):
    cookies = {"session": open("../../credentials", "r").readlines()[0]}
    response = req.post(
        url=f'https://adventofcode.com/2023/day/4/answer',
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
    score = 0
    for i in data:
        card_multiplier = 0

        game = i[7:].split("|")

        winning_numbers = [int(n) for n in game[0].split(" ") if str.isdigit(n)]
        card_numbers = [int(n) for n in game[1].split(" ") if str.isdigit(n)]

        for n in card_numbers:
            if n in winning_numbers and card_multiplier >= 1:
                card_multiplier *= 2
            elif n in winning_numbers and card_multiplier == 0:
                card_multiplier = 1

        score += card_multiplier

    return score





def task2(data):
    """Write the code for task 2 here"""

    card_counter = [1 for i in data]
    for idx, i in enumerate(data):

        game = i[7:].split("|")

        winning_numbers = [int(n) for n in game[0].split(" ") if str.isdigit(n)]
        card_numbers = [int(n) for n in game[1].split(" ") if str.isdigit(n)]

        copies = 0
        for x, n in enumerate(card_numbers):
            if n in winning_numbers:
                copies += 1

        for x in range(copies):
            card_counter[idx+x+1] += 1 * card_counter[idx]


    return sum(card_counter)


def main():
    puzzle_input = Data(["puzzle_input.txt", "test_input.txt"])

    print(task1(puzzle_input.data["test_input"]))  # Set example answer here
    print(task1(puzzle_input.data['puzzle']))

    print(task2(puzzle_input.data["test_input"]))  # Set example answer here
    print(task2(puzzle_input.data['puzzle']))


main()
