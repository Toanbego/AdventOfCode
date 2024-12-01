import numpy as np
import requests as req
import collections

def submit_answer(answer, level):
    cookies = {"session": open("../../credentials", "r").readlines()[0]}
    response = req.post(
        url=f'https://adventofcode.com/2023/day/7/answer',
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

    score_card = {"7": [],
                  "6": [],
                  "5": [],
                  "4": [],
                  "3": [],
                  "2": [],
                  "1": []}
    # card_types = {"A": 13, "K": 12, "Q": 11, "J": 10, "T": 9, "9": 8, "8": 7, "7": 6, "6": 5, "5": 4, "4": 3, "3": 2, "2": 1}
    card_types = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    for i in data:

        hand, bid = i.split(" ")
        hand_counter = {}

        # Count card occurences
        for card in hand:
            if card not in hand_counter:
                hand_counter[card] = 1
            else:
                hand_counter[card] += 1

        if 5 in hand_counter.values():
            score_card["7"].append([hand, bid])
        elif 4 in hand_counter.values():
            score_card["6"].append([hand, bid])
        elif 3 in hand_counter.values() and 2 in hand_counter.values():
            score_card["5"].append([hand, bid])
        elif 3 in hand_counter.values() and 2 not in hand_counter.values():
            score_card["4"].append([hand, bid])
        elif len(list(filter(lambda x: x >= 2, hand_counter.values()))) >= 2:
            score_card["3"].append([hand, bid])
        elif len(list(filter(lambda x: x >= 2, hand_counter.values()))) >= 1:
            score_card["2"].append([hand, bid])
        elif len(list(filter(lambda x: x == 1, hand_counter.values()))) == 5:
            score_card["1"].append([hand, bid])

    ranking = []
    for card_group in score_card:
        for card in score_card[card_group]:
            print(card)
            print("I was here")


def task2(data):
    """Write the code for task 2 here"""



def main():
    puzzle_input = Data(["puzzle_input.txt", "test_input.txt"])

    print(task1(puzzle_input.data["test_input"]))
    exit()
    print(task1(puzzle_input.data['puzzle']))

    print(task2(puzzle_input.data["test_input"]))  # Set example answer here
    print(task2(puzzle_input.data['puzzle']))


main()
