import numpy as np
from collections import Counter

class Data:

    def __init__(self, inputs):
        """Reads puzzle input"""
        self.inputs = inputs
        self.data = {}
        for i in range(len(inputs)):
            if "puzzle" not in list(self.data.keys()):
                self.data["puzzle"] = self.parse_data(inputs[i])
            else:
                self.data[f"test_input{i}"] = self.parse_data(inputs[i])


    def parse_data(self, path):
        fin = open(path, "r")
        lines = [line.strip() for line in fin.readlines() if line.strip()]
        template = lines[0]
        keys, values = [i.split(" -> ")[0] for i in lines[1:]], [i.split(" -> ")[1] for i in lines[1:]]
        pair_insertion = {key: value for key, value in zip(keys, values)}
        return [template, pair_insertion]


class Polymer:
    def __init__(self, data):
        self.data = data
        self.template = data[0]
        self.insertions = data[1:][0]
        self.pairs = self.get_pairs()
        self.pair_count = Counter(self.pairs)
        self.letter_count = Counter(self.template)

    def get_pairs(self):
        return [self.template[i-1] + self.template[i] for i in range(1, len(self.template))]


    def insert_polymers(self):
        new_template = ""
        for pair in self.pairs:
            new_template += pair[0] + self.insertions[pair]
        new_template += self.pairs[-1][1]
        self.template = new_template

    def solve_large_polymer(self, pair_count):
        """
        Iterate through existing pairs
        for x each pair
        Then Add:
              1. Add new pairs to paircount
              2. Add x=pair_count of new letters to to letter count
        :return:
        """
        for pair in pair_count:
            new_pair1, new_pair2 = pair[0] + self.insertions[pair], self.insertions[pair] + pair[1]
            self.pair_count[pair] -= pair_count[pair]
            self.letter_count[self.insertions[pair]] += pair_count[pair]
            if new_pair1 not in list(self.pair_count.keys()):
                self.pair_count[new_pair1] = pair_count[pair]
            else:
                self.pair_count[new_pair1] += pair_count[pair]

            if new_pair2 not in list(self.pair_count.keys()):
                self.pair_count[new_pair2] = pair_count[pair]
            else:
                self.pair_count[new_pair2] += pair_count[pair]


def task1(data):
    """Write the code for task 1 here"""
    polymer_solver = Polymer(data)
    for i in range(10):
        polymer_solver.insert_polymers()
        polymer_solver.pairs = polymer_solver.get_pairs()
    counter = list(Counter(polymer_solver.template).values())

    return max(counter) - min(counter)


def task2(data):
    """Write the code for task 2 here"""
    polymer_solver = Polymer(data)
    for i in range(40):
        polymer_solver.solve_large_polymer(polymer_solver.pair_count.copy())
    counter = list(polymer_solver.letter_count.values())
    return max(counter) - min(counter)


def main():
    puzzle_input = Data(["puzzle_input.txt", "test_input.txt"])

    assert task1(puzzle_input.data["test_input1"]) == 1588
    print(f"Solution to task 1: {task1(puzzle_input.data['puzzle'])}")

    assert task2(puzzle_input.data["test_input1"]) == 2188189693529
    print(f"Solution to task 2: {task2(puzzle_input.data['puzzle'])}")


main()
