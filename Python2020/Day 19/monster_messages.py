import numpy as np
from collections import *
from copy import deepcopy
import re

def read_data(path="puzzle_input.txt"):
    """ Reads puzzle input """
    with open(path, 'r') as f:
        data = f.read().split('\n')
    return data


def format_ruleset(data):
    """ Formats rueles to dict """
    ruleset = {}
    for line in data:
        rule_nr = int(line[:line.index(":")])
        options = [op.split() for op in line[line.index(":") + 2:].split('|')]
        ruleset[rule_nr] = options
    return ruleset




def get_new_combinations(rules, rule_combination, new_code=[]):
    # Declare list
    code = []
    # Loop through the rules parsed as arguments
    for rule in rule_combination:

        # Check first sub rule in list
        sub_rule = rules[rule]

        # If len is > 1, then a pipe most exists, and the number of possible combinations splits
        if len(sub_rule) > 1:
            new_combination = []
            for s in sub_rule:
                # new_combination.append(get_new_combinations(rules, s, new_code))
                hey = get_new_combinations(rules, s, new_code)
                print("")
                # new_code.append(add(rules, s, new_code))
                code.append(hey)
            print("")
        # If no pipe, add to combination
        else:
            if isinstance(sub_rule, list):
                sub_rule = get_new_combinations(rules, sub_rule, new_code)[0]
                # return letter_code

            code.append(sub_rule)
            # code + "".join(new_code)

    return code
    # return "".join(new_code)


def solve1(rules, num, string_rules):
    rule_options = rules[num]
    if ['"a"'] in rule_options:
        return ['a']
    if ['"b"'] in rule_options:
        return ['b']

    if num in string_rules:
        return string_rules[num]

    final = []
    for option in rule_options:
        str_options = []
        for rule in option:
            sub_options = solve1(rules, int(rule), string_rules)
            if len(str_options) == 0:
                str_options = sub_options.copy()
            else:
                combined = []
                for s in sub_options:
                    for op in str_options:
                        combined.append(op+s)
                str_options = combined.copy()

        final += str_options
    string_rules[num] = final
    return final


def task1(data):
    """Write the code for task 1 here"""

    rules_set = data[:data.index("")]
    messages = data[data.index("")+1:]
    rules = format_ruleset(rules_set)


    all_possibilities = solve1(rules, 0, string_rules)
    all_set = set()
    for solutions in all_possibilities:
        all_set.add(solutions)

    count = 0
    for msg in messages:
        if msg in all_set:
            count += 1

    return count


def task2(data):
    """Write the code for task 2 here"""

    messages = data[data.index("")+1:]

    rule_42 = string_rules[42]
    rule_31 = string_rules[31]
    chunk_size = len(rule_42[0])

    count = 0
    for msg in messages:
        chunks42 = [False for _ in range(len(msg) // chunk_size)]
        chunks31 = [False for _ in range(len(msg) // chunk_size)]

        current_chunk = 0
        for i in range(0, len(msg), chunk_size):
            if msg[i:i+chunk_size] in rule_42:
                chunks42[current_chunk] = True
            if msg[i:i+chunk_size] in rule_31:
                chunks31[current_chunk] = True

            current_chunk += 1

        count42, count31 = 0, 0
        current_chunk = 0
        if chunks42[current_chunk]:
            count42 += 1
            current_chunk += 1
            while current_chunk < len(chunks42) and chunks42[current_chunk]:
                count42 += 1
                current_chunk += 1
            while current_chunk < len(chunks31) and chunks31[current_chunk]:
                count31 += 1
                current_chunk += 1
            if current_chunk == len(chunks31) and 0 < count31 < count42:
                count += 1

    return count


if __name__ == '__main__':

    puzzle_input = read_data()

    string_rules = {}

    print(f"Solution to task 1: {task1(puzzle_input)}")
    print(f"Solution to task 2: {task2(puzzle_input)}")


