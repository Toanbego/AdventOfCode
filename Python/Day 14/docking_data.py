
import itertools
import re
from copy import deepcopy


def read_data(path="puzzle_input.txt"):
    """Reads puzzle input"""
    fin = open(path, "r")
    lines = [line.strip() for line in fin.readlines() if line.strip()]
    return lines


class Bitmask:

    def __init__(self, input_code):
        self.operations = self.parse_input(input_code)
        self.memory = {}

    @staticmethod
    def parse_input(input_code):
        """Creates a list with value, memory address and bitmask to use"""
        memory = []
        for datapoint in input_code:
            data_type, value = datapoint.split(' ')[0], datapoint.split(' ')[2]
            if 'mask' in data_type:
                mask = value
            else:
                memory_address = int(re.findall(r"mem\[(\d*)]", data_type)[0])
                memory.append({'value': int(value), 'address': memory_address, 'mask': mask})
        return memory

    def sum_values(self):
        """Sums the values written in memory"""
        return sum(self.memory.values())


def perform_bitwise_operation(value, mask):
    bits = bitfield(value)
    new_result = ''
    for bit, mask_bit in zip(bits, mask):
        if mask_bit != 'X':
            new_result += mask_bit
        else:
            new_result += bit
    return new_result


def combine_mask(value, mask):
    bits = bitfield(value)
    new_result = ''
    for bit, mask_bit in zip(bits, mask):
        if mask_bit == 'X' or mask_bit == '1':
            new_result += mask_bit
        else:
            new_result += bit
    return new_result


def create_permutations(bit_sequence):
    """Creates al possible combinations of a bit sequence that contains floating numbers"""
    permutations = list(map(list, itertools.product([0, 1], repeat=bit_sequence.count('X'))))
    memory_indexes = []
    for permutation in permutations:
        new_sequence = list(deepcopy(bit_sequence))
        for bit_perm in permutation:
            first_x_index = new_sequence.index('X')
            new_sequence[first_x_index] = str(bit_perm)
        memory_indexes.append("".join(new_sequence))
    return memory_indexes


def bitfield(n):
    """Takes an integer and return a 36 bit bitfield as a list"""
    return '0'*(36-len(bin(n)[2:]))+bin(n)[2:]


def reverse_bitfield(bits):
    """Takes a string of integer(s) and return a 36 bit bitfield as a list"""
    return int('0b' + bits, 2)


def task2(data):
    """Solve task 2"""
    bitmask = Bitmask(data)

    for idx, operation in enumerate(bitmask.operations):
        new_result = combine_mask(operation['address'], operation['mask'])
        permutations = create_permutations(new_result)
        for permutation in permutations:
            bitmask.memory[reverse_bitfield(permutation)] = operation['value']
    return bitmask.sum_values()


def task1(data):
    """Solve task 1"""
    bitmask = Bitmask(data)
    for idx, operation in enumerate(bitmask.operations):
        new_result = perform_bitwise_operation(operation['value'], operation['mask'])
        bitmask.memory[operation['address']] = reverse_bitfield(new_result)
    return bitmask.sum_values()


def main():

    puzzle_input = read_data()

    print(f"Solution to task 1: {task1(puzzle_input)}")
    print(f"Solution to task 2: {task2(puzzle_input)}")


main()
