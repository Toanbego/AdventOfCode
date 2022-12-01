

def read_data(path):
    """ Reads puzzle input """
    with open(path, 'r') as f:
        data = f.read().split('\n')
    return data


def define_password_policy(inputs):
    """
     Creates a list from each nr1-nr2 letter: password
     that looks like [password, nr1, nr2, letter]
    :param inputs: The list of data read from read_data function
    :return:
    """
    data = []
    for element in inputs:

        # Extracts elements from each data point in the input list
        nr1, nr2 = int(element.split(" ")[0].split("-")[0]), int(element.split(" ")[0].split("-")[1])
        letter = element.split(" ")[1][0]
        password = element.split(" ")[2]

        # Adds it to a new list
        data.append([password, nr1, nr2, letter])

    return data


def check_first_password_policy(passwords):
    """ Checks password policy occurrence wise (First task)"""
    number_of_valid_passwords = 0
    for element in passwords:
        password, lower, upper, letter = element[0], element[1], element[2], element[3]

        # Count occurences of the given letter in the password
        counts = password.count(letter)

        # Check if the count is within the range of lower and upper boundary.
        if counts > 0 and lower <= counts <= upper:
            number_of_valid_passwords += 1

    return number_of_valid_passwords


def check_second_password_policy(passwords):
    """ Checks password policy position wise (Second task)"""
    number_of_valid_passwords = 0
    for element in passwords:
        password, pos1, pos2, letter = element[0], element[1]-1, element[2]-1, element[3]

        # Retrieves the letter for the positions in pos1 and pos2
        pos1_letter, pos2_letter = password[pos1], password[pos2]

        # Check if it matches criteria
        if pos1_letter == letter and pos2_letter != letter or pos1_letter != letter and pos2_letter == letter:
            number_of_valid_passwords += 1

    return number_of_valid_passwords


if __name__ == '__main__':

    puzzle_input = read_data("puzzle_input.txt")

    puzzle_input = define_password_policy(puzzle_input)

    valid_checks = check_first_password_policy(puzzle_input)
    print(f"Number of valid passwords for old policy: {valid_checks}")
    valid_checks = check_second_password_policy(puzzle_input)
    print(f"Number of valid passwords for new policy: {valid_checks}")


