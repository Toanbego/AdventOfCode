import numpy as np


class Data:
    def __init__(self, inputs):
        """Reads puzzle input"""
        self.inputs = inputs
        self.data = {}
        for i in range(len(inputs)):
            if "input" not in list(self.data.keys()):
                self.data["input"] = self.parse_data(inputs[i])
            else:
                self.data[f"test_input{i}"] = self.parse_data(inputs[i])


    def parse_data(self, path):
        fin = open(path, "r")
        lines = [line.strip() for line in fin.readlines() if line.strip()]
        dots = []
        fold_instructions = []
        for i in lines:
            if "," in i:
                x, y = i.split(",")
                dots.append([int(x), int(y)])
            else:
                direction, num = i.split("=")
                fold_instructions.append([direction[-1], int(num)])

        return [dots, fold_instructions]


def fill_dots_on_paper(paper, data):
    for x, y in data:
            paper[y, x] = True
    return paper

def fold_paper(paper, fold):
    if fold[0] == "y":
        fold_axis = 0
        fold_paper1 = np.flip(paper[-fold[1]:], axis=fold_axis)
        fold_paper2 = paper[-(fold[1] * 2) - 1:fold[1]]
        paper[-(fold[1] * 2) - 1:fold[1]] = fold_paper1 + fold_paper2
        return paper[:fold[1]]
    elif fold[0] == "x":
        fold_axis = 1
        fold_paper1 = np.flip(paper[:, -fold[1]:], axis=fold_axis)
        fold_paper2 = paper[:, -(fold[1] * 2) - 1:fold[1]]
        paper[:, -(fold[1] * 2) - 1:fold[1]] = fold_paper1 + fold_paper2
        return paper[:, :fold[1]]



def task1(data):
    """Write the code for task 1 here"""

    grid_size = [max([i[1] for i in data[0]]) + 1, max([i[0] for i in data[0]]) + 1]
    trnsp_paper = fill_dots_on_paper(np.full((grid_size[0], grid_size[1]), False, dtype=bool), data[0])

    for fold in data[1]:

        trnsp_paper = fold_paper(trnsp_paper, fold)

        return np.sum(trnsp_paper)


def task2(data):
    """Write the code for task 2 here"""
    grid_size = [max([i[1] for i in data[0]]) + 1, max([i[0] for i in data[0]]) + 1]
    trnsp_paper = fill_dots_on_paper(np.full((grid_size[0], grid_size[1]), False, dtype=bool), data[0])

    for fold in data[1]:
        trnsp_paper = fold_paper(trnsp_paper, fold)
    zeroes = np.ones(trnsp_paper.shape)
    zeroes = zeroes * trnsp_paper

    return zeroes




def main():
    puzzle_input = Data(["puzzle_input.txt", "test_input.txt"])

    assert task1(puzzle_input.data["test_input1"]) == 17
    print(f"Solution to task 1: {task1(puzzle_input.data['input'])}")

    # assert task2(puzzle_input.data["test_input1"]) == "", "Failed test"
    print(f"Solution to task 2: {task2(puzzle_input.data['input'])}")


main()
