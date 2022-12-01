import numpy as np



def read_data(path="puzzle_input.txt"):
    """ Reads puzzle input """
    with open(path, 'r') as f:
        data = f.read().split('\n')
    return data


def two_sum_problem(expenses, goal):
    """ Solves the Two Sum Problem """
    for number in expenses:
        number_required_for_goal = goal - number

        # Check if the number required exists in expenses
        if np.argwhere(expenses == number_required_for_goal):
            return number, number_required_for_goal


def three_sum_problem(expenses, goal):
    """ Solves the Three Sum Problem """
    for number in expenses:
        number_required_for_goal = goal - number
        result_two_sum = two_sum_problem(expenses, goal=number_required_for_goal)
        if result_two_sum:
            return number, result_two_sum[0], result_two_sum[1]


if __name__ == '__main__':
    puzzle_input = np.array(read_data("puzzle_input"), dtype=int)

    # Task 1
    nr1, nr2 = two_sum_problem(puzzle_input, goal=2020)
    print("Solving the Two Sum Problem")
    print(f'{nr1} + {nr2} = {(nr1 + nr2)}')
    print(f'Multiplying numbers: {nr1} * {nr2} = {nr1 * nr2}')


    # Task 2
    nr1, nr2, nr3 = three_sum_problem(puzzle_input, goal=2020)
    print("\nSolving the Three Sum Problem")
    print(f'{nr1} + {nr2} + {nr3} = {(nr1 + nr2 + nr3)}')
    print(f'Multiplying numbers: {nr1} * {nr2} * {nr3} = {nr1 * nr2 * nr3}')
