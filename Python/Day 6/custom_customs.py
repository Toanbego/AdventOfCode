import numpy as np


def read_data(path='puzzle_input.txt'):
    """ Reads puzzle input """
    with open(path, 'r') as f:
        data = f.read().split('\n\n')
    return data

def find_duplicates_in_group(p):

    result = set(p[0])
    for s in p[1:]:
        result.intersection_update(s)
    return result


if __name__ == '__main__':

    puzzle_input = read_data()

    # Task one
    total_answers = 0
    for answers in puzzle_input:
        answers = answers.replace("\n", '')
        total_answers += len(np.unique(list(answers)))
    print(f"Solution to part 1: {total_answers}")

    total_answers = 0
    for answers in puzzle_input:
        answers = answers.split("\n")

        if len(answers) > 1:
            answers = find_duplicates_in_group(answers)
            total_answers += len(answers)
        else:
            answers = list(answers[0])
            total_answers += len(list(answers))
    print(f"Solution to part 2: {total_answers}")


