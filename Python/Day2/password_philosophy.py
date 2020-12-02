import numpy as np

def read_data(path):
    """ Reads puzzle input """
    with open(path, 'r') as f:
        data = f.read().split('\n')
    return data


# def define_password_policy(inputs):
#     """ Creates a dict with passwords as keys, and policy as value pair"""
#     data = {}
#     counter = 0
#     for element in inputs:
#
#         # Extract dict values
#         instances_lower, instances_upper = element.split(" ")[0].split("-")[0], element.split(" ")[0].split("-")[1]
#         letter = element.split(" ")[1][0]
#         password = element.split(" ")[2]
#
#         # Format dict
#         data[password] = {}
#         data[password]['lower'] = int(instances_lower)
#         data[password]['upper'] = int(instances_upper)
#         data[password]['letter'] = letter
#         counter += 1
#     print(counter)
#     print(len(data))
#
#     return data

def define_password_policy(inputs):
    """ Creates a dict with passwords as keys, and policy as value pair"""
    data = []
    counter = 0
    for element in inputs:

        # Extract dict values
        nr1, nr2 = int(element.split(" ")[0].split("-")[0]), int(element.split(" ")[0].split("-")[1])
        letter = element.split(" ")[1][0]
        password = element.split(" ")[2]

        # Format dict
        data.append([password, nr1, nr2, letter])
        counter += 1
    print(counter)
    print(len(data))

    return data


def check_first_password_policy(passwords):
    """ Checks password policy occurrence wise"""
    number_of_valid_passwords = 0
    for element in passwords:
        password, lower, upper, letter = element[0], element[1], element[2], element[3]
        counts = password.count(letter)
        if counts > 0 and lower <= counts <= upper:
            number_of_valid_passwords += 1
    return number_of_valid_passwords


def check_second_password_policy(passwords):
    """ Checks password policy position wise"""
    number_of_valid_passwords = 0
    for element in passwords:
        password, pos1, pos2, letter = element[0], element[1]-1, element[2]-1, element[3]
        pos1_letter, pos2_letter = password[pos1], password[pos2]
        if pos1_letter == letter and pos2_letter != letter or pos1_letter != letter and pos2_letter == letter:
            number_of_valid_passwords += 1
    return number_of_valid_passwords



if __name__ == '__main__':

    puzzle_input = read_data("puzzle_input.txt")
    # puzzle_input = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']
    puzzle_input = define_password_policy(puzzle_input)

    valid_checks = check_first_password_policy(puzzle_input)
    print(f"Number of valid passwords for old policy: {valid_checks}")
    valid_checks = check_second_password_policy(puzzle_input)
    print(f"Number of valid passwords for new policy: {valid_checks}")


