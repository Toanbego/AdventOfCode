import statistics

def read_data(path="puzzle_input.txt"):
    """Reads puzzle input"""
    fin = open(path, "r")
    lines = [line.strip() for line in fin.readlines() if line.strip()]
    return lines


def check_for_unbalance(chunks, signs):
    stack = []
    for i, sign in enumerate(chunks):
        if sign in signs.keys():
            stack.append(sign)
        else:
            current_sign = stack.pop()
            if current_sign == '(':
                if sign != ")":
                    return sign
            if current_sign == '{':
                if sign != "}":
                    return sign
            if current_sign == '[':
                if sign != "]":
                    return sign
            if current_sign == '<':
                if sign != ">":
                    return sign
    # Check Empty Stack
    if stack:
        return 0
    return 0


def check_for_incomplete(chunks, signs):
    open_stack = []
    for i, sign in enumerate(chunks):
        if sign in signs.keys():
            open_stack.append(sign)
        else:
            open_stack = open_stack[:-1]
    return open_stack


def task1(data):
    """Write the code for task 1 here"""
    score_table = {")": 3, "]": 57, "}": 1197, ">": 25137}
    signs = {"(": ")", "[": "]", "{": "}", "<": ">"}
    current_score = 0
    for chunks in data:
        sign = check_for_unbalance(chunks, signs)
        if sign == 0:
            continue
        else:
            current_score += score_table[sign]
    return current_score


def task2(data):
    """Write the code for task 2 here"""

    score_table = {")": 1, "]": 2, "}": 3, ">": 4}
    signs = {"(": ")", "[": "]", "{": "}", "<": ">"}
    current_score = []

    for chunks in data:
        # Ignore corrupted
        if check_for_unbalance(chunks, signs) != 0:
            continue

        # Get signs needed to complete
        sign = check_for_incomplete(chunks, signs)
        sign.reverse()
        required_signs = [signs[i] for i in sign]

        # Calculate score
        total_score = 0
        for i in required_signs:
            total_score = total_score * 5 + score_table[i]
        current_score.append(total_score)

    return statistics.median(current_score)


def main():
    puzzle_input = read_data()
    if task1(read_data("test_input.txt")) == 26397:
        print(f"Solution to task 1: {task1(puzzle_input)}")
    if task2(read_data("test_input.txt")) == 288957:
        print(f"Solution to task 2: {task2(puzzle_input)}")


main()
