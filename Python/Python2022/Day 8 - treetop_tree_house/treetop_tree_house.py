import numpy as np
import requests as req


def submit_answer(answer, level):
    cookies = {"session": open("../../credentials", "r").readlines()[0]}
    response = req.post(
        url=f'https://adventofcode.com/2022/day/8/answer',
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
        return np.array([[int(num) for num in line.strip()] for line in file.readlines()])

def find_visibile_trees(data):
    tree_list = 0
    for row in range(1, len(data[0, :])-1):
        for col in range(1, len(data[:, 0]) - 1):
            tree = data[col, row]
            left, right, top, bottom = data[col, :row], data[col, row+1:], data[:col, row], data[col+1:, row]
            if max(left) < tree or max(right) < tree or max(top) < tree or max(bottom) < tree:
                tree_list += 1
    return tree_list


def score(tree, dir):
    counter = 0
    for i in dir:
        if i < tree:
            counter += 1
        elif i >= tree:
            counter += 1
            return counter
    return counter


def find_scenic_score(data):
    scenic_score = []
    for row in range(1, len(data[0, :]) - 1):
        for col in range(1, len(data[:, 0]) - 1):
            scenic_score.append(score(data[col, row], np.flip(data[col, :row]))
                                *score(data[col, row], data[col, row + 1:])
                                *score(data[col, row], np.flip(data[:col, row]))
                                *score(data[col, row], data[col + 1:, row]))
    return max(scenic_score)





def task1(data):
    """Write the code for task 1 here"""
    edges = data.shape[0]*2 + (data.shape[1]-2)*2
    return edges + find_visibile_trees(data)



def task2(data):
    """Write the code for task 2 here"""
    return find_scenic_score(data)



def main():
    puzzle_input = Data(["puzzle_input.txt", "test_input.txt"])

    assert task1(puzzle_input.data["test_input"]) == 21  # Set example answer here
    submit_answer(task1(puzzle_input.data['puzzle']), 1)

    assert task2(puzzle_input.data["test_input"]) == 8  # Set example answer here
    submit_answer(task2(puzzle_input.data['puzzle']), 2)


main()
