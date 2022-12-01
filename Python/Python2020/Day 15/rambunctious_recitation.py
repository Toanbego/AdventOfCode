import numpy as np
from collections import *
from tqdm import tqdm



def task1(data, max_turns=2020):
    """Write the code for task 1 here"""
    starting_numbers = defaultdict(list)

    for i, num in enumerate(data, 1):
        starting_numbers[num] = [i]
        last_spoken_num = num

    for i in tqdm(range(len(starting_numbers)+1, max_turns+1)):

        if len(starting_numbers[last_spoken_num]) == 1:
            next_spoken_number = 0
        else:
            next_spoken_number = starting_numbers[last_spoken_num][-1] - starting_numbers[last_spoken_num][-2]

        starting_numbers[next_spoken_number].append(i)
        last_spoken_num = next_spoken_number

    return last_spoken_num


def task2(data):
    """Write the code for task 1 here"""
    return task1(data, max_turns=30000000)


def main():
    puzzle_input = [0, 6, 1, 7, 2, 19, 20]

    print(f"Solution to task 1: {task1(puzzle_input)}")

    print(f"Solution to task 2: {task2(puzzle_input)}")




main()