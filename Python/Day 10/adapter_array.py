import itertools
import operator
from collections import Counter
from functools import reduce
from math import factorial

import numpy as np
from itertools import combinations
from copy import deepcopy


def read_data(path="puzzle_input.txt"):
    fin = open(path, "r")
    lines = [int(line.strip()) for line in fin.readlines() if line.strip()]
    return lines


class Partials:
    def __init__(self):
        self.count = 0

    def subset_sum(self, numbers, target, partial=[]):
        s = sum(partial)

        # check if the partial sum is equals to target
        if s == target:

            self.count += 1
            print(self.count)

        if s >= target:
            return  # if we reach the number why bother to continue

        for i in range(len(numbers)):
            n = numbers[i]
            remaining = numbers[i+1:]
            self.subset_sum(remaining, target, partial + [n])


def count_adapter_differences(adapters):
    joltage_difference_small = []
    joltage_difference_large = []
    current_adapter = 0
    for adapter in np.array(adapters):
        difference = adapter - current_adapter
        if difference == 1:
            joltage_difference_small.append(adapter - current_adapter)
        elif difference == 3:
            joltage_difference_large.append(adapter - current_adapter)
        current_adapter = adapter
    joltage_difference_large.append(3)
    return joltage_difference_small, joltage_difference_large


def combinations_count(adapters):
    possible_combinations = [1]
    for i in range(1, len(adapters)):
        count = 0
        for j in range(i):
            if adapters[j] + 3 >= adapters[i]:
                count += possible_combinations[j]
        possible_combinations.append(count)
    return possible_combinations[-1]


def main():
    adapters = np.sort(np.array(read_data()))
    adapters_sorted = np.sort(np.array(adapters))
    joltage_small, joltage_large = count_adapter_differences(adapters_sorted)
    print(f"The number of 1's multiplied with the number of 3's: {len(joltage_small)} * {len(joltage_large)} = "
          f"{len(joltage_small) * len(joltage_large)}")

    print(f"The number of possible adapter arrangements: {combinations_count(adapters_sorted)}")


main()
