import numpy as np
from collections import Counter
from itertools import *


def read_data(path="puzzle_input.txt"):
    """Reads puzzle input"""
    fin = open(path, "r")
    lines = [line.strip() for line in fin.readlines() if line.strip()]
    return lines


def task1(data):
    """Write the code for task 1 here"""
    counter = 0
    for segment_puzzle in data:
        unique_patterns, output = segment_puzzle.split(" | ")
        segment_lengths = Counter([len(i) for i in unique_patterns.split(" ")])
        for key in segment_lengths:
            if segment_lengths[key] == 1:
                counter += sum([1 for i in output.split(" ") if len(i) == key])
    return counter


def task2(data):
    """Write the code for task 2 here"""
    puzzle_answer = []

    for segment_puzzle in data:
        unique_patterns, output = segment_puzzle.split(" | ")
        decoded_segments = {0: "", 1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: ""}
        segment_group = {}
        for key in Counter([len(i) for i in unique_patterns.split(" ")]):
            segment_group[key] = [pattern for pattern in unique_patterns.split(" ") if len(pattern) == key]

        # Get easy segments
        lengths = {1: 2, 4: 4, 7: 3, 8: 7}
        for pattern in unique_patterns.split(" "):
            if len(pattern) in list(lengths.values()):
                decoded_segments[list(lengths.keys())[list(lengths.values()).index(len(pattern))]] = pattern

        # Solve puzzle with known information
        for group in segment_group[6]:
            check = "".join(i for i in group
                            if i not in decoded_segments[7])
            if len(check) == 4:
                decoded_segments[6] = group
                segment_group[6].remove(group)

        for group in segment_group[5]:
            check = "".join(i for i in decoded_segments[6]
                            if i not in group)
            if len(check) == 1:
                decoded_segments[5] = group
                segment_group[5].remove(group)

        for group in segment_group[5]:
            check = "".join(i for i in group
                            if i not in decoded_segments[7])
            if len(check) == 2:
                decoded_segments[3] = group

            if len(check) == 3:
                decoded_segments[2] = group

        for group in segment_group[6]:
            check = "".join(i for i in group
                            if i not in decoded_segments[4])
            if len(check) == 2:
                decoded_segments[9] = group
            if len(check) == 3:
                decoded_segments[0] = group

        # Decode the output
        decoded_output = ""
        for num in output.split(" "):
            for key in decoded_segments:
                if sorted(decoded_segments[key]) == sorted(num):
                    decoded_output += str(key)

        puzzle_answer.append(int(decoded_output))

    return sum(puzzle_answer)





def main():
    puzzle_input = read_data()
    if task1(read_data("test_input.txt")) == 26:
        print(f"Solution to task 1: {task1(puzzle_input)}")
    if task2(read_data("test_input.txt")) == 61229:
        print(f"Solution to task 2: {task2(puzzle_input)}")


main()
