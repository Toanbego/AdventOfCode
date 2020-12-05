
import numpy as np


def read_data(path='puzzle_input.txt'):
    """ Reads puzzle input """
    with open(path, 'r') as f:
        data = f.read().split('\n')
    return data


def get_number_id(data_input, id_type):
    """
    Gets either correct row or column.
    Since both row and column uses the same logic, same function is called, but with different parameters.
    :param data_input: seating letters
    :param id_type: string with either 'row' or 'column'
    :return:
    """
    row_id_lower = 0
    if id_type == 'row':
        data_input = data_input[:7]
        lower_letter, upper_letter = 'F', 'B'
        row_id_upper = 127
    elif id_type == 'column':
        data_input = data_input[7:]
        lower_letter, upper_letter = 'L', 'R'
        row_id_upper = 7

    for letter_id in data_input:
        # Find the median value, then round down with np.floor()
        halfway_point = np.floor(np.median([row_id_lower, row_id_upper]))
        if letter_id == lower_letter:
            row_id_upper = halfway_point
        elif letter_id == upper_letter:
            row_id_lower = halfway_point

    # Return either row_id_lower or row_id_upper based on which ws changed latest.
    return int(row_id_upper) if data_input[-1] == letter_id else int(row_id_lower)


def get_row(seating_id):
    """Gets the correct row"""
    return get_number_id(seating_id, id_type='row')


def get_column(seating_id):
    """Gets the correct column"""
    return get_number_id(seating_id, id_type='column')


def find_missing_number(numbers):
    """ Checks for missing numbers in a list of numbers. Returns the first missing number it finds"""
    numbers = np.sort(np.array(numbers).astype(int))
    for idx, number in enumerate(numbers[1:]):
        diff = number - numbers[idx]
        if diff != 1:
            return numbers[idx]+1


if __name__ == '__main__':
    puzzle_input = read_data()
    seat_numbers = []
    for i in puzzle_input:
        row = get_row(i)
        column = get_column(i)
        seat_numbers.append(row * 8 + column)

    print(f"The highest seating ID: {max(seat_numbers)}")
    print(f"Your seat ID: {find_missing_number(seat_numbers)}")


