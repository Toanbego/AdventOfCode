import numpy as np
from copy import deepcopy


def read_data(path="puzzle_input.txt"):
    """Reads puzzle input"""
    fin = open(path, "r")
    lines = [line.strip() for line in fin.readlines() if line.strip()]
    return lines


def binatodeci(binary):
    return sum(val*(2**idx) for idx, val in enumerate(reversed(binary)))


def calculate_lifesupport(binary, life_support_type):
    if life_support_type == "O2":
        bit1, bit2 = 1, 0
    elif life_support_type == "CO2":
        bit1, bit2 = 0, 1

    sequence_length = len(binary[0])
    binary_length = len(binary.transpose()[0])
    i = 0

    while True:
        if binary_length == 1:
            break

        bit_position = binary.transpose()[i]
        if len(bit_position[bit_position == 1]) >= len(bit_position[bit_position == 0]):
            binary_length = len(np.argwhere(bit_position == bit1))
            binary = binary[np.argwhere(bit_position == bit1)].reshape(binary_length,
                                                                       sequence_length)
        else:
            binary_length = len(np.argwhere(bit_position == bit2))
            binary = binary[np.argwhere(bit_position == bit2)].reshape(binary_length,
                                                                       sequence_length)

        if i > sequence_length:
            i = 0
        else:
            i += 1
    return binary[0]


def task1(data):
    """Write the code for task 1 here"""
    binary_array = np.stack([[int(binary) for binary in sequence] for sequence in data])
    gamma, epislon = [], []
    for column in binary_array.transpose():

        if len(column[column != 1]) > len(column[column != 0]):
            epislon.append(1)
            gamma.append(0)
        else:
            gamma.append(1)
            epislon.append(0)

    return binatodeci(gamma) * binatodeci(epislon)


def task2(data):
    """Write the code for task 2 here"""
    binary_array = np.stack([[int(binary) for binary in sequence] for sequence in data])
    return binatodeci(calculate_lifesupport(binary_array, "O2")) * binatodeci(calculate_lifesupport(binary_array, "CO2"))


def main():
    puzzle_input = read_data()
    print(f"Solution to task 1: {task1(puzzle_input)}")
    print(f"Solution to task 2: {task2(puzzle_input)}")


main()
