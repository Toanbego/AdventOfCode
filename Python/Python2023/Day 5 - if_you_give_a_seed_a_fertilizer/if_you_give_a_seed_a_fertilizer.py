import re

import numpy as np
import requests as req


def submit_answer(answer, level):
    cookies = {"session": open("../../credentials", "r").readlines()[0]}
    response = req.post(
        url=f'https://adventofcode.com/2023/day/5/answer',
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

        data = file.read().split("\n\n")
        data = [i.split(":")[1] for i in data]
        data = [i.split("\n") for i in data]
        data[0] = [int(i) for i in data[0][0].split(" ") if str.isdigit(i)]
        data[1:] = [i[1:] for i in data[1:]]
       # for x, i in enumerate(data[1:]):
        #    for idx, b in enumerate(i):

#                data[1+x][idx] = [int(d) for d in b.split(" ") if str.isdigit(d)]

        #data[1:] = [[[int(x) for x in b.split(" ") if str.isdigit(x)] for b in i] for i in [i[1:] for i in data[1:]]]
        return data


def get_map(data):
    seed_map = []
    for line in data:
        map_cords = line.split(" ")
        dest = int(map_cords[0])
        source = int(map_cords[1])
        range = int(map_cords[2])
        seed_map.append([source, source + range - 1, dest, dest + range -1, range])
    return seed_map

def task1(data):
    """Write the code for task 1 here"""
    seeds = data[0]
    for i in data[1:]:
        seed_map = get_map(i)
        for seed_idx, seed in enumerate(seeds):
            for ranges in seed_map:
                if ranges[0] <= seed <= ranges[1]:
                    seeds[seed_idx] = seed - ranges[0] + ranges[2]
    return min(seeds)



def task2(data):
    """Write the code for task 2 here"""

    seeds = [[data[0][i], data[0][i+1]] for i in range(0, len(data[0][:-1]), 2)]

    for i in data[1:]:
        seed_range = [[int(x) for x in b.split(" ")] for b in i]
        seed_range = [[(a, a + c), (b, b + c)] for a, b, c in seed_range]
        new_seed_range = []

        for seed_idx, seed in enumerate(seeds):
            for tr, fr in seed_range:

                offset = tr[0] - fr[0]
                if seed[1] <= fr[0] or fr[1] <= seed[0]:
                    continue

                ir = [max(seed[0], fr[0]), min(seed[1], fr[1])]
                lr = [seed[0], ir[0]]
                rr = [ir[1], seed[1]]

                if lr:
                    seeds.append(lr)
                if rr:
                    seeds.append(rr)
                new_seed_range.append([ir[0] + offset, ir[1] + offset])
                break
            else:
                new_seed_range.append(seed)

        seeds = new_seed_range

    return min(x[0] for x in seeds)


def pairs(l):
    it = iter(l)
    return zip(it, it)

def p2(seeds):
    f = open("test_input.txt")
    seeds, *mappings = f.read().split("\n\n")
    seeds = seeds.split(": ")[1]
    seeds = [int(x) for x in seeds.split()]
    seeds = [range(a, a + b) for a, b in pairs(seeds)]

    for m in mappings:
        _, *ranges = m.splitlines()
        ranges = [[int(x) for x in r.split()] for r in ranges]
        ranges = [(range(a, a + c), range(b, b + c)) for a, b, c in ranges]
        new_seeds = []

        for r in seeds:
            for tr, fr in ranges:
                offset = tr.start - fr.start
                if r.stop <= fr.start or fr.stop <= r.start:
                    continue
                ir = range(max(r.start, fr.start), min(r.stop, fr.stop))
                lr = range(r.start, ir.start)
                rr = range(ir.stop, r.stop)
                if lr:
                    seeds.append(lr)
                if rr:
                    seeds.append(rr)
                new_seeds.append(range(ir.start + offset, ir.stop + offset))
                break
            else:
                new_seeds.append(r)

        seeds = new_seeds

    return min(x.start for x in seeds)

def main():
    puzzle_input = Data(["puzzle_input.txt", "test_input.txt"])

   # print(task1(puzzle_input.data["test_input"]))
   # print(task1(puzzle_input.data['puzzle']))

    print(task2(puzzle_input.data["test_input"]))  # Set example answer here
    print(p2(puzzle_input.data["test_input"]))

    # exit()
    # print(task2(puzzle_input.data['puzzle']))


main()
