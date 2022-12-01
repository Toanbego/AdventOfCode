
import numpy as np


def read_data(path="puzzle_input.txt"):
    fin = open(path, "r")
    lines = [int(line.strip()) for line in fin.readlines() if line.strip()]
    return lines


def count_adapter_differences(adapters):
    joltage_difference_small, joltage_difference_large = 0, 0
    current_adapter = 0
    for adapter in np.array(adapters):
        difference = adapter - current_adapter
        joltage_difference_small += 1 if difference == 1 else 0
        joltage_difference_large += 1 if difference == 3 else 0
        current_adapter = adapter

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
    adapters = np.append(np.array(read_data())[:], 0)
    adapters = np.sort(np.append(adapters, max(adapters) + 3))
    joltage_small, joltage_large = count_adapter_differences(adapters)
    print(f"The number of 1's multiplied with the number of 3's: {joltage_small} * {joltage_large} = "
          f"{joltage_small * joltage_large}")

    print(f"The number of possible adapter arrangements: {combinations_count(adapters)}")


main()
